// Les 20 pages du pack « pages suivantes » V1 (docs/pages-suivantes/v1, reçu le 21/09/2026).
// Leurs textes ne sont pas recopiés ici : ils sont lus directement dans les fichiers du pack
// (src/lib/pack.ts). Ce fichier ne garde que ce que le pack laisse à Claude :
//  - l'ordre de livraison par lots (00_ARBORESCENCE_ET_ORDRE.md) ;
//  - les passages du pack qui ressemblent à des consignes internes, non affichés en attendant
//    la confirmation de ChatGPT ;
//  - les liens dont le libellé ne figure pas dans la liste « Liens internes » de la page ;
//  - la mise en page : emplacements d'images (§9 de chaque fichier) et compositions choisies
//    parmi celles des composants gelés ;
//  - les décisions de ChatGPT qui précisent le pack (validation consolidée du 22/09/2026,
//    docs/echanges/2026-09-22-chatgpt-23-validation-consolidee-lots-a-b-c-d.md).

// Source unique depuis le 22/09/2026 : la V1.2 finale (D41). La V1 reste archivée à côté.
export const PACK_DIR = "docs/pages-suivantes/v1.2";

// Arborescence définitive (00 — ordre d'intégration A → B → C → D)
export const arborescence = [
  { num: "01", lot: "A", url: "/dentisterie-esthetique-paris/" },
  { num: "02", lot: "A", url: "/bilan-esthetique-personnalise/" },
  { num: "03", lot: "A", url: "/composite-bonding-paris/" },
  { num: "04", lot: "A", url: "/facettes-dentaires-paris/" },
  { num: "05", lot: "A", url: "/eclaircissement-dentaire-paris/" },
  { num: "06", lot: "A", url: "/taches-dentaires-dyschromies-icon/" },
  { num: "07", lot: "B", url: "/diagnostic-usures-dentaires/" },
  { num: "08", lot: "B", url: "/rehabilitation-dents-usees/" },
  { num: "09", lot: "B", url: "/bruxisme-usure-dentaire/" },
  { num: "10", lot: "B", url: "/erosion-dentaire/" },
  { num: "11", lot: "B", url: "/dents-courtes-usees/" },
  { num: "12", lot: "B", url: "/tca-dents/" },
  { num: "13", lot: "B", url: "/anorexie-erosion-dentaire-sans-vomissements/" },
  { num: "14", lot: "C", url: "/publications/" },
  { num: "15", lot: "C", url: "/conferences-formations/" },
  { num: "16", lot: "C", url: "/activite-hospitaliere/" },
  { num: "17", lot: "C", url: "/medias-interviews/" },
  { num: "18", lot: "C", url: "/chirurgien-dentiste-paris-9/" },
  { num: "19", lot: "D", url: "/contact/" },
  { num: "20", lot: "D", url: "/mentions-legales/" },
] as const;

// Lots construits à ce jour
export const builtLots: string[] = ["A", "B", "C", "D"];
export const builtNums: string[] = arborescence.filter((p) => builtLots.includes(p.lot)).map((p) => p.num);
export const builtPackUrls: string[] = arborescence.filter((p) => builtLots.includes(p.lot)).map((p) => p.url);

// Passages du contenu « mot pour mot » qui ressemblent à des consignes de rédaction glissées
// dans le texte : non affichés, listés dans le rapport, à confirmer par ChatGPT.
// « section » : toute la section ; « text » : un paragraphe (début exact).
// V1.2 : les quatre consignes relevées dans la V1 (pages 05, 10, 12, 14) ont été retirées du
// texte par ChatGPT ; plus rien à masquer.
export const hidden: Record<string, { section?: string; text?: string; why: string }[]> = {};

// Remplacements décidés par ChatGPT, appliqués au fichier du pack avant sa lecture — par le site
// comme par les contrôles, qui les listent. Sans effet si le pack contient déjà le nouveau texte.
// Informations fournies par Franck dans sa fiche en ligne (22/09/2026), insérées à la place des
// emplacements « [À FOURNIR] » / « à compléter » du pack. Hébergeur : OVH, choisi par Franck ;
// coordonnées légales reprises des mentions légales d'OVHcloud (numéro 1007 : usage courant, à
// confirmer dans l'espace client OVH).
export const fiche = {
  telephone: "01 83 75 52 16",
  email: "drfranckmoyal@gmail.com",
  hebergeur: {
    nom: "OVH",
    raison: "OVH SAS, SAS au capital de 10 069 020 €, RCS Lille Métropole 424 761 419 00045",
    adresse: "2 rue Kellermann, 59100 Roubaix, France",
    contact: "1007 (depuis la France), +33 9 72 10 10 07",
  },
};

