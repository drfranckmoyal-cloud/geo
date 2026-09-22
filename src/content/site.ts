// Réglages communs à tout le site : identité, menu (verrou V23), pied de page (V15).
// Les libellés viennent du pack ou de la réponse de ChatGPT du 21/09/2026 (D10).

import { builtPackUrls } from "./pages-suivantes.ts";

export const site = {
  url: "https://drfranckmoyal.fr",
  name: "Dr Franck Moyal",
  role: "Chirurgien-dentiste à Paris",
  personId: "https://drfranckmoyal.fr/#franck-moyal",
  websiteId: "https://drfranckmoyal.fr/#website",
  lang: "fr-FR",
  // Prise de rendez-vous : pas de réservation en ligne (fiche de Franck, 22/09/2026) ; tous les
  // boutons et liens « Prendre rendez-vous » mènent à la section du même nom de la page Contact, qui
  // donne le téléphone (règle globale de la V1.2, D41). Libellé court : en-tête mobile (D33).
  rdv: { label: "Prendre rendez-vous", shortLabel: "Rendez-vous", href: "/contact/#prendre-rendez-vous", provisional: false },
  // Profils officiels du Dr Moyal (fiche du 22/09/2026), déclarés aux moteurs (sameAs) : ceux que
  // ChatGPT a retenus (LinkedIn, Instagram, AP-HP, Blendi) ; les autres attendent sa revue.
  sameAs: [
    "https://www.linkedin.com/in/franck-moyal-7581b6161/",
    "https://www.instagram.com/drfranckmoyal/",
    "https://www.aphp.fr/dr-moyal-franck",
    "https://blendi.fr/formateurs/franck-moyal",
  ],
  // Adresse du cabinet (D22), reprise dans les données structurées
  address: { street: "2 rue Hippolyte Lebas", postalCode: "75009", city: "Paris", country: "FR" },
} as const;

// Pages construites : le golden master (V1), puis les lots du pack « pages suivantes » livrés.
// Tout autre lien interne mène à une page à venir.
export const builtPages = ["/", "/franck-moyal/", "/usures-dentaires/", ...builtPackUrls];

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
  phone: "01 83 75 52 16", // fiche de Franck, 22/09/2026
  phoneIntl: "+33183755216",
  legal: { label: "Mentions légales", href: "/mentions-legales/" }, // page du lot D (D38)
};
