# 21 — MANIFESTE D’INTÉGRATION CLAUDE CODE

## Principe
Ces fichiers sont les contrats éditoriaux des 20 pages restantes. Le texte visible doit être repris mot pour mot, à l’exception :
- des éléments explicitement marqués `[À FOURNIR]` ;
- des notes d’implémentation marquées « NON AFFICHÉES » ;
- des URLs de preuves/sources qui deviennent des liens ;
- des libellés de structure du fichier (`ROUTING`, `SEO`, etc.), qui ne sont pas du contenu patient.

## Golden Master
Réutiliser exclusivement les composants gelés.

## Contrôles automatiques à ajouter
Pour chaque nouvelle route :
1. un seul H1 ;
2. fil d’Ariane conforme ;
3. title + meta + canonical ;
4. `dateModified` si page clinique/médicale ;
5. auteur relié à `https://drfranckmoyal.fr/#franck-moyal` ;
6. sources présentes dans le HTML des pages médicales ;
7. liens internes descriptifs ;
8. aucun texte « dentiste esthétique » ;
9. aucune image stock inventée ;
10. aucune modification des tokens du Golden Master.

## Livraison par lot
Après chaque lot A/B/C/D :
- build ;
- `npm run verify` ;
- contrôle HTML ;
- Lighthouse sur 1 page représentative desktop/mobile ;
- captures uniquement des nouvelles compositions qui n’existaient pas déjà.

## Données toujours en attente
- téléphone ;
- URL de prise de rendez-vous ;
- e-mail professionnel pour mentions légales ;
- hébergeur pour mentions légales ;
- URLs sameAs exactes ;
- visuels propriétaires.
