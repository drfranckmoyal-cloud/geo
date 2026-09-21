# Pages suivantes — lot B : usures, érosion, TCA

*Claude Code, 22 septembre 2026. Pack « pages suivantes » V1, fichiers 07 à 13, même gabarit
et mêmes composants gelés que le lot A. Les écarts relevés dans l'ensemble du pack
(renvois bibliographiques, H1 trop longs sur mobile, consignes glissées dans le texte, liens)
sont détaillés une seule fois, dans le rapport du lot A (partie 5).*

---

## 1. Ce qui est livré

| N° | Page | Adresse | Données structurées |
|---|---|---|---|
| 07 | Diagnostic des usures dentaires | `/diagnostic-usures-dentaires/` | MedicalWebPage |
| 08 | Réhabilitation des dents usées | `/rehabilitation-dents-usees/` | MedicalWebPage |
| 09 | Bruxisme et usure dentaire | `/bruxisme-usure-dentaire/` | MedicalWebPage |
| 10 | Érosion dentaire | `/erosion-dentaire/` | MedicalWebPage |
| 11 | Dents courtes ou usées | `/dents-courtes-usees/` | MedicalWebPage |
| 12 | TCA et santé bucco-dentaire | `/tca-dents/` | MedicalWebPage |
| 13 | Anorexie restrictive et érosion sans vomissements | `/anorexie-erosion-dentaire-sans-vomissements/` | MedicalWebPage + Article |

Fil d'Ariane de la page 13 : Accueil > Usures dentaires > Érosion dentaire > Anorexie sans
vomissements (enfant de la page Érosion, comme le veut ton arborescence).

## 2. Contrôles

- **Textes** : sur les 7 pages, aucun passage du pack oublié, aucun texte ajouté. Les écarts du
  pack sont signalés à chaque construction (renvois des pages 09 à 13, rapport du lot A §5.1).
- **HTML et 10 contrôles du manifeste** : réussis sur les 16 pages construites. Plan du site :
  les 16 pages.
- **Golden master** : toujours identique, sauf les liens vers les pages désormais construites,
  qui ne sont plus marqués « à venir ».
- **Lighthouse**, page 12 (TCA, la plus longue du lot) :

| | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | Poids |
|---|---|---|---|---|---|---|
| Mobile, 3 passages | 99 | 100 | 100 | 100 | 1,95 s | 199 Ko |
| Ordinateur | 100 | 100 | 100 | 100 | 0,44 s | 199 Ko |

## 3. Une optimisation technique (autorisée par D35), sans effet sur le design

À la première mesure, la page TCA faisait 97 sur mobile, LCP 2,55 s, 283 Ko. La cause : un seul
caractère, le « ń » de Gruszczyński, dans la référence [2]. Il n'appartient pas au jeu de
caractères latin de la police Inter : le navigateur téléchargeait donc un second fichier de
83 Ko, qui retardait l'affichage.

- **Correction** : le site ne déclare plus que le jeu latin d'Inter, exactement la déclaration
  du paquet d'origine, recopiée telle quelle.
- **Résultat** : 99, LCP 1,95 s, 199 Ko.
- **Effet visible** : ce « ń », seul sur le site, s'affiche dans la police du système. La flèche
  « → » (page 12, « repérer tôt → prévenir → … ») s'y affichait déjà : aucun jeu d'Inter ne la
  contient.
- **Golden master** : aucune de ses pages ne contient ces caractères. La page Usures reste à
  99, LCP 1,95 s, 200 Ko.

## 4. Compositions nouvelles (captures)

- **Sommaire cliquable des sections** (page 07) : demandé par son contrat ; c'est le
  « parcours clinique » de la page Usures (capture 01).
- **Intertitres en grille contenant des listes** : « Sources externes / Sources internes »,
  page 10 (captures 02, 03).
- **Bloc « domaine spécifique »** pour l'activité à la CMME (page 12), comme le demande son
  contrat : la composition sur fond vert sauge de la page Usures (captures 04, 05).
- **Appel final réduit au titre et au bouton** : les pages 07 à 13 n'ont pas de phrase
  d'appel ; l'écart titre → bouton reste celui du golden master (captures 06, 07).
- **Emplacement d'infographie en pleine largeur** sous la première section de la page 13
  (capture 08).
- **Le H1 le plus long du pack**, page 12 : 8 lignes à 390 px (capture 09 ; rapport du lot A
  §5.3).

## 5. Rappels propres au lot B

- **Non affichés, à confirmer** : page 10, « Sur le site patient, le message doit donc rester
  simple : » ; page 12, section DentCA, « Cette présence devra être reliée à une page officielle
  DentCA indexable… ».
- **Liens à l'adresse déduite** :
  - 07 « Comprendre le bruxisme et son rôle dans l'usure dentaire » ;
  - 09 « Érosion dentaire : dépistage et prévention » ;
  - 10 « Anorexie restrictive : pourquoi peut-on observer des érosions sans vomissements ? ».
- **Contrat de la page 12** : la CMME est bien en « domaine spécifique ». Le texte cite « les
  chefs de service de la CMME », sans nom, conformément à la note non affichée.

## 6. Emplacements réservés du lot B

| Page | Section | Légende (§9 du fichier) |
|---|---|---|
| 07 | Quels signes font penser à une usure dentaire ? | Photo clinique d'usure avec légende diagnostique |
| 07 | Pourquoi photographier et scanner ? | Comparaison de scans ou capture de monitoring |
| 08 | Réhabiliter une dentition usée… (1re section) | Cas complet de réhabilitation : initial → planification → résultat |
| 08 | Qu'est-ce que la dimension verticale d'occlusion ? | Schéma ou capture de planification DVO issu d'un vrai cas |
| 09 | Pourquoi les dents peuvent-elles s'user chez un patient qui bruxe ? | Schéma — mécanismes d'usure (celui de la page Usures, pas encore produit) |
| 10 | Quels sont les premiers signes ? | Macro de lésions érosives réelles |
| 10 | Comment dépiste-t-on l'érosion ? | Série de scans de suivi |
| 11 | Quel résultat peut-on rechercher ? | Avant / après centré sur les longueurs incisives |
| 12 | Pourquoi le dépistage dentaire est-il important ? | Schéma clinique, photo institutionnelle autorisée ou visuel de prévention neutre |
| 13 | L'absence de vomissements… (pleine largeur) | Infographie sobre des mécanismes : salive / acides / médicaments / contraintes mécaniques |

Non posé : le schéma des sources acides (10), « uniquement s'il est construit dans le langage
graphique gelé ». La grille « Sources externes / internes » tient déjà ce rôle.

## 7. Captures (`captures/`)

| N° | Contenu |
|---|---|
| 01 | Réponse directe et sommaire cliquable (page 07), ordinateur |
| 02, 03 | Intertitres en grille avec listes (page 10), ordinateur et mobile |
| 04, 05 | Activité à la CMME en « domaine spécifique » (page 12), ordinateur et mobile |
| 06, 07 | Appel final réduit au titre et au bouton (page 12), ordinateur et mobile |
| 08 | Première section et emplacement d'infographie pleine largeur (page 13) |
| 09 | Ouverture de la page 12 à 390 px : H1 de 8 lignes |
