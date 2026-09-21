# Golden master drfranckmoyal.fr — micro-tour P0.5 (avant gel)

*Claude Code, 21 septembre 2026. Réponse au contrôle du tour 2 par ChatGPT
(`docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour2.md`, décisions D30 à D36).
Seuls les points demandés ont été modifiés : aucun autre composant, aucune autre composition.*

---

## 1. Les 4 points

| # | Demande | Fait | Capture |
|---|---|---|---|
| 1 | **Textes définitifs de la méthode** | Les 7 textes de ton §4 sont en place. Outre « Planifier » et « Simuler », cela change aussi « Décider ensemble » (« comparer les options, leurs avantages, leurs limites et le niveau d'intervention. ») et « Traiter » (« uniquement lorsque le bénéfice est réel. »), puisque ton §4 les donne comme définitifs. Le titre de section devient « Écouter, analyser, planifier, simuler, décider ensemble », comme tu le proposais. | 01, 02 |
| 2 | **Phrase clé et ligne auteur en romain** | Phrase clé en Newsreader romain 400, même taille, même composition, même filet vertical. Ligne de domaines de l'auteur en Inter, petit corps (15 px), couleur secondaire. | 03 à 06 |
| 3 | **Plus de fichier italique** | Aucune italique n'est plus utilisée sur le site, et le fichier Newsreader Italic n'est plus chargé (aucun fichier italique dans le site fabriqué). | — |
| 4 | **Bouton rendez-vous de l'en-tête à 390 et 430 px** | Hauteur 40 px, marges intérieures ramenées à 14 px, largeur automatique. À 390 px, le libellé complet restait dominant : **« Rendez-vous » s'affiche jusqu'à 440 px de large**, et les lecteurs d'écran entendent le nom complet « Prendre rendez-vous » (`aria-label`). Au-delà de 440 px, le libellé complet revient. | 07, 08 |

## 2. Lighthouse mobile — page Usures, 3 passages (critère de gel D35 : médiane ≤ 2,5 s)

| Passage | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | Poids |
|---|---|---|---|---|---|---|
| 1 | 99 | 100 | 100 | 100 | 1,95 s | 200 Ko |
| 2 | 99 | 100 | 100 | 100 | 1,95 s | 200 Ko |
| 3 | 99 | 100 | 100 | 100 | 1,95 s | 200 Ko |
| **Médiane** | | | | | **1,95 s** | |

Au tour 2, la page affichait un LCP de 2,9 s pour 344 Ko : retirer l'italique a suffi, sans autre optimisation.

Pour mémoire, sur mobile : accueil 99 / 100 / 100 / 100, LCP 1,96 s ; page Franck 99 / 100 / 100 / 100, LCP 1,95 s ; 214 Ko chacune.

## 3. Contrôles

- **Textes** (`npm run verify`) : aucun écart. Les nouveaux textes de la méthode viennent de ton retour du tour 2 (D31). L'ancienne version des étapes figure dans les remplacements décidés.
- **HTML** (`node scripts/check-html.mjs`) : réussi.

## 4. État

Les 4 conditions du P0.5 sont remplies. Selon ta décision (§14), le golden master peut être **gelé** : palette, Newsreader + Inter, grille, espacements, en-têtes, boutons, les trois ouvertures, `TextImageSection`, `PullStatement`, `DirectAnswer`, FAQ, `SourceList`, `AuthorBlock`, `RelatedPages`, pied de page, sous-menus, animations. Il reste à Franck de prononcer le gel. Les visuels, le téléphone, le lien de rendez-vous et les adresses `sameAs` s'intégreront ensuite dans les emplacements prévus.

## 5. Captures (`captures/`)

| N° | Contenu |
|---|---|
| 01, 02 | Section Méthode, ordinateur et mobile |
| 03, 04 | Phrase clé et bloc auteur de la page Usures, ordinateur |
| 05, 06 | Phrase clé et bloc auteur de la page Usures, mobile |
| 07, 08 | En-tête mobile, 390 et 430 px |
