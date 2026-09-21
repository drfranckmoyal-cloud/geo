# Reconstruction des 23 pages depuis la V1.2 finale

*Claude Code, 22 septembre 2026. Source unique : `PACK_PAGES_SUIVANTES_CLAUDE_CODE_V1_2_FINAL`
(26 fichiers, archivés tels quels dans `docs/pages-suivantes/v1.2/`), avec ton message de
reconstruction. La V1 reste archivée à côté.*

---

## 1. Ce qui est appliqué

- **Les 20 pages** sont reconstruites à partir des fichiers 01 à 20 de la V1.2, lus directement :
  - renvois bibliographiques corrigés ;
  - H1 raccourcis ;
  - consignes retirées du texte patient ;
  - appel final de la page Éclaircissement ;
  - liens explicités ;
  - H1 de la page Contact ;
  - formulation Pitié-Salpêtrière de la page 16 ;
  - dates au 22 septembre 2026.
- **Règle globale des rendez-vous.** Tous les boutons et liens « Prendre rendez-vous » /
  « Rendez-vous » mènent à `/contact/#prendre-rendez-vous`, sur les 23 pages, pages gelées
  comprises :
  - en-tête, ordinateur et mobile ;
  - bouton de l'ouverture de l'accueil ;
  - appels finaux, quel que soit leur libellé (« Réaliser un bilan d'usure dentaire »…) ;
  - pied de page ;
  - page Paris 9.

  La section de la page Contact porte l'ancre unique `id="prendre-rendez-vous"`. L'ancre
  `#rendez-vous` n'existe plus : le bloc d'appel final s'appelle désormais `#appel-final`, sans
  effet visible. Ces liens restent marqués « provisoires » pour le contrôle avant mise en ligne,
  jusqu'à l'arrivée du lien de réservation définitif.
- **Page 02** : `MethodSteps` titré « Du projet au traitement : sept étapes ».
- **Pages 19 et 20** : aucune ligne auteur dans l'ouverture, aucun bloc auteur.
- **Page 19** : les 7 motifs sont des liens. « À lire aussi » contient exactement les trois
  pages de ton contrat.
- **Pages 14 à 17** : ni bloc auteur ni appel final.
- **Page 18** : bouton « Prendre rendez-vous » dans le bloc final.
- **Listes « À lire aussi » construites à partir des liens à câbler** : le lien de rendez-vous
  en est écarté (pages 05 et 18), et une page n'y figure qu'une fois (pages 07, 09 et 10, où le
  libellé long d'un lien du texte mène à une page déjà listée).

## 2. Contrôles

- **Textes** (`npm run verify`) : sur les 20 pages, aucun passage oublié, aucun texte ajouté.
  **Plus aucun écart de renvois** : chaque `[n]` du texte a sa référence, et chaque référence
  est citée.
- **HTML, JSON-LD, adresses de référence, plan du site** (`node scripts/check-html.mjs`) :
  réussi sur les 23 pages.
  - 22 pages indexables dans le plan du site ; mentions légales en `noindex,follow`, hors du plan.
  - Aucun lien « à venir ».
  - Tous les liens de rendez-vous vont vers `/contact/#prendre-rendez-vous`.
  - Une seule section `#prendre-rendez-vous`, sur la page Contact.
  - Aucune ancre `#rendez-vous`.
- **H1 sur mobile** : les 20 tiennent en 4 lignes au plus à 390 px. La règle V16 est respectée
  partout, contre 9 pages à 5–8 lignes en V1.
- **Références** : les 37 PMID de la V1.2 existent sur PubMed, et titres, revues, années,
  premiers auteurs et DOI concordent, nouvelles références comprises (Imfeld 2005, Faine 2003,
  Lo Russo 2008). Un seul détail : Bartlett et O'Toole est paru en ligne en décembre 2020, et le
  pack indique 2021, l'année du numéro.
- **Golden master** : sur les 3 pages gelées, seuls ont changé les liens de rendez-vous et le nom
  de l'ancre du bloc final, comme demandé.
- **Lighthouse** (mobile ; ordinateur pour la page TCA) :

| Page | Rapidité | Accessibilité | Bonnes pratiques | Référencement | LCP | Poids |
|---|---|---|---|---|---|---|
| TCA, mobile (3 passages) | 99 | 100 | 100 | 100 | 1,95 s | 200 Ko |
| TCA, ordinateur | 100 | 100 | 100 | 100 | 0,44 s | 200 Ko |
| Dentisterie esthétique | 99 | 100 | 100 | 100 | 1,95 s | 199 Ko |
| Contact | 100 | 100 | 100 | 100 | 1,80 s | 192 Ko |
| Accueil (golden master, 3 passages) | 99 | 100 | 100 | 100 | 2,10 s | 214 Ko |
| Usures (golden master) | 99 | 100 | 100 | 100 | 1,95 s | 200 Ko |

  L'accueil était à 1,96 s au gel. Mesurée aujourd'hui dans les mêmes conditions, la version
  gelée d'origine donne aussi 2,10 s : l'écart vient de l'outil de mesure, pas du site.

## 3. Remarques, non bloquantes

- **Page 04** : les références [3] Alqutaibi et [4] Klein n'ont plus de DOI dans la V1.2. Ils
  figuraient dans la V1 et sont exacts : `10.1016/j.prosdent.2024.03.019` et
  `10.1111/jerd.13351`. Les deux références s'affichent avec leur seul lien PubMed ; à rétablir
  si c'est un oubli.
- **Page 12, [6] Imfeld 2005** : sans DOI, lien PubMed seul, ce qui est normal si la revue n'en
  attribue pas.

## 4. Avant la mise en ligne

Le contrôle automatique (`npm run launch-check`) ne relève plus que 5 points bloquants, tous du
ressort de Franck :
- informations « à fournir » (33 emplacements) ;
- visuels et consentements (28 emplacements) ;
- lien de réservation définitif ;
- adresses `sameAs` ;
- décision sur les robots d'IA.

Franck dispose d'une page en ligne privée pour les renseigner. Je lis ses réponses directement.
