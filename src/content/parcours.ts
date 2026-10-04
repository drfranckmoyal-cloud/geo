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
      { label: "Dentisterie esthétique et adhésive", href: "/dentisterie-esthetique-paris/" },
      { label: "Usures dentaires", href: "/usures-dentaires/" },
      { label: "Facettes dentaires", href: "/facettes-dentaires-paris/" },
      { label: "Composite bonding", href: "/composite-bonding-paris/" },
      { label: "Éclaircissement dentaire", href: "/eclaircissement-dentaire-paris/" },
      { label: "Taches blanches, MIH et dyschromies", href: "/taches-dentaires-dyschromies-icon/" },
      { label: "Érosion dentaire", href: "/erosion-dentaire/" },
      { label: "Bilan esthétique personnalisé", href: "/bilan-esthetique-personnalise/" },
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
