// Données structurées (schema.org) : les informations cachées que lisent Google et les IA.
// Types imposés par le pack : accueil WebSite + renvoi vers Person#franck-moyal ;
// page Franck ProfilePage + Person ; page Usures MedicalWebPage + BreadcrumbList + auteur.
// Chaque fait repris ici figure en toutes lettres sur les pages.
import { site } from "../content/site";

const abs = (path: string) => new URL(path, site.url).href;

export function person(image?: string, full = false) {
  const base: Record<string, unknown> = {
    "@type": "Person",
    "@id": site.personId,
    name: "Franck Moyal",
    honorificPrefix: "Dr",
    jobTitle: "Chirurgien-dentiste",
    url: abs("/franck-moyal/"),
    ...(image ? { image } : {}),
  };
  if (!full) return base;
  return {
    ...base,
    description:
      "Une pratique dédiée à la dentisterie esthétique et adhésive, au diagnostic des usures dentaires et à leur réhabilitation.",
    workLocation: {
      "@type": "Place",
      address: {
        "@type": "PostalAddress",
        streetAddress: site.address.street,
        postalCode: site.address.postalCode,
        addressLocality: site.address.city,
        addressCountry: site.address.country,
      },
    },
    knowsAbout: [
      "Dentisterie esthétique et adhésive",
      "Usures dentaires",
      "Réhabilitation adhésive",
      "Érosion dentaire",
      "Troubles des conduites alimentaires (TCA)",
    ],
    affiliation: [
      {
        "@type": "Hospital",
        name: "Hôpital Sainte-Anne — GHU Paris",
        department: { "@type": "MedicalClinic", name: "CMME — Clinique des Maladies Mentales et de l’Encéphale" },
      },
      {
        "@type": "Hospital",
        name: "Hôpital Pitié-Salpêtrière — AP-HP",
        department: { "@type": "MedicalClinic", name: "Service de Médecine Bucco-dentaire" },
      },
    ],
    // sameAs : profils externes (LinkedIn…) à ajouter quand les adresses seront fournies (§6, point 11).
  };
}

export function website() {
  return {
    "@type": "WebSite",
    "@id": site.websiteId,
    url: abs("/"),
    name: site.name,
    inLanguage: site.lang,
    publisher: { "@id": site.personId },
    about: { "@id": site.personId },
  };
}

export function breadcrumbs(items: { name: string; path: string }[]) {
  return {
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: item.name,
      item: abs(item.path),
    })),
  };
}

export function graph(nodes: unknown[]) {
  return { "@context": "https://schema.org", "@graph": nodes };
}

export { abs };
