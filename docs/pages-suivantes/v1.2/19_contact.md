# SPEC PAGE — Contact et rendez-vous
## Version V1.2 finale — prête pour industrialisation Claude Code — 22 septembre 2026

## 1. ROUTING ET FIL D’ARIANE
- **URL définitive** : `/contact/`
- **Page parente** : `/`
- **Fil d’Ariane** : Accueil > Contact
- **Composant d’ouverture** : `ClinicalHero`

## 2. HERO
- **H1** : Contact et rendez-vous — Dr Franck Moyal, Paris 9e
- **Chapeau** : Informations pratiques pour contacter le cabinet du Dr Franck Moyal au 2 rue Hippolyte Lebas, 75009 Paris.

## 3. RÉPONSE DIRECTE
- **Pas de DirectAnswer spécifique sur cette page.**

## 4. CONTRAT DE COMPOSANTS
- `ClinicalHero` compact **sans ligne auteur visible** (`showAuthor=false` ou variante équivalente du composant existant).
- `TextImageSection` pour informations pratiques.
- Les 7 « Motifs de consultation » sont des liens internes sobres à flèche.
- `RelatedPages` avec : Dr Franck Moyal, Chirurgien-dentiste Paris 9, Activité hospitalière.
- Pas d’`AuthorBlock` final.
- `FinalCTA` remplacé par les moyens de contact dès qu’ils sont fournis.

## 5. CONTENU ÉDITORIAL À RENDRE — MOT POUR MOT

# Contact et rendez-vous — Dr Franck Moyal, Paris 9e

## Cabinet

**Dr Franck Moyal**  
Chirurgien-dentiste à Paris

**2 rue Hippolyte Lebas  
75009 Paris**

La pratique privée présentée sur ce site est orientée vers la dentisterie esthétique et adhésive, les usures dentaires, l’érosion et leur réhabilitation.

## Prendre rendez-vous

**Téléphone**  
[À FOURNIR]

**Prise de rendez-vous en ligne**  
[URL À FOURNIR]

## Avant votre consultation

Selon le motif de consultation, il peut être utile d’apporter :
- les radiographies ou examens récents dont vous disposez ;
- d’anciennes photographies du sourire lorsqu’une évolution des usures est recherchée ;
- la liste de vos traitements médicaux lorsque cela peut influencer la prise en charge.

Aucun document n’est obligatoire pour demander un premier rendez-vous.

## Activité hospitalière

L’activité privée du 2 rue Hippolyte Lebas est distincte de l’activité hospitalière du Dr Franck Moyal à la Pitié-Salpêtrière et à la CMME de l’Hôpital Sainte-Anne.

→ **Découvrir l’activité hospitalière**

## Motifs de consultation

- **Bilan esthétique personnalisé**
- **Composite bonding**
- **Facettes dentaires**
- **Éclaircissement dentaire**
- **Usures dentaires**
- **Érosion dentaire**
- **TCA et santé bucco-dentaire**

## 6. LIENS INTERNES À CÂBLER
- **Dr Franck Moyal** → `/franck-moyal/`
- **Chirurgien-dentiste Paris 9** → `/chirurgien-dentiste-paris-9/`
- **Activité hospitalière** → `/activite-hospitaliere/`
- **Découvrir l’activité hospitalière** → `/activite-hospitaliere/`
- **Bilan esthétique personnalisé** → `/bilan-esthetique-personnalise/`
- **Composite bonding** → `/composite-bonding-paris/`
- **Facettes dentaires** → `/facettes-dentaires-paris/`
- **Éclaircissement dentaire** → `/eclaircissement-dentaire-paris/`
- **Usures dentaires** → `/usures-dentaires/`
- **Érosion dentaire** → `/erosion-dentaire/`
- **TCA et santé bucco-dentaire** → `/tca-dents/`

## 7. FRAÎCHEUR
- **Aucune ligne auteur visible dans le hero et aucun AuthorBlock final.**
- **Date de mise à jour** : 22 septembre 2026
- **`dateModified`** : `2026-09-22`

## 8. RÉFÉRENCEMENT
- **Title** : Contact et rendez-vous | Dr Franck Moyal Paris 9
- **Meta description** : Adresse et prise de rendez-vous avec le Dr Franck Moyal : 2 rue Hippolyte Lebas, 75009 Paris.
- **Données structurées** : `ContactPage` + `BreadcrumbList` + référence à `Person#franck-moyal` et `PostalAddress`

## 9. IMAGES / MÉDIAS ATTENDUS
- Aucun visuel obligatoire. Une photo réelle du cabinet peut être ajoutée ultérieurement sans changer le layout.

## 11. NOTES D’IMPLÉMENTATION — NON AFFICHÉES

Donner à la section **« Prendre rendez-vous »** l’ancre unique `id="prendre-rendez-vous"`.
Cette décision **supersède** toute mention antérieure de `#rendez-vous`.
Tant que l’URL de réservation définitive n’est pas fournie, tous les boutons de rendez-vous du site pointent vers `/contact/#prendre-rendez-vous`.
