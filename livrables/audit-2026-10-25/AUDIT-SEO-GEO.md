# Audit SEO / GEO du site en ligne — 25/10/2026

Demande de Franck, le soir de la mise en ligne de la refonte : « refais un audit SEO GEO du site nouveau ».

Méthode : exploration des 37 pages publiées (titres, descriptions, contenus, liens, images, données
structurées) ; contrôles techniques sur le vrai domaine ; Lighthouse en mode téléphone sur quatre pages
clés (PageSpeed de Google refusait les mesures ce soir-là, quota dépassé) ; positions Google du relevé
quotidien (`suivi/releves/2026-10-25.json`) et visibilité dans les IA (relevés des 21–22/10). Positions et
IA décrivent encore **l'ancien site** : la refonte n'est en ligne que depuis quelques heures. Ce sont les
chiffres de départ, à comparer dans trois à quatre semaines.

## 1. En bref

| | État | Ce qu'il faut retenir |
|---|---|---|
| Technique | **Très bon** | Lighthouse « SEO » 100 sur 4 pages sur 4 ; https, redirections, plan du site, adresses de référence, page 404, compression, réponse du serveur en 0,09 s. |
| Vitesse | **À améliorer** | Accueil 78/100 (affichage complet en 5,9 s), Espace patients 75/100 (10,4 s, 4,4 Mo) ; Usure 95, TCA 100. Cause unique : les images, trop lourdes. |
| Partage (LinkedIn, WhatsApp) | **À faire** | Aucune des 37 pages n'a d'image d'aperçu : un lien partagé s'affiche sans photo. |
| Données pour Google et les IA | **Bon, à compléter** | Présentes partout. Fiche du cabinet incomplète (horaires, coordonnées GPS, lien fiche Google) ; fiche du praticien sans domaines d'expertise ni affiliations. Vidéos corrigées ce soir. |
| Contenu | **Inégal** | Usure et TCA sont au format que les IA citent (une question, une réponse courte) ; les 26 autres pages ont des titres « de revue ». |
| Positions Google (ancien site) | 22 recherches en 1re page | Composite, blanchiment, esthétique du sourire, « spécialiste bruxisme Paris », le nom ; **32 recherches absentes** : TCA, érosion, usures, facettes (générique), éclaircissement Paris, taches blanches, MIH. |
| IA (ancien site) | Faible | Nommé dans 5 réponses sur 36 sur les TCA, 2 sur 18 sur les usures. |

## 2. Ce qui est bien en place

- Une page = une adresse de référence ; les 27 anciennes adresses servies ou redirigées ; aucune page en double.
- Aucun titre ni description en double ; un seul grand titre par page ; toutes les images ont un texte de
  remplacement (39 volontairement vides : décoratives).
- Données structurées sur chaque page : praticien, cabinet, fil d'Ariane, FAQ, pages médicales, vidéos.
- Robots des moteurs et des IA explicitement autorisés ; plan du site de 36 adresses, renvoyé à Google ;
  35 adresses signalées à Bing (IndexNow).
- Polices hébergées sur le site, aucune ressource extérieure chargée, pages revalidées à chaque visite.

## 3. Corrigé pendant l'audit

1. **Les 6 vidéos** : les données lues par Google citaient une couverture et un fichier vidéo à des adresses
   inexistantes (erreur 404) — ce qui empêchait l'affichage des vidéos dans les résultats. Adresses corrigées,
   publié, signalé à Bing.
2. **Contrôle permanent** : la publication s'arrête désormais si une adresse citée pour Google n'existe pas.
3. (Plus tôt dans la soirée : portrait des données structurées, cache des pages, ligne des mentions légales
   sur l'accueil, police du nom.)

## 4. À faire, par priorité

### Priorité 1 — technique, sans toucher aux textes (Claude, une soirée)

**Faite le 26/10/2026 (D99)** : points 1 à 6. Mesuré ensuite : accueil 99, Espace patients 99, Usure 100, TCA 99 ; référencement, accessibilité et bonnes pratiques à 100.

1. **Alléger les images** — le plus gros levier. Le portrait de la signature (811 Ko, affiché en vignette) est
   chargé sur 34 pages, et c'est lui qui retarde l'accueil ; les cartes de l'Espace patients chargent des
   photos de 2 000 px pour un affichage de 400. Versions WebP aux bonnes tailles : 60 à 90 % de poids en moins,
   Espace patients et accueil attendus au-dessus de 90/100.
2. **Aperçus de partage** sur toutes les pages (titre, description, image, adresse) : indispensable pour les
   posts LinkedIn qui renvoient au site (D90). Image = la photo de couverture de la page, ou le portrait.
3. **Compléter la fiche du cabinet** pour Google et les IA : coordonnées GPS, horaires (consultations mardi et
   vendredi 9 h – 19 h, standard du lundi au vendredi), lien vers la fiche Google, photo.
4. **Compléter la fiche du praticien** : domaines d'expertise (usure, érosion, TCA, facettes, composite,
   éclaircissement, taches blanches), affiliations (Pitié-Salpêtrière, CMME de Sainte-Anne), fondateur de DenTCA
   et de Smile Club Formations, profils Doctolib et Google ajoutés aux liens. C'est ce qui dit aux IA « qui est
   expert de quoi ».
5. **Accessibilité** (89/100 sur trois pages) : quelques contrastes trop faibles, ordre des niveaux de titres
   dans les encadrés, liens trop petits pour le doigt sur téléphone.
6. **Dates de révision** sur les 12 pages qui n'en ont pas.

### Priorité 2 — titres et contenus (avec Franck)

