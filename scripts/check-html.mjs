// Contrôle du HTML et des informations pour les moteurs (livrable 9 de 06_PROMPT_CLAUDE_CODE),
// sur toutes les pages construites : un seul H1, intertitres sans saut de niveau, titre,
// description, adresse de référence, langue, images décrites, données structurées conformes au
// pack, plan du site, robots.
// Pages du pack « pages suivantes » : les 10 contrôles de 21_MANIFESTE_INTEGRATION.md (fil
// d'Ariane, dateModified, auteur relié à Person#franck-moyal, sources dans le HTML, liens
// descriptifs, aucune image inventée, réglages de design inchangés depuis le gel…).
// Lancer après « npm run build » : node scripts/check-html.mjs
import { readFile, readdir } from "node:fs/promises";
import { execSync } from "node:child_process";
import { parse } from "node-html-parser";
import { parsePack } from "../src/lib/pack.ts";
import { builtNums, PACK_DIR } from "../src/content/pages-suivantes.ts";

const SITE = "https://drfranckmoyal.fr";
const PERSON = `${SITE}/#franck-moyal`;
const pages = [
  { file: "dist/index.html", url: `${SITE}/`, types: ["WebSite", "Person"] },
  { file: "dist/franck-moyal/index.html", url: `${SITE}/franck-moyal/`, types: ["ProfilePage", "Person"] },
  { file: "dist/usures-dentaires/index.html", url: `${SITE}/usures-dentaires/`, types: ["MedicalWebPage", "BreadcrumbList", "Person"] },
];

// Pages du pack : ce que le fichier impose
const packFiles = (await readdir(PACK_DIR)).filter((f) => /^\d\d_/.test(f) && !/^(00|21)_/.test(f));
const all = await Promise.all(packFiles.map(async (f) => parsePack(await readFile(`${PACK_DIR}/${f}`, "utf8"), f)));
const parents = { "/usures-dentaires/": "/", "/franck-moyal/": "/" };
for (const p of all) parents[p.url] = p.parent;
for (const p of all.filter((p) => builtNums.includes(p.num))) {
  const chain = [p.url];
  while (parents[chain[0]] && parents[chain[0]] !== "/") chain.unshift(parents[chain[0]]);
  chain.unshift("/");
  pages.push({
    file: `dist${p.url}index.html`,
    url: SITE + p.url,
    types: [...p.seo.schema.filter((t) => /Page$/.test(t) || t === "Article"), "BreadcrumbList", "Person"],
    pack: p,
    chain: chain.map((u) => SITE + u),
  });
}

let problems = 0;
const bad = (m) => {
  problems++;
  console.log("  ✗ " + m);
};
const ok = (m) => console.log("  ✓ " + m);
const info = (m) => console.log("  • " + m);
const VAGUE = /^(en savoir plus|lire la suite|cliquez ici|ici|voir plus|plus d’infos?)$/i;

