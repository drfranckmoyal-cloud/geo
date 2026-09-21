# 24 — CHECKLIST AVANT MISE EN LIGNE

## A. Données à fournir par Franck — bloquantes
- [ ] Téléphone du cabinet
- [ ] URL finale de prise de rendez-vous
- [ ] E-mail professionnel
- [ ] Hébergeur : nom / raison sociale
- [ ] Hébergeur : adresse
- [ ] Hébergeur : téléphone ou contact légal
- [ ] URLs officielles `sameAs` : LinkedIn, Instagram et autres profils officiellement retenus

## B. Assets cliniques — à préparer
- [ ] Portrait HD — déjà fourni
- [ ] 2 cas composite bonding
- [ ] 2 cas facettes
- [ ] 1 cas éclaircissement
- [ ] 1–2 cas dyschromies / ICON
- [ ] 1 parcours bilan → planification / SmileCloud → résultat
- [ ] 2 cas usures / réhabilitation
- [ ] 1 exemple d’érosion clinique
- [ ] scans / monitoring si disponibles
- [ ] visuels de formation / conférence utiles
- [ ] visuels du cabinet seulement s’ils sont au niveau esthétique du site
- [ ] consentement de publication web vérifié pour chaque cas patient

## C. À décider avec ChatGPT / Claude
- [ ] robots IA : Google/Bing/OAI-SearchBot + décision séparée pour les crawlers d’entraînement
- [ ] URL de production et redirections éventuelles
- [ ] domaines secondaires à rediriger vers `drfranckmoyal.fr`
- [ ] analytics : aucun / solution sans consentement / solution nécessitant consentement
- [ ] outil externe de rendez-vous : simple lien ou intégration embarquée
- [ ] politique cookies / données à réviser si un tiers est ajouté

## D. QA finale
- [ ] reconstruire les 23 pages depuis V1.2
- [ ] `npm run verify`
- [ ] check HTML / JSON-LD / canonical / sitemap
- [ ] vérifier 22 URLs indexables + mentions légales noindex hors sitemap
- [ ] aucun lien « à venir »
- [ ] aucun `[À FOURNIR]` visible en production
- [ ] Lighthouse pages représentatives
- [ ] responsive 390 / 430 / 1440
- [ ] vérification des formulaires/liens de RDV
- [ ] vérification consentements visuels
- [ ] Search Console
- [ ] Bing Webmaster Tools
- [ ] sitemap soumis
- [ ] robots.txt final
