// Pages de cas cliniques (POINT 3, phase B — 24/09/2026) : ce que le pack ne porte pas.
//  - la mention commune de fin de page, décidée par ChatGPT (§32) ;
//  - les annonces de cas posées dans les pages thérapeutiques (§21 et §24) : une photographie,
//    la problématique, l'approche en une ligne, et le lien. Les libellés de lien sont ceux que
//    la consigne donne ; les deux lignes de texte sont rédigées à partir des faits validés.
// Les textes des pages elles-mêmes vivent dans docs/pages-suivantes/v1.6/, comme les autres.

/** Mention de fin de page, identique sur les trois pages de cas (ChatGPT, §32) */
export const MENTION_CLINIQUE =
  "Les photographies présentent des situations cliniques individuelles. Le traitement et le résultat dépendent de la situation initiale et ne peuvent être transposés à un autre patient sans examen clinique.";

export interface AnnonceCas {
  /** Cas du registre dont la première photographie illustre l'annonce */
  cas: string;
  probleme: string;
  approche: string;
  lien: { label: string; href: string };
}

export const annoncesCas: Record<string, AnnonceCas> = {
  "planification-facettes": {
    cas: "facettes-planification",
    probleme: "Planifier avant de restaurer",
    approche: "Projet numérique, puis orthodontie pré-prothétique, puis quatre facettes minimalement invasives.",
    lien: {
      label: "Voir un cas clinique associant planification, orthodontie pré-prothétique et facettes",
      href: "/cas-cliniques/planification-facettes-ceramique/",
    },
  },
  "rehabilitation-facettes": {
    cas: "bilan-esthetique",
    probleme: "Voir le projet avant de le réaliser",
    approche: "Simulation numérique d’une réhabilitation esthétique étendue, puis vingt facettes en céramique.",
    lien: {
      label: "Voir un exemple de projet esthétique planifié avant une réhabilitation par facettes",
      href: "/cas-cliniques/planification-rehabilitation-facettes/",
    },
  },
  // Cas d'usure (POINT 3.5) : deux annonces, deux angles — l'origine des lésions sur la page
  // Usures, la préservation tissulaire sur la page Facettes (§21 et §22)
  "usure-3step-origine": {
    cas: "usure-3step",
    probleme: "Comprendre l’origine avant de restaurer",
    approche: "Usures antérieures importantes, une habitude ancienne retrouvée à l’interrogatoire, puis une réhabilitation par facettes minimalement invasives.",
    lien: { label: "Découvrir le cas clinique", href: "/cas-cliniques/usures-dentaires-facettes-minimalement-invasives/" },
  },
  "usure-3step-facettes": {
    cas: "usure-3step",
    probleme: "Facettes et préservation tissulaire",
    approche: "Une réhabilitation esthétique réalisée après analyse d’usures importantes, selon une approche minimalement invasive.",
    lien: { label: "Voir ce cas d’usures traité par facettes minimalement invasives", href: "/cas-cliniques/usures-dentaires-facettes-minimalement-invasives/" },
  },
  "mih-infiltration": {
    cas: "mih-erosion-infiltration",
    probleme: "Réduire le contraste avant de traiter la tache",
    approche: "Éclaircissement puis érosion-infiltration, dans deux situations cliniques différentes.",
    lien: {
      label: "Voir deux cas cliniques de MIH traités par éclaircissement et érosion-infiltration",
      href: "/cas-cliniques/mih-eclaircissement-erosion-infiltration/",
    },
  },
};
