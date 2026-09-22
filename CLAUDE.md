# Consignes pour Claude — projet GEO (site drfranckmoyal.fr)

1. **Lire d'abord `PROJET-MAITRE.md`** : où en est le projet, les verrous, les décisions,
   les questions ouvertes, le journal.
2. Puis le pack de référence en vigueur (indiqué au §3 du fichier maître, aujourd'hui
   `docs/golden-master/v1.3.1/`), dans l'ordre de `00_README.md`, en commençant par
   `00_PROJECT_CONTEXT.md`. Avant tout travail d'interface : `07_ART_DIRECTION.md` et
   `08_VISUAL_QA_CLAUDE.md` en entier. Pour les 20 pages suivantes : le pack en vigueur,
   `docs/pages-suivantes/v1.2/` (`00_ARBORESCENCE_ET_ORDRE.md`, `21_MANIFESTE_INTEGRATION.md`,
   puis un fichier par page, et les fichiers 22 à 25) ; ses textes sont lus directement par
   `src/lib/pack.ts`.
3. **Rôle de Claude : développeur exécutant.** Il ne modifie ni la stratégie, ni
   l'arborescence, ni les textes, ni les couleurs, ni les polices, ni l'ordre des sections.
   Une information manque : emplacement réservé clairement signalé, jamais d'invention.
4. **Tenir `PROJET-MAITRE.md` à jour** à chaque étape et après chaque échange qui décide
   quelque chose : tableau de bord (§0), décisions (§5), questions (§6), étapes et suivi
   des pages (§7), journal (§10), date en bas. Puis commit en français et push.
5. Les fichiers du pack ne se modifient jamais ; une nouvelle version va dans son propre
   dossier (`docs/golden-master/v1.4/`…).
6. Aucune photo ni donnée de patient dans le dépôt. Les photos cliniques du site peuvent rester
   sur le Bureau (synchronisé iCloud) : Franck l'a accepté le 22/09/2026 (D44).
7. Jamais l'expression « dentiste esthétique » (verrou V21) : écrire « dentisterie
   esthétique » ou « exercice exclusif en dentisterie esthétique ».
8. **Golden master gelé le 21/09/2026 (verrou V24)** : ne plus modifier le design system
   (composants, réglages de `src/styles/tokens.css`, typographie, espacements). Toute
   nouvelle page réutilise les composants gelés ; un nouveau composant seulement si aucun
   existant ne convient ; aucune réinterprétation de la direction artistique sans instruction
   explicite. Version de référence : étiquette git `golden-master-gele`.
