// Choix de la composition de chaque section d'une page du pack « pages suivantes », parmi
// celles des composants gelés (TextImageSection) — jamais une nouvelle composition :
//  - image attendue (§9) : texte et emplacement réservé côte à côte, à droite puis à gauche ;
//  - plusieurs intertitres H3 courts : grille à filets vert sauge (« mécanismes » de la page
//    Usures) ;
//  - une seule liste, qui clôt la section : liste en colonne latérale (« aside ») ;
//  - sinon : texte décalé (« offset »), comme la plupart des sections de la page Usures.
// Un fond ivoire toutes les trois sections donne le rythme ; les réglages de
// src/content/pages-suivantes.ts priment. Une image attendue sans visuel validé ne compte pas :
// sur le site public, la section se compose sans elle (correctif V1.3, src/lib/emplacements.ts).
import type { Block, Section } from "./pack.ts";
import type { Layout, SectionOverride } from "../content/pages-suivantes.ts";
import { showPlaceholders } from "./emplacements.ts";

export interface SectionPlan {
  section: Section;
  id: string;
  layout: Layout;
  tone: "paper" | "ivory";
  media?: { label: string; ratio?: string; wide?: boolean };
  entries: boolean;
  main: Block[];
  aside: Block[];
}

const size = (b: Block) => JSON.stringify(b).length;

// Intertitres H3 courts, au moins deux, chacun suivi de peu de texte : une grille
export function isEntries(s: Section): boolean {
  const firstH3 = s.blocks.findIndex((b) => b.kind === "h3");
  if (firstH3 < 0) return false;
  const intro = s.blocks.slice(0, firstH3);
  if (intro.length > 1 || intro.some((b) => b.kind !== "p")) return false;
  const entries: Block[][] = [];
  for (const b of s.blocks.slice(firstH3)) {
    if (b.kind === "h3") entries.push([]);
    else entries.at(-1)!.push(b);
  }
  return entries.length >= 2 && entries.length <= 4 && entries.every((e) => e.length <= 5 && e.reduce((n, b) => n + size(b), 0) <= 760);
}

// Une seule liste, à puces, placée en fin de section et précédée de texte seulement
function asideList(s: Section): boolean {
  const lists = s.blocks.filter((b) => b.kind === "ul" || b.kind === "ol");
  const last = s.blocks.at(-1);
  return (
    lists.length === 1 &&
    last?.kind === "ul" &&
    last.items.length >= 4 &&
    s.blocks.slice(0, -1).every((b) => b.kind === "p") &&
    s.blocks.length <= 5
  );
}

export function planSections(sections: Section[], overrides: Record<string, SectionOverride> = {}, defaults: SectionOverride = {}): SectionPlan[] {
  let splits = 0;
  return sections.map((section, i) => {
    const o = { ...defaults, ...overrides[section.id] };
    if (o.cas) delete o.media; // le cas clinique remplace l'emplacement réservé
    if (!showPlaceholders) delete o.media;
    const entries = o.entries ?? isEntries(section);
    let layout = o.layout;
    if (!layout) {
      if (o.media && !o.media.wide) layout = splits++ % 2 === 0 ? "split-right" : "split-left";
      else if (entries) layout = "narrow";
      else if (asideList(section)) layout = "aside";
      else layout = "offset";
    }
    const tone = o.tone ?? (i % 3 === 2 && layout !== "panel" ? "ivory" : "paper");
    const inAside = layout === "aside" ? [section.blocks.at(-1)!] : [];
    return {
      section,
      id: o.id ?? section.id,
      layout,
      tone,
      media: o.media,
      entries,
      main: layout === "aside" ? section.blocks.slice(0, -1) : section.blocks,
      aside: inAside,
    };
  });
}
