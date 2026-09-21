// Lecture des fichiers du pack « pages suivantes » (docs/pages-suivantes/v1) : chaque fichier
// devient une page structurée — routage, ouverture, réponse directe, sections, FAQ, appel
// final, liens, auteur, référencement, images attendues, sources. Les textes ne sont ni
// recopiés ni retouchés : ils sont lus tels quels dans le fichier du pack au moment de
// fabriquer le site. Seules les marques de mise en forme du fichier (# titres, - listes,
// ** gras, → liens) sont interprétées.
//
// Aucune dépendance : ce module sert aussi aux scripts de contrôle (Node).

export type Block =
  | { kind: "p"; text: string } // texte courant : **gras**, renvois [n], retours à la ligne « \n »
  | { kind: "ul"; items: string[] }
  | { kind: "ol"; items: string[] }
  | { kind: "h3"; text: string }
  | { kind: "link"; label: string } // « → **Libellé** » : lien interne, adresse résolue par la page
  | { kind: "evidence"; label: string; href: string }; // « **Libellé** » puis une adresse web : preuve externe

export interface Section {
  id: string;
  title: string;
  group: boolean; // titre « # » du fichier (bloc) plutôt que « ## »
  blocks: Block[];
}

export interface Source {
  n: number;
  authors: string;
  title: string;
  journal: string;
  details: string;
  year: string;
  doi: string;
  pmid: string;
  pubmed: string;
}

export interface PackPage {
  num: string; // « 01 » … « 20 »
  file: string;
  url: string;
  parent: string;
  crumbs: string[]; // libellés du fil d'Ariane, de « Accueil » à la page
  opening: string;
  h1: string;
  contentH1: string; // le « # » en tête du contenu éditorial (normalement identique au H1)
  lead: string;
  answer?: string;
  contract: string[];
  sections: Section[];
  faq?: { title: string; items: { q: string; a: string }[] };
  cta?: { title: string; paragraphs: string[]; label?: string };
  related?: { title: string; labels: string[] };
  links: { label: string; href: string }[];
  author: { name: string; href: string; date: string; iso: string };
  seo: { title: string; description: string; schema: string[]; robots?: string };
  images: string[];
  sources: Source[];
  sourceNotes: string[]; // paragraphs du §10 qui ne sont pas des références numérotées
  notes: string; // §11, jamais affiché
}

// Découpe le fichier en ses rubriques numérotées « ## 1. ROUTING… » à « ## 11. NOTES… »
function specSections(md: string): Map<number, string> {
  const out = new Map<number, string>();
  const parts = md.split(/^## (\d+)\. .*$/m);
  for (let i = 1; i < parts.length; i += 2) out.set(Number(parts[i]), parts[i + 1]);
  return out;
}

const field = (text: string, label: RegExp): string | undefined => {
  for (const line of text.split("\n")) {
    const m = line.match(new RegExp(`^- \\*\\*${label.source}\\*\\* : (.+?)\\s*$`));
    if (m) return m[1];
  }
  return undefined;
};
const code = (s = "") => s.replace(/^`|`$/g, "");
const bullets = (text = "") =>
  text
    .split("\n")
    .filter((l) => l.startsWith("- "))
    .map((l) => l.slice(2).trim());

export function slugify(text: string): string {
  return text
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/œ/g, "oe")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .split("-")
    .slice(0, 8)
    .join("-");
}

// Jetons du contenu éditorial : titres, paragraphes (lignes jointes par « \n »), puces,
// numéros, liens « → ».
type Token =
  | { t: "h"; level: number; text: string }
  | { t: "p"; text: string }
  | { t: "li"; text: string }
  | { t: "oli"; text: string }
  | { t: "link"; label: string };

