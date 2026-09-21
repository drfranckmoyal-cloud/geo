# 21 — MANIFESTE D’INTÉGRATION CLAUDE CODE — V1.2 FINAL

## Principe
Ces fichiers sont les contrats éditoriaux des 20 pages restantes. Le texte visible doit être repris mot pour mot, à l’exception :
- des éléments explicitement marqués `[À FOURNIR]` ;
- des notes d’implémentation marquées « NON AFFICHÉES » ;
- des URLs de preuves/sources qui deviennent des liens ;
- des libellés de structure du fichier (`ROUTING`, `SEO`, etc.), qui ne sont pas du contenu patient.

## Golden Master
Réutiliser exclusivement les composants gelés.

## Contrôles automatiques à ajouter
Pour chaque nouvelle route :
1. un seul H1 ;
2. fil d’Ariane conforme ;
3. title + meta + canonical ;
4. `dateModified` si page clinique/médicale ;
5. auteur relié à `https://drfranckmoyal.fr/#franck-moyal` ;
6. sources présentes dans le HTML des pages médicales ;
7. liens internes descriptifs ;
8. aucun texte « dentiste esthétique » ;
9. aucune image stock inventée ;
10. aucune modification des tokens du Golden Master.

## Livraison par lot
Après chaque lot A/B/C/D :
- build ;
- `npm run verify` ;
- contrôle HTML ;
- Lighthouse sur 1 page représentative desktop/mobile ;
- captures uniquement des nouvelles compositions qui n’existaient pas déjà.

## Données toujours en attente
- téléphone ;
- URL de prise de rendez-vous ;
- e-mail professionnel pour mentions légales ;
- hébergeur pour mentions légales ;
- URLs sameAs exactes ;
- visuels propriétaires.

## Décisions V1.1 issues des lots A et B
- Ordre des pages cliniques : **FAQ → Sources → Auteur → Pages liées → Appel final**. La page Usures du Golden Master reste une exception historique ; ne pas rouvrir son design.
- `MethodSteps` de la page Bilan : conserver les 7 étapes, avec le titre **« Du projet au traitement : sept étapes »**.
- Grilles H3, listes en deux colonnes, listes latérales, sommaire cliquable Diagnostic, bloc CMME sauge et CTA final réduit titre+bouton : **validés**.
- Les H1 listés dans la V1.1 ont été raccourcis pour respecter la règle mobile V16.
- Ne pas afficher de « date de vérification bibliographique » au patient.
- Gras Inter autorisé avec parcimonie dans le texte courant.
- Tant que l’URL de réservation définitive n’est pas fournie, tous les CTA et le bouton d’en-tête **Prendre rendez-vous / Rendez-vous** pointent vers `/contact/#prendre-rendez-vous`.
- Les consignes éditoriales ou de normalisation restent dans les notes non affichées, jamais dans le texte patient.


## Décisions finales issues des lots C et D

### Lot C — Autorité / Entité / Local
- Ouverture clinique sobre des pages 14 à 17 : **VALIDÉE**.
- Pages 14 à 17 : **pas d’AuthorBlock final, pas de FinalCTA** ; `RelatedPages` uniquement lorsque prévu par le contenu.
- Preuves externes en liste sobre à filets + flèche : **VALIDÉES**.
- Grilles 2–4 entrées courtes : **VALIDÉES**.
- Aucun visuel obligatoire sur 14 à 18 tant qu’un asset réel et suffisamment bon n’est pas disponible.
- Page 18 : le bloc final affiche désormais le bouton **« Prendre rendez-vous »** → `/contact/#prendre-rendez-vous`.
- `Paris 9` reste insécable dans les titres lorsque nécessaire.
- Publications : décrire les 5 travaux dans `CollectionPage.hasPart` selon leur type (`Article` ou `Book`) ; ne pas inclure les travaux académiques encadrés comme publications de Franck.

### Lot D — Contact / Mentions légales
- `/contact/` : H1 définitif **« Contact et rendez-vous — Dr Franck Moyal, Paris 9e »**.
- `/contact/` : les 7 motifs sont des liens internes.
- `/contact/` : `RelatedPages` = Dr Franck Moyal / Chirurgien-dentiste Paris 9 / Activité hospitalière.
- `/contact/` : ancre unique **`#prendre-rendez-vous`**. Ne plus utiliser `#rendez-vous`.
- `/contact/` et `/mentions-legales/` : **aucune ligne auteur visible dans l’ouverture** et aucun AuthorBlock final.
- `/mentions-legales/` : page de lecture simple, `noindex,follow`, hors sitemap, sans CTA et sans pages liées.
- Date visible des mentions légales : **22 septembre 2026**.

## État après revue A → D
- 23 pages construites.
- 22 pages indexables ; Mentions légales hors sitemap en `noindex,follow`.
- Aucun lien interne « à venir ».
- Les corrections bibliographiques et H1 de la V1.1 restent applicables.
- Le Golden Master demeure gelé.
