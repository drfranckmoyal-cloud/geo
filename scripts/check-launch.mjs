// Contrôle avant mise en ligne : la partie technique de la checklist de ChatGPT
// (docs/echanges/2026-09-22-chatgpt-24-checklist-avant-mise-en-ligne.md, §D), sur le site
// construit (dist/). Il dit ce qui empêche encore la mise en ligne, page par page, et ne passe
// au vert que lorsque tout est levé.
// Lancer après « npm run build » : npm run launch-check
import { readFile, readdir } from "node:fs/promises";
import { parse } from "node-html-parser";
import { verifyPack } from "./verify-pack.mjs";

async function pagesOf(dir = "dist") {
  const out = [];
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const path = `${dir}/${entry.name}`;
    if (entry.isDirectory() && entry.name !== "_astro") out.push(...(await pagesOf(path)));
    else if (entry.name === "index.html") out.push(path);
  }
  return out.sort();
}

const blockers = [];
const block = (what, detail) => blockers.push({ what, detail });
const count = { texte: 0, visuels: 0, rdv: 0, avenir: 0, rdvPages: 0 };
const perPage = [];

for (const file of await pagesOf()) {
  const url = file.replace(/^dist/, "").replace(/index\.html$/, "");
  const root = parse(await readFile(file, "utf8"));
  const texts = root.querySelectorAll("main .placeholder-text, .site-footer .placeholder-text").length;
  const visuals = root.querySelectorAll("[data-emplacement='visuel']").length;
  const rdv = root.querySelectorAll("a[data-emplacement]").length;
  const avenir = root.querySelectorAll("[data-a-venir]").length;
  count.texte += texts;
  count.visuels += visuals;
  count.rdv += rdv;
  if (rdv) count.rdvPages++;
  count.avenir += avenir;
  if (texts || visuals || avenir) perPage.push(`  ${url.padEnd(48)} ${texts} texte(s) « à fournir », ${visuals} visuel(s) à fournir${avenir ? `, ${avenir} lien(s) à venir` : ""}`);
}

if (count.avenir) block("Liens vers des pages pas encore construites", `${count.avenir} lien(s)`);
if (count.texte) block("Informations « à fournir » visibles (téléphone, lien de rendez-vous, e-mail, hébergeur…)", `${count.texte} emplacement(s)`);
if (count.visuels) block("Visuels propriétaires à intégrer (avec consentement pour chaque cas patient)", `${count.visuels} emplacement(s)`);
if (count.rdv) block("Bouton « Prendre rendez-vous » sans lien définitif", `sur ${count.rdvPages} page(s)`);

// Profils officiels du Dr Moyal pour les moteurs (sameAs)
const home = parse(await readFile("dist/franck-moyal/index.html", "utf8"));
const graph = home.querySelectorAll('script[type="application/ld+json"]').flatMap((s) => JSON.parse(s.text)["@graph"] ?? []);
const person = graph.find((n) => n["@type"] === "Person");
if (!person?.sameAs?.length) block("Profils officiels (sameAs : LinkedIn, Instagram…) absents des données structurées", "adresses exactes à fournir");

// robots.txt : décision attendue sur les robots d'IA (D27)
const robots = await readFile("dist/robots.txt", "utf8");
if (!/OAI-SearchBot|GPTBot|Google-Extended|ClaudeBot|CCBot/i.test(robots)) block("robots.txt : règles des robots d'IA non encore décidées (D27)", "décision à prendre");

// Écarts du pack encore ouverts (renvois bibliographiques…)
const pack = await verifyPack();
if (pack.problems) block("Contrôle des textes en échec", `${pack.problems} écart(s) de construction`);
if (pack.warnings) block("Écarts du pack à corriger par ChatGPT (renvois bibliographiques)", `${pack.warnings} écart(s)`);

console.log("■ Contrôle avant mise en ligne\n");
if (perPage.length) console.log(`Emplacements encore visibles, page par page :\n${perPage.join("\n")}\n`);
if (blockers.length) {
  console.log("Ce qui empêche encore la mise en ligne :");
  for (const b of blockers) console.log(`  ✗ ${b.what} — ${b.detail}`);
  console.log(`\n${blockers.length} point(s) bloquant(s) : le site n'est pas prêt à être mis en ligne.`);
  process.exit(1);
}
console.log("✓ Aucun point bloquant : le site peut être mis en ligne (après le contrôle visuel final).");
