// Réglages communs à tout le site : identité, menu (verrou V23), pied de page (V15).
// Les libellés viennent du pack ou de la réponse de ChatGPT du 21/09/2026 (D10).

import { builtPackUrls, fiche } from "./pages-suivantes.ts";

export const site = {
  url: "https://drfranckmoyal.fr",
  name: "Dr Franck Moyal",
  role: "Chirurgien-dentiste à Paris",
  personId: "https://drfranckmoyal.fr/#franck-moyal",
  websiteId: "https://drfranckmoyal.fr/#website",
  // Le cabinet, entité locale distincte de Franck (type Dentist, correctif V1.3 §3)
  practiceId: "https://drfranckmoyal.fr/#practice",
  lang: "fr-FR",
  // Prise de rendez-vous : pas de réservation en ligne (fiche de Franck, 22/09/2026) ; tous les
  // boutons et liens « Prendre rendez-vous » mènent à la section de prise de rendez-vous de la page
  // Contact, qui donne le téléphone et l'e-mail (règle globale de la V1.2, D41 ; correctif V1.3).
  // Libellé court : en-tête mobile (D33).
  rdv: { label: "Prendre rendez-vous", shortLabel: "Rendez-vous", href: "/contact/#prendre-rendez-vous", provisional: false },
  // Profils officiels du Dr Moyal (fiche du 22/09/2026), déclarés aux moteurs (sameAs) : liste
  // du correctif V1.3 (§2). La fiche Google n'y figure pas : elle ira au cabinet (#practice)
  // quand son adresse publique stable sera connue ; DentCA et Smileclub Formation sont des
  // organisations distinctes (src/content/pages-suivantes.ts, schemaNodes).
  sameAs: [
    "https://www.linkedin.com/in/franck-moyal-7581b6161/",
    "https://www.instagram.com/drfranckmoyal/",
    "https://www.aphp.fr/dr-moyal-franck",
    "https://blendi.fr/formateurs/franck-moyal",
    "https://www.tiktok.com/@drfranckmoyal",
    "https://www.lefildentaire.com/auteur/franck-moyal/",
  ],
  // Contact des patients : téléphone et e-mail, au même niveau (correctif V1.3)
  telephone: fiche.telephone,
  telephoneIntl: fiche.telephoneIntl,
  email: fiche.email,
  mailto: fiche.mailto,
  // Adresse du cabinet (D22), reprise dans les données structurées
  address: { street: "2 rue Hippolyte Lebas", postalCode: "75009", city: "Paris", country: "FR" },
  // Organisations fondées par Franck : des entités distinctes, reliées à lui par « founder », jamais
  // dans ses sameAs (correctif V1.3 §4). Smileclub Formation : type déjà retenu pour la page Franck.
  organizations: {
    dentca: { type: "Organization", id: "https://drfranckmoyal.fr/#dentca", name: "DentCA", url: "https://dentca-asso.com/" },
    smileclub: {
      type: "EducationalOrganization",
      id: "https://drfranckmoyal.fr/#smileclub-formation",
      name: "Smileclub Formation",
      url: "https://smileclubformations.com/",
    },
  },
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
  phone: fiche.telephone, // fiche de Franck, 22/09/2026
  phoneIntl: fiche.telephoneIntl,
  email: fiche.email, // à côté du téléphone (correctif V1.3)
  legal: { label: "Mentions légales", href: "/mentions-legales/" }, // page du lot D (D38)
};
