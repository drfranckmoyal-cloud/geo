// Contrôle des textes des pages du pack « pages suivantes » (docs/pages-suivantes/v1), lancé
// par verify-texts.mjs. Il relit les fichiers du pack par ses propres moyens (sans passer par
// le programme qui fabrique les pages) et compare avec les pages construites (dist/) :
//  1. Rien d'oublié : chaque passage affichable du fichier (titres, textes, listes, liens, FAQ,
//     appel final, auteur, sources, title et meta) se retrouve dans la page.
//  2. Rien d'inventé : chaque texte de la zone principale de la page existe dans le fichier du
//     pack, ou fait partie des libellés d'interface validés au golden master.
//  3. Renvois bibliographiques : chaque renvoi [n] du texte a sa référence dans la liste, et
//     chaque référence est citée (écarts du pack, signalés sans bloquer).
// Les passages volontairement non affichés (src/content/pages-suivantes.ts) sont listés.
import { readFile } from "node:fs/promises";
import { readdirSync } from "node:fs";
import { parse } from "node-html-parser";
import { applyDecisions, arborescence, builtNums, hidden, layouts, linkOverrides, packPath, shownSourceNotes, PACK_DIR } from "../src/content/pages-suivantes.ts";
import { home } from "../src/content/home.ts";
import { usures } from "../src/content/usures.ts";

