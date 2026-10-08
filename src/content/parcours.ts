// Les deux parcours de lecture (D65, 04/10/2026) : le site s'adressait à deux publics
// dans un même menu de neuf entrées, sans jamais les distinguer. On trie le visiteur
// avant de lui parler, comme le font les trois sites donnés en exemple par Franck.
//
// Les libellés reprennent ceux du menu et les titres des pages : Franck a demandé de
// ne pas les réécrire pour l'instant (ils relèvent de ChatGPT). Aucune adresse n'est
// modifiée ; ces listes ne font qu'ouvrir depuis l'accueil des pages qui n'étaient
// atteignables qu'au fil d'un paragraphe.

export interface Destination {
  label: string;
  href: string;
  /** Lien vers un autre site : ouvre une nouvelle page, marqué comme tel. */
  externe?: boolean;
  /**
   * Intertitre de regroupement (D70, 08/10/2026). La porte « Patient » listait huit
   * pages d'esthétique et laissait toute la famille des usures derrière la seule page
   * pilier : bruxisme et dents usées n'étaient atteignables qu'en deux clics, avec deux
   * liens internes chacun, alors que ce sont des mots que les patients cherchent.
   */
  rubrique?: string;
}

export interface Parcours {
  id: string;
  /** « Vous êtes » */
  surtitre: string;
  titre: string;
  intro: string;
  destinations: Destination[];
  /** Le lien principal, mis en avant sous la liste. */
  suite: Destination;
}

export const parcours: Parcours[] = [
  {
    id: "patients",
    surtitre: "Vous êtes",
    titre: "Patient",
    intro:
      "Vous cherchez à comprendre ce que vous avez, ou ce qu’il est possible de faire. Chaque page part d’une situation clinique et explique la démarche avant la technique.",
    destinations: [
      { rubrique: "Esthétique", label: "Dentisterie esthétique et adhésive", href: "/dentisterie-esthetique-paris/" },
      { rubrique: "Esthétique", label: "Facettes dentaires", href: "/facettes-dentaires-paris/" },
      { rubrique: "Esthétique", label: "Composite bonding", href: "/composite-bonding-paris/" },
      { rubrique: "Esthétique", label: "Éclaircissement dentaire", href: "/eclaircissement-dentaire-paris/" },
      { rubrique: "Esthétique", label: "Taches blanches, MIH et dyschromies", href: "/taches-dentaires-dyschromies-icon/" },
      { rubrique: "Esthétique", label: "Bilan esthétique personnalisé", href: "/bilan-esthetique-personnalise/" },
      { rubrique: "Usures et érosion", label: "Usures dentaires", href: "/usures-dentaires/" },
      { rubrique: "Usures et érosion", label: "Bruxisme et usure dentaire", href: "/bruxisme-usure-dentaire/" },
      { rubrique: "Usures et érosion", label: "Dents courtes ou usées", href: "/dents-courtes-usees/" },
      { rubrique: "Usures et érosion", label: "Érosion dentaire", href: "/erosion-dentaire/" },
      { rubrique: "Usures et érosion", label: "TCA et santé bucco-dentaire", href: "/tca-dents/" },
    ],
    suite: { label: "Prendre rendez-vous", href: "/contact/#prendre-rendez-vous" },
  },
  {
    id: "praticiens",
    surtitre: "Vous êtes",
    titre: "Chirurgien-dentiste",
    intro:
      "Formation, publications, enseignement hospitalier : l’activité qui prolonge la pratique clinique, et les cas documentés de bout en bout.",
    destinations: [
      { label: "Conférences et formations", href: "/conferences-formations/" },
      { label: "Smile Club Formations", href: "https://smileclubformations.com/", externe: true },
      { label: "Publications", href: "/publications/" },
      { label: "Activité hospitalière", href: "/activite-hospitaliere/" },
      { label: "TCA et santé bucco-dentaire", href: "/tca-dents/" },
      { label: "Médias et interviews", href: "/medias-interviews/" },
    ],
    suite: { label: "À propos du Dr Franck Moyal", href: "/franck-moyal/" },
  },
];

/** Les cas montrés sur l'accueil : un par traitement, pour couvrir ce qu'on vient chercher. */
export interface CasVitrine {
  cas: string;
  titre: string;
  href: string;
}

export const casVitrine: CasVitrine[] = [
  {
    cas: "facettes-ceramique",
    titre: "Facettes en céramique",
    href: "/facettes-dentaires-paris/",
  },
  {
    cas: "rehabilitation-usure",
    titre: "Réhabilitation de dents usées",
    href: "/rehabilitation-dents-usees/",
  },
  {
    cas: "eclaircissement-ambulatoire",
    titre: "Éclaircissement ambulatoire",
    href: "/eclaircissement-dentaire-paris/",
  },
  {
    cas: "mih-erosion-infiltration",
    titre: "Taches de MIH",
    href: "/taches-dentaires-dyschromies-icon/",
  },
];
