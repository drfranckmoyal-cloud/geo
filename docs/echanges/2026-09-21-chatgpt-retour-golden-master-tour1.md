# RETOUR CHATGPT — GOLDEN MASTER TOUR 1
## drfranckmoyal.fr — 21 septembre 2026

## Verdict général

Le Golden Master est **structurellement réussi**. Il respecte très bien la direction éditoriale et la majorité de la direction artistique. Il peut servir de base au site complet **après un tour 2 ciblé**, sans refonte.

Les principaux écarts à corriger ne concernent pas l’architecture générale mais :
1. la police de titres ;
2. le header mobile ;
3. la méthode en 7 étapes ;
4. la logique du menu pour les rubriques groupées ;
5. la présentation des sources / auteur sur la page Usures ;
6. le remplacement du portrait 480 px ;
7. quelques détails de densité mobile.

---

# 1. AUDIT 08 C — ACCUEIL

| Critère | Décision | Commentaire |
|---|---|---|
| H1 immédiatement visible | VALIDÉ | Très lisible, fort, suffisamment éditorial. |
| Hero aéré | VALIDÉ | Bonne respiration desktop. |
| Premier écran non surchargé | VALIDÉ | CTA bien hiérarchisés. |
| Deux piliers identifiables | VALIDÉ SOUS RÉSERVE PHOTOS | Structure bonne, les vrais visuels feront une grande partie du niveau de gamme. |
| Esthétique / Fonction / Préservation fort | VALIDÉ | Une des meilleures sections de la home. |
| Méthode non-SaaS | VALIDÉ AVEC CORRECTION | Présentation réussie, mais rétablir **Simuler** comme étape distincte : 7 étapes. |
| TCA secondaire | VALIDÉ | Bonne hiérarchie. |
| Autorité discrète | VALIDÉ | Ni CV, ni mur de logos. |
| CTA final net | VALIDÉ | Sobre et cohérent. |
| Pas de cartes répétitives | VALIDÉ | Bonne variété de composition. |

### Correction Accueil
La séquence doit redevenir :

**Écouter → Documenter → Analyser → Planifier → Simuler → Décider ensemble → Traiter**

`Simuler` est un élément différenciant de la méthode esthétique et ne doit pas disparaître dans `Planifier`.

---

# 2. AUDIT 08 D — PAGE FRANCK MOYAL

| Critère | Décision | Commentaire |
|---|---|---|
| Portrait dominant | VALIDÉ | La composition fonctionne. |
| Page incarnée | VALIDÉ | Bonne présence personnelle sans autopromotion lourde. |
| Pas de look CV | VALIDÉ | Très bon point. |
| Esthétique avant hospitalier | VALIDÉ | Hiérarchie correcte. |
| Usures clairement présentes | VALIDÉ | Axe majeur bien identifié. |
| TCA = expertise spécifique | VALIDÉ | Très bien positionné. |
| Enseignement valorisé | VALIDÉ | Bonne place. |
| Hospitalier plus bas | VALIDÉ | Conforme au positionnement voulu. |
| Phrases fortes mises en scène | VALIDÉ | « Traiter juste » fonctionne très bien. |
| Pas de grille de logos | VALIDÉ | À conserver. |

### Portrait
La **mise en page du portrait est validée**, mais le fichier 480 × 480 px ne peut pas devenir l’actif final.

Demande :
- original **≥ 2000 px** sur le grand côté ;
- idéalement 2500–3000 px ;
- ne pas faire d’upscale artificiel comme solution finale ;
- conserver le traitement noir doux / noir et blanc ;
- avec le fichier HD, augmenter légèrement le contraste local du visage : le rendu actuel est un peu trop doux / gris.

Le portrait actuel reste uniquement un **placeholder de validation de composition**.

---

# 3. AUDIT 08 E — PAGE USURES

| Critère | Décision | Commentaire |
|---|---|---|
| H1 lisible | VALIDÉ | Fort et parfaitement compréhensible. |
| Direct answer rapide | VALIDÉ | Très bon bloc GEO. |
| Causes / diagnostic avant traitement | VALIDÉ | Hiérarchie clinique excellente. |
| Prévention visible | VALIDÉ | Conforme au positionnement. |
| Réhabilitation esthétique + fonction | VALIDÉ | Bien équilibrée. |
| Liens érosion / TCA / réhabilitation | VALIDÉ | À maintenir. |
| Ambiance non sombre | VALIDÉ | Bonne sobriété clinique. |
| Pas d’image dentaire générique | VALIDÉ | Ne pas dégrader cela avec des stocks. |
| FAQ lisible | VALIDÉ | Garder ouverte pour l’instant. |
| Sources + auteur | VALIDÉ AVEC CORRECTIONS | Présents, mais leur présentation doit être raffinée. |

### Corrections page Usures

#### A. Sources
Les **7 références restent dans le HTML**, mais les mentions internes de type **« Soutient : » ne doivent pas être visibles au patient**.