const INVISIBLES = new RegExp("[" + String.fromCharCode(0x00a0, 0x202f) + "]", "g");
const norm = (s) =>
  s
    .replace(INVISIBLES, " ")
    .replace(/\*\*|`|\*/g, "")
    .replace(/\s+/g, " ")
    .trim();
const low = (s) => norm(s).toLocaleLowerCase("fr");
// « [À FOURNIR] » s'affiche comme un emplacement réservé « à fournir »
const placeholders = (s) => s.replace(/\[([^\]]*À FOURNIR[^\]]*)\]/g, (_, x) => x.toLowerCase().replace("url", "URL"));

// Libellés d'interface validés au golden master (page Usures, D19–D21, D31) et au pack
const UI_EXACT = [
  "Accueil",
  "FAQ",
  "À lire aussi",
  usures.sources.title,
  usures.sources.intro,
  usures.author.label,
  usures.author.tagline,
  home.method.title,
  ...home.method.steps.flatMap((s) => [s.name, s.text]),
].map(norm);
const UI_PATTERNS = [/^Voir les \d+ sources scientifiques$/, /^\[\d+\]$/, /^DOI\s?: \S+?\s?PubMed$/, /^Mis à jour le \d{1,2} \S+ \d{4}$/];

// Légendes, étiquettes et attribution des cas cliniques : textes décidés par ChatGPT hors du pack
// (intégration des photographies du 24/09/2026). Le registre est lu tel quel, sans charger les
// images, que Node ne sait pas résoudre.
// Textes des pages de cas cliniques décidés hors du pack (POINT 3, phase B) : la mention commune
// de fin de page et les trois annonces posées dans les pages thérapeutiques.
const casPages = await readFile("src/content/cas-pages.ts", "utf8");
const CAS_PAGES_TEXTES = [
  ...[...casPages.matchAll(/^\s*"(.+?)";$/gm)].map((m) => m[1]),
  ...[...casPages.matchAll(/(?:probleme|approche|label): "(.+?)",/g)].map((m) => m[1]),
].map(norm);

const registre = await readFile("src/content/cas-cliniques.ts", "utf8");
const attribution = registre.match(/const ATTRIBUTION = "(.+?)";/)[1];
const CAS_TEXTES = [
  ...[...registre.matchAll(/legende: "(.+?)",/g)].flatMap((m) => [m[1], `${m[1]}${attribution}`]),
  ...[...registre.matchAll(/etiquette: "(.+?)"/g)].map((m) => m[1]),
  attribution,
].map(norm);

function specSections(md) {
  const out = new Map();
  const parts = md.split(/^## (\d+)\. .*$/m);
  for (let i = 1; i < parts.length; i += 2) out.set(Number(parts[i]), parts[i + 1]);
  return out;
}
const field = (text, label) => (text.split("\n").find((l) => l.startsWith(`- **${label}** : `)) ?? "").replace(`- **${label}** : `, "").trim();

// Passages affichables d'un fichier du pack
function segments(md, num) {
  const spec = specSections(md);
  const segs = [];
  const add = (text, kind, where = "text") => text && segs.push({ text, kind, where });
  add(field(spec.get(2), "H1"), "H1");
  add(field(spec.get(2), "Chapeau"), "chapeau");
  for (const line of (spec.get(3) ?? "").split("\n").map((l) => l.trim())) if (line && !line.startsWith("- ")) add(line, "réponse directe");

  const masks = hidden[num] ?? [];
  const skipped = [];
  let inHiddenSection = false;
  for (const para of (spec.get(5) ?? "").split(/\n\s*\n/)) {
    const lines = para.split("\n").map((l) => l.trim()).filter((l) => l && l !== "---");
    if (!lines.length) continue;
    if (masks.some((m) => m.text && lines[0].startsWith(m.text))) {
      skipped.push(lines.join(" "));
      continue;
    }
    for (const line of lines) {
      const h = line.match(/^(#{1,3}) (.+)$/);
      if (h) {
        inHiddenSection = masks.some((m) => m.section === h[2]);
        if (inHiddenSection) skipped.push(h[2]);
        else if (h[2] !== "CTA") add(h[2], `titre ${h[1]}`);
        continue;
      }
      if (inHiddenSection) {
        skipped.push(line);
        continue;
      }
      let m;
      // Tableau comparatif : chaque cellule est rendue séparément (la ligne de tirets ne l'est pas)
      if (/^\|.*\|$/.test(line)) {
        const cells = line.slice(1, -1).split("|").map((c) => c.trim());
        if (!cells.every((c) => /^:?-{2,}:?$/.test(c))) for (const cell of cells) add(cell, "cellule de tableau");
        continue;
      }
      if ((m = line.match(/^- (.+)$/))) add(m[1], "élément de liste");
      else if ((m = line.match(/^\d+\. (.+)$/))) add(m[1], "étape numérotée");
      else if ((m = line.match(/^→ \*\*(.+)\*\*$/))) add(m[1], "lien");
      else if ((m = line.match(/^\*\*CTA : (.+)\*\*$/))) add(m[1], "bouton");
      else if (/^https?:\/\/\S+$/.test(line)) add(line, "adresse de preuve", "html");
      else add(line, "texte");
    }
  }
  const author = spec.get(7) ?? "";
  const contract = (spec.get(4) ?? "").split("\n").map((l) => l.replace(/^- /, "").replace(/\*\*/g, "").trim());
  // Le nom de l'auteur s'affiche dans la ligne auteur de l'ouverture, quand le fichier en nomme un
  // (pas sur Contact ni Mentions légales, V1.2)
  if (!layouts[num]?.hideByline) add(field(author, "Auteur"), "auteur");
  // La date s'affiche dans le bloc auteur, quand le contrat le prévoit (« `AuthorBlock` court… » ;
  // jamais « Pas d'`AuthorBlock` ») ; sinon elle figure dans les données structurées (dateModified)
  if (contract.some((c) => /^`AuthorBlock`/.test(c))) add(field(author, "Date de mise à jour"), "date de mise à jour");
  // Titre du bloc MethodSteps donné par le contrat (page 02)
  const methodTitle = (contract.join("\n").match(/`MethodSteps`[^\n]*titre « (.+?) »/) ?? [])[1];
  if (methodTitle) add(methodTitle, "titre de la méthode");
  add(field(spec.get(8), "Title"), "title", "title");
  add(field(spec.get(8), "Meta description"), "meta description", "desc");
  const notesShown = shownSourceNotes[num] ?? [];
  const sourceLines = (spec.get(10) ?? "").split("\n").map((l) => l.trim());
  sourceLines.forEach((line, i) => {
    let m;
    if ((m = line.match(/^\*\*\[\d+\] (.+)$/))) add(m[1], "source");
    else if ((m = line.match(/^DOI: `([^`]+)`/))) add(m[1], "source (DOI)");
    else if ((m = line.match(/^PubMed: (\S+)/))) add(m[1], "source (lien PubMed)", "html");
    else if (notesShown.some((n) => line.startsWith(n))) {
      add(line, "note sous les sources");
      if (/^https?:\/\/\S+$/.test(sourceLines[i + 1] ?? "")) add(sourceLines[i + 1], "note sous les sources (adresse)", "html");
    }
  });
  return { segs, skipped };
}

