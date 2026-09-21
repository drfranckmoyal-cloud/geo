# Golden master drfranckmoyal.fr — tour 2 (corrections P0)

*Claude Code, 21 septembre 2026. Réponse au contrôle du tour 1 par ChatGPT
(`docs/echanges/2026-09-21-chatgpt-retour-golden-master-tour1.md`, décisions D16 à D28).
Série courte de 15 captures dans `captures/`, comme demandé : pas de nouveau tour de 26 captures.*

---

## 1. Les 10 corrections P0

| # | Demande | Fait | Capture |
|---|---|---|---|
| 1 | Titres en **Newsreader** (400 pour H1 et H2, 400 ou 500 pour H3, `font-optical-sizing: auto`), Inter inchangée | Fait. H1, H2 et phrases manifestes en 400 ; H3 et noms d'étapes en 500 ; ajustement au corps actif. **Tailles inchangées**, testées d'abord comme demandé : aucun titre ne dépasse 4 lignes et aucun ne déborde, à aucune des 6 largeurs. Seul ajustement : les interlettrages négatifs prévus pour Cormorant, adoucis. | 01 à 06 |
| 2 | **En-tête mobile** : bouton 40–42 px, 14–15 px, marges 16–18 px, largeur automatique ; « Menu » 14–15 px ; en-tête compact | Fait. Bouton 40 px, texte 14 px, marges 16 px ; « Menu » 15 px ; en-tête de 64 px sur mobile. Les boutons dans les pages restent à 52 px. | 11, 12 |
| 3 | **Méthode en 7 étapes**, « Simuler » entre « Planifier » et « Décider ensemble » | Fait. **Texte provisoire** pour « Simuler » : « simulation 2D / 3D / dynamique selon les cas. », repris mot pour mot de 00 §5. « Planifier » garde son texte (« simulation et projet lorsque pertinent. »), qui parle déjà de simulation : les deux textes sont à valider (question ci-dessous). | 07, 08 |
| 4 | **Sous-menus** « Érosion & TCA » et « Publications & enseignement », ordinateur et mobile | Fait. Ordinateur : bouton avec un petit chevron, qui ouvre un panneau sobre bordé d'un filet, sans ombre, au clic ou au clavier, et se ferme par Échap ou par un clic à côté. Mobile : les deux groupes apparaissent dans le panneau « Menu », sous une petite étiquette. Tous les liens restent dans le HTML. | 13, 14, 15 |
| 5 | **Sources Usures** : sans « Soutient : », DOI et PubMed discrets, liste repliable sur mobile | Fait. Les notes « Soutient : » ne sont plus affichées ; elles restent dans les données, pour la traçabilité. Sur mobile, la liste se replie derrière « Voir les 7 sources scientifiques » : elle est fermée au chargement, s'ouvre si l'on clique un renvoi [n], et reste entière dans le HTML. | 09, 10 |
| 6 | **Bloc auteur court** + « Mis à jour le 21 septembre 2026 » + `dateModified` | Fait. « Dr Franck Moyal — Chirurgien-dentiste à Paris » est un lien vers `/franck-moyal/`, suivi de « *Dentisterie esthétique et adhésive, usures dentaires et érosion.* » et de la date de mise à jour, balisée pour les moteurs. `dateModified: 2026-09-21` figure dans les données structurées de la page. | 09, 10 |
| 7 | **Parcours clinique** cliquable ou supprimé | Déjà cliquable : chaque étape mène à l'ancre de sa section, sans que l'en-tête ne la masque. Conservé. | 05, 06 |
| 8 | **Pages liées** → « Approfondir les usures dentaires » | Fait. | — |
| 9 | **Adresse** : 2 rue Hippolyte Lebas, 75009 Paris | Fait : dans le pied de page (balise `address`) et dans les données structurées (lieu d'exercice de Franck). Téléphone toujours « à fournir ». | — |
| 10 | **Réponse directe** moins massive sur mobile : 19–20 px, marges 24–28 px | Fait : 19 px et 26 px de marges à 390–430 px. Inchangée sur ordinateur. | 06 |

## 2. Portrait en haute définition (P1, n° 11) — reçu et intégré

Franck a fourni l'original le 21/09/2026 : **6 048 × 4 024 px**, la résolution native de son Nikon D780. Le détail est réel (cils, grain de la peau), sans aucun agrandissement artificiel.

Traitement appliqué :
- recadrage vertical 4:5 sur toute la hauteur, centré sur le visage (10 % d'air au-dessus des cheveux), exporté en 1 600 × 2 000 px ;
- **contraste local du visage légèrement renforcé**, comme demandé : égalisation locale douce, mélangée à 60 % avec l'original pour rester discrète ;
- point noir calé sur le noir doux, tons du noir doux au blanc cassé (traitement du tour 1 conservé).

Le portrait remplit désormais toute la largeur de son aplat sur l'accueil, et s'affiche plus grand sur la page Franck, net sur les écrans haute définition.

## 3. Contrôles

- **Textes** (`npm run verify`) : aucun écart. Les nouveaux textes viennent tous du retour de ChatGPT : menu, étiquette des sources, bloc auteur, titre des pages liées, adresse. Les 7 notes « Soutient : » sont comptées comme volontairement non affichées (D19). « Dentiste esthétique » : absent partout.
- **HTML** (`node scripts/check-html.mjs`) : réussi. Un seul H1 par page, aucun saut de niveau, données structurées conformes.
- **Lighthouse 13.5** (build final servi en local) :

| Page | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | Poids |
|---|---|---|---|---|---|---|
| Accueil — mobile / ordinateur | 99 / 100 | 100 | 100 | 100 | 2,1 s / 0,4 s | 214 Ko |
| Franck — mobile / ordinateur | 99 / 100 | 100 | 100 | 100 | 2,1 s / 0,4 s | 214 Ko |
| Usures — mobile / ordinateur | 95 / 100 | 100 | 100 | 100 | 2,9 s / 0,6 s | 344 Ko |

Newsreader et le portrait HD alourdissent un peu les pages (92–117 Ko au tour 1). Sur la page Usures, l'italique de Newsreader (147 Ko) ne sert qu'à la phrase clé et à la ligne de l'auteur. **Option** : les passer en romain ferait tomber la page à environ 200 Ko. Je ne l'ai pas fait sans votre accord, car cela change l'aspect validé de la phrase clé.

## 4. Points encore ouverts

1. **Textes de « Planifier » et de « Simuler »** : à valider ou à fournir (§1, n° 3).
2. **Téléphone du cabinet** et **lien de prise de rendez-vous** : toujours attendus.
3. **Profils `sameAs`** (LinkedIn, AP-HP, Le Fil Dentaire, Blendi) : il manque les adresses exactes.
4. **P1** : photos des deux piliers, photographie clinique, schéma des mécanismes, cas avant / après avec consentement.
5. **Avant la mise en ligne** : réglage des robots par usage (D27) — OAI-SearchBot, Googlebot et Bingbot autorisés ; GPTBot à décider à part.

## 5. Captures (`captures/`)

| N° | Contenu |
|---|---|
| 01 à 06 | Ouvertures des 3 pages, ordinateur (1440 px) et mobile (430 px) |
| 07, 08 | Section Méthode (7 étapes), ordinateur et mobile |
| 09, 10 | Sources et auteur, ordinateur et mobile (liste repliée) |
| 11, 12 | En-tête mobile, 390 et 430 px |
| 13, 14 | Menu ordinateur, sous-menus ouverts |
| 15 | Menu mobile ouvert |
