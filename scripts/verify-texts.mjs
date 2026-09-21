// Contrôle automatique des textes (verrou V2 : « les textes ne se touchent pas »).
//  1. Rien d'inventé : chaque texte des fichiers src/content/*.ts existe mot pour mot dans le
//     pack en vigueur ou dans les compléments de ChatGPT (docs/echanges).
//  2. Rien de perdu : chaque texte préparé apparaît bien dans la page construite (dist/).
//  3. Rien d'oublié : chaque passage affichable du pack (citations, titres, listes, FAQ,
//     sources) se retrouve dans la page.
// Les seules différences admises sont les décisions notées au fichier maître (D6, D11, D12).
// Pages du pack « pages suivantes » : contrôle dédié (scripts/verify-pack.mjs).
// Lancer après « npm run build » : npm run verify
import { readFile } from "node:fs/promises";
import { verifyPack } from "./verify-pack.mjs";
import { builtPages } from "../src/content/site.ts";
import { home } from "../src/content/home.ts";
import { franck } from "../src/content/franck.ts";
import { usures } from "../src/content/usures.ts";
import { nav, footer } from "../src/content/site.ts";

const PACK = "docs/golden-master/v1.3.1";
const ECHANGES = [
  "docs/echanges/2026-09-21-chatgpt-reponses-points-17-20.md",
  "docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour1.md",
  "docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour2.md",
];

// Remplacements décidés (fichier maître) : texte du pack → texte retenu
const DECISIONS = [
  { ref: "D6", pack: "Dr Franck Moyal | Dentiste esthétique et usures dentaires à Paris", site: home.seo.title },
  { ref: "D11", pack: "Non.", site: usures.treat.title },
  { ref: "D11", pack: "FAUT-IL TOUJOURS TRAITER ?", site: usures.treat.label },
  { ref: "D12", pack: "Attrition / contraintes mécaniques", site: "Attrition et contraintes mécaniques" },
  // Méthode : titre et textes définitifs (D31, contrôle du tour 2 par ChatGPT)
  { ref: "D31", pack: "Écouter, analyser, planifier, décider ensemble", site: "Écouter, analyser, planifier, simuler, décider ensemble" },
  { ref: "D31", pack: "simulation et projet lorsque pertinent.", site: "construire les formes, les proportions et les options thérapeutiques." },
  { ref: "D31", pack: "options, avantages, limites, niveau d’intervention.", site: "comparer les options, leurs avantages, leurs limites et le niveau d’intervention." },
  { ref: "D31", pack: "uniquement si le bénéfice est réel.", site: "uniquement lorsque le bénéfice est réel." },
];
// Passages du pack volontairement non affichés (décisions du fichier maître)
const HIDDEN = [{ ref: "D19", kind: "source (note)", why: "notes « Soutient : » retirées de l'affichage" }];
// Libellés de structure du pack (consignes au rédacteur), jamais affichés
const STRUCTURE = /^(Texte|Lien|Liens|CTA|Intro|Étapes|Sous-blocs|Message clé|Titre|Visuel|Objectif)\s*:?$/i;
// Sections du pack qui sont des consignes, pas du contenu affichable
const NOT_DISPLAYED = ["Objectif", "Visuel", "Entités à rendre explicites", "Schema", "Liens internes prioritaires", "Règle d’affichage", "Person ID", "URL"];

