# POINT 1 — page pilier « Dentisterie esthétique à Paris » : intégrée et en ligne

*Claude Code, 24 septembre 2026. Spécification archivée dans
`docs/echanges/2026-09-24-chatgpt-point-1-page-pilier-esthetique.md` ; texte de la page dans
`docs/pages-suivantes/v1.4/01_dentisterie-esthetique-paris_V1_4.md`.*

## Contrôle après déploiement

| | |
|---|---|
| URL | https://drfranckmoyal.fr/dentisterie-esthetique-paris/ — inchangée, aucune nouvelle page créée |
| Statut HTTP | `200` |
| Title | Dentiste esthétique à Paris : approche et traitements \| Dr Franck Moyal (71 caractères) |
| Meta description | Dentisterie esthétique à Paris : découvrez l’approche du Dr Franck Moyal, les critères de choix et les solutions conservatrices pour améliorer le sourire. (154 caractères) |
| H1 | Dentisterie esthétique à Paris : concevoir un sourire — un seul H1 |
| Hiérarchie | H1 → 17 H2 → 22 H3, aucun saut de niveau |
| Canonical | `https://drfranckmoyal.fr/dentisterie-esthetique-paris/`, auto-référente |
| Index | indexable, follow (aucune balise `robots`) |
| Sitemap | présente dans `/sitemap.xml` et `/sitemap-0.xml` |
| Liens ajoutés | `/eclaircissement-dentaire-paris/`, `/composite-bonding-paris/`, `/facettes-dentaires-paris/`, `/taches-dentaires-dyschromies-icon/`, `/usures-dentaires/` (deux fois : bloc usures et FAQ), `/franck-moyal/`, `/bilan-esthetique-personnalise/`, `/contact/#prendre-rendez-vous` |
| Données structurées | inchangées dans leur structure : `WebSite`, `WebPage`, `BreadcrumbList`, `Person#franck-moyal`, `Dentist#practice`. Aucun nouvel identifiant. Seul ajout : les six sujets de la page (`about`), tels que les nomme le §21. Pas de `FAQPage` : le site n’en utilise pas (§22) |
| Mobile | 390 px : aucun débordement, H1 en 4 lignes, matrice en cartes verticales, cartes de traitements et FAQ lisibles. 375 px : un débordement de 5 px, **antérieur à ce travail** (voir plus bas) |
| Rapidité | contrôles automatiques du site : textes, HTML, données structurées et contrôle avant mise en ligne, tous au vert |

## Ce que contient la page, dans l’ordre

1. Ouverture et réponse directe (inchangées)
2. Une pratique esthétique ne commence pas par des facettes *(V1.2, conservée)*
3. **Comment choisir son dentiste esthétique à Paris ?** *(nouveau, §6)*
4. **Comment évaluer une prise en charge esthétique ?** — les six critères, en grille à deux colonnes avec filets vert sauge *(nouveau, §7)*
5. **La bonne question n’est pas toujours « quel traitement choisir ? »** sur fond ivoire, suivie immédiatement de la **matrice demande → solutions** *(nouveau, §8 et §9)*
6. **Quelles solutions en dentisterie esthétique ?** — éclaircissement, composite bonding, facettes en céramique *(nouveau, §10)* et **taches blanches et dyschromies** *(V1.2, conservée)*, chacune avec son lien
7. **Et si les dents sont usées ?** — panneau vert sauge, composition « domaine spécifique » des composants gelés, avec le lien vers la page Usures *(nouveau, §11)*
8. Sections cliniques de la V1.2, conservées dans leur ordre : qu’est-ce qu’un beau sourire ; comment débute un projet esthétique ; pourquoi documenter le sourire ; quelle place pour le smile design (avec ses références [1] et [2]) ; le gradient thérapeutique ; esthétique, fonction, préservation ; le nombre de dents
9. **L’approche du Dr Franck Moyal** *(nouveau, §12)*, avec le lien vers la page Parcours
10. FAQ : les cinq questions nouvelles *(§13)* puis les cinq questions de la V1.2
11. Appel final « Commencer par définir le sourire » *(V1.2)*, bouton vers `/contact/#prendre-rendez-vous`