function tokenize(md: string): Token[] {
  const out: Token[] = [];
  let para: string[] = [];
  const flush = () => {
    if (para.length) out.push({ t: "p", text: para.join("\n") });
    para = [];
  };
  for (const raw of md.split("\n")) {
    const line = raw.replace(/\s+$/, "");
    if (!line.trim() || line.trim() === "---") {
      flush();
      continue;
    }
    let m: RegExpMatchArray | null;
    if ((m = line.match(/^(#{1,3}) (.+)$/))) {
      flush();
      out.push({ t: "h", level: m[1].length, text: m[2].trim() });
    } else if ((m = line.match(/^- (.+)$/))) {
      flush();
      out.push({ t: "li", text: m[1] });
    } else if ((m = line.match(/^\d+\. (.+)$/))) {
      flush();
      out.push({ t: "oli", text: m[1] });
    } else if ((m = line.match(/^→ \*\*(.+)\*\*$/))) {
      flush();
      out.push({ t: "link", label: m[1] });
    } else {
      para.push(line.trim());
    }
  }
  flush();
  return out;
}

// Un paragraphe « **Libellé** » suivi d'une adresse web sur la ligne suivante : une preuve externe
function toBlock(text: string): Block {
  const ev = text.match(/^\*\*(.+?)\*\*\n(https?:\/\/\S+)$/);
  if (ev) return { kind: "evidence", label: ev[1], href: ev[2] };
  return { kind: "p", text };
}

function parseContent(md: string, file: string) {
  const tokens = tokenize(md);
  const sections: Section[] = [];
  let contentH1 = "";
  let faq: PackPage["faq"];
  let cta: PackPage["cta"];
  let related: PackPage["related"];
  let mode: "content" | "faq" | "faq-bold" | "cta" | "related" = "content";
  let section: Section | undefined;
  let inGroup = false;
  const ids = new Set<string>();
  const open = (title: string, group: boolean) => {
    let id = slugify(title) || "section";
    for (let i = 2; ids.has(id); i++) id = `${slugify(title)}-${i}`;
    ids.add(id);
    section = { id, title, group, blocks: [] };
    sections.push(section);
    inGroup = group;
    mode = "content";
  };
  const push = (b: Block) => {
    if (!section) throw new Error(`${file} : texte avant toute section (« ${JSON.stringify(b).slice(0, 60)} »)`);
    const last = section.blocks.at(-1);
    if (b.kind === "ul" && last?.kind === "ul") last.items.push(...b.items);
    else if (b.kind === "ol" && last?.kind === "ol") last.items.push(...b.items);
    else section.blocks.push(b);
  };

  for (const tok of tokens) {
    if (tok.t === "h") {
      const { level, text } = tok;
      if (level === 1 && !contentH1) {
        contentH1 = text;
        continue;
      }
      if (level === 1 && /^FAQ$/i.test(text)) {
        mode = "faq";
        faq = { title: text, items: [] };
        continue;
      }
      if (level === 2 && /^FAQ$/i.test(text)) {
        mode = "faq-bold";
        faq = { title: text, items: [] };
        continue;
      }
      if (level === 1 && /^CTA$/i.test(text)) {
        mode = "cta";
        cta = { title: "", paragraphs: [] };
        continue;
      }
      if (level === 1 && /^À lire aussi$/i.test(text)) {
        mode = "related";
        related = { title: text, labels: [] };
        continue;
      }
      if (level === 2 && mode === "faq") {
        faq!.items.push({ q: text, a: "" });
        continue;
      }
      if (level === 2 && mode === "cta" && !cta!.title) {
        cta!.title = text;
        continue;
      }
      if (level === 1) {
        open(text, true);
        continue;
      }
      if (level === 2 && mode === "content" && inGroup && section) {
        section.blocks.push({ kind: "h3", text });
        continue;
      }
      if (level === 2) {
        open(text, false);
        continue;
      }
      if (level === 3 && mode === "content" && section && !inGroup) {
        section.blocks.push({ kind: "h3", text });
        continue;
      }
      throw new Error(`${file} : titre inattendu « ${"#".repeat(level)} ${text} »`);
    }

    if (mode === "faq") {
      const item = faq!.items.at(-1);
      if (!item || tok.t !== "p") throw new Error(`${file} : FAQ mal formée près de « ${JSON.stringify(tok).slice(0, 60)} »`);
      item.a = item.a ? `${item.a}\n${tok.text}` : tok.text;
      continue;
    }
    if (mode === "faq-bold") {
      const m = tok.t === "p" ? tok.text.match(/^\*\*(.+?)\*\*\n([\s\S]+)$/) : null;
      if (!m) throw new Error(`${file} : FAQ mal formée près de « ${JSON.stringify(tok).slice(0, 60)} »`);
      faq!.items.push({ q: m[1], a: m[2] });
      continue;
    }
    if (mode === "cta") {
      if (tok.t !== "p") throw new Error(`${file} : bloc CTA inattendu`);
      const label = tok.text.match(/^\*\*CTA : (.+)\*\*$/);
      if (label) cta!.label = label[1];
      else cta!.paragraphs.push(tok.text);
      continue;
    }
    if (mode === "related") {
      const m = tok.t === "li" ? tok.text.match(/^\*\*(.+)\*\*$/) : null;
      if (!m) throw new Error(`${file} : liste « À lire aussi » mal formée`);
      related!.labels.push(m[1]);
      continue;
    }
    if (tok.t === "p") push(toBlock(tok.text));
    else if (tok.t === "li") push({ kind: "ul", items: [tok.text] });
    else if (tok.t === "oli") push({ kind: "ol", items: [tok.text] });
    else if (tok.t === "link") push({ kind: "link", label: tok.label });
  }
  return { contentH1, sections, faq, cta, related };
}

function parseSources(text = ""): { sources: Source[]; notes: string[] } {
  const sources: Source[] = [];
  const notes: string[] = [];
  const paras = text
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter(Boolean);
  for (const p of paras) {
    const lines = p.split("\n").map((l) => l.trim());
    const ref = lines[0].match(/^\*\*\[(\d+)\] (.+?)\*\* (.+?) \*(.+?)\* ?(.*?)$/);
    if (!ref) {
      notes.push(lines.join("\n"));
      continue;
    }
    const ids = (lines.find((l) => l.startsWith("DOI:")) ?? "").match(/DOI: `([^`]+)`(?: — PMID: `(\d+)`)?/);
    const pubmed = (lines.find((l) => l.startsWith("PubMed:")) ?? "").replace(/^PubMed:\s*/, "");
    const [, n, authors, title, journal, details] = ref;
    sources.push({
      n: Number(n),
      authors,
      title,
      journal,
      details,
      year: (details.match(/\d{4}/) ?? [""])[0],
      doi: ids?.[1] ?? "",
      pmid: ids?.[2] ?? "",
      pubmed,
    });
  }
  return { sources, notes };
}

export function parsePack(md: string, file: string): PackPage {
  const s = specSections(md);
  const routing = s.get(1) ?? "";
  const hero = s.get(2) ?? "";
  const answerText = s.get(3) ?? "";
  const author = s.get(7) ?? "";
  const seo = s.get(8) ?? "";
  const answerLines = answerText
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith("- "));
  const content = parseContent(s.get(5) ?? "", file);
  const { sources, notes } = parseSources(s.get(10));
  const links = (s.get(6) ?? "")
    .split("\n")
    .map((l) => l.match(/^- \*\*(.+?)\*\* → `([^`]+)`/))
    .filter((m): m is RegExpMatchArray => Boolean(m))
    .map((m) => ({ label: m[1], href: m[2] }));
  const page: PackPage = {
    num: file.slice(0, 2),
    file,
    url: code(field(routing, /URL définitive/)),
    parent: code(field(routing, /Page parente/)),
    crumbs: (field(routing, /Fil d.Ariane/) ?? "").split(" > ").map((c) => c.trim()),
    opening: code(field(routing, /Composant d.ouverture/)),
    h1: field(hero, /H1/) ?? "",
    contentH1: content.contentH1,
    lead: field(hero, /Chapeau/) ?? "",
    answer: /Pas de DirectAnswer/.test(answerText) ? undefined : answerLines.join("\n") || undefined,
    contract: bullets(s.get(4)),
    sections: content.sections,
    faq: content.faq,
    cta: content.cta,
    related: content.related,
    links,
    author: {
      name: field(author, /Auteur/) ?? "",
      href: code(field(author, /Lien auteur/)),
      date: field(author, /Date de mise à jour/) ?? "",
      iso: code(field(author, /`dateModified`/)),
    },
    seo: {
      title: field(seo, /Title/) ?? "",
      description: field(seo, /Meta description/) ?? "",
      schema: [...(field(seo, /Données structurées/) ?? "").matchAll(/`([^`]+)`/g)].map((m) => m[1]),
      robots: code(field(seo, /Robots/)) || undefined,
    },
    images: bullets(s.get(9)),
    sources,
    sourceNotes: notes,
    notes: (s.get(11) ?? "").trim(),
  };
  for (const [key, value] of Object.entries({ url: page.url, h1: page.h1, lead: page.lead, title: page.seo.title })) {
    if (!value) throw new Error(`${file} : « ${key} » introuvable`);
  }
  return page;
}
