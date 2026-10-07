// Compare deux relevés de positions et dit ce qui a bougé.
//   node suivi/comparer.mjs                → le dernier relevé contre le précédent
//   node suivi/comparer.mjs 2026-10-08     → ce relevé-là contre le précédent
//
// Un relevé est un fichier suivi/releves/AAAA-MM-JJ.json de la forme :
//   { "date": "2026-10-08", "termes": { "bruxisme": { "clics": 0, "impressions": 0, "position": null }, … } }
// position vaut null quand le terme ne sort sur rien : Search Console n'en donne pas.
import { readdir, readFile } from "node:fs/promises";
import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ici = dirname(fileURLToPath(import.meta.url));
const DOSSIER = join(ici, "releves");

const fichiers = (await readdir(DOSSIER).catch(() => []))
  .filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f))
  .sort();

if (fichiers.length === 0) {
  console.log("Aucun relevé pour l'instant. Le premier sera la référence.");
  process.exit(0);
}

const voulu = process.argv[2];
const courantNom = voulu ? `${voulu}.json` : fichiers[fichiers.length - 1];
const i = fichiers.indexOf(courantNom);
if (i < 0) {
  console.error(`Relevé introuvable : ${courantNom}`);
  process.exit(1);
}

const lire = async (f) => JSON.parse(await readFile(join(DOSSIER, f), "utf8"));
const courant = await lire(courantNom);

if (i === 0) {
  const t = Object.entries(courant.termes);
  const vus = t.filter(([, v]) => v.position != null);
  console.log(`Premier relevé, ${courant.date} — c'est la référence.\n`);
  console.log(`  ${t.length} termes suivis`);
  console.log(`  ${vus.length} sortent dans Google, ${t.length - vus.length} n'apparaissent sur rien\n`);
  vus.sort((a, b) => a[1].position - b[1].position)
     .forEach(([m, v]) => console.log(`  ${String(v.position).padStart(5)}  ${m}  (${v.impressions} impr., ${v.clics} clic·s)`));
  process.exit(0);
}

const precedent = await lire(fichiers[i - 1]);
const flou = (n) => (n == null ? null : Math.round(n * 10) / 10);

const entrees = [], sorties = [], montees = [], descentes = [], stables = [];
for (const [mot, v] of Object.entries(courant.termes)) {
  const av = precedent.termes[mot];
  const a = flou(av?.position ?? null), b = flou(v.position);
  if (a == null && b != null) entrees.push([mot, b]);
  else if (a != null && b == null) sorties.push([mot, a]);
  else if (a != null && b != null) {
    const d = +(a - b).toFixed(1); // positif = on monte (position plus petite)
    if (d >= 0.5) montees.push([mot, a, b, d]);
    else if (d <= -0.5) descentes.push([mot, a, b, d]);
    else stables.push([mot, b]);
  }
}

console.log(`Positions au ${courant.date}, comparées au ${precedent.date}\n`);

const bloc = (titre, lignes) => {
  if (!lignes.length) return;
  console.log(titre);
  lignes.forEach((l) => console.log("  " + l));
  console.log();
};

bloc(`▲ ${montees.length} terme(s) en progression`,
  montees.sort((x, y) => y[3] - x[3]).map(([m, a, b, d]) => `${m} : ${a} → ${b}  (+${d})`));
bloc(`▼ ${descentes.length} terme(s) en recul`,
  descentes.sort((x, y) => x[3] - y[3]).map(([m, a, b, d]) => `${m} : ${a} → ${b}  (${d})`));
bloc(`✦ ${entrees.length} terme(s) qui apparaissent pour la première fois`,
  entrees.sort((x, y) => x[1] - y[1]).map(([m, b]) => `${m} : position ${b}`));
bloc(`✕ ${sorties.length} terme(s) qui ne sortent plus`,
  sorties.map(([m, a]) => `${m} : était en ${a}`));

const absents = Object.entries(courant.termes).filter(([, v]) => v.position == null).length;
console.log(`${stables.length} stable(s), ${absents} terme(s) toujours absents sur ${Object.keys(courant.termes).length}.`);
