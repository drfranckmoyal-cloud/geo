# Pages suivantes — lot C : autorité, entité, page locale

*Claude Code, 22 septembre 2026. Pack « pages suivantes » V1, fichiers 14 à 18, même gabarit
et mêmes composants gelés que les lots A et B. Les écarts de l'ensemble du pack restent
détaillés dans le rapport du lot A (partie 5).*

---

## 1. Ce qui est livré

| N° | Page | Adresse | Données structurées |
|---|---|---|---|
| 14 | Publications et travaux | `/publications/` | CollectionPage, avec les 5 publications (voir §3) |
| 15 | Conférences et formations | `/conferences-formations/` | CollectionPage |
| 16 | Activité hospitalière | `/activite-hospitaliere/` | WebPage |
| 17 | Médias et interviews | `/medias-interviews/` | CollectionPage |
| 18 | Chirurgien-dentiste à Paris 9 | `/chirurgien-dentiste-paris-9/` | WebPage + adresse du lieu d'exercice (PostalAddress) |

Pages 14 à 17 : fil d'Ariane Accueil > Dr Franck Moyal > …, et la page déclarée « à propos »
de `Person#franck-moyal`.

## 2. Contrôles

- **Textes** : sur les 5 pages, aucun passage du pack oublié, aucun texte ajouté.
- **HTML et 10 contrôles du manifeste** : réussis sur les 21 pages construites. Plan du site :
  les 21 pages.
- **Liens externes** : les preuves s'ouvrent dans un nouvel onglet, en
  `rel="noopener noreferrer"`, comme le demande le fichier 17.
- **Golden master** : toujours identique, sauf les liens vers les pages désormais construites,
  qui ne sont plus marqués « à venir ».
- **Lighthouse**, page 18 (page locale) :

| | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | Poids |
|---|---|---|---|---|---|---|
| Mobile, 3 passages | 99 | 100 | 100 | 100 | 1,95 s | 194 Ko |
| Ordinateur | 100 | 100 | 100 | 100 | 0,44 s | 194 Ko |

## 3. Choix à valider

1. **Ouverture** : l'ouverture clinique est gardée pour les pages d'autorité (fil d'Ariane, H1,
   chapeau, auteur). Ton contrat l'autorisait « sans bloc médical lourd », et elle n'en a pas.
2. **Pas de bloc auteur sur les pages 14 à 17**, ni d'appel final : leurs contrats ne les
   prévoient pas, et le pack ne donne pas de CTA. La date de mise à jour figure dans les
   données structurées (`dateModified`).
3. **Blocs « # Titre »** (« Smileclub Formation », « Hôpital Pitié-Salpêtrière »…) : titre de
   section (H2) ; leurs sous-titres « ## » deviennent des H3, sans saut de niveau.
4. **Preuves externes** (« Lire l'article original », « Voir la source »…) : liste sobre à
   filets et flèche fine, la composition des liens de preuve de la page Franck (captures 02, 06).
5. **Grilles** : quand un bloc aligne 2 à 4 entrées courtes, elles passent en grille à filets
   vert sauge. C'est le cas des deux ouvrages (14), des quatre interventions (15), des trois
   changements apportés par l'hôpital (16), des trois conférences (17), des trois motifs de
   consultation et des trois principes (18).
6. **Aucun emplacement d'image** sur ces pages : toutes les images prévues au §9 sont
   facultatives (« si droits d'utilisation clairs », « si autorisées », « si disponible »), et
   le fichier 18 exclut toute carte générique.
7. **Page 18, bloc final** : le pack donne l'adresse, « Téléphone : à compléter » et « Prise de
   rendez-vous en ligne : lien à compléter », sans libellé de bouton. Le bloc est donc affiché
   sans bouton ; il porte l'ancre `#rendez-vous`, et le bouton de l'en-tête y mène (capture 10).
8. **Typographie** : « Paris 9 » ne se coupe plus en fin de ligne. Le « 9 » partait seul sur la
   ligne suivante du H1 de la page 18 ; une espace insécable relie désormais « Paris » au numéro
   d'arrondissement. Pages 18 et 19 seulement, rien au golden master.

## 4. Données structurées de la page Publications

Ton §8 demande « Person auteur lorsqu'une publication lui est attribuée ». Les 5 publications de
la page y sont décrites, auteur relié à `Person#franck-moyal`, co-auteurs nommés comme sur la
page :

1. « Fermeture de diastème au composite en technique directe : la « Front Wing Technique » »,
   Le Fil Dentaire, 9 octobre 2023 ;
2. « Santé et précarité : les permanences d'accès aux soins de santé bucco-dentaire », La Santé
   de l'Homme, 2012, n° 417, p. 31–33, avec les 8 co-auteurs cités ;
3. « Cancers de la cavité buccale — du diagnostic aux applications thérapeutiques », Éditions
   CdP, 2008, ISBN 9782843611292 ;
4. « La chirurgie orale » — sans date ni éditeur : la page n'en affiche pas (la note de
   normalisation bibliographique n'est pas affichée) ;
5. « La première consultation en implantologie », Le Fil Dentaire.

Les travaux académiques encadrés n'y figurent pas, conformément à ton §10.

## 5. Rappels propres au lot C

- **Non affichée, à confirmer** : page 14, la « Note de normalisation bibliographique » de
  « La chirurgie orale ».
- **Liens à l'adresse déduite** : 14 « Découvrir le composite bonding » ; 15 « Usures
  dentaires : comprendre avant de reconstruire ».
- **Liens à câbler placés nulle part** : « Composite bonding à Paris » (15) et « Usures
  dentaires » (17), absents des listes « À lire aussi » écrites dans le pack (rapport du lot A,
  §5.6).
- **Page 16** : la formulation publique indiquée dans la note non affichée diffère légèrement du
  texte ; c'est le texte du §5 qui est affiché (rapport du lot A, §5.7).

## 6. Captures (`captures/`)

| N° | Contenu |
|---|---|
| 01 | Page Activité hospitalière entière, ordinateur 1440 (page d'autorité, sans image) |
| 02 | Une publication : date, liste, preuve externe, lien interne (page 14) |
| 03 | Deux ouvrages en grille (page 14) |
| 04, 05 | Quatre interventions documentées en grille (page 15), ordinateur et mobile |
| 06 | Deux preuves externes à la suite (page 17) |
| 07, 08 | Trois motifs de consultation en grille, avec listes et liens (page 18), ordinateur et mobile |
| 09 | Trois principes en grille (page 18) |
| 10 | Bloc final d'informations pratiques, sans bouton (page 18) |
| 11 | « À lire aussi » écrit dans le pack, sans appel final, puis pied de page (page 14) |
