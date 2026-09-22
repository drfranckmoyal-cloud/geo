// Données structurées (schema.org) : les informations cachées que lisent Google et les IA.
// Types imposés par le pack : accueil WebSite + renvoi vers Person#franck-moyal ;
// page Franck ProfilePage + Person ; page Usures MedicalWebPage + BreadcrumbList + auteur.
// Chaque fait repris ici figure en toutes lettres sur les pages.
// Correctif V1.3 : le cabinet est une entité locale distincte (#practice, type Dentist), décrite
// sur chaque page ; il porte l'adresse, le téléphone et l'e-mail, et Franck y exerce
// (workLocation) — sans répéter ces coordonnées sur Person.
import { site } from "../content/site";

const abs = (path: string) => new URL(path, site.url).href;

export function person(image?: string, full = false, withAddress = false) {
  const base: Record<string, unknown> = {
    "@type": "Person",
    "@id": site.personId,
    name: "Franck Moyal",
    honorificPrefix: "Dr",
    jobTitle: "Chirurgien-dentiste",
    url: abs("/franck-moyal/"),
    ...(image ? { image } : {}),
    ...(site.sameAs.length ? { sameAs: [...site.sameAs] } : {}),
  };
  const workLocation = { "@id": site.practiceId };
  if (!full) return withAddress ? { ...base, workLocation } : base;
  return {
    ...base,
    description:
      "Une pratique dédiée à la dentisterie esthétique et adhésive, au diagnostic des usures dentaires et à leur réhabilitation.",
    workLocation,
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
    // sameAs : profils officiels, sur le nœud de base (site.sameAs)
  };
}

// Le cabinet. sameAs : la fiche Google, quand son adresse publique stable sera connue (V1.3 §3).
export function practice() {
  return {
    "@type": "Dentist",
    "@id": site.practiceId,
    name: site.name,
    url: abs("/"),
    telephone: site.telephoneIntl,
    email: `mailto:${site.email}`,
    address: {
      "@type": "PostalAddress",
      streetAddress: site.address.street,
      postalCode: site.address.postalCode,
      addressLocality: site.address.city,
      addressCountry: site.address.country,
    },
  };
}

// Une organisation fondée par Franck (DentCA, Smileclub Formation)
export function organization(key: keyof typeof site.organizations) {
  const o = site.organizations[key];
  return { "@type": o.type, "@id": o.id, name: o.name, url: o.url, founder: { "@id": site.personId } };
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
