// Signale des pages du site à Bing (et aux autres moteurs du protocole IndexNow), sans compte
// ni connexion : `npm run indexnow` (toutes les adresses du plan du site) ou
// `npm run indexnow -- https://drfranckmoyal.fr/tca-dents/ …` (seulement celles-là).
//
// Le moteur vérifie que la demande vient bien du site en lisant la clé publiée à sa racine
// (public/<clé>.txt, copiée par docs/refonte/maquettes/publier.py). Mis en place le 25/10/2026,
// à la mise en ligne de la refonte : Bing Webmaster Tools demandait de se connecter au compte
// de Franck, IndexNow n'en a pas besoin.
//
// Ne signaler que des pages nouvelles ou modifiées : renvoyer sans cesse les mêmes adresses
// est déconseillé par le protocole.
import { readdirSync, readFileSync, existsSync } from "node:fs";
import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const racine = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const HOTE = "drfranckmoyal.fr";

const fichierCle = readdirSync(join(racine, "public")).find((n) => /^[0-9a-f]{32}\.txt$/.test(n));
if (!fichierCle) {
  console.error("Aucune clé IndexNow dans public/ (un fichier de 32 caractères hexadécimaux, .txt).");
  process.exit(1);
}
const cle = readFileSync(join(racine, "public", fichierCle), "utf8").trim();
const adresseCle = `https://${HOTE}/${fichierCle}`;

let adresses = process.argv.slice(2).filter((a) => a.startsWith("https://"));
if (!adresses.length) {
  const plan = join(racine, "dist-refonte", "sitemap-0.xml");
  if (!existsSync(plan)) {
    console.error("Plan du site introuvable : lancez d'abord npm run refonte.");
    process.exit(1);
  }
  adresses = [...readFileSync(plan, "utf8").matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
}

// la clé doit être en ligne avant de signaler quoi que ce soit
const enLigne = await fetch(adresseCle, { cache: "no-store" });
if (!enLigne.ok || (await enLigne.text()).trim() !== cle) {
  console.error(`La clé n'est pas encore en ligne (${adresseCle} → ${enLigne.status}). Déposez d'abord le site.`);
  process.exit(1);
}

const reponse = await fetch("https://api.indexnow.org/indexnow", {
  method: "POST",
  headers: { "Content-Type": "application/json; charset=utf-8" },
  body: JSON.stringify({ host: HOTE, key: cle, keyLocation: adresseCle, urlList: adresses }),
});
const sens = {
  200: "reçu",
  202: "reçu, la clé sera vérifiée par le moteur",
  400: "demande mal formée",
  403: "clé refusée",
  422: "adresses hors du site ou clé incorrecte",
  429: "trop de demandes, réessayer plus tard",
};
console.log(`${adresses.length} adresse(s) signalée(s) à IndexNow : ${reponse.status} — ${sens[reponse.status] || "réponse inattendue"}`);
if (reponse.status >= 300) process.exit(1);