// Espaces insécables et trait d'union insécable ramenés à leur forme simple avant comparaison
const INVISIBLES = new RegExp("[" + String.fromCharCode(0x00a0, 0x202f) + "]", "g");
const NBHY = new RegExp(String.fromCharCode(0x2011), "g");
const norm = (s) =>
  s
    .replace(INVISIBLES, " ")
    .replace(NBHY, "-")
    .replace(/\*\*|`|\*/g, "")
    .replace(/\s+/g, " ")
    .trim();
const low = (s) => norm(s).toLocaleLowerCase("fr");

// Texte visible d'une page construite
async function pageText(file) {
  const html = await readFile(file, "utf8");
  const body = html
    // texte réservé aux lecteurs d'écran (« Sources 1 à 3 » dans les renvois) : hors comparaison
    .replace(/<span class="visually-hidden">[^<]*<\/span>/g, "")
    .replace(/<script[\s\S]*?<\/script>/g, " ")
    .replace(/<style[\s\S]*?<\/style>/g, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">");
  const title = (html.match(/<title>([^<]*)<\/title>/) ?? [])[1] ?? "";
  const desc = (html.match(/<meta name="description" content="([^"]*)"/) ?? [])[1] ?? "";
  return { html, text: norm(body), title: norm(title.replace(/&amp;/g, "&")), desc: norm(desc.replace(/&amp;/g, "&")) };
}

// Toutes les chaînes d'un objet de contenu, avec leur chemin
function strings(obj, path = []) {
  if (typeof obj === "string") return [{ path: path.join("."), value: obj }];
  if (Array.isArray(obj)) return obj.flatMap((v, i) => strings(v, [...path, i]));
  if (obj && typeof obj === "object") return Object.entries(obj).flatMap(([k, v]) => strings(v, [...path, k]));
  return [];
}
const SKIP_KEYS = /(^|\.)(href|id|media|verifiedIso|updatedIso|year|n)$/;
// Textes gardés dans les données pour la traçabilité, mais non affichés (D19)
const NOT_SHOWN_KEYS = /(^|\.)supports$/;

// Passages affichables d'un fichier du pack
function segments(md, { labels = false } = {}) {
  const out = [];
  let section = "";
  let skip = false;
  let inFaq = false;
  for (const raw of md.split("\n")) {
    const line = raw.trim();
    if (!line || line === "---") continue;
    const h = line.match(/^(#{1,3})\s+(.*)$/);
    if (h) {
      const title = h[2].trim();
      if (h[1] === "#") {
        inFaq = /^FAQ$/i.test(title);
        section = title;
        const lab = title.match(/^SECTION \d+ — (.+)$/);
        if (lab && labels) out.push({ text: lab[1], kind: "étiquette de section", ci: true });
        skip = /^(SEO|SOURCES SCIENTIFIQUES|PAGE \d)/.test(title);
        if (/^SOURCES SCIENTIFIQUES/.test(title)) skip = "sources";
      } else {
        skip = NOT_DISPLAYED.some((n) => title.startsWith(n)) ? true : skip === "sources" ? "sources" : /^(Title|Meta)$/.test(title) ? "seo" : section.startsWith("SEO") ? true : false;
        if (inFaq && h[1] === "##") out.push({ text: title, kind: "question FAQ" });
      }
      continue;
    }
    if (skip === true) continue;
    if (skip === "seo") {
      const b = line.match(/^\*\*(.+)\*\*$/);
      if (b) out.push({ text: b[1], kind: "référencement" });
      continue;
    }
    if (skip === "sources") {
      const ref = line.match(/^\*\*\[(\d)\] (.+?)\*\* (.+?)\s*$/);
      if (ref) {
        out.push({ text: ref[2], kind: "source (auteurs)" });
        out.push({ text: ref[3].replace(/\*/g, ""), kind: "source (titre, revue)" });
      }
      const doi = line.match(/^DOI: `(.+)`/);
      if (doi) out.push({ text: doi[1], kind: "source (DOI)" });
      const pm = line.match(/^PubMed: (\S+)/);
      if (pm) out.push({ text: pm[1], kind: "source (lien PubMed)", html: true });
      const sup = line.match(/^\*\*Soutient :\*\* (.+)$/);
      if (sup) out.push({ text: "Soutient : " + sup[1], kind: "source (note)" });
      const date = line.match(/^\*\*(\d+ \w+ \d{4})\*\*$/);
      if (date) out.push({ text: date[1], kind: "date de vérification" });
      if (line.startsWith("Les références ci-dessous")) out.push({ text: line.split(". ")[0] + ".", kind: "source (introduction)" });
      continue;
    }
    if (line.startsWith("> ")) {
      out.push({ text: line.slice(2), kind: "texte" });
      continue;
    }
    const bold = line.match(/^\*\*(.+)\*\*$/);
    if (bold) {
      out.push({ text: bold[1], kind: "titre ou libellé" });
      continue;
    }
    const step = line.match(/^\d+\. \*\*(.+?)\*\* — (.+)$/);
    if (step) {
      out.push({ text: step[1], kind: "étape" }, { text: step[2], kind: "étape" });
      continue;
    }
    const li = line.match(/^- (.+)$/);
    if (li && !li[1].startsWith("`")) {
      out.push({ text: li[1], kind: "élément de liste" });
      continue;
    }
    const label = line.match(/^(.+?)\s*:$/);
    if (label && !STRUCTURE.test(label[1])) {
      out.push({ text: label[1], kind: "légende de liste", ci: true });
      continue;
    }
    if (inFaq && !line.startsWith("#")) out.push({ text: line, kind: "réponse FAQ" });
  }
  return out;
}

const packFiles = await Promise.all(
  ["02_HOME.md", "03_FRANCK_MOYAL.md", "04_USURES_DENTAIRES.md", "07_ART_DIRECTION.md"].map((f) => readFile(`${PACK}/${f}`, "utf8")),
);
const echange = (await Promise.all(ECHANGES.map((f) => readFile(f, "utf8")))).join("\n");
const allSources = norm(packFiles.join("\n") + "\n" + echange);
const allSourcesLow = allSources.toLocaleLowerCase("fr");

let problems = 0;
const report = [];
const note = (s) => report.push(s);

