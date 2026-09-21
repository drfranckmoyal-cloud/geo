import { builtPages } from "../content/site";

// Les liens vers des pages pas encore construites gardent leur adresse définitive (verrou V4)
// et sont marqués, pour être listés dans le rapport de fin de phase.
export function linkAttrs(href: string): Record<string, string> {
  // « /contact/#prendre-rendez-vous » : la page est « /contact/ »
  const future = href.startsWith("/") && !builtPages.includes(href.split("#")[0]);
  if (future) return { "data-a-venir": "" };
  if (href === "#rendez-vous" || href === "#") return { "data-emplacement": "lien à fournir" };
  return {};
}
