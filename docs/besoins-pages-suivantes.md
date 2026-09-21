# Pages suivantes — ce dont Claude Code a besoin

*Pour ChatGPT, de la part de Claude Code — 21 septembre 2026. Le golden master est gelé
(décision du 21/09/2026) : chaque nouvelle page s'assemble avec les composants existants,
sans nouveau design.*

---

## 1. Deux décisions d'abord

1. **Arborescence définitive.** 00 §11 liste 16 pages restantes, mais 00 §14 parle de « 20 autres pages ». Merci de confirmer la liste exacte, et de dire si « Contact » et « Mentions légales » sont des pages, avec leur adresse.
2. **Ordre de livraison.** Par exemple : le pilier Esthétique et ses 5 pages filles, puis les 6 pages filles du pilier Usures (dont Érosion et TCA), puis les 4 pages d'autorité.

## 2. Pour chaque page, un fichier au format de 02, 03 et 04

- **Adresse** définitive et **page parente**, pour le fil d'Ariane.
- **H1** et **chapeau**.
- **Réponse directe** (40 à 100 mots), si la page en a une.
- **Sections, dans l'ordre**, avec pour chacune :
  - l'étiquette (la question ou l'intention du patient), si la page en utilise ;
  - le titre (H2) ;
  - les textes, les listes et leurs légendes ;
  - les liens : un libellé descriptif et son adresse ;
  - facultatif : le composant souhaité (liste au §3). À défaut, Claude choisit parmi les compositions existantes.
- **FAQ** (questions et réponses), si besoin.
- **Sources scientifiques**, pour les pages médicales, au format du fichier 04 : auteurs, titre, revue, année, DOI, PubMed.
- **Auteur et date de mise à jour.**
- **Référencement** : title, meta description, type de données structurées.
- **Images attendues** : ce qu'elles montrent et où elles vont. Claude pose des emplacements réservés en attendant.

Les textes sont repris mot pour mot et vérifiés par un contrôle automatique. Tout ce qui doit apparaître doit donc être écrit dans le fichier : Claude n'invente rien.

## 3. Composants gelés disponibles

| Composant | Rôle |
|---|---|
| `EditorialHero` | Ouverture avec portrait (page de profil) |
| `ClinicalHero` | Ouverture clinique : fil d'Ariane, H1, chapeau, auteur |
| `HeroSplit` | Ouverture de l'accueil |
| `DirectAnswer` | Réponse directe, sur fond vert sauge discret |
| `ClinicalPathway` | Sommaire cliquable des sections de la page |
| `TextImageSection` | Section de texte, en 6 compositions : image à droite, image à gauche, texte décalé, colonne de lecture, texte + colonne latérale, bloc « domaine spécifique » sur fond sauge |
| `SymptomList` | Liste clinique (signes, facteurs, outils), sur 1 ou 2 colonnes |
| `PullStatement` | Titre-manifeste ou phrase clé en grand |
| `MethodSteps` | Liste d'étapes numérotées |
| `PillarPair` | Deux territoires côte à côte |
| `PhilosophyStatement` | Mots manifestes empilés + texte |
| `AuthorityStrip` / `InlineEvidenceLinks` | Texte + liens de preuve |
| `FAQAccordion` | FAQ, ouverte par défaut |
| `SourceList` | Sources scientifiques, repliables sur mobile |
| `AuthorBlock` | Auteur, en bloc court, avec date de mise à jour |
| `RelatedPages` | Pages liées (« Approfondir… ») |
| `FinalCTA` | Appel final (prise de rendez-vous) |

## 4. Règles de rédaction déjà actées

- **Jamais « dentiste esthétique »** : écrire « dentisterie esthétique » ou « exercice exclusif en dentisterie esthétique ».
- **Intertitres (H2)** formulés comme des intentions ou de vraies questions ; réponses directes de 40 à 100 mots.
- **Liens** avec des libellés descriptifs, compréhensibles hors contexte (jamais « En savoir plus »).
- **Pages médicales** : sources, auteur, date de mise à jour.
- **Libellés et adresses** : ceux du menu figé et de l'arborescence du pack.

## 5. Toujours attendus (non bloquants)

- Téléphone du cabinet.
- Lien de prise de rendez-vous.
- Adresses exactes des profils `sameAs` (LinkedIn, AP-HP, Le Fil Dentaire, Blendi).
- Visuels : piliers, photographie clinique, schéma des mécanismes d'usure, cas avant / après.
