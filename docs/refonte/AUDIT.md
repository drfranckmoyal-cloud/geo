# Audit de drfranckmoyal.fr avant refonte

*12 octobre 2026. Toutes les mesures sont prises sur le site en ligne, ce jour, sur un
écran d'ordinateur portable (1440 × 900) et sur un téléphone (375 × 812).*

> **La version en ligne n'est pas touchée.** Ce document ne fait que constater.

---

## Le verdict, en une phrase

**Le site n'a pas trop de texte : il a trop peu de texte par écran.**
Il affiche **104 mots par écran** là où une page lisible en affiche 250 à 400, et il
découpe chaque page en **douze chapitres de même rang** au lieu de quatre ou cinq.
Le lecteur fait défiler sans jamais voir de structure. C'est ça, « anarchique ».

---

## Ce qui n'est PAS en cause

À écarter tout de suite, pour ne pas y perdre du temps dans la refonte.

| | Constat |
|---|---|
| **La quantité de texte** | 1 373 mots en moyenne sur une page de soins. Le site de référence du Dr Cohen Samama en fait **1 347** sur sa page facettes. Identique. |
| **La lisibilité des caractères** | Contraste minimum mesuré : **9,7**. Le seuil d'accessibilité est à 4,5. Aucun texte en dessous. |
| **Le ciblage** | Titres, descriptions et H1 vérifiés page par page le 8 octobre : tous justes. |
| **La technique** | 28 pages en ligne, aucune erreur, certificat valide, plan du site lu par Google. |
| **Le fond** | Les textes sont bons. Ce sont ceux du pack, validés. Le problème est leur mise en page. |

**Ce n'est donc pas un problème de contenu. C'est un problème de forme.**

---

## Ce qui est en cause : trois mécanismes, mesurés

### 1. Douze chapitres au lieu de quatre

Une page de soins du site porte en moyenne **12,8 titres de niveau 2**. Chacun annonce
un nouveau chapitre, au même rang que les autres.

| | drfranckmoyal.fr | Dr Cohen Samama |
|---|---|---|
| Titres de niveau 2 | **11 à 19** | **4 à 5** |
| Titres de niveau 3 | 6 à 10 | 8 |

Chez eux : quatre ou cinq grands chapitres, chacun avec ses sous-points. Le lecteur
voit la structure d'un coup d'œil et peut sauter directement à ce qui le concerne.

Chez nous : douze blocs côte à côte, tous de même importance apparente. **Rien ne
ressort, donc rien ne guide.** Le lecteur ne peut pas survoler : il doit tout lire, ou
abandonner. Il abandonne.

### 2. Un écran pour trente mots

Mesure section par section de `/usures-dentaires/` :

| Section | Hauteur | Mots | Mots par écran |
|---|---|---|---|
| Faire le point sur une usure dentaire | 0,6 écran | **30** | **52** |
| Introduction | 0,7 écran | 40 | 61 |
| Quand les dents commencent à changer | 1,1 écran | 69 | 63 |
| Restaurer l'esthétique et la fonction ensemble | **1,7 écran** | 120 | 70 |
| **Moyenne de la page** | | | **104** |

Une page web lisible affiche **250 à 400 mots par écran**. La page facettes du Dr Cohen
Samama en affiche **218**.

Il faut donc **deux à trois fois plus de défilement** pour lire la même chose.

### 3. La moitié de l'écran est vide

Le texte occupe une colonne de **640 pixels sur 1 440** — **44 % de la largeur**. Le
reste est blanc. Chez le Dr Cohen Samama : **830 pixels, 58 %**.

La page ne se sert pas de la largeur disponible, donc tout s'empile vers le bas.

### Ce que ça donne au total

| Page | drfranckmoyal.fr | équivalent Dr Cohen Samama |
|---|---|---|
| Page facettes / soins (ordinateur) | **13,4 écrans** | **5,4 écrans** |
| La même (téléphone) | **16,8 écrans** | **9,2 écrans** |
| Espace vertical par mot | **9 px** | **3,7 px** |

Et les deux pires :

- `/facettes-ou-composite/` : **18 756 px, soit 20,8 écrans**, 19 titres de niveau 2
- `/dentisterie-esthetique-paris/` : **16 755 px, soit 18,6 écrans**

**Vingt-et-un écrans pour une page.** Personne ne descend jusqu'en bas.

Et `/contact/` fait **4,5 écrans** pour 227 mots. Une page contact devrait en faire un.

