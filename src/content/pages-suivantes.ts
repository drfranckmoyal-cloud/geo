// Les 20 pages du pack « pages suivantes » : V1.2 finale (docs/pages-suivantes/v1.2), page 06
// remplacée par le correctif V1.3 (docs/pages-suivantes/v1.3) et page 01 par la V1.4, page pilier
// de la dentisterie esthétique (docs/pages-suivantes/v1.4).
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

// Correctif pré-lancement V1.3 (22/09/2026, archivé tel quel dans docs/pages-suivantes/v1.3/) :
// il remplace le seul fichier de la page 06, qui met les taches de MIH en avant. Ses fiches de
// décisions (DECISIONS_PRE_LANCEMENT_V1_3.md, puis la fiche corrective du contact, qui prime pour
// les coordonnées) sont appliquées plus bas : remplacements, boutons, liens, données structurées.
export const PATCH_DIR = "docs/pages-suivantes/v1.3";
// Fichiers postérieurs à la V1.2 qui remplacent celui d'une page, avec leur chemin complet
export const packReplacements: Record<string, string> = {
  // Page pilier « Dentisterie esthétique » (POINT 1 SEO/GEO, 24/09/2026)
  "01": "docs/pages-suivantes/v1.4/01_dentisterie-esthetique-paris_V1_4.md",
  // Page Taches, MIH renforcée (correctif pré-lancement V1.3, 22/09/2026)
  "06": "docs/pages-suivantes/v1.3/06_taches-dentaires-dyschromies-icon_V1_3.md",
};
// Chemin du fichier d'une page, parmi les fichiers de la V1.2 (pour les contrôles)
export const packPath = (num: string, v12Files: string[]): string =>
  packReplacements[num] ?? `${PACK_DIR}/${v12Files.find((f) => f.startsWith(`${num}_`))}`;

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
// emplacements « [À FOURNIR] » / « à compléter » du pack. Hébergeur : Hostinger, où Franck a son
// abonnement (22/09/2026 ; le nom de domaine reste chez OVH) ; coordonnées légales reprises des
// conditions d'utilisation d'Hostinger (société contractante pour les clients européens), qui ne
// donnent qu'une adresse électronique de contact.
// Téléphone et e-mail : les deux canaux de contact des patients, au même niveau (fiche corrective
// du correctif V1.3) ; l'adresse e-mail ouvre un message déjà intitulé.
const EMAIL = "drfranckmoyal@gmail.com";
export const fiche = {
  telephone: "01 83 75 52 16",
  telephoneIntl: "+33183755216",
  email: EMAIL,
  mailto: `mailto:${EMAIL}?subject=${encodeURIComponent("Demande de rendez-vous - Dr Franck Moyal")}`,
  hebergeur: {
    nom: "Hostinger",
    raison: "Hostinger International Limited, société de droit chypriote",
    adresse: "61 Lordou Vironos, 6023 Larnaca, Chypre",
    contact: "compliance@hostinger.com",
  },
};