// Remplacements appliqués au pack avant lecture : informations de la fiche, et DOI rétablis sur
// la page Facettes (omissions de la V1.2 confirmées par ChatGPT, 22/09/2026).
const FICHE = "fiche de Franck, 22/09/2026";
export const decisions: Record<string, { from: string; to: string; ref: string }[]> = {
  "04": [
    { from: "\nPMID: `38604905`", to: "\nDOI: `10.1016/j.prosdent.2024.03.019` — PMID: `38604905`", ref: "DOI rétabli (ChatGPT, 22/09/2026)" },
    { from: "\nPMID: `39523553`", to: "\nDOI: `10.1111/jerd.13351` — PMID: `39523553`", ref: "DOI rétabli (ChatGPT, 22/09/2026)" },
  ],
  "18": [{ from: "**Téléphone**  \nà compléter", to: `**Téléphone**  \n${fiche.telephone}`, ref: FICHE }],
  "19": [{ from: "**Téléphone**  \n[À FOURNIR]", to: `**Téléphone**  \n${fiche.telephone}`, ref: FICHE }],
  "20": [
    { from: "**Téléphone** : [À FOURNIR]", to: `**Téléphone** : ${fiche.telephone}`, ref: FICHE },
    { from: "**Adresse électronique professionnelle** : [À FOURNIR]", to: `**Adresse électronique professionnelle** : ${fiche.email}`, ref: FICHE },
    { from: "**Hébergeur** : [À FOURNIR AVANT MISE EN LIGNE]", to: `**Hébergeur** : ${fiche.hebergeur.nom}`, ref: FICHE },
    { from: "**Raison sociale** : [À FOURNIR]", to: `**Raison sociale** : ${fiche.hebergeur.raison}`, ref: FICHE },
    { from: "**Adresse** : [À FOURNIR]", to: `**Adresse** : ${fiche.hebergeur.adresse}`, ref: FICHE },
    { from: "**Téléphone / contact** : [À FOURNIR]", to: `**Téléphone / contact** : ${fiche.hebergeur.contact}`, ref: FICHE },
  ],
};

export function applyDecisions(md: string, num: string): { md: string; applied: string[] } {
  const applied: string[] = [];
  for (const d of decisions[num] ?? []) {
    const n = md.split(d.from).length - 1;
    if (n === 1) {
      md = md.replace(d.from, d.to);
      applied.push(`« ${d.from} » → « ${d.to} » (${d.ref})`);
    } else if (n === 0 && md.includes(d.to)) applied.push(`« ${d.to} » : déjà dans le pack (${d.ref})`);
    else throw new Error(`Décision « ${d.from} » (page ${num}) : texte trouvé ${n} fois dans le pack`);
  }
  return { md, applied };
}

// Notes du §10 (sources) affichées sous la liste des références, ligne par ligne (début exact).
// Les autres lignes du §10 sont des consignes (« À présenter comme… », « À ne pas écrire… »).
export const shownSourceNotes: Record<string, string[]> = {
  "01": ["**Source fonctionnelle — SmileCloud**"],
  "02": ["**Source fonctionnelle — SmileCloud**"],
  "03": ["**Repère clinique du Dr Franck Moyal**"],
  "04": ["**Source fonctionnelle — SmileCloud**"],
};

// Liens « → » dont le libellé n'est pas dans la liste « Liens internes » de la page : adresse
// déduite (page évidente, libellé validé ailleurs), signalée dans le rapport.
// V1.2 : chaque lien du texte figure désormais dans la liste « Liens internes » de sa page ; plus
// aucune adresse à déduire.
export const linkOverrides: Record<string, string> = {};

// Libellés des pages du golden master et du menu, pour relier les libellés du pack à leur adresse
export const knownLabels: Record<string, string> = {
  Accueil: "/",
  "Usures dentaires": "/usures-dentaires/",
  "Dr Franck Moyal": "/franck-moyal/",
  "Dentisterie esthétique": "/dentisterie-esthetique-paris/",
};

