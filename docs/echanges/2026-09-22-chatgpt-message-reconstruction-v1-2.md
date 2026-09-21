# Message à Claude Code — reconstruction V1.2 finale

Utiliser **PACK_PAGES_SUIVANTES_CLAUDE_CODE_V1_2_FINAL** comme unique source pour reconstruire les 23 pages.

Points importants :
- les fichiers 01 à 20 contiennent les versions corrigées des textes ;
- les corrections V1.1 déjà intégrées portent notamment sur les renvois bibliographiques, les H1 mobiles trop longs, les consignes éditoriales retirées du texte patient et les liens/CTA ;
- le fichier 22 est `22_CHANGELOG_V1_1.md` ; il est volontairement conservé car il documente les corrections intégrées avant la consolidation finale ;
- le fichier 25 `25_CHANGELOG_V1_2_FINAL.md` documente les derniers changements C/D ;
- les fichiers 23 et 24 sont la validation consolidée et la checklist de lancement.

## Destination provisoire des rendez-vous — règle globale
Tant que l’URL finale de réservation n’est pas fournie, **tous les boutons et liens “Prendre rendez-vous” / “Rendez-vous” du site** doivent pointer vers :

`/contact/#prendre-rendez-vous`

Cela s’applique :
- à l’en-tête desktop et mobile ;
- aux CTA de fin de page ;
- au pied de page ;
- à la page Paris 9 ;
- à tout autre lien de rendez-vous visible.

La section Contact doit avoir l’ancre unique :

`id="prendre-rendez-vous"`

Ne plus utiliser `#rendez-vous`.

Après reconstruction : relancer `npm run verify`, les contrôles HTML/JSON-LD/canonical/sitemap et les tests Lighthouse représentatifs.
