// Chargement des 20 fichiers du pack « pages suivantes » au moment de fabriquer le site, et
// résolution des libellés de liens et du fil d'Ariane vers les adresses définitives (V4).
import { parsePack, type PackPage } from "./pack.ts";
import { arborescence, builtNums, knownLabels, linkOverrides } from "../content/pages-suivantes.ts";

// Nouvelle version du pack (docs/pages-suivantes/v1.1/…) : changer ce chemin — il doit rester
// écrit en toutes lettres — et PACK_DIR dans src/content/pages-suivantes.ts.
const raw = import.meta.glob("/docs/pages-suivantes/v1/[0-9][0-9]_*.md", {
  query: "?raw",
  import: "default",
  eager: true,
}) as Record<string, string>;

export const packPages: PackPage[] = Object.entries(raw)
  .map(([path, md]) => ({ file: path.split("/").pop()!, md }))
  .filter(({ file }) => !/^(00|21)_/.test(file))
  .map(({ file, md }) => parsePack(md, file))
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