// Textes visibles de la zone principale : un par bloc (paragraphe, élément de liste, titre…)
const BLOCKS = new Set(["P", "LI", "H1", "H2", "H3", "H4", "SUMMARY", "BLOCKQUOTE", "FIGCAPTION"]);
function mainBlocks(root) {
  const main = root.querySelector("main");
  for (const el of main.querySelectorAll("script, style, svg, .visually-hidden, figure[data-emplacement]")) el.remove();
  const groups = new Map();
  const blockOf = (node) => {
    let el = node.parentNode;
    while (el && el !== main && !BLOCKS.has(el.tagName) && !el.classList?.contains("step__name") && !el.classList?.contains("step__text")) el = el.parentNode;
    return el && el !== main ? el : node.parentNode;
  };
  const walk = (node) => {
    for (const child of node.childNodes) {
      if (child.nodeType === 3) groups.set(blockOf(child), (groups.get(blockOf(child)) ?? "") + child.text);
      else if (child.nodeType === 1 && child.tagName === "BR") groups.set(blockOf(child), (groups.get(blockOf(child)) ?? "") + " ");
      else if (child.nodeType === 1) walk(child);
    }
  };
  walk(main);
  return [...groups.values()].map(norm).filter(Boolean);
}

function citations(md) {
  const spec = specSections(md);
  const text = [spec.get(2), spec.get(3), spec.get(5)].join("\n");
  const cited = new Set();
  for (const m of text.matchAll(/\[(\d+(?:[–,-]\d+)*)\]/g)) {
    for (const part of m[1].split(",")) {
      const [a, b] = part.split(/[–-]/).map(Number);
      for (let n = a; n <= (b || a); n++) cited.add(n);
    }
  }
  const listed = [...(spec.get(10) ?? "").matchAll(/^\*\*\[(\d+)\]/gm)].map((m) => Number(m[1]));
  return {
    missing: [...cited].filter((n) => !listed.includes(n)).sort((a, b) => a - b),
    uncited: [...new Set(listed)].filter((n) => !cited.has(n)),
    duplicates: listed.filter((n, i) => listed.indexOf(n) !== i),
  };
}