L’`Evidence Map` est un outil de gouvernance éditoriale, pas un élément du design patient.

Sur le front :
- citation bibliographique propre ;
- DOI / PubMed discret ;
- aucune note « soutient ce claim » visible.

Sur mobile, la liste complète peut être placée dans un `<details>` accessible intitulé :
**« Voir les 7 sources scientifiques »**
à condition que toutes les références restent présentes dans le HTML.

#### B. Auteur / fraîcheur
Ajouter :
- `Mis à jour le 21 septembre 2026`
- lien vers `/franck-moyal/`

Le bloc auteur doit être court :
**Dr Franck Moyal — Chirurgien-dentiste à Paris**  
*Dentisterie esthétique et adhésive, usures dentaires et érosion.*

Ne pas recopier un long paragraphe de la page bio.

Ajouter également `dateModified` aux données structurées.

#### C. ClinicalPathway
Le sommaire clinique des 8 sections est validé **uniquement s’il est cliquable** et mène aux ancres correspondantes.

S’il n’est pas interactif, il devient redondant et doit être supprimé.

#### D. RelatedPages
Garder le bloc final, mais renommer le titre :

**Approfondir les usures dentaires**

plutôt que simplement « Usures dentaires ».

---

# 4. AUDIT DES 8 CRITÈRES 08 F

## 1. Singularité
**VALIDÉ.**
Le site ne ressemble pas à un cabinet dentaire générique.

## 2. Niveau de gamme
**VALIDATION CONDITIONNELLE.**
La structure est premium, mais le niveau définitif ne pourra être jugé qu’avec :
- portrait HD ;
- vraies photographies des 2 piliers ;
- photographie clinique ;
- schéma d’usures ;
- cas avant/après.

Les rectangles vides abaissent actuellement artificiellement la perception.

## 3. Calme
**VALIDÉ.**
Très bon contrôle des effets, couleurs et densité.

## 4. Lisibilité
**VALIDÉ avec un ajustement mobile.**
Le bloc `DirectAnswer` Usures est un peu trop massif sur 430 px.
Réduire légèrement :
- taille texte mobile vers **19–20 px** ;
- padding interne autour de **24–28 px** ;
sans diminuer son importance.

## 5. Cohérence
**VALIDÉ.**
Les trois pages appartiennent clairement au même système.

## 6. Personnalité
**VALIDATION CONDITIONNELLE.**
La typographie, le monogramme et le portrait donnent déjà une identité.
Les photographies propriétaires doivent maintenant empêcher le site de devenir un simple « beau template éditorial ».

## 7. Mobile
**VALIDÉ AVEC CORRECTION DU HEADER.**
Le contenu reste élégant. Le CTA du header prend cependant trop de place.

## 8. Extensibilité
**VALIDÉ.**
Le système de composants paraît suffisamment flexible pour industrialiser le site sans uniformiser toutes les pages.

---

# 5. QUESTION BLOQUANTE 1 — POLICE DES TITRES

## DÉCISION : NEWSREADER

Remplacer **Cormorant Garamond** par **Newsreader**.

### Pourquoi
Cormorant est élégant mais ses accents français très hauts et très fins deviennent un élément graphique trop présent sur :
- esthétique ;
- hôpital ;
- même ;
- etc.

EB Garamond paraît plus classique et plus « livre ».

Newsreader offre le meilleur équilibre :
- éditorial ;
- haut de gamme ;
- contemporain ;
- très lisible en français ;
- moins précieux / fragile que Cormorant ;
- moins académique qu’EB Garamond.

### Réglage conseillé
- H1 / H2 : Newsreader **400**
- H3 / titres plus petits : 400 ou 500 selon contraste
- `font-optical-sizing: auto`
- Inter inchangée pour le texte courant.

Ne pas changer les tailles avant d’avoir testé Newsreader avec les tailles actuelles.

---

# 6. QUESTION BLOQUANTE 2 — PORTRAIT HD

## DÉCISION
Oui : **un original HD est nécessaire**.

La composition actuelle est validée, donc Claude ne doit pas attendre pour le reste du tour 2.

Mais le portrait n’est **pas validé comme asset final** tant que le 480 px n’est pas remplacé.

Minimum recommandé : 2000 px.
Idéal : 2500–3000 px ou davantage.

---

# 7. POINTS D’INTERPRÉTATION — DÉCISIONS

## Répartition des couleurs
**VALIDÉE.**
Conserver la version issue de `07_ART_DIRECTION`.

## Méthode en 6 étapes
**À CORRIGER.**
Passer à **7 étapes** et remettre `Simuler` entre `Planifier` et `Décider ensemble`.

## « Découvrir ma démarche »
**VALIDÉ.**
Le lien vers la section Méthode de la homepage est logique.

## Menu — Érosion & TCA
**À CORRIGER.**
Ne pas faire pointer le libellé global uniquement vers `/tca-dents/`.