// Remplacements appliqués au pack avant lecture : informations de la fiche, DOI rétablis sur
// la page Facettes (omissions de la V1.2 confirmées par ChatGPT, 22/09/2026), textes du correctif
// V1.3 (coordonnées de contact, liens vers DentCA et Smileclub Formation).
const FICHE = "fiche de Franck, 22/09/2026";
const CONTACT_V13 = "fiche corrective du contact, correctif V1.3";
const PATCH_V13 = "décisions pré-lancement, correctif V1.3";
const EDITO = "audit éditorial de ChatGPT, 24/09/2026";
export const decisions: Record<string, { from: string; to: string; ref: string }[]> = {
  "04": [
    { from: "\nPMID: `38604905`", to: "\nDOI: `10.1016/j.prosdent.2024.03.019` — PMID: `38604905`", ref: "DOI rétabli (ChatGPT, 22/09/2026)" },
    { from: "\nPMID: `39523553`", to: "\nDOI: `10.1111/jerd.13351` — PMID: `39523553`", ref: "DOI rétabli (ChatGPT, 22/09/2026)" },
  ],
  // Lien visible vers DentCA, en fin de la section qui la présente (§4)
  "12": [
    {
      from: "- la prise en charge bucco-dentaire des patients atteints de TCA.\n",
      to: "- la prise en charge bucco-dentaire des patients atteints de TCA.\n\n**Découvrir DentCA — prévention et santé bucco-dentaire dans les TCA**  \nhttps://dentca-asso.com/\n",
      ref: PATCH_V13,
    },
  ],
  // Lien visible vers Smileclub Formation, avec le lien Blendi qui clôt la section (§4)
  "15": [
    {
      from: "**Voir mon profil de formateur Blendi**  \nhttps://blendi.fr/formateurs/franck-moyal\n",
      to: "**Découvrir Smileclub Formation — formations pour chirurgiens-dentistes**  \nhttps://smileclubformations.com/\n\n**Voir mon profil de formateur Blendi**  \nhttps://blendi.fr/formateurs/franck-moyal\n",
      ref: PATCH_V13,
    },
  ],
  // « Erosive tooth wear » dans le texte patient : remplacé par la terminologie française du site,
  // « usure dentaire érosive » (audit éditorial de ChatGPT, 24/09/2026, §9 et §17). Les titres des
  // publications scientifiques gardent leur libellé original. Accord au féminin quand la phrase
  // l'impose (« défini » → « définie »).
  "07": [
    {
      from: "Il est recommandé dans les documents de consensus sur l’erosive tooth wear.",
      to: "Il est recommandé dans les documents de consensus sur l’usure dentaire érosive.",
      ref: EDITO,
    },
    { from: "peuvent participer à l’erosive tooth wear, parfois", to: "peuvent participer à l’usure dentaire érosive, parfois", ref: EDITO },
  ],
  "09": [{ from: "Les consensus sur l’erosive tooth wear décrivent", to: "Les consensus sur l’usure dentaire érosive décrivent", ref: EDITO }],
  "10": [
    {
      from: "L’erosive tooth wear est un processus chimico-mécanique différent de la carie.",
      to: "L’usure dentaire érosive est un processus chimico-mécanique différent de la carie.",
      ref: EDITO,
    },
    { from: "L’**erosive tooth wear** correspond à une perte progressive", to: "L’**usure dentaire érosive** correspond à une perte progressive", ref: EDITO },
  ],
  "13": [
    {
      from: "L’erosive tooth wear est aujourd’hui défini comme un processus",
      to: "L’usure dentaire érosive est aujourd’hui définie comme un processus",
      ref: EDITO,
    },
    { from: "la progression réelle de l’erosive tooth wear restent limitées", to: "la progression réelle de l’usure dentaire érosive restent limitées", ref: EDITO },
  ],
  // Bloc final de la page Paris 9, remplacé tel que l'écrit la fiche corrective (§4)
  "18": [
    {
      from: "## Prendre rendez-vous\n\n**Adresse**  \n2 rue Hippolyte Lebas  \n75009 Paris\n\n**Téléphone**  \nà compléter\n\n**Prise de rendez-vous en ligne**  \nlien à compléter\n\n**CTA : Prendre rendez-vous**",
      to: `## Prendre rendez-vous ou contacter le cabinet\n\n**Par téléphone**  \n${fiche.telephone}\n\n**Par e-mail**  \n${fiche.email}\n\n**CTA : Prendre rendez-vous**`,
      ref: CONTACT_V13,
    },
  ],
  // Section « Prendre rendez-vous » de la page Contact : les deux canaux, au même niveau (§3)
  "19": [
    {
      from: "## Prendre rendez-vous\n\n**Téléphone**  \n[À FOURNIR]\n\n**Prise de rendez-vous en ligne**  \n[URL À FOURNIR]\n",
      to: `## Prendre rendez-vous ou nous écrire\n\nVous pouvez contacter le cabinet par téléphone ou par e-mail pour une demande de rendez-vous, une question avant consultation ou pour préciser votre motif de consultation.\n\n**Téléphone**  \n${fiche.telephone}\n\n**E-mail**  \n${fiche.email}\n`,
      ref: CONTACT_V13,
    },
  ],
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
  "06": ["**Source réglementaire — Union européenne.**"], // V1.3 : éclaircissement avant 18 ans
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
// Sur le site public, un emplacement sans visuel validé disparaît, et la section se compose
// comme une section sans image (correctif V1.3 §7) ; EMPLACEMENTS=1 les montre pour les revues.
// actions : boutons décidés par ChatGPT, sous le texte de la section, d'égale importance.
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
  actions?: { label: string; href: string }[];
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
  // Page pilier (V1.4, POINT 1) : six critères en grille, matrice demande → solutions sous le
  // texte, quatre solutions en grille, bloc « usures » en panneau vert sauge (composition
  // « domaine spécifique » des composants gelés)
  "01": {
    sections: {
      "comment-evaluer-une-prise-en-charge-esthetique": { entries: true },
      "la-bonne-question-n-est-pas-toujours-quel": { layout: "narrow", tone: "ivory" },
      "quelles-solutions-en-dentisterie-esthetique": { entries: true, media: { label: "3 à 5 cas cliniques réels — à fournir", ratio: "3 / 1", wide: true } },
      "et-si-les-dents-sont-usees": { layout: "panel" },
      "quelle-place-pour-le-smile-design": { media: { label: "Photographie réelle de planification esthétique — à fournir", ratio: "4 / 5" } },
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
    // §9 de la V1.3 : le cas de MIH en priorité, dans la section qui en parle
    sections: {
      "taches-de-mih-peut-on-les-traiter-chez": { media: { label: "Cas réel de MIH sur une incisive : état initial puis résultat, avec consentement web — à fournir", ratio: "4 / 3" } },
      "pourquoi-une-tache-blanche-parait-elle-blanche": { media: { label: "Macro clinique réelle de lésion et résultat — à fournir", ratio: "4 / 5" } },
      "qu-est-ce-que-l-erosion-infiltration-de": { media: { label: "1 autre cas de dyschromie / white spot : avant / après, avec consentement — à fournir", ratio: "4 / 3" } },
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
      // Ancre unique de la section de prise de rendez-vous : #prendre-rendez-vous (V1.2), gardée
      // sous le titre de la V1.3. Deux boutons d'égale importance : appeler ou écrire.
      "prendre-rendez-vous-ou-nous-ecrire": {
        id: "prendre-rendez-vous",
        actions: [
          { label: "Appeler le cabinet", href: `tel:${fiche.telephoneIntl}` },
          { label: "Écrire au cabinet", href: fiche.mailto },
        ],
      },
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
  // Page pilier : les six sujets réellement traités, tels que les nomme le POINT 1 (§21)
  "01": {
    about: ["Dentisterie esthétique", "Dentisterie adhésive", "Composite bonding", "Facettes", "Éclaircissement", "Usures dentaires"].map((name) => ({ "@type": "Thing", name })),
  },
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

// Organisations fondées par Franck (src/content/site.ts), décrites sur la page qui les présente et
// mène à leur site (correctif V1.3 §4).
export const schemaOrganizations: Record<string, ("dentca" | "smileclub")[]> = {
  "12": ["dentca"],
  "15": ["smileclub"],
};