7. **16 titres trop longs** pour Google (coupés au-delà de 60 caractères : cas cliniques, article, Espace pro,
   accueil…) et **14 descriptions trop longues** (au-delà de 160 ; accueil : 244). Propositions à valider : ce
   sont les textes que les patients lisent dans Google.
8. **Passer au format questions / réponses** les pages des recherches absentes, une à la fois, comme Usure et
   TCA : Érosion dentaire (absente sur toutes ses recherches), Éclaircissement, Facettes, Bruxisme, Taches
   blanches et MIH (ICON), Dents courtes ; puis Composite et Bilan.
9. **Maillage** : relier davantage la rubrique Articles et l'article, Médias, et la vidéo Grossesse (en attente
   de sa section).
10. **La nouvelle section Grossesse**, où la vidéo trouvera sa place (« grossesse érosion dentaire », « enceinte
    dents », « hyperémèse gravidique dents »).

### Priorité 3 — hors du site, là où les IA vont chercher

11. **YouTube** : les vidéos y publiées (YouTube est la première source des IA sur ces sujets).
12. **Liens et mentions** (diagnostics Usure et TCA) : nom et lien sur dentca-asso.com ; mention de la
    consultation dentaire sur la page de la CMME ; thèses dans DUMAS ; FFAB ; presse santé ; liens depuis Blendi,
    Eugenol, AO News, ARTEMIS, Le Fil Dentaire ; site sur la fiche Doctolib.
13. **Mesurer** : le relevé quotidien des positions continue ; relevé IA allégé (questions TCA, usures,
    facettes, composite) dans trois à quatre semaines, une fois les nouvelles pages indexées.

## 5. Les pages une par une

En gras : titre de plus de 60 caractères, description hors de 70–160, plus de 1 Mo d'images, une seule page qui
les cite dans un texte (menus et pied de page non comptés).

| Page | Titre (car.) | Description (car.) | Mots | Images (Ko) | Liens reçus dans les textes |
|---|---|---|---|---|---|
| `/` | **63** | **244** | 148 | 792 | 36 |
| `/activite-hospitaliere/` | 39 | 140 | 450 | 792 | 4 |
| `/anorexie-erosion-dentaire-sans-vomissements/` | **64** | 158 | 1353 | 792 | 7 |
| `/articles/` | 26 | 106 | 148 | 0 | **1** |
| `/articles/jeunes-chirurgiens-dentistes-formes-en-europe/` | **110** | 100 | 1038 | 792 | **1** |
| `/bilan-esthetique-personnalise/` | 55 | 145 | 1353 | **1583** | 9 |
| `/bruxisme-usure-dentaire/` | 52 | 138 | 1135 | 792 | 4 |
| `/cas-cliniques/mih-eclaircissement-erosion-infiltration/` | **79** | 138 | 592 | **1479** | 3 |
| `/cas-cliniques/planification-facettes-ceramique/` | **73** | 139 | 609 | **1385** | 3 |
| `/cas-cliniques/planification-rehabilitation-facettes/` | **74** | 138 | 483 | **1549** | 3 |
| `/cas-cliniques/usures-dentaires-facettes-minimalement-invasives/` | **84** | **195** | 1616 | **2872** | 7 |
| `/chirurgien-dentiste-paris-9/` | 45 | 143 | 791 | 792 | 2 |
| `/composite-bonding-paris/` | **70** | 153 | 1668 | **2530** | 19 |
| `/conferences-formations/` | 43 | **170** | 477 | 792 | 5 |
| `/contact/` | 48 | **191** | 184 | 0 | 26 |
| `/dentisterie-esthetique-paris/` | **71** | 154 | 1806 | **1121** | 17 |
| `/dents-courtes-usees/` | 48 | 131 | 1101 | 792 | 4 |
| `/eclaircissement-dentaire-paris/` | **73** | 144 | 1185 | **1866** | 10 |
| `/erosion-dentaire/` | **69** | 134 | 1392 | **1382** | 16 |
| `/espace-patients/` | **66** | **165** | 246 | **4217** | **1** |
| `/espace-pro/` | **80** | **174** | 195 | **2659** | 2 |
| `/facettes-dentaires-paris/` | 59 | 150 | 1634 | **2810** | 15 |
| `/facettes-ou-composite/` | 59 | 149 | 1981 | 913 | 6 |
| `/franck-moyal/` | 45 | **189** | 502 | 792 | 19 |
| `/medias-interviews/` | 38 | 129 | 481 | 792 | **1** |
| `/mentions-legales/` | 34 | **58** | 350 | 792 | **1** |
| `/publications/` | 41 | 143 | 554 | 792 | 2 |
| `/taches-dentaires-dyschromies-icon/` | 54 | 144 | 1630 | **2115** | 6 |
| `/tca-dents/` | 58 | 147 | 3305 | **3047** | 12 |
| `/usures-dentaires/` | 57 | 148 | 2654 | **2045** | 18 |
| `/videos/` | 24 | 142 | 68 | 659 | 7 |
| `/videos/anorexie-dents/` | 54 | **182** | 199 | **1210** | 8 |
| `/videos/composite-bonding/` | **61** | **176** | 234 | **1189** | 8 |
| `/videos/erosion-dentaire/` | 52 | **185** | 204 | **1212** | 8 |
| `/videos/grossesse-erosion-dentaire/` | **68** | **179** | 235 | **1212** | **1** |
| `/videos/premiere-consultation-esthetique/` | **73** | **206** | 203 | **1208** | 8 |
| `/videos/sourire-gingival/` | 53 | **181** | 222 | **1183** | 6 |