// Mise en page, section par section (identifiant = titre de la section sans accents).
// media : emplacement réservé pour une image attendue (§9 du fichier), légende reprise du §9.
// Par défaut (src/lib/pack-layout.ts) : texte décalé, liste en colonne latérale quand elle
// clôt la section, intertitres H3 courts en grille (composition « mécanismes » de la page
// Usures), un fond ivoire toutes les trois sections.
export type Layout = "split-right" | "split-left" | "offset" | "narrow" | "aside" | "panel";
export interface SectionOverride {
  layout?: Layout;
  tone?: "paper" | "ivory";
  media?: { label: string; ratio?: string; wide?: boolean };
  entries?: boolean;
  id?: string;
  links?: boolean; // liste de noms de pages en gras : chaque nom devient un lien vers sa page
}
export interface PageLayout {
  hideByline?: boolean; // ouverture sans ligne auteur (Contact, Mentions légales : validation 23)
  cta?: { label: string; href: string }; // bouton de l'appel final décidé hors du pack (page 18 : validation 23)
  defaults?: SectionOverride; // réglage commun à toutes les sections de la page
  sections?: Record<string, SectionOverride>;
  method?: { before: string }; // MethodSteps (page 02), placé avant cette section
  pathway?: boolean; // ClinicalPathway (sommaire cliquable des sections)
}

export const layouts: Record<string, PageLayout> = {
  "01": {
    sections: {
      "quelle-place-pour-le-smile-design": { media: { label: "Photographie réelle de planification esthétique — à fournir", ratio: "4 / 5" } },
      "quels-traitements-peuvent-transformer-un-sourire": { media: { label: "3 à 5 cas cliniques réels — à fournir", ratio: "3 / 1", wide: true } },
    },
  },
  "02": {
    method: { before: "premiere-etape-ecouter" },
    sections: {
      "deuxieme-etape-documenter": { media: { label: "Séquence photo / scan / simulation d’un vrai cas, avec consentement — à fournir", ratio: "4 / 5" } },
      "qu-apporte-le-smile-design": { media: { label: "Vidéo ou capture réelle de simulation SmileCloud — à fournir", ratio: "4 / 3" } },
    },
  },
  "03": {
    sections: {
      "qu-est-ce-que-la-stratification-composite": { media: { label: "Macro-photo de texture et de stratification — à fournir", ratio: "4 / 5" } },
      "ce-que-je-recherche-avec-un-composite-anterieur": { media: { label: "2 cas de composite antérieur stratifié, cadrage constant — à fournir", ratio: "4 / 3" } },
    },
  },
  "04": {
    sections: {
      "sublimer-un-sourire-plutot-que-remplacer-des-dents": { media: { label: "2 cas de facettes complets : état initial → projet → résultat — à fournir", ratio: "4 / 3" } },
      "smile-design-et-simulation": { media: { label: "Vidéo / simulation SmileCloud réelle — à fournir", ratio: "4 / 3" } },
    },
  },
  "05": {
    sections: {
      "la-technique-que-je-privilegie-l-eclaircissement-ambulatoire": { media: { label: "Photo sobre de gouttières personnalisées — à fournir", ratio: "4 / 5" } },
      "est-ce-que-le-resultat-est-visible": { media: { label: "Cas avant / après éclaircissement, mêmes conditions photographiques — à fournir", ratio: "4 / 3" } },
    },
  },
  "06": {
    sections: {
      "pourquoi-une-tache-blanche-parait-elle-blanche": { media: { label: "Macro clinique réelle de lésion et résultat — à fournir", ratio: "4 / 5" } },
      "qu-est-ce-que-l-erosion-infiltration-de": { media: { label: "2 cas de dyschromie / white spot : avant / après, avec consentement — à fournir", ratio: "4 / 3" } },
    },
  },
  "07": {
    pathway: true,
    sections: {
      "quels-signes-font-penser-a-une-usure-dentaire": { media: { label: "Photo clinique d’usure avec légende diagnostique — à fournir", ratio: "4 / 3" } },
      "pourquoi-photographier-et-scanner": { media: { label: "Comparaison de scans ou capture de monitoring — à fournir", ratio: "4 / 3" } },
    },
  },
  "08": {
    sections: {
      "rehabiliter-une-dentition-usee-ne-signifie-plus-automatiquement": { media: { label: "Cas complet de réhabilitation : initial → planification → résultat — à fournir", ratio: "4 / 5" } },
      "qu-est-ce-que-la-dimension-verticale-d": { media: { label: "Schéma ou capture de planification DVO issu d’un vrai cas — à fournir", ratio: "4 / 3" } },
    },
  },
  "09": {
    sections: {
      // Le schéma attendu est celui de la page Usures (« si déjà produit pour le cluster »)
      "pourquoi-les-dents-peuvent-elles-s-user-chez": { media: { label: "Schéma — mécanismes d’usure (celui de la page Usures) — à fournir", ratio: "4 / 3" } },
    },
  },
  "10": {
    sections: {
      "quels-sont-les-premiers-signes": { media: { label: "Macro de lésions érosives réelles — à fournir", ratio: "4 / 5" } },
      "comment-depiste-t-on-l-erosion": { media: { label: "Série de scans de suivi — à fournir", ratio: "4 / 3" } },
    },
  },
  "11": {
    sections: {
      "quel-resultat-peut-on-rechercher": { media: { label: "Avant / après centré sur les longueurs incisives — à fournir", ratio: "4 / 3" } },
    },
  },
  "12": {
    sections: {
      "pourquoi-le-depistage-dentaire-est-il-important": { media: { label: "Schéma clinique, photo institutionnelle autorisée ou visuel de prévention neutre — à fournir", ratio: "4 / 3" } },
      "mon-activite-a-la-cmme": { layout: "panel" }, // contrat : composition « domaine spécifique » pour la CMME
    },
  },
  "13": {
    sections: {
      "l-absence-de-vomissements-n-elimine-pas-le": { layout: "narrow", media: { label: "Infographie sobre des mécanismes : salive / acides / médicaments / contraintes mécaniques — à fournir", ratio: "3 / 1", wide: true } },
    },
  },
  "19": {
    sections: {
      // Ancre unique de la section « Prendre rendez-vous » : #prendre-rendez-vous (V1.2) — c'est
      // l'identifiant que lui donne déjà son titre.
      // Les 7 motifs, écrits en gras dans le pack, deviennent des liens vers leurs pages (validés)
      "motifs-de-consultation": { links: true },
    },
  },
  // « Page de lecture simple » : colonne de lecture, fond uni
  "20": { defaults: { layout: "narrow", tone: "paper" } },
};

