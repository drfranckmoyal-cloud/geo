# RETOUR CHATGPT — GOLDEN MASTER TOUR 2
## drfranckmoyal.fr — décision de gel
## 21 septembre 2026

# VERDICT

Le Golden Master est **visuellement validé à 95 %** et peut être considéré comme la base définitive du site.

Je recommande toutefois **un dernier micro-tour P0.5 avant gel technique complet**, limité à 4 ajustements :

1. corriger les textes `Planifier` / `Simuler` ;
2. passer la phrase clé et la ligne auteur de la page Usures en **romain** ;
3. alléger encore légèrement le CTA du header mobile ;
4. refaire un Lighthouse mobile Usures après suppression de l’italique Newsreader et ne geler que si le LCP revient idéalement sous 2,5 s.

Aucune refonte visuelle n’est demandée.

---

# 1. DIRECTION VISUELLE — VALIDÉE

## Newsreader
**VALIDÉE DÉFINITIVEMENT.**

Le changement depuis Cormorant Garamond est très positif :
- meilleur dessin des accents français ;
- aspect éditorial haut de gamme ;
- plus contemporain ;
- moins fragile visuellement ;
- bonne cohérence avec Inter.

Conserver :
- H1/H2 : Newsreader 400 ;
- H3 / noms d’étapes : 500 si nécessaire ;
- `font-optical-sizing: auto`.

Ne plus rouvrir ce choix typographique.

---

# 2. PORTRAIT HD — VALIDÉ

Le nouveau portrait haute définition fonctionne nettement mieux.

La composition est validée sur :
- homepage desktop ;
- homepage mobile ;
- page Franck desktop ;
- page Franck mobile.

Le traitement noir et blanc + noir doux reste cohérent avec l’identité générale.

Ne pas modifier davantage le contraste pour le moment.

---

# 3. HOMEPAGE — VALIDÉE

## Hero
**VALIDÉ.**

Le couple :
- grand titre éditorial ;
- texte clinique sobre ;
- portrait en aplat noir ;

fonctionne très bien.

Le site paraît désormais réellement personnel et non générique.

## Navigation desktop
**VALIDÉE.**

Les deux rubriques avec sous-menu sont lisibles et sobres.

## Navigation mobile
**VALIDÉE SOUS RÉSERVE D’UN MICRO-AJUSTEMENT.**

Le header est beaucoup meilleur qu’au tour 1, mais le CTA `Prendre rendez-vous` reste encore légèrement dominant sur 390–430 px.

Dernier ajustement conseillé :
- garder hauteur 40 px ;
- réduire légèrement le padding horizontal si nécessaire ;
- ne pas élargir davantage ;
- si cela reste trop dominant à 390 px, afficher visuellement `Rendez-vous` sur mobile uniquement, avec `aria-label="Prendre rendez-vous"`.

Ce point ne remet pas en cause le système.

---

# 4. MÉTHODE — TEXTES DÉFINITIFS

La séquence à figer est :

**Écouter → Documenter → Analyser → Planifier → Simuler → Décider ensemble → Traiter**

## Textes définitifs

### Écouter
**attentes, gêne, objectifs.**

### Documenter
**photographies, scans 3D, examens nécessaires.**

### Analyser
**esthétique, fonction, tissus, causes.**

### Planifier
**construire les formes, les proportions et les options thérapeutiques.**

### Simuler
**visualiser le projet en 2D, 3D ou en dynamique selon les cas.**

### Décider ensemble
**comparer les options, leurs avantages, leurs limites et le niveau d’intervention.**

### Traiter
**uniquement lorsque le bénéfice est réel.**

## Titre de section
Le titre actuel peut être légèrement complété pour refléter la signature complète :

**Écouter, analyser, planifier, simuler, décider ensemble**

Il n’est pas nécessaire d’énumérer les 7 verbes dans le titre ; la liste à droite porte le détail complet.

---

# 5. PAGE FRANCK MOYAL — VALIDÉE

La composition est maintenant suffisamment forte pour être gelée.

Points particulièrement réussis :
- portrait très présent sans devenir une page personnelle narcissique ;
- titre ample et très lisible ;
- esthétique / adhésif immédiatement identifiés ;
- usures visibles dans le lead ;
- architecture très éditoriale.

Aucune modification structurelle.

---

# 6. PAGE USURES — VALIDÉE AVEC 2 MICRO-CORRECTIONS

## Hero
**VALIDÉ.**

Très bon équilibre entre :
- H1 ;
- lead ;
- signature auteur ;
- réponse directe.

Le DirectAnswer mobile est maintenant beaucoup mieux proportionné.

## Sources
**VALIDÉES.**

La logique :
- sources visibles sur desktop ;
- liste repliable sur mobile ;
- références toujours présentes dans le HTML ;

est la bonne.

Conserver.

## Bloc auteur
**VALIDÉ dans son contenu.**

Conserver :
- Dr Franck Moyal — Chirurgien-dentiste à Paris ;
- activité clinique courte ;
- `Mis à jour le 21 septembre 2026` ;
- lien `/franck-moyal/`.

