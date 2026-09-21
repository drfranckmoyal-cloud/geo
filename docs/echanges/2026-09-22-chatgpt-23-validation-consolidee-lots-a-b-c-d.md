# 23 — VALIDATION CONSOLIDÉE FINALE — LOTS A + B + C + D
## drfranckmoyal.fr — 22 septembre 2026

# VERDICT
**Les choix de composition des lots A, B, C et D sont validés.**
La V1.2 devient la source éditoriale finale pour la reconstruction avant mise en ligne.

Le Golden Master reste gelé : aucune refonte et aucun nouveau langage graphique.

## Lot A — validé
- ordre des blocs des nouvelles pages cliniques ;
- texte décalé comme composition dominante avec variété à partir des composants gelés ;
- H3 / grilles sauge ;
- listes 1–2 colonnes, latérales et numérotées ;
- MethodSteps 7 étapes ;
- placeholders d’images ;
- FAQ / Sources / Auteur / À lire aussi ;
- gras Inter parcimonieux.

## Lot B — validé
- sommaire cliquable Diagnostic ;
- grille Sources externes / internes de la page Érosion ;
- bloc CMME « domaine spécifique » ;
- CTA réduit titre + bouton ;
- emplacement infographie Anorexie pleine largeur.

## Lot C — validé avec deux précisions
- ouverture clinique des pages d’autorité conservée ;
- preuves externes, grilles et absence d’images obligatoires validées ;
- pages 14–17 : pas d’AuthorBlock final et pas de CTA final ;
- page 18 : contrairement à la capture issue de la V1, le bloc final doit afficher **« Prendre rendez-vous »** et pointer vers `/contact/#prendre-rendez-vous` ;
- données structurées Publications : 5 travaux en `hasPart`, avec un type adapté (`Article` / `Book`) et sans métadonnée inventée.

## Lot D — validé avec normalisation
- section Contact « Prendre rendez-vous » : ancre définitive **`#prendre-rendez-vous`** ;
- 7 motifs de consultation cliquables : validés ;
- H1 Contact : **« Contact et rendez-vous — Dr Franck Moyal, Paris 9e »** ;
- « À lire aussi » : les 3 liens proposés sont validés ;
- Mentions légales : lecture simple, sans CTA, RelatedPages ou AuthorBlock ;
- retirer la ligne auteur visible du hero **sur Contact et Mentions légales** ;
- Mentions légales : date visible harmonisée au **22 septembre 2026**.

## Performance / technique
Les rapports Claude indiquent :
- lots A–C : Lighthouse 99–100 sur les pages représentatives ;
- Contact : 100/100/100/100, LCP mobile 1,80 s ;
- Mentions légales : baisse SEO Lighthouse attendue à cause de `noindex`.

Aucune optimisation visuelle supplémentaire n’est requise avant l’intégration des assets.

## Restent bloquants avant mise en ligne
1. téléphone ;
2. URL finale de prise de rendez-vous ;
3. e-mail professionnel ;
4. hébergeur + raison sociale + adresse + contact ;
5. URLs exactes `sameAs` ;
6. choix final des règles robots IA ;
7. visuels propriétaires / consentements.

## Assets
Claude compte 28 emplacements réservés : 22 sur les nouvelles pages et 6 sur le Golden Master.
Le site peut être reconstruit sans eux, mais ils doivent être intégrés avant la validation visuelle de lancement pour les pages où ils portent la preuve clinique.