// Données structurées propres à une page. Chaque fait figure en toutes lettres sur la page.
// Page 14 : « Person auteur lorsqu'une publication lui est attribuée » (§8 du fichier) — les
// articles et ouvrages de la page, reliés à Person#franck-moyal ; pas les travaux encadrés.
// Types validés le 22/09/2026 : Article ou Book, sans métadonnée absente de la page.
const FRANCK = { "@id": "https://drfranckmoyal.fr/#franck-moyal" };
const coauthor = (name: string) => ({ "@type": "Person", name });
export const schemaExtras: Record<string, Record<string, unknown>> = {
  "14": {
    hasPart: [
      {
        "@type": "Article",
        name: "Fermeture de diastème au composite en technique directe : la « Front Wing Technique »",
        author: FRANCK,
        datePublished: "2023-10-09",
        isPartOf: { "@type": "Periodical", name: "Le Fil Dentaire" },
        url: "https://www.lefildentaire.com/articles/fermeture-de-diasteme-composite-technique-directe-front-wing-technique/",
      },
      {
        "@type": "Article",
        name: "Santé et précarité : les permanences d’accès aux soins de santé bucco-dentaire",
        author: [
          coauthor("Frédéric Rilliard"),
          coauthor("Lisa Friedlander"),
          coauthor("Julien Descorps-Declere"),
          coauthor("Nadhia Khelifa"),
          FRANCK,
          coauthor("Shéhérazade Saadi"),
          coauthor("Florence Schvallinger"),
          coauthor("Christelle Naud-Llamas"),
        ],
        datePublished: "2012",
        pagination: "31–33",
        isPartOf: { "@type": "PublicationIssue", issueNumber: "417", isPartOf: { "@type": "Periodical", name: "La Santé de l’Homme" } },
        url: "https://www.santepubliquefrance.fr/docs/article/sante-et-precarite-les-permanences-dacces-aux-soins-de-sante-bucco-dentaire",
      },
      {
        "@type": "Book",
        name: "Cancers de la cavité buccale — du diagnostic aux applications thérapeutiques",
        author: [coauthor("Hervé Tarragano"), coauthor("Patrick Missika"), coauthor("Lotfi Ben Slama"), coauthor("Benjamin Illouz"), FRANCK],
        publisher: { "@type": "Organization", name: "Éditions CdP" },
        datePublished: "2008",
        isbn: "9782843611292",
      },
      {
        "@type": "Book",
        name: "La chirurgie orale",
        author: [coauthor("Hervé Tarragano"), coauthor("Patrick Missika"), coauthor("Benjamin Illouz"), coauthor("Yvon Roche"), FRANCK],
        url: "https://books.google.com/books/about/La_chirurgie_orale_Editions_CdP.html?id=J9N4BwAAQBAJ",
      },
      {
        "@type": "Article",
        name: "La première consultation en implantologie",
        author: FRANCK,
        url: "https://www.lefildentaire.com/articles/clinique/implantologie/la-premiere-consultation-en-implantologie/",
      },
    ],
  },
};