for (const p of pages) {
  const root = parse(await readFile(p.file, "utf8"));
  console.log(`\n■ ${p.url}`);
  const h1 = root.querySelectorAll("h1");
  h1.length === 1 ? ok(`un seul H1 : « ${h1[0].text.trim()} »`) : bad(`${h1.length} H1`);
  const levels = root.querySelectorAll("h1, h2, h3, h4, h5, h6").map((h) => Number(h.tagName[1]));
  const jumps = levels.filter((l, i) => i > 0 && l > levels[i - 1] + 1);
  jumps.length ? bad(`saut de niveau d'intertitre (${levels.join(" ")})`) : ok(`${levels.length} titres, aucun saut de niveau (H2 : ${levels.filter((l) => l === 2).length}, H3 : ${levels.filter((l) => l === 3).length})`);
  const lang = root.querySelector("html")?.getAttribute("lang");
  lang === "fr" ? ok("langue : fr") : bad(`langue : ${lang}`);
  const title = root.querySelector("title")?.text ?? "";
  title ? ok(`titre (${title.length} caractères)`) : bad("titre absent");
  const desc = root.querySelector('meta[name="description"]')?.getAttribute("content") ?? "";
  desc ? ok(`description (${desc.length} caractères)`) : bad("description absente");
  const canon = root.querySelector('link[rel="canonical"]')?.getAttribute("href");
  canon === p.url ? ok(`adresse de référence : ${canon}`) : bad(`adresse de référence : ${canon}`);
  const imgs = root.querySelectorAll("img");
  const noAlt = imgs.filter((i) => i.getAttribute("alt") === undefined);
  noAlt.length ? bad(`${noAlt.length} image(s) sans attribut alt`) : ok(`${imgs.length} image(s), toutes avec un attribut alt`);
  const main = root.querySelectorAll("main");
  main.length === 1 ? ok("une zone principale <main>") : bad(`${main.length} <main>`);
  let graph = [];
  try {
    graph = root.querySelectorAll('script[type="application/ld+json"]').flatMap((s) => JSON.parse(s.text)["@graph"] ?? []);
    const types = graph.flatMap((n) => [n["@type"]].flat());
    const missing = p.types.filter((t) => !types.includes(t));
    missing.length ? bad(`données structurées : manque ${missing.join(", ")}`) : ok(`données structurées : ${types.join(", ")}`);
    const person = graph.find((n) => n["@type"] === "Person");
    person?.["@id"] === PERSON ? ok("identifiant de Franck : …/#franck-moyal") : bad("identifiant de Franck absent");
  } catch (e) {
    bad("données structurées illisibles : " + e.message);
  }
  const future = root.querySelectorAll("[data-a-venir]").map((a) => a.getAttribute("href"));
  info(`${new Set(future).size} adresses de pages à venir en lien : ${[...new Set(future)].sort().join(" ")}`);
  const ext = root.querySelectorAll('a[target="_blank"]');
  const unsafe = ext.filter((a) => !/noopener/.test(a.getAttribute("rel") ?? "") || !/noreferrer/.test(a.getAttribute("rel") ?? ""));
  if (ext.length) unsafe.length ? bad(`${unsafe.length} lien(s) externe(s) sans rel="noopener noreferrer"`) : ok(`${ext.length} liens externes, tous en rel="noopener noreferrer"`);

  // Ancres internes à la page : chaque « #… » mène à un élément existant
  const ids = new Set(root.querySelectorAll("[id]").map((e) => e.getAttribute("id")));
  const anchors = [...new Set(root.querySelectorAll('a[href^="#"]').map((a) => a.getAttribute("href")))].filter((h) => h !== "#");
  const broken = anchors.filter((h) => !ids.has(h.slice(1)) && h !== "#rendez-vous");
  broken.length ? bad(`ancres sans cible : ${broken.join(" ")}`) : ok(`${anchors.length} ancres internes, toutes avec une cible`);
  if (anchors.includes("#rendez-vous") && !ids.has("rendez-vous")) info("pas de bloc d'appel final : le bouton « Prendre rendez-vous » de l'en-tête (lien encore à fournir) ne mène nulle part sur cette page");

  if (!p.pack) continue;
  // --- Contrôles du manifeste (pages suivantes) ---
  const pk = p.pack;
  // 2. Fil d'Ariane visible et BreadcrumbList
  const crumbs = root.querySelectorAll("nav.breadcrumbs li").map((li) => li.text.trim());
  const bl = graph.find((n) => n["@type"] === "BreadcrumbList");
  const blNames = bl?.itemListElement.map((i) => i.name) ?? [];
  const blUrls = bl?.itemListElement.map((i) => i.item) ?? [];
  JSON.stringify(crumbs) === JSON.stringify(pk.crumbs) && JSON.stringify(blNames) === JSON.stringify(pk.crumbs) && JSON.stringify(blUrls) === JSON.stringify(p.chain)
    ? ok(`fil d'Ariane conforme : ${crumbs.join(" > ")}`)
    : bad(`fil d'Ariane : page « ${crumbs.join(" > ")} », données « ${blNames.join(" > ")} » (${blUrls.join(" ")}), pack « ${pk.crumbs.join(" > ")} »`);
  // 3. Title et meta du pack
  title === pk.seo.title && desc === pk.seo.description ? ok("title et meta description : ceux du pack") : bad("title ou meta description différents du pack");
  // 4 et 5. Page : dateModified, auteur relié à Person#franck-moyal
  const node = graph.find((n) => [n["@type"]].flat().some((t) => /Page$/.test(t)));
  node?.dateModified === pk.author.iso ? ok(`dateModified : ${node.dateModified}`) : bad(`dateModified : ${node?.dateModified}`);
  node?.author?.["@id"] === PERSON ? ok("auteur relié à …/#franck-moyal") : bad("auteur non relié à Person#franck-moyal");
  // 6. Sources dans le HTML
  if (pk.sources.length) {
    const items = root.querySelectorAll("li.source").length;
    items === pk.sources.length ? ok(`${items} sources scientifiques dans le HTML`) : bad(`${items} sources dans la page, ${pk.sources.length} dans le pack`);
  }
  // 7. Liens internes descriptifs
  const internal = root.querySelectorAll("main a[href^='/']").map((a) => a.text.trim());
  const vague = internal.filter((t) => VAGUE.test(t));
  vague.length ? bad(`liens peu descriptifs : ${vague.join(", ")}`) : ok(`${internal.length} liens internes, tous avec un libellé descriptif`);
  // 9. Aucune image inventée : seule la photo du Dr Moyal (bloc auteur) est une vraie image
  const images = root.querySelectorAll("main img").map((i) => i.getAttribute("src"));
  const foreign = images.filter((src) => !/portrait-franck/.test(src));
  foreign.length ? bad(`images inattendues : ${foreign.join(" ")}`) : ok(`aucune image inventée (${root.querySelectorAll("main [data-emplacement='visuel']").length} emplacement(s) réservé(s))`);
  // Consigne aux moteurs
  const robots = root.querySelector('meta[name="robots"]')?.getAttribute("content");
  (robots ?? "") === (pk.seo.robots ?? "") ? ok(`consigne aux moteurs : ${robots ?? "aucune (page indexable)"}`) : bad(`consigne aux moteurs : ${robots} au lieu de ${pk.seo.robots}`);
}

