// Enregistre des lectures dans le relevé IA du jour, au fur et à mesure.
//   node suivi/ia/noter.mjs < lectures.json        → ajoute au relevé du jour
//   node suivi/ia/noter.mjs --reste                → liste ce qui reste à lire aujourd'hui
//   node suivi/ia/noter.mjs --date 2026-10-21 ...  → pour un autre jour
//
// Entrée attendue (stdin) : { "<moteur>": { "<question>": { statut, cite, nom, site, sources, praticiens, extrait } } }
// On peut envoyer un seul moteur et quelques questions à la fois : le fichier se complète.
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ici = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const iDate = args.indexOf("--date");
const auj = new Date();
const date = iDate >= 0 ? args[iDate + 1]
  : `${auj.getFullYear()}-${String(auj.getMonth() + 1).padStart(2, "0")}-${String(auj.getDate()).padStart(2, "0")}`;

const config = JSON.parse(await readFile(join(ici, "questions.json"), "utf8"));
const moteurs = Object.keys(config.moteurs);
const familleDe = {};
for (const [f, qs] of Object.entries(config.familles)) for (const q of qs) familleDe[q] = f;

await mkdir(join(ici, "releves"), { recursive: true });
const chemin = join(ici, "releves", `${date}.json`);
let releve;
try { releve = JSON.parse(await readFile(chemin, "utf8")); }
catch { releve = { date, moteurs, questions: {} }; }

const STATUTS = new Set(["ok", "pas d'aperçu", "anti-robot", "limite", "échec"]);

if (!args.includes("--reste")) {
  let brut = "";
  for await (const morceau of process.stdin) brut += morceau;
  const entree = JSON.parse(brut);
  let n = 0;
  for (const [moteur, lectures] of Object.entries(entree)) {
    if (!moteurs.includes(moteur)) { console.error(`Moteur inconnu, ignoré : ${moteur}`); continue; }
    for (const [q, l] of Object.entries(lectures)) {
      if (!familleDe[q]) { console.error(`Question absente de questions.json, ignorée : « ${q} »`); continue; }
      if (!STATUTS.has(l.statut)) { console.error(`Statut inconnu pour « ${q} » (${moteur}) : ${l.statut}`); continue; }
      const propre = l.statut === "ok"
        ? { statut: "ok", cite: !!(l.nom || l.site), nom: !!l.nom, site: !!l.site,
            sources: (l.sources || []).slice(0, 12), praticiens: (l.praticiens || []).slice(0, 10),
            extrait: (l.extrait || "").slice(0, 300) }
        : { statut: l.statut };
      releve.questions[q] ??= { famille: familleDe[q] };
      releve.questions[q][moteur] = propre;
      n++;
    }
  }
  // Ordre stable : celui de questions.json.
  const range = {};
  for (const q of Object.keys(familleDe)) if (releve.questions[q]) range[q] = releve.questions[q];
  releve.questions = range;
  await writeFile(chemin, JSON.stringify(releve, null, 2) + "\n");
  console.log(`${n} lecture(s) enregistrée(s) dans releves/${date}.json`);
}

const manque = [];
for (const q of Object.keys(familleDe))
  for (const m of moteurs)
    if (!releve.questions[q]?.[m]) manque.push(`${m} — ${q}`);
const total = Object.keys(familleDe).length * moteurs.length;
console.log(`${total - manque.length} / ${total} lectures faites aujourd'hui.`);
if (args.includes("--reste")) manque.forEach((l) => console.log("  " + l));
