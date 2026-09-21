// Configuration du site : pages HTML statiques, adresses terminées par « / » comme dans
// l'arborescence du pack (verrou V4), plan du site pour les moteurs.
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://drfranckmoyal.fr",
  trailingSlash: "always",
  build: { format: "directory", inlineStylesheets: "always" },
  integrations: [sitemap()],
  devToolbar: { enabled: false },
});