// 8 et 10. « Dentiste esthétique » (contrôle des textes) ; réglages de design inchangés depuis le gel
console.log("\n■ Réglages de design (src/styles/tokens.css)");
try {
  execSync("git diff --quiet golden-master-gele -- src/styles/tokens.css");
  ok("identiques à la version gelée (étiquette golden-master-gele)");
} catch {
  bad("modifiés depuis le gel");
}

const sitemap = await readFile("dist/sitemap-0.xml", "utf8");
const locs = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const expected = pages.filter((p) => !p.pack?.seo.robots?.includes("noindex")).map((p) => p.url);
console.log(`\n■ Plan du site : ${locs.length} adresses`);
JSON.stringify([...locs].sort()) === JSON.stringify([...expected].sort())
  ? ok(`les ${expected.length} pages indexables construites, et elles seules`)
  : bad(`plan du site : ${locs.join(", ")} ; attendu : ${expected.join(", ")}`);
const robots = await readFile("dist/robots.txt", "utf8");
/Sitemap: https:\/\/drfranckmoyal\.fr\/sitemap-index\.xml/.test(robots) && /Allow: \//.test(robots)
  ? ok("robots.txt : tout est ouvert aux moteurs, plan du site déclaré")
  : bad("robots.txt incomplet");

console.log(problems ? `\n${problems} problème(s).` : "\nContrôle HTML réussi.");
process.exit(problems ? 1 : 0);