export async function verifyPack() {
  const out = [];
  let problems = 0;
  let warnings = 0;
  for (const num of builtNums) {
    const entry = arborescence.find((a) => a.num === num);
    const path = packPath(num, readdirSync(PACK_DIR));
    const file = path.split("/").pop();
    // Remplacements décidés par ChatGPT (validation du 22/09/2026, correctif V1.3), listés plus bas
    const { md, applied } = applyDecisions(await readFile(path, "utf8"), num);
    const html = await readFile(`dist${entry.url}index.html`, "utf8");
    const root = parse(html);
    const title = norm(root.querySelector("title")?.text ?? "");
    const desc = norm(root.querySelector('meta[name="description"]')?.getAttribute("content") ?? "");
    const blocks = mainBlocks(root);
    const pageText = blocks.join(" \n ");
    const pageLow = pageText.toLocaleLowerCase("fr");
    const packText = norm(placeholders(md)); // « [À FOURNIR] » s'affiche « à fournir »
    const packLow = packText.toLocaleLowerCase("fr");

    // 1. Rien d'oublié
    const { segs, skipped } = segments(md, num);
    const missing = [];
    for (const seg of segs) {
      const v = norm(placeholders(seg.text));
      const ok =
        seg.where === "html" ? html.includes(seg.text) : seg.where === "title" ? title === v : seg.where === "desc" ? desc === v : pageText.includes(v) || pageLow.includes(v.toLocaleLowerCase("fr"));
      if (!ok) missing.push(`[${seg.kind}] « ${v} »`);
    }
    // 2. Rien d'inventé (sauf les boutons de section décidés par ChatGPT, listés plus bas)
    const actions = Object.values(layouts[num]?.sections ?? {}).flatMap((o) => o.actions ?? []);
    const invented = blocks.filter(
      (b) =>
        !packText.includes(b) &&
        !packLow.includes(b.toLocaleLowerCase("fr")) &&
        !UI_EXACT.includes(b) &&
        !UI_PATTERNS.some((re) => re.test(b)) &&
        !CAS_TEXTES.includes(b) &&
        !CAS_PAGES_TEXTES.includes(b) &&
        // Suite d'étapes (gradient thérapeutique) : le composant écrit « 01 » devant le mot du pack
        !(/^\d{2}\S/.test(b) && packLow.includes(b.replace(/^\d{2}/, "").toLocaleLowerCase("fr"))) &&
        !actions.some((a) => norm(a.label) === b),
    );
    // 3. Renvois
    const cites = citations(md);
    const citeIssues = [
      cites.missing.length && `renvois sans référence dans la liste : ${cites.missing.join(", ")}`,
      cites.uncited.length && `références jamais citées : ${cites.uncited.join(", ")}`,
      cites.duplicates.length && `numéros en double : ${cites.duplicates.join(", ")}`,
    ].filter(Boolean);
    // Liens dont l'adresse est déduite (libellé absent de la liste « Liens internes »)
    const listedLinks = [...md.split(/^## 6\. .*$/m)[1]?.matchAll(/^- \*\*(.+?)\*\* →/gm) ?? []].map((m) => m[1]);
    const inline = [...md.matchAll(/^→ \*\*(.+)\*\*$/gm)].map((m) => m[1]);
    const deduced = inline.filter((l) => !listedLinks.includes(l) && linkOverrides[l]).map((l) => `« ${l} » → ${linkOverrides[l]}`);

    problems += missing.length + invented.length;
    warnings += citeIssues.length;
    out.push(`\n■ ${file.replace(/\.md$/, "")} — ${segs.length} passages du pack, ${blocks.length} blocs de texte dans la page`);
    out.push(missing.length ? `  ✗ Passages du pack absents de la page :\n    ${missing.join("\n    ")}` : "  ✓ Aucun passage du pack oublié");
    out.push(invented.length ? `  ✗ Textes de la page absents du pack :\n    ${invented.map((b) => `« ${b} »`).join("\n    ")}` : "  ✓ Aucun texte inventé ni modifié");
    if (citeIssues.length) out.push(`  ⚠ Écart du pack — ${citeIssues.join(" ; ")}`);
    for (const m of hidden[num] ?? []) out.push(`  • Non affiché (à confirmer par ChatGPT) : « ${norm(m.section ?? m.text)} » — ${m.why}`);
    if (deduced.length) out.push(`  • Liens à l'adresse déduite : ${deduced.join(" ; ")}`);
    for (const a of applied) out.push(`  • Remplacement décidé : ${a}`);
    for (const a of actions) out.push(`  • Bouton décidé hors du pack : « ${a.label} » → ${a.href} (fiche corrective du contact, correctif V1.3)`);
    for (const a of Object.values(layouts[num]?.sections ?? {}).flatMap((o) => (o.annonce ? [o.annonce] : [])))
      out.push(`  • Annonce d'un cas clinique : « ${a} » — texte décidé hors du pack (POINT 3, phase B)`);
    if (layouts[num]?.mentionClinique) out.push("  • Mention commune des pages de cas — texte décidé hors du pack (POINT 3 §32)");
    for (const id of Object.values(layouts[num]?.sections ?? {}).flatMap((o) => [o.cas ?? []].flat()))
      out.push(`  • Cas clinique affiché : « ${id} » — photographie réelle, légende décidée hors du pack (intégration du 24/09/2026)`);
    if (!/\*\*Auteur\*\* : /.test(md)) out.push("  • Ouverture sans ligne auteur (le fichier ne nomme pas d'auteur)");
    if (layouts[num]?.cta) out.push(`  • Bouton de l'appel final décidé hors du pack : « ${layouts[num].cta.label} » → ${layouts[num].cta.href} (validation 23)`);
    if (skipped.length && !(hidden[num] ?? []).length) out.push(`  ✗ Passages sautés sans décision : ${skipped.join(" / ")}`);
  }
  return { out, problems, warnings };
}
