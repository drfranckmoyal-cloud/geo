// Compare deux relevés IA et dit ce qui a bougé.
//   node suivi/ia/comparer.mjs              → le dernier relevé contre le précédent
//   node suivi/ia/comparer.mjs 2026-10-21   → ce relevé-là contre le précédent
//
// « Cité » veut dire : l'IA nomme Franck, ou s'appuie sur drfranckmoyal.fr comme source.
// Pour la famille « Marque », dont les questions contiennent déjà son nom, seul compte le site.
import { readdir, readFile } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ici = dirname(fileURLToPath(import.meta.url));
const DOSSIER = join(ici, "releves");
const config = JSON.parse(await readFile(join(ici, "questions.json"), "utf8"));
const moteurs = Object.keys(config.moteurs);
const NOM = { "google-apercu": "Aperçu IA de Google", "google-mode-ia": "Mode IA de Google", "chatgpt": "ChatGPT" };

const fichiers = (await readdir(DOSSIER).catch(() => [])).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort();
if (!fichiers.length) { console.log("Aucun relevé IA pour l'instant."); process.exit(0); }
const voulu = process.argv[2];
const nomCourant = voulu ? `${voulu}.json` : fichiers.at(-1);
const i = fichiers.indexOf(nomCourant);
if (i < 0) { console.error(`Relevé introuvable : ${nomCourant}`); process.exit(1); }
const lire = async (f) => JSON.parse(await readFile(join(DOSSIER, f), "utf8"));
const courant = await lire(nomCourant);
const precedent = i > 0 ? await lire(fichiers[i - 1]) : null;

const estCite = (q, l) => l?.statut === "ok" && (q.famille === "Marque" ? l.site : l.cite);
const lus = (r, m) => Object.values(r.questions).filter((q) => q[m]?.statut === "ok");

console.log(`Visibilité dans les IA au ${courant.date}` + (precedent ? `, comparée au ${precedent.date}` : " — premier relevé, c'est la référence") + "\n");

// 1. Le score par moteur
for (const m of moteurs) {
  const ok = lus(courant, m);
  const c = ok.filter((q) => estCite(q, q[m])).length;
  let ligne = `  ${NOM[m].padEnd(22)} cité sur ${String(c).padStart(2)} / ${ok.length} questions lues`;
  if (precedent) {
    const okP = lus(precedent, m);
    const cP = okP.filter((q) => estCite(q, q[m])).length;
    ligne += `   (veille : ${cP} / ${okP.length})`;
  }
  const pasLu = Object.values(courant.questions).filter((q) => q[m] && q[m].statut !== "ok");
  const motifs = {};
  pasLu.forEach((q) => (motifs[q[m].statut] = (motifs[q[m].statut] || 0) + 1));
  if (pasLu.length) ligne += `   — non lues : ${Object.entries(motifs).map(([k, v]) => `${v} ${k}`).join(", ")}`;
  console.log(ligne);
}
console.log();

// 2. Entrées et sorties, question par question
if (precedent) {
  const entrees = [], sorties = [];
  for (const [q, v] of Object.entries(courant.questions)) {
    const p = precedent.questions[q];
    if (!p) continue;
    for (const m of moteurs) {
      if (v[m]?.statut !== "ok" || p[m]?.statut !== "ok") continue; // on ne compare que deux vraies lectures
      const a = estCite(p, p[m]), b = estCite(v, v[m]);
      if (!a && b) entrees.push(`${NOM[m]} — « ${q} »`);
      if (a && !b) sorties.push(`${NOM[m]} — « ${q} »`);
    }
  }
  if (entrees.length) { console.log(`✦ ${entrees.length} nouvelle(s) citation(s)`); entrees.forEach((l) => console.log("  " + l)); console.log(); }
  if (sorties.length) { console.log(`✕ ${sorties.length} citation(s) perdue(s)`); sorties.forEach((l) => console.log("  " + l)); console.log(); }
  if (!entrees.length && !sorties.length) console.log("Aucune citation gagnée ni perdue depuis la veille.\n");
}

// 3. Par famille
console.log("Par famille (citations / lectures, tous moteurs confondus) :");
const parFamille = {};
for (const q of Object.values(courant.questions)) {
  const f = (parFamille[q.famille] ??= { c: 0, n: 0 });
  for (const m of moteurs) if (q[m]?.statut === "ok") { f.n++; if (estCite(q, q[m])) f.c++; }
}
for (const [f, v] of Object.entries(parFamille)) console.log(`  ${f.padEnd(34)} ${v.c} / ${v.n}`);
console.log();

// 4. Les questions où il est cité aujourd'hui
const cites = [];
for (const [q, v] of Object.entries(courant.questions)) {
  const ms = moteurs.filter((m) => estCite(v, v[m])).map((m) => NOM[m]);
  if (ms.length && v.famille !== "Marque") cites.push(`« ${q} » — ${ms.join(", ")}`);
}
console.log(cites.length ? `Cité aujourd'hui (hors questions à son nom) :` : "Cité sur aucune question hors questions à son nom.");
cites.forEach((l) => console.log("  " + l));
console.log();

// 5. Ceux que les IA citent à sa place
const sites = {}, docteurs = {};
for (const v of Object.values(courant.questions)) {
  if (v.famille === "Marque") continue;
  for (const m of moteurs) {
    const l = v[m];
    if (l?.statut !== "ok") continue;
    for (const s of l.sources) if (s !== "drfranckmoyal.fr") sites[s] = (sites[s] || 0) + 1;
    for (const d of l.praticiens) docteurs[d] = (docteurs[d] || 0) + 1;
  }
}
const top = (o, n) => Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, n);
console.log("Sites les plus cités à sa place :");
top(sites, 12).forEach(([s, n]) => console.log(`  ${String(n).padStart(3)}  ${s}`));
console.log("\nPraticiens les plus nommés à sa place :");
top(docteurs, 10).forEach(([d, n]) => console.log(`  ${String(n).padStart(3)}  ${d}`));
