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
  rdv: { label: "Prendre rendez-vous", shortLabel: "Rendez-vous", href: "#rendez-vous" }, // libellé court : en-tête mobile (D33)
  // Adresse du cabinet (D22), reprise dans les données structurées
  address: { street: "2 rue Hippolyte Lebas", postalCode: "75009", city: "Paris", country: "FR" },
} as const;

// Pages construites dans le golden master (V1). Tout autre lien interne mène à une page à venir.
export const builtPages = ["/", "/franck-moyal/", "/usures-dentaires/"];

// Deux rubriques groupées ouvrent un sous-menu (D18, contrôle du tour 1 par ChatGPT).
export type NavLink = { label: string; href: string };
export type NavItem = { label: string; href?: string; children?: NavLink[] };

export const nav: NavItem[] = [
  { label: "Dentisterie esthétique", href: "/dentisterie-esthetique-paris/" },
  { label: "Usures dentaires", href: "/usures-dentaires/" },
  {
    label: "Érosion & TCA",
    children: [
      { label: "Érosion dentaire", href: "/erosion-dentaire/" },
      { label: "TCA et santé bucco-dentaire", href: "/tca-dents/" },
    ],
  },
  { label: "Dr Franck Moyal", href: "/franck-moyal/" },
  {
    label: "Publications & enseignement",
    children: [
      { label: "Publications", href: "/publications/" },
      { label: "Conférences & formations", href: "/conferences-formations/" },
      { label: "Activité hospitalière", href: "/activite-hospitaliere/" },
      { label: "Médias & interviews", href: "/medias-interviews/" },
    ],
  },
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
  address: "2 rue Hippolyte Lebas, 75009 Paris", // D22
  phone: "Téléphone — à fournir", // emplacement réservé (D8)
  legal: { label: "Mentions légales", href: "#" }, // page non prévue dans l'arborescence (§6, point 9)
};
