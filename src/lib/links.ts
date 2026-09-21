import { builtPages, site } from "../content/site";

// Les liens vers des pages pas encore construites gardent leur adresse définitive (verrou V4)
// et sont marqués, pour être listés dans le rapport de fin de phase.
export function linkAttrs(href: string): Record<string, string> {
  // « /contact/#prendre-rendez-vous » : la page est « /contact/ »
  const future = href.startsWith("/") && !builtPages.includes(href.split("#")[0]);
  if (future) return { "data-a-venir": "" };
  // Prise de rendez-vous : destination provisoire tant que le lien définitif manque (D8, D41)
  if (href === site.rdv.href && site.rdv.provisional) return { "data-emplacement": "lien de rendez-vous à fournir" };
  if (href === "#") return { "data-emplacement": "lien à fournir" };
  return {};
}