---

# 7. ITALIQUE — DÉCISION

## PASSER EN ROMAIN

Je recommande de supprimer l’italique Newsreader pour :
1. la phrase clé de la page Usures ;
2. la ligne de spécialité du bloc auteur.

### Pourquoi
Visuellement, l’italique est élégant mais non indispensable.
La phrase clé possède déjà :
- sa taille ;
- son espace ;
- son filet ;
- sa position ;

pour être suffisamment mise en valeur.

L’italique ajoute une tonalité légèrement plus « magazine » alors que le site doit rester calme et clinique.

Surtout, le fichier italique ajoute environ **147 Ko** à la page Usures.

### Nouveau traitement
Phrase clé :
- Newsreader Roman 400 ;
- même taille ;
- même composition ;
- même filet vertical.

Ligne auteur :
- Inter Roman ou Medium ;
- petit corps ;
- couleur secondaire.

Ne charger **aucun fichier italique Newsreader** si aucune autre utilisation réelle ne le nécessite.

---

# 8. PERFORMANCE — CONDITION DE GEL TECHNIQUE

Le rapport Tour 2 donne :
- Home mobile : LCP 2,1 s ;
- Franck mobile : LCP 2,1 s ;
- Usures mobile : LCP 2,9 s.

La cible du projet est **LCP < 2,5 s**.

Après suppression de l’italique Newsreader :
1. rebuild ;
2. Lighthouse mobile Usures à nouveau ;
3. idéalement trois passages et retenir la médiane.

## Critère de gel
Si médiane LCP ≤ 2,5 s :
**Golden Master gelé.**

Si elle reste > 2,5 s :
faire une optimisation technique ciblée, sans toucher au design :
- preload uniquement des fontes réellement critiques ;
- sous-ensemble latin / latin-ext si possible ;
- vérifier `font-display`;
- inspecter l’élément LCP ;
- éviter tout preload d’asset non visible au-dessus de la ligne de flottaison.

---

# 9. MENUS — VALIDÉS

## Desktop

### Érosion & TCA
- Érosion dentaire
- TCA et santé bucco-dentaire

### Publications & enseignement
- Publications
- Conférences & formations
- Activité hospitalière
- Médias & interviews

**VALIDÉ.**

## Mobile
Même structure dans le panneau Menu.

**VALIDÉ.**

---

# 10. CLINICAL PATHWAY / RELATED PAGES

## ClinicalPathway
Conserver s’il reste cliquable vers les ancres.

**VALIDÉ.**

## Bloc pages liées
Titre :
**Approfondir les usures dentaires**

**VALIDÉ.**

---

# 11. DESIGN SYSTEM À GELER APRÈS P0.5

Après les quatre micro-corrections, geler :

- palette ;
- Newsreader + Inter ;
- grille ;
- espacements ;
- header desktop ;
- header mobile ;
- boutons ;
- hero Home ;
- hero Profile ;
- hero Clinical ;
- TextImageSection ;
- PullStatement ;
- DirectAnswer ;
- FAQ ;
- SourceList ;
- AuthorBlock ;
- RelatedPages ;
- footer ;
- sous-menus ;
- animations.

Une fois gelés :
**ne plus modifier ces composants au fur et à mesure de la création des pages**, sauf problème réel découvert à l’usage.

---

# 12. ASSETS ENCORE À FOURNIR — NON BLOQUANTS POUR LE GEL

Ils ne doivent pas empêcher le gel du système :

- visuel pilier Dentisterie esthétique ;
- visuel pilier Usures ;
- photo clinique Usures ;
- schéma mécanismes d’usure ;
- cas avant / après ;
- téléphone ;
- URL définitive de prise de rendez-vous ;
- URLs exactes `sameAs`.

Ces éléments seront intégrés dans les emplacements déjà prévus.

---

# 13. INSTRUCTION À CLAUDE CODE — TOUR P0.5

Faire uniquement :

1. remplacer les textes `Planifier` et `Simuler` par les textes définitifs ci-dessus ;
2. passer en romain la phrase clé Usures et la ligne auteur ;
3. supprimer le chargement de la fonte Newsreader Italic si elle n’est plus utilisée ;
4. vérifier une dernière fois le CTA header à 390 et 430 px ; si le rendu reste dominant à 390 px, utiliser `Rendez-vous` visuellement sur mobile avec aria-label complet ;
5. rebuild ;
6. Lighthouse mobile Usures x3 ;
7. fournir :
   - capture Méthode desktop/mobile ;
   - capture phrase clé/auteur Usures ;
   - capture header 390/430 ;
   - résultats Lighthouse Usures mobile.

**Ne modifier aucun autre composant ni aucune autre composition.**

---

# 14. DÉCISION

Le système graphique est **validé**.

Le P0.5 est un contrôle de finition et de performance.

Si les quatre points passent :

# GOLDEN MASTER = GELÉ

Claude Code pourra ensuite industrialiser les autres pages à partir de ce système sans nouvelle phase de direction artistique.
