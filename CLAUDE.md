# Consignes pour Claude — projet GEO (site drfranckmoyal.fr)

1. **Lire d'abord `PROJET-MAITRE.md`** : où en est le projet, les verrous, les décisions,
   les questions ouvertes, le journal.
2. Puis le pack de référence en vigueur (indiqué au §3 du fichier maître, aujourd'hui
   `docs/golden-master/v1.3.1/`), dans l'ordre de `00_README.md`, en commençant par
   `00_PROJECT_CONTEXT.md`. Avant tout travail d'interface : `07_ART_DIRECTION.md` et
   `08_VISUAL_QA_CLAUDE.md` en entier. Pour les 20 pages suivantes : le pack en vigueur,
   `docs/pages-suivantes/v1.2/` (`00_ARBORESCENCE_ET_ORDRE.md`, `21_MANIFESTE_INTEGRATION.md`,
   puis un fichier par page, et les fichiers 22 à 25), avec le correctif pré-lancement
   `docs/pages-suivantes/v1.3/` (page 06 et décisions) et la page pilier `docs/pages-suivantes/v1.4/` ;
   ses textes sont lus directement par `src/lib/pack.ts`. Les consignes de ChatGPT reçues après le
   gel sont archivées telles quelles dans `docs/echanges/` (une par fichier daté).
3. **Rôle de Claude : développeur exécutant.** Il ne modifie ni la stratégie, ni
   l'arborescence, ni les textes, ni les couleurs, ni les polices, ni l'ordre des sections.
   Une information manque : emplacement réservé clairement signalé, jamais d'invention.
4. **Tenir `PROJET-MAITRE.md` à jour** à chaque étape et après chaque échange qui décide
   quelque chose : tableau de bord (§0), décisions (§5), questions (§6), étapes et suivi
   des pages (§7), journal (§10), date en bas. Puis commit en français et push.
5. Les fichiers du pack ne se modifient jamais ; une nouvelle version va dans son propre
   dossier (`docs/golden-master/v1.4/`…).
6. **Photographies cliniques** : les versions publiées sur le site vivent dans le dépôt
   (`src/assets/photos/cas/`, fabriquées par `npm run photos`), Franck l'a tranché le 24/09/2026
   (D52) ; les originaux restent dans son dossier `~/Desktop/icono GEO`, qu'on ne modifie jamais
   (D44, 22/09/2026). Aucun nom, aucune date, aucune donnée nominative de patient, nulle part —
   ni dans les légendes, ni dans les noms de fichiers, ni dans les métadonnées. Le registre des
   cas est `src/content/cas-cliniques.ts`.
7. Jamais l'expression « dentiste esthétique » (verrou V21) : écrire « dentisterie
   esthétique » ou « exercice exclusif en dentisterie esthétique ». Seule exception, décidée par
   Franck le 24/09/2026 (D50) : la page pilier `/dentisterie-esthetique-paris/`, où l'expression
   reprend la recherche des patients. `npm run verify` contrôle les deux.
8. **Golden master gelé le 21/09/2026 (verrou V24)** : ne plus modifier le design system
   (composants, réglages de `src/styles/tokens.css`, typographie, espacements). Toute
   nouvelle page réutilise les composants gelés ; un nouveau composant seulement si aucun
   existant ne convient ; aucune réinterprétation de la direction artistique sans instruction
   explicite. Version de référence : étiquette git `golden-master-gele`.
