# La maquette de la refonte — comment la regarder

## En deux clics, sans rien installer

Ouvrez **`site/index.html`** (double-clic). C'est la porte d'entrée du site :
l'animation d'ouverture, puis les deux moitiés, espace patients et espace pro.
Tout fonctionne hors ligne, photographies comprises.

Pour voir **toutes les pages d'un coup**, ouvrez **`site/sommaire.html`**.
Cette page-là n'existe que pour vous ; elle ne fera pas partie du site.

## Ce que vous regardez

C'est **une maquette**. Les textes sont ceux du site en ligne, repris mot pour
mot, sans rien réécrire : ce qui change, c'est la mise en page. Les titres de
chapitre et les deux pages d'espace sont les seuls textes nouveaux, et ils
attendent la relecture de ChatGPT.

**Le site en ligne n'a pas été touché.** https://drfranckmoyal.fr continue de
tourner exactement comme avant.

## Si quelque chose cloche

Dites lequel des trois :

- **la forme** — une page trop longue, une carte mal placée, une photo mal choisie ;
- **le parcours** — on ne trouve pas quelque chose, on ne sait pas où on est ;
- **le texte** — une phrase fausse ou mal dite (celles-là partent chez ChatGPT).

## Pour qui travaille sur le code

Une seule commande reconstruit tout, dans le seul ordre qui marche :

```bash
./construire.sh
```

Elle enchaîne `generer.py` (remise en page mécanique), `composer.py` (regroupement
en chapitres, avec relecture mot à mot contre l'original) et `verifier.py`, qui
refuse de se taire : liens morts, images absentes, éléments vides, balises dans
les titres, verrou V21, données structurées, et toute divergence du menu, du pied
de page ou de la feuille de style d'une page à l'autre.

Dernier relevé : **29 pages, 1 260 liens internes, 0 mort, 0 débordement de 375
à 1 440 px, données structurées sur les 29**.
