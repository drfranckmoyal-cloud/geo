// Dépose le site chez Hostinger par SSH, en une commande : `npm run publier`.
// Repris tel quel du projet SMILECLUB (04/10/2026) : même hébergement, même compte.
//
// Remplace la procédure manuelle du gestionnaire de fichiers (vider public_html,
// envoyer l'archive, l'extraire, la supprimer). Ici on n'envoie que ce qui a changé,
// et le site n'est jamais vide une seule seconde.
//
// Pourquoi SSH et pas FTP : le FTP de Hostinger refuse tout fichier au-delà
// d'environ 8 Ko — « 450 Transfer aborted. Link to file server lost », côté serveur,
// quelle que soit l'option essayée. Constaté le 4 octobre 2026. Nos pages font
// 22 à 49 Ko, le FTP est donc inutilisable ici.
//
// Les réglages vivent dans .env, qui n'est pas versionné. L'authentification se fait
// par clé : aucun mot de passe nulle part.
import { readdir, readFile } from "node:fs/promises";
import { existsSync, readFileSync } from "node:fs";
import { join, posix, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { createHash } from "node:crypto";

const executer = promisify(execFile);
const racine = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const DIST = join(racine, "dist");
const ORIGINE = "https://drfranckmoyal.fr/";

// ——— les réglages ————————————————————————————————————————————————
function lireEnv() {
  const f = join(racine, ".env");
  if (!existsSync(f)) return {};
  const env = {};
  for (const ligne of readFileSync(f, "utf8").split("\n")) {
    const m = ligne.match(/^([A-Z_]+)=(.*)$/);
    if (m) env[m[1]] = m[2].trim();
  }
  return env;
}

const env = { ...lireEnv(), ...process.env };
const HOTE = env.SSH_HOTE;
const PORT = env.SSH_PORT || "65002";
const UTILISATEUR = env.SSH_UTILISATEUR;
const CHEMIN = env.SSH_CHEMIN;

if (!HOTE || !UTILISATEUR || !CHEMIN) {
  console.error(`
Il manque les réglages SSH dans le fichier .env, à la racine du projet :

  SSH_HOTE=        l'adresse du serveur
  SSH_UTILISATEUR= le nom d'utilisateur SSH
  SSH_CHEMIN=      le dossier du site sur le serveur

Ils se lisent dans le hPanel Hostinger : Avancé → Accès SSH.
Voir docs/COMMENT-MODIFIER.md.
`);
  process.exit(1);
}

const sshArgs = ["-p", PORT, "-o", "BatchMode=yes", "-o", "ConnectTimeout=20"];
const cible = `${UTILISATEUR}@${HOTE}`;

// ——— la liste des fichiers ————————————————————————————————————————
async function balayer(dossier, prefixe = "") {
  const sortie = [];
  for (const e of await readdir(dossier, { withFileTypes: true })) {
    const chemin = join(dossier, e.name);
    const distant = prefixe ? posix.join(prefixe, e.name) : e.name;
    if (e.isDirectory()) sortie.push(...(await balayer(chemin, distant)));
    else if (e.name !== ".DS_Store") sortie.push({ chemin, distant });
  }
  return sortie;
}

const empreinte = async (chemin) =>
  createHash("sha1").update(await readFile(chemin)).digest("hex");

// ——— le dépôt ————————————————————————————————————————————————————
async function verifierConnexion() {
  try {
    const { stdout } = await executer("ssh", [...sshArgs, cible, `test -d "${CHEMIN}" && echo ok`]);
    if (stdout.trim() !== "ok") throw new Error(`le dossier ${CHEMIN} n'existe pas sur le serveur`);
  } catch (e) {
    console.error(`
Impossible de se connecter au serveur en SSH.

  ${String(e.stderr || e.message).trim()}

À vérifier, dans le hPanel Hostinger → Avancé → Accès SSH :
  • l'accès SSH est bien « ACTIF » ;
  • la clé publique de ce Mac y est enregistrée (« Ajouter une clé SSH »).
`);
    process.exit(1);
  }
}

async function main() {
  if (!existsSync(DIST)) {
    console.error("Le dossier dist/ n'existe pas. Lancez d'abord : npm run build");
    process.exit(1);
  }
  await verifierConnexion();

  const fichiers = await balayer(DIST);

  // On établit nous-mêmes ce qui diffère, en comparant les empreintes des deux côtés.
  // Le rsync livré avec macOS (openrsync) se trompe sur quelques fichiers avec -c :
  // il les annonce envoyés à chaque fois alors qu'ils sont identiques. Vérifié le
  // 04/10/2026. Son compte-rendu n'est donc pas fiable, le nôtre l'est.
  const { stdout: brut } = await executer(
    "ssh",
    [...sshArgs, cible, `cd "${CHEMIN}" && find . -type f -exec sha1sum {} + 2>/dev/null`],
    { maxBuffer: 1 << 26 }
  );
  const surLeServeur = new Map(
    brut.split("\n").filter(Boolean).map((l) => {
      const [h, ...reste] = l.split(/\s+/);
      return [reste.join(" ").replace(/^\.\//, ""), h];
    })
  );

  const aEnvoyer = [];
  for (const f of fichiers) {
    if (surLeServeur.get(f.distant) !== (await empreinte(f.chemin))) aEnvoyer.push(f.distant);
  }
  const connus = new Set(fichiers.map((f) => f.distant));
  const aRetirer = [...surLeServeur.keys()].filter((d) => !connus.has(d));

  if (!aEnvoyer.length && !aRetirer.length) {
    console.log(`${fichiers.length} fichiers comparés : le site en ligne est déjà à jour.`);
    console.log("Rien à envoyer.\n");
  } else {
    console.log(`${fichiers.length} fichiers comparés.\n`);
    if (aEnvoyer.length) {
      console.log(`${aEnvoyer.length} fichier(s) à mettre à jour :`);
      aEnvoyer.forEach((d) => console.log("  " + d));
    }
    if (aRetirer.length) {
      console.log(`\n${aRetirer.length} fichier(s) que le site ne produit plus, à retirer :`);
      aRetirer.forEach((d) => console.log("  " + d));
    }
    console.log();
  }

  // rsync fait le transfert. --delete retire du serveur ce que le site ne produit plus ;
  // public_html ne contient rien d'autre que notre build, et la liste ci-dessus le redit
  // à chaque fois avant que ça parte.
  await executer(
    "rsync",
    ["-rlptz", "--delete", "-e", `ssh ${sshArgs.join(" ")}`, `${DIST}/`, `${cible}:${CHEMIN}/`],
    { maxBuffer: 1 << 26 }
  );

  // ——— on vérifie que le serveur sert bien ce qu'on vient d'envoyer ———
  console.log("\nContrôle du site en ligne…");
  let bons = 0;
  const soucis = [];
  for (const f of fichiers) {
    if (f.distant === ".htaccess") continue; // 403 attendu : Apache refuse de le servir
    const r = await fetch(ORIGINE + f.distant, { cache: "no-store" });
    const enLigne = r.ok
      ? createHash("sha1").update(Buffer.from(await r.arrayBuffer())).digest("hex")
      : null;
    if (enLigne && enLigne === (await empreinte(f.chemin))) bons++;
    else soucis.push(`${f.distant} (${r.status})`);
  }
  console.log(`\n${bons} fichier(s) identiques à la version fabriquée.`);
  if (soucis.length) {
    console.log(`\n${soucis.length} écart(s) :`);
    soucis.forEach((s) => console.log("  " + s));
    process.exit(1);
  }
  console.log("Le site en ligne est à jour.");
}

main().catch((e) => {
  console.error(String(e.stderr || e.message || e).trim());
  process.exit(1);
});
