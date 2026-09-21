// Réglages communs à tout le site : identité, menu (verrou V23), pied de page (V15).
// Les libellés viennent du pack ou de la réponse de ChatGPT du 21/09/2026 (D10).

export const site = {
  url: "https://drfranckmoyal.fr",
  name: "Dr Franck Moyal",
  role: "Chirurgien-dentiste à Paris",
  personId: "https://drfranckmoyal.fr/#franck-moyal",
  websiteId: "https://drfranckmoyal.fr/#website",
  lang: "fr-FR",
  // Prise de rendez-vous : en attente (D8). Emplacement réservé : ancre vers le bloc final.
  rdv: { label: "Prendre rendez-vous", href: "#rendez-vous" },
} as const;

// Pages construites dans le golden master (V1). Tout autre lien interne mène à une page à venir.
export const builtPages = ["/", "/franck-moyal/", "/usures-dentaires/"];

export const nav = [
  { label: "Dentisterie esthétique", href: "/dentisterie-esthetique-paris/" },
  { label: "Usures dentaires", href: "/usures-dentaires/" },
  { label: "Érosion & TCA", href: "/tca-dents/" }, // destination à confirmer (§6, point 23)
  { label: "Dr Franck Moyal", href: "/franck-moyal/" },
  { label: "Publications & enseignement", href: "/publications/" }, // idem
];

export const footer = {
  groups: [
    [
      { label: "Dentisterie esthétique et adhésive", href: "/dentisterie-esthetique-paris/" },
      { label: "Usures dentaires", href: "/usures-dentaires/" },
    ],
    [
      { label: "Dr Franck Moyal", href: "/franck-moyal/" },
      { label: "Publications", href: "/publications/" },
      { label: "Activité hospitalière", href: "/activite-hospitaliere/" },
    ],
  ],
  contactLabel: "Contact",
  // Emplacements réservés (D8)
  address: "Adresse du cabinet — à fournir",
  phone: "Téléphone — à fournir",
  legal: { label: "Mentions légales", href: "#" }, // page non prévue dans l'arborescence (§6, point 9)
};