// 1 et 2, page par page
const pages = [
  { name: "Accueil", file: "dist/index.html", content: home, md: packFiles[0] },
  { name: "Dr Franck Moyal", file: "dist/franck-moyal/index.html", content: franck, md: packFiles[1] },
  { name: "Usures dentaires", file: "dist/usures-dentaires/index.html", content: usures, md: packFiles[2], labels: true },
];
for (const page of pages) {
  const { html, text, title, desc } = await pageText(page.file);
  const low_text = text.toLocaleLowerCase("fr");
  let checked = 0, invented = [], lost = [], decided = [];
  for (const { path, value } of strings(page.content)) {
    if (SKIP_KEYS.test(path)) continue;
    const v = norm(value);
    checked++;
    const decision = DECISIONS.find((d) => norm(d.site) === v);
    if (decision) decided.push(`${decision.ref} : « ${decision.pack} » → « ${v} »`);
    else if (!allSources.includes(v) && !allSourcesLow.includes(v.toLocaleLowerCase("fr"))) invented.push(`${path} : « ${v} »`);
    const inPage = NOT_SHOWN_KEYS.test(path) ? true : /pubmed$/.test(path) ? html.includes(v) : path === "seo.title" ? title === v : path === "seo.description" ? desc === v : text.includes(v) || low_text.includes(v.toLocaleLowerCase("fr"));
    if (!inPage) lost.push(`${path} : « ${v} »`);
  }
  // 3. Complétude : passages du pack présents dans la page
  let found = 0, missing = [], hidden = 0;
  for (const seg of segments(page.md, { labels: page.labels })) {
    const v = norm(seg.text);
    if (DECISIONS.some((d) => norm(d.pack) === v)) continue;
    if (HIDDEN.some((h) => h.kind === seg.kind)) { hidden++; continue; }
    const ok = seg.html ? html.includes(v) : seg.kind === "référencement" ? title === v || desc === v : text.includes(v) || (seg.ci && low_text.includes(v.toLocaleLowerCase("fr")));
    if (ok) found++;
    else missing.push(`[${seg.kind}] « ${v} »`);
  }
  problems += invented.length + lost.length + missing.length;
  note(`\n■ ${page.name} — ${checked} textes contrôlés, ${found} passages du pack retrouvés`);
  note(invented.length ? `  ✗ Absents du pack (inventés ou modifiés) :\n    ${invented.join("\n    ")}` : "  ✓ Aucun texte inventé ni modifié");
  note(lost.length ? `  ✗ Préparés mais absents de la page :\n    ${lost.join("\n    ")}` : "  ✓ Tous les textes préparés sont dans la page");
  note(missing.length ? `  ✗ Passages du pack absents de la page :\n    ${missing.join("\n    ")}` : "  ✓ Aucun passage du pack oublié");
  if (decided.length) note(`  • Remplacements décidés :\n    ${decided.join("\n    ")}`);
  if (hidden) note(`  • ${hidden} passage(s) du pack volontairement non affiché(s) : ${HIDDEN.map((h) => `${h.why} (${h.ref})`).join(", ")}`);
}

// Menu et pied de page : libellés issus de la réponse de ChatGPT (menu) et du pack (pied de page)
const chrome = [
  ...nav.flatMap((n) => [n.label, ...(n.children ?? []).map((c) => c.label)]),
  ...footer.groups.flat().map((l) => l.label),
  footer.contactLabel,
  footer.address,
  footer.legal.label,
];
const unknown = chrome.filter((l) => !allSourcesLow.includes(low(l)));
problems += unknown.length;
note(`\n■ Menu et pied de page — ${chrome.length} libellés`);
note(unknown.length ? `  ✗ Libellés sans source : ${unknown.join(", ")}` : "  ✓ Tous les libellés viennent du pack ou de la réponse de ChatGPT");

// Pages du pack « pages suivantes »
const pack = await verifyPack();
problems += pack.problems;
report.push(...pack.out);

// « Dentiste esthétique » : jamais (verrou V21), sur toutes les pages construites
for (const f of builtPages.map((u) => `dist${u}index.html`)) {
  const raw = await readFile(f, "utf8");
  if (/dentiste esth/i.test(raw)) {
    problems++;
    note(`  ✗ « dentiste esthétique » trouvé dans ${f}`);
  }
}
note("\n■ Verrou V21 — « dentiste esthétique » : " + (problems && report.some((r) => r.includes("dentiste esthétique » trouvé")) ? "présent ✗" : "absent partout ✓"));

console.log(report.join("\n"));
if (pack.warnings) console.log(`\n${pack.warnings} écart(s) du pack signalé(s) (⚠), à corriger par ChatGPT : ils ne bloquent pas la construction.`);
console.log(problems ? `\n${problems} écart(s) à examiner.` : "\nContrôle réussi : aucun écart de construction.");
process.exit(problems ? 1 : 0);