Desktop :
`Érosion & TCA` ouvre un sous-menu minimal :
- Érosion dentaire
- TCA et santé bucco-dentaire

Mobile :
même groupe dans le panneau Menu.

## Menu — Publications & enseignement
**À CORRIGER.**
Ne pas pointer uniquement vers `/publications/`.

Sous-menu :
- Publications
- Conférences & formations
- Activité hospitalière
- Médias & interviews

## Étiquettes de sections Usures
**VALIDÉ.**
Petite question / intention au-dessus + grand titre éditorial dessous : très bon compromis GEO / design.

## ClinicalPathway
**VALIDÉ SOUS CONDITION : ancres cliquables.**

## RelatedPages
**VALIDÉ avec changement du titre** en :
`Approfondir les usures dentaires`.

## Notes « Soutient : »
**À RETIRER DU FRONT.**
Les conserver uniquement dans l’Evidence Map interne.

## Auteur
**À CORRIGER.**
Bloc plus court + date de mise à jour.

## FAQ ouverte
**VALIDÉE.**
Pas besoin d’accordéon pour l’instant.

## Header desktop — monogramme seul
**VALIDÉ.**
Élégant et suffisamment identifiable.

## Bloc TCA — réutilisation TextImageSection
**VALIDÉE.**
Pas besoin d’un nouveau composant uniquement pour cette section.

---

# 8. HEADER MOBILE — CORRECTION IMPORTANTE

Le header mobile est la principale faiblesse visuelle actuelle.

Le bouton `Prendre rendez-vous` est trop dominant par rapport au monogramme et au bouton Menu.

### Correction
Sur 390–430 px :
- hauteur CTA header : **40–42 px**
- font-size : **14–15 px**
- padding horizontal : **16–18 px**
- largeur automatique, ne pas étirer
- `Menu` : 14–15 px
- conserver une hauteur totale de header compacte.

Les boutons CTA dans le contenu peuvent rester à 50–52 px.

Le header doit ressembler à une barre de navigation premium, pas à un bandeau de conversion.

---

# 9. FOOTER ET DONNÉES EN ATTENTE

## Adresse
Le placeholder peut maintenant être remplacé par l’adresse canonique validée :

**2 rue Hippolyte Lebas, 75009 Paris**

## Téléphone
Reste à fournir.

## Rendez-vous
Conserver le lien provisoire jusqu’à fourniture de l’URL réelle de réservation.

## SameAs — candidats
À intégrer après contrôle final des URLs :
- LinkedIn
- AP-HP
- Le Fil Dentaire — page auteur
- Blendi — page formateur

Ne pas utiliser `sameAs` pour chaque article ou événement.

---

# 10. ROBOTS / IA

Le rapport indique actuellement un `robots.txt` ouvert à tous les moteurs et IA.

Ce n’est pas bloquant pour le Golden Master, mais avant lancement :
- **OAI-SearchBot : autorisé**
- Googlebot / Bingbot : autorisés
- décision GPTBot à traiter séparément, car indexation ChatGPT Search et entraînement ne sont pas le même usage.

Ne pas présenter « tous les bots IA » comme un seul réglage conceptuel.

---

# 11. TOUR 2 — ORDRE EXACT DES MODIFICATIONS

## P0 — avant nouvelle validation visuelle
1. Passer les titres à **Newsreader**.
2. Corriger le **header mobile**.
3. Restaurer les **7 étapes** de la méthode avec `Simuler`.
4. Transformer les deux rubriques groupées du menu en sous-menus.
5. Nettoyer la présentation des sources Usures.
6. Ajouter `Mis à jour le 21 septembre 2026` + bloc auteur court.
7. Rendre `ClinicalPathway` cliquable ou le supprimer.
8. Renommer RelatedPages → `Approfondir les usures dentaires`.
9. Remplacer l’adresse footer par `2 rue Hippolyte Lebas, 75009 Paris`.
10. Réduire légèrement la densité du DirectAnswer Usures sur mobile.

## P1 — assets
11. Remplacer le portrait 480 px dès réception du HD.
12. Ajouter les vrais visuels piliers.
13. Ajouter photo clinique Usures.
14. Créer / intégrer le schéma des mécanismes.
15. Ajouter cas clinique avant/après avec consentement.

---

# 12. VERDICT POUR INDUSTRIALISATION

**NE PAS encore geler définitivement le design system.**

Mais nous sommes proches.

Après les corrections P0 et une nouvelle série courte de captures :
- Home hero desktop/mobile
- Franck hero desktop/mobile
- Usures hero desktop/mobile
- section Méthode
- section Sources/Auteur
- header mobile
- menu desktop + mobile

si ces éléments sont conformes, le Golden Master pourra être **gelé et utilisé pour industrialiser toutes les autres pages**.

Il n’est pas nécessaire de refaire un « Tour 1 bis » de 26 captures.
Un **Tour 2 ciblé** suffit.
