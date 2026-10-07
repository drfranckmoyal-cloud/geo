# Suivi quotidien des positions

*Mis en place le 8 octobre 2026, à la demande de Franck.*

## Ce que c'est

Chaque matin à 8 h, un agent relève la position de **drfranckmoyal.fr** dans Google sur
**47 mots-clés** choisis par Franck, écrit le relevé du jour, le compare à celui de la
veille, et dit ce qui a bougé.

La source est **Search Console** — les chiffres de Google lui-même, pas une estimation.
C'est la seule façon fiable : interroger Google directement avec un robot fait apparaître
un test anti-robot au bout de quelques requêtes.

## Les fichiers

| | |
|---|---|
| `mots-cles.json` | Les 47 termes, rangés en six familles. **C'est ici qu'on ajoute ou retire un mot.** |
| `releves/AAAA-MM-JJ.json` | Un relevé par jour : clics, impressions et position de chaque terme. |
| `comparer.mjs` | Compare deux relevés. `node suivi/comparer.mjs` prend le dernier contre le précédent. |

## Lire un relevé

`position: null` veut dire **le terme ne sort sur rien**. Search Console affiche 0 faute de
données ; ce n'est pas une position, et il ne faut pas le lire comme telle.

Une position de 86 signifie « page 9 » : techniquement présent, concrètement invisible.
En dessous de 10, on est en première page. Entre 11 et 20, on est en deuxième page — c'est
là que l'effort rapporte le plus, parce qu'il suffit de quelques places.

## Ce que le suivi ne dit pas

Il mesure le **référencement classique**. Il ne dit rien de ce que répondent les IA : ça,
c'est `docs/VISIBILITE-IA.md`, à refaire à la main tous les trois mois.

## Ajouter un mot

Ouvrir `mots-cles.json`, ajouter la ligne dans la bonne famille, entre guillemets, avec
une virgule. Le lendemain matin il est suivi.
