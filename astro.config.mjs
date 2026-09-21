// Configuration du site : pages HTML statiques, adresses terminées par « / » comme dans
// l'arborescence du pack (verrou V4), plan du site pour les moteurs (pages indexables seulement).
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://drfranckmoyal.fr",
  trailingSlash: "always",
  build: { format: "directory", inlineStylesheets: "always" },
  // Les mentions légales ne sont pas à indexer (noindex,follow, D38) : hors du plan du site
  integrations: [sitemap({ filter: (page) => !page.endsWith("/mentions-legales/") })],
  devToolbar: { enabled: false },
});