Aucun superlatif, aucun avis, aucune note, aucun badge. L’expression « meilleur dentiste
esthétique à Paris » n’apparaît qu’une fois, dans le texte du §6.

## Différences entre la spécification et l’implémentation

1. **H1.** La spécification écrit « Conserver : Dentisterie esthétique à Paris » alors que le H1
   existant est « Dentisterie esthétique à Paris : concevoir un sourire ». J’ai **conservé le H1
   existant**, littéralement. Dis-le si tu veux le raccourcir : c’est une ligne à changer.
2. **Section des traitements.** Arbitrage de Franck : la nouvelle section remplace l’ancienne, en
   gardant l’entrée « Taches blanches et dyschromies ». Trois paragraphes de la V1.2 ne sont donc
   plus affichés ; les voici, si tu veux les réintégrer :
   - *Éclaircissement dentaire* : « L’éclaircissement, souvent appelé blanchiment, permet de gagner
     en luminosité sans retirer de tissu dentaire. Il peut constituer à lui seul l’ensemble du
     traitement esthétique. »
   - *Composite bonding* : « Le composite permet de modifier directement les formes, les
     proportions ou certains espaces, souvent de manière très additive. En esthétique antérieure,
     la stratification et la finition jouent un rôle majeur dans la qualité du résultat. »
   - *Facettes* : « Les facettes permettent de redessiner avec une grande précision l’architecture
     d’un sourire, notamment lorsqu’une transformation plus importante des formes, proportions ou
     teintes est recherchée. »
3. **FAQ.** Elle compte dix questions : les cinq nouvelles, puis les cinq de la V1.2, qu’aucune
   consigne ne demandait de supprimer. Dis-moi si tu préfères n’en garder que cinq.
4. **Matrice demande → solutions.** Rendue comme une liste de lignes — demande en gras, flèche,
   solutions — séparées par des filets, et non comme un tableau HTML : le site n’a pas de style de
   tableau dans son système gelé, et cette forme est celle que tu autorises pour le mobile. Le
   contenu et l’ordre sont identiques ; l’en-tête « Votre demande / Solutions pouvant être
   discutées » n’est pas affiché.
5. **Lien « Facettes ou composite : comment choisir ? »** : **non posé**, la page n’existe pas
   encore (POINT 2). Le composant est prêt : un lien contextuel peut désormais suivre une réponse
   de FAQ, et il sert déjà pour « Comprendre les usures dentaires ». Il suffira d’ajouter la ligne
   quand la page existera.
6. **Title de 71 caractères** : au-delà des 60 caractères affichés par Google, le titre sera coupé.
   C’est ton choix, je le signale seulement.
7. **Maillage entrant** (§15) : les pages Composite bonding, Facettes et Éclaircissement mènent
   chacune à la page pilier par trois liens (fil d’Ariane, « À lire aussi », pied de page). La page
   **Usures** n’y mène que par le pied de page : y ajouter un lien contextuel supposerait de
   modifier une page du golden master gelé. À décider.
8. **Liens Érosion et Bruxisme** (§14, « lorsque contextuellement pertinent ») : non posés, aucun
   passage de la page ne les mentionne. Les ajouter demanderait un texte de ta part.
9. **Verrou V21.** Franck a levé, pour cette seule page, l’interdiction d’écrire « dentiste
   esthétique » (six occurrences : title, section §6, question de FAQ). Le reste du site continue
   d’écrire « dentisterie esthétique », et le contrôle automatique le vérifie.
10. **`dateModified`** passe au 24/09/2026.

## Anomalie détectée, non corrigée

À **375 px** de large (iPhone SE, iPhone 13 mini), le bouton de l’appel final « Réaliser un bilan
esthétique personnalisé » mesure 360 px dans une colonne de 343 px : la page déborde de 5 px
horizontalement. **Ce comportement existait déjà avant ce travail** — je l’ai vérifié sur la
version en ligne précédente — et vient du bouton gelé, qui ne coupe jamais son libellé. Aucune
autre page du site n’est concernée. Conformément à ta consigne, je n’ai rien modifié : la
correction touche soit le libellé du bouton, soit le composant gelé. À toi de trancher.