---

## La cause de fond

Le design a été conçu en septembre pour **trois pages courtes** — le golden master.
À cette échelle, ses grands espaces, sa colonne étroite et sa typographie ample
produisent un très bel objet.

Il a ensuite été appliqué tel quel à **vingt-trois pages de mille à deux mille cinq
cents mots**, elles-mêmes découpées en douze sections.

**Le système n'est pas mauvais. Il est appliqué hors de son échelle.** Multipliez des
espacements généreux par douze sections, et vous obtenez treize écrans.

---

## Ce que fait le site que vous citez en exemple

Le Dr Cohen Samama range son site sur **deux axes séparés** :

- **`/besoins/`** — dans les mots du patient : *aligner les dents*, *effacer les
  taches*, *blanchir les dents*, *améliorer l'aspect des dents abîmées*, *remplacer
  une dent manquante*
- **`/solutions/`** — dans les mots du praticien : *facettes*, *blanchiment*,
  *Invisalign*, *ICON*, *couronnes*

Deux pages sommaires très courtes (1,9 et 2,4 écrans) donnent accès à tout.

**Chez nous, les deux sont mélangés dans la même liste** : « Usures dentaires » est un
problème, « Facettes dentaires » est une solution, « Facettes ou composite » est une
comparaison — et les trois sont au même niveau, dans le même menu. Le visiteur doit
deviner dans quelle catégorie il se trouve.

---

## L'état des lieux en chiffres

| Type de page | Nombre | Mots | Moyenne | Titres H2 en moyenne |
|---|---|---|---|---|
| Accueil | 1 | 467 | 467 | 6,0 |
| **Soins et problèmes** | **15** | **20 591** | **1 373** | **12,8** |
| Cas cliniques | 4 | 3 164 | 791 | 9,2 |
| Parcours et autorité | 6 | 3 371 | 562 | 6,3 |
| Service | 2 | 544 | 272 | 7,5 |
| **Total** | **28** | **28 137** | | |

**28 137 mots, soit 141 minutes de lecture.** Et l'accueil, la porte d'entrée, est la
page la plus courte du site après les mentions légales.

---

## Ce qu'une refonte doit changer

Dans l'ordre d'effet, le plus fort d'abord.

1. **Ramener chaque page de soins à quatre ou cinq chapitres**, avec des sous-points
   dedans. Le texte ne bouge pas : c'est son découpage qui change.
2. **Densifier.** Viser 250 mots par écran au lieu de 104 : espacements réduits,
   colonne élargie, blocs mis côte à côte plutôt qu'empilés.
3. **Séparer les deux axes** : « ce que j'ai » et « ce qu'on peut faire ». Ça clarifie
   le menu, l'accueil, et le lien entre les pages.
4. **Donner un vrai rôle à l'accueil.** 467 mots, c'est trop peu pour orienter.
5. **Refaire la page contact.** Un écran.

---

## Deux décisions qui vous reviennent

### Le verrou du design (V24)

Le golden master a été gelé le 21 septembre : ni les composants, ni la typographie,
ni les espacements ne devaient plus bouger. **Les points 1 à 3 ci-dessus le brisent.**

Une refonte totale suppose de lever ce verrou. C'est votre décision, et elle doit être
explicite : sans elle, je ne peux que redécorer, et nous avons déjà vu début octobre
que redécorer ne suffit pas.

### Qui écrit

La règle du projet est : ChatGPT rédige, Claude exécute, vous validez. **La refonte
telle que décrite ne réécrit aucun texte** — elle les regroupe et les remet en page.
Mais si vous voulez aussi raccourcir ou réécrire, cela passe par ChatGPT.

**Dites-moi lequel des deux vous voulez :**
une refonte de la forme seule, à texte inchangé — ou forme *et* texte.

---

## Ce que la refonte ne réglera pas

À dire franchement, pour éviter une déception.

Le relevé du 8 octobre montre que **33 des 47 mots suivis ne donnent rien** dans
Google, et que « usure dentaire » est en position 86. **Ce n'est pas un problème de
lisibilité**, c'est l'ancienneté du domaine et le manque de liens entrants.

Une refonte rendra le site lisible et retiendra les visiteurs qui arrivent. Elle ne
les fera pas arriver plus nombreux. Les deux chantiers sont distincts et il faut mener
les deux.

---

*Mesures du 12 octobre 2026. Aucune modification apportée au site.*
