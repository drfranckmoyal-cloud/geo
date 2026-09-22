# MESSAGE POUR CLAUDE — PATCH PRÉ-LANCEMENT V1.3

Appliquer le contenu de `DECISIONS_PRE_LANCEMENT_V1_3.md`.

1. Remplacer uniquement le fichier de contenu 06 par `06_taches-dentaires-dyschromies-icon_V1_3.md`.
2. Supprimer les deux lignes résiduelles « Prise de rendez-vous en ligne » et appliquer les libellés téléphone définis.
3. Mettre à jour `Person#franck-moyal.sameAs` selon la liste V1.3.
4. Garder la fiche Google hors du `sameAs` Person ; préparer `#practice` en type `Dentist`.
5. Ajouter DentCA et Smileclub Formation comme `Organization` distinctes avec `founder` → `Person#franck-moyal`, et ajouter les deux liens visibles demandés.
6. Laisser robots.txt totalement ouvert aux moteurs, robots IA de recherche et robots d’entraînement.
7. Masquer automatiquement tout emplacement visuel sans asset validé.
8. Ne publier aucun cas patient tant que le statut de consentement web n’est pas confirmé.
9. Relancer `npm run verify`, le contrôle HTML/JSON-LD, `npm run launch-check` et Lighthouse de la page 06.
10. Confirmer que le H1 V1.3 tient en 4 lignes maximum à 390 px.

Ne modifier aucun token ni composant visuel du Golden Master.
