// Chargement des 20 fichiers du pack « pages suivantes » au moment de fabriquer le site, et
// résolution des libellés de liens et du fil d'Ariane vers les adresses définitives (V4).
import { parsePack, type PackPage } from "./pack.ts";
import { applyDecisions, arborescence, builtNums, knownLabels, linkOverrides, packReplacements, PACK_DIR, PATCH_DIR } from "../content/pages-suivantes.ts";

// Nouvelle version du pack : changer ces chemins — ils doivent rester écrits en toutes lettres —,
// et PACK_DIR / PATCH_DIR dans src/content/pages-suivantes.ts.
const raw = import.meta.glob(
  [
    "/docs/pages-suivantes/v1.2/[0-9][0-9]_*.md",
    "/docs/pages-suivantes/v1.3/[0-9][0-9]_*.md",
    "/docs/pages-suivantes/v1.4/[0-9][0-9]_*.md",
    "/docs/pages-suivantes/v1.5/[0-9][0-9]_*.md",
    "/docs/pages-suivantes/v1.6/[0-9][0-9]_*.md",
    "/docs/pages-suivantes/v1.7/[0-9][0-9]_*.md",
  ],
  {
    query: "?raw",
    import: "default",
    eager: true,
  },
) as Record<string, string>;

// Une page par numéro de l'arborescence : son fichier du correctif V1.3 s'il la remplace, sinon
// celui de la V1.2 (les autres fichiers du correctif sont des fiches de décisions, pas des pages)
const fileOf = (num: string) => {
  const path = packReplacements[num]
    ? `/${packReplacements[num]}`
    : Object.keys(raw).find((p) => p.startsWith(`/${PACK_DIR}/${num}_`));
  if (!path || !(path in raw)) throw new Error(`Page ${num} : fichier du pack introuvable (${path ?? "aucun"})`);
  return path;
};

export const packPages: PackPage[] = arborescence
  .map((a) => fileOf(a.num))
  .map((path) => ({ file: path.split("/").pop()!, md: raw[path] }))
  .map(({ file, md }) => parsePack(applyDecisions(md, file.slice(0, 2)).md, file))
  .sort((a, b) => a.num.localeCompare(b.num));

// Le fichier et l'arborescence doivent donner la même adresse
for (const p of packPages) {
  const expected = arborescence.find((a) => a.num === p.num)?.url;
  if (p.url !== expected) throw new Error(`${p.file} : adresse ${p.url} ≠ arborescence ${expected}`);
}

export const builtPackPages = () => packPages.filter((p) => builtNums.includes(p.num));

// Libellé → adresse : pages du golden master, liens « Liens internes » de chaque fichier,
// dernier élément du fil d'Ariane de chaque page, liens déduits.
const table = new Map<string, string>(Object.entries(knownLabels));
for (const p of packPages) {
  for (const l of p.links) if (!table.has(l.label)) table.set(l.label, l.href);
  const own = p.crumbs.at(-1)!;
  if (!table.has(own)) table.set(own, p.url);
}
for (const [label, href] of Object.entries(linkOverrides)) table.set(label, href);

export function resolveLink(page: PackPage, label: string): string {
  const href = page.links.find((l) => l.label === label)?.href ?? table.get(label);
  if (!href) throw new Error(`${page.file} : aucun lien connu pour « ${label} »`);
  return href;
}

// Fil d'Ariane : les libellés du fichier, les adresses de la chaîne des pages parentes
const parents: Record<string, string> = { "/usures-dentaires/": "/", "/franck-moyal/": "/" };
for (const p of packPages) parents[p.url] = p.parent;

export function crumbTrail(page: PackPage): { label: string; href: string }[] {
  const chain = [page.url];
  while (parents[chain[0]] && parents[chain[0]] !== "/") chain.unshift(parents[chain[0]]);
  chain.unshift("/");
  if (chain.length !== page.crumbs.length) {
    throw new Error(`${page.file} : fil d'Ariane « ${page.crumbs.join(" > ")} » ≠ pages parentes ${chain.join(" ")}`);
  }
  return page.crumbs.map((label, i) => ({ label, href: chain[i] }));
}
