// Contrôle du HTML et des informations pour les moteurs (livrable 9 de 06_PROMPT_CLAUDE_CODE).
// Un seul H1, intertitres sans saut de niveau, titre, description, adresse de référence,
// langue, images décrites, données structurées conformes au pack, plan du site, robots.
// Lancer après « npm run build » : node scripts/check-html.mjs
import { readFile } from "node:fs/promises";
import { parse } from "node-html-parser";

const pages = [
  { file: "dist/index.html", url: "https://drfranckmoyal.fr/", types: ["WebSite", "Person"] },
  { file: "dist/franck-moyal/index.html", url: "https://drfranckmoyal.fr/franck-moyal/", types: ["ProfilePage", "Person"] },
  { file: "dist/usures-dentaires/index.html", url: "https://drfranckmoyal.fr/usures-dentaires/", types: ["MedicalWebPage", "BreadcrumbList", "Person"] },
];
let problems = 0;
const bad = (m) => { problems++; console.log("  ✗ " + m); };
const ok = (m) => console.log("  ✓ " + m);

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
  const ld = root.querySelectorAll('script[type="application/ld+json"]');
  try {
    const graph = ld.flatMap((s) => JSON.parse(s.text)["@graph"] ?? []);
    const types = graph.map((n) => n["@type"]);
    const missing = p.types.filter((t) => !types.includes(t));
    missing.length ? bad(`données structurées : manque ${missing.join(", ")}`) : ok(`données structurées : ${types.join(", ")}`);
    const person = graph.find((n) => n["@type"] === "Person");
    person?.["@id"] === "https://drfranckmoyal.fr/#franck-moyal" ? ok("identifiant de Franck : …/#franck-moyal") : bad("identifiant de Franck absent");
  } catch (e) {
    bad("données structurées illisibles : " + e.message);
  }
  const future = root.querySelectorAll("[data-a-venir]").map((a) => a.getAttribute("href"));
  console.log(`  • ${new Set(future).size} adresses de pages à venir en lien : ${[...new Set(future)].sort().join(" ")}`);
  const ext = root.querySelectorAll('a[target="_blank"]');
  const unsafe = ext.filter((a) => !/noopener/.test(a.getAttribute("rel") ?? "") || !/noreferrer/.test(a.getAttribute("rel") ?? ""));
  if (ext.length) unsafe.length ? bad(`${unsafe.length} lien(s) externe(s) sans rel="noopener noreferrer"`) : ok(`${ext.length} liens externes, tous en rel="noopener noreferrer"`);
}

const sitemap = await readFile("dist/sitemap-0.xml", "utf8");
const locs = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
console.log(`\n■ Plan du site : ${locs.join(", ")}`);
locs.length === 3 ? ok("les 3 pages, et elles seules") : bad(`${locs.length} adresses`);
const robots = await readFile("dist/robots.txt", "utf8");
/Sitemap: https:\/\/drfranckmoyal\.fr\/sitemap-index\.xml/.test(robots) && /Allow: \//.test(robots)
  ? ok("robots.txt : tout est ouvert aux moteurs, plan du site déclaré")
  : bad("robots.txt incomplet");

console.log(problems ? `\n${problems} problème(s).` : "\nContrôle HTML réussi.");
process.exit(problems ? 1 : 0);
