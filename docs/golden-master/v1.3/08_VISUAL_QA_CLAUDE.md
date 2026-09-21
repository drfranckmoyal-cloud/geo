# 08 — VISUAL QA / DO & DON'T
## Instructions strictes pour Claude Code

Ce document sert à contrôler le rendu du Golden Master.

Le but n’est pas d’évaluer si “ça marche”.
Le but est de vérifier si le rendu respecte **exactement l’intention esthétique**.

---

# A. DO — OBLIGATOIRE

## Composition
- grands espaces blancs ;
- hiérarchie très nette ;
- sections peu nombreuses mais fortes ;
- équilibre texte / image ;
- largeurs de lecture contrôlées ;
- rythme éditorial.

## Typographie
- serif premium pour titres ;
- sans-serif très lisible pour texte ;
- contraste fort entre niveaux ;
- line-height confortable.

## Couleurs
- blanc cassé / ivoire dominants ;
- noir doux ;
- vert sauge comme accent rare.

## Images
- placeholders neutres si visuels manquants ;
- ratio cohérent ;
- pas de contenu stock inventé.

## CTA
- peu nombreux ;
- clairement hiérarchisés ;
- sobres.

## Responsive
- tester à minima :
  - 1440 px
  - 1280 px
  - 1024 px
  - 768 px
  - 430 px
  - 390 px

## Performance
- pas de librairie lourde pour de simples animations ;
- images optimisées ;
- fonts chargées correctement ;
- aucune ressource externe inutile.

---

# B. DON'T — INTERDIT

## Interdit visuellement
- bleu médical ;
- bleu nuit corporate ;
- gradients ;
- or ;
- cartes avec grosses ombres ;
- coins exagérément arrondis ;
- glassmorphism ;
- 3D de dents ;
- sourire stock ;
- fond vidéo automatique ;
- carrousel ;
- testimonial slider ;
- chiffres animés ;
- micro-interactions gadget ;
- effets de glow ;
- navbar flottante façon SaaS ;
- boutons pill géants.

## Interdit éditorialement
- inventer du texte ;
- raccourcir les textes sans validation ;
- ajouter des slogans ;
- ajouter des chiffres marketing ;
- créer des badges « expert », « premium », « leader ».

---

# C. CHECKLIST HOMEPAGE

Valider :
- [ ] H1 immédiatement visible
- [ ] hero très aéré
- [ ] pas de surcharge dans le premier écran
- [ ] deux piliers clairement identifiables
- [ ] bloc Esthétique / Fonction / Préservation visuellement fort
- [ ] méthode lisible sans ressembler à un onboarding SaaS
- [ ] bloc TCA présent mais secondaire
- [ ] bloc autorité discret
- [ ] CTA final net
- [ ] aucune répétition de carte inutile

---

# D. CHECKLIST PAGE FRANCK

- [ ] portrait dominant
- [ ] page incarnée
- [ ] pas de look CV
- [ ] activité esthétique visible avant hospitalier
- [ ] usures clairement présentes
- [ ] TCA en expertise spécifique
- [ ] enseignement bien valorisé
- [ ] hospitalier plus bas
- [ ] phrases fortes mises en scène
- [ ] aucune grille de logos agressive

---

# E. CHECKLIST PAGE USURES

- [ ] H1 très lisible
- [ ] direct answer visible rapidement
- [ ] cause / diagnostic avant traitement
- [ ] prévention clairement visible
- [ ] réhabilitation esthétique ET fonctionnelle
- [ ] liens vers érosion / TCA / réhabilitation
- [ ] pas d’ambiance trop sombre
- [ ] aucun visuel de dent générique
- [ ] FAQ lisible
- [ ] sources et auteur présents

---

# F. CRITÈRES DE VALIDATION VISUELLE

Le golden master est validé uniquement si les 8 critères suivants sont tous satisfaits.

## 1. Singularité
Le site ne ressemble pas à un template de cabinet dentaire.

## 2. Niveau de gamme
Il paraît immédiatement soigné et coûteux à produire.

## 3. Calme
Aucun élément ne cherche excessivement l’attention.

## 4. Lisibilité
Le contenu clinique reste très facile à lire.

## 5. Cohérence
Les trois pages donnent l’impression de faire partie du même système.

## 6. Personnalité
Le site a une identité propre, pas seulement une esthétique minimaliste générique.

## 7. Mobile
La version mobile conserve le niveau de gamme.

## 8. Extensibilité
Les composants peuvent être réutilisés sans rendre toutes les pages identiques.

---

# G. CAPTURES À FOURNIR À LA FIN

Pour chaque page :
- 1440 × page complète
- 430 × page complète

Et en plus :
- hero desktop
- hero mobile
- une section de contenu
- footer

Total minimal :
**10 à 12 captures**

---

# H. RAPPORT DE FIN DE PHASE

Claude Code doit remettre un court rapport :

## Design
- composants créés ;
- tokens ;
- choix typographiques ;
- variantes responsive.

## Technique
- build ;
- routes ;
- metadata ;
- structured data ;
- performance.

## Placeholders
- photos manquantes ;
- vidéos manquantes ;
- liens externes non finalisés.

## Questions
Uniquement les décisions réellement bloquantes.

---

# I. SEUIL DE QUALITÉ

Ne pas considérer le Golden Master comme terminé parce que :
- les routes existent ;
- le build passe ;
- le responsive est fonctionnel.

Le niveau attendu est :

> **“Ce rendu peut devenir la référence définitive de toutes les pages futures sans devoir repenser le système visuel.”**

Si cette phrase n’est pas vraie, le Golden Master n’est pas validé.
