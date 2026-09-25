# AUDIT ANTI-PROMPT — drfranckmoyal.fr

*Claude Code, 25 septembre 2026. Audit demandé par ChatGPT après un signalement de Franck sur
`/medias-interviews/`. Cahier des charges archivé dans
`docs/echanges/2026-09-25-chatgpt-audit-anti-prompt.md`.*

---

## Périmètre

| | |
|---|---|
| **URL contrôlées** | **28 / 28** — les 27 adresses du plan du site, plus `/mentions-legales/` (volontairement hors index) |
| **Pages indexables** | 27 |
| **Fichiers du serveur inventoriés** | 215 avant nettoyage, 214 après : 28 pages HTML, 178 fichiers d'images et de polices, 9 fichiers techniques. **Aucun fichier en double, aucune archive, aucune page orpheline hors celle signalée plus bas** |
| **Fichiers source analysés** | 127 sources éditoriales susceptibles d'être rendues : les rubriques 2, 3 et 5 des 28 fichiers du pack, les 9 fichiers de `src/content/`, et l'ensemble des composants, gabarits et routes (`src/components`, `src/layouts`, `src/pages`) |
| **Documents internes** | 94 fichiers dans `docs/` et 108 dans `livrables/` : **aucun n'est publié** — vérifié dans le site fabriqué. Le dossier `public/`, copié tel quel en ligne, ne contient que quatre fichiers (favicons, `robots.txt`) |
| **Build contrôlé** | **oui** : site refabriqué après correction, puis rebalayé — et rebalayé une seconde fois **sur le site en ligne** |

---

## Fuites certaines détectées : 2

### 1. `/medias-interviews/` — la page s'adresse aux moteurs génératifs

| | |
|---|---|
| **Texte publié** | « Ils constituent une **couche de corroboration externe** particulièrement importante pour la compréhension de mon parcours par les patients, confrères et **moteurs génératifs**. » |
| **Emplacement** | `docs/pages-suivantes/v1.2/17_medias-interviews.md`, ligne 174 — **rubrique 5, « CONTENU ÉDITORIAL À RENDRE — MOT POUR MOT »** |
| **Origine** | Phrase de stratégie GEO écrite dans le pack éditorial et marquée comme contenu à rendre : le gabarit du site l'a donc affichée, comme toutes les autres phrases de cette rubrique. Ce n'est pas un prompt destiné à Claude ; c'est une intention de référencement publiée comme du texte patient |
| **Pourquoi c'était visible** | Le site n'affiche que ce que la rubrique 5 contient. Le mécanisme prévu pour écarter une consigne glissée dans le texte (`hidden`) était vide depuis la V1.2 |
| **Correction** | Phrase **masquée** par ce mécanisme. Le fichier du pack n'est pas modifié ; le retrait est listé à chaque contrôle (`npm run verify`) et réversible en une ligne. Le titre de la section, la phrase d'introduction et la liste des ressources sont **conservés** |

### 2. `/mentions-legales/` — une consigne de construction du site

| | |
|---|---|
| **Texte publié** | « **La version initiale du site ne doit intégrer aucun outil de suivi publicitaire ou analytique nécessitant un consentement sans décision explicite préalable.** » |
| **Emplacement** | `docs/pages-suivantes/v1.2/20_mentions-legales.md`, ligne 70 — rubrique 5, section « Données personnelles » |
| **Origine** | Consigne adressée à l'équipe du site (ce que le site *doit* faire), publiée à la place d'un état des lieux (ce que le site *fait*) |
| **Correction** | Phrase **masquée** de la même façon. La phrase suivante, qui prévoit la mise à jour de la page en cas d'ajout d'un formulaire ou d'un outil de mesure, est conservée. Aucune obligation légale n'est perdue : le site n'utilise aujourd'hui **aucun traqueur, aucun cookie, aucun script externe** — vérifié |

---

## Éléments suspects — signalés, non modifiés : 5

Aucun de ces passages n'a été touché : leur caractère interne n'est pas certain, et le §11 du
cahier des charges interdit de réécrire ce qui est validé.

| # | URL | Extrait | Raison du doute |
|---|---|---|---|
| 1 | `/publications/` | « Elles permettent également aux patients, confrères et **moteurs de recherche** de retrouver les sources originales associées à ces domaines. » | Même famille que la fuite n° 1 : la page explique au lecteur qu'elle sert aussi au référencement. « Moteurs de recherche » reste du français courant, contrairement à « moteurs génératifs » — d'où le classement en suspect |
| 2 | `/publications/` | Section « **Pourquoi ces publications apparaissent-elles sur le site ?** — Parce qu'elles constituent des preuves documentaires indépendantes de plusieurs axes de mon parcours » | Discours du site sur lui-même. Défendable pour un lecteur, mais c'est une justification de stratégie éditoriale |
| 3 | `/medias-interviews/` | Section « **Pourquoi relier ces contenus depuis mon site ?** — Parce qu'un site personnel ne devrait pas demander au visiteur de croire uniquement ce qu'il affirme lui-même. » | Même remarque. Cette phrase-ci est plutôt élégante pour un patient ; c'est la phrase suivante, retirée, qui posait problème |
| 4 | `/mentions-legales/` | « Les photographies cliniques publiées sur ce site **ne doivent être utilisées** qu'après vérification du consentement correspondant. » | Rédigé comme une consigne à l'éditeur du site. Mais la retirer affaiblirait en apparence l'engagement sur le consentement : à réécrire plutôt qu'à supprimer, si ChatGPT le souhaite |
| 5 | `/anorexie-erosion-dentaire-sans-vomissements/` | Intertitre « **Il faut éviter ce raccourci** » | Détecté par la recherche de tournures impératives. Lecture faite, c'est une figure de style adressée au lecteur (« l'anorexie est-elle une cause directe d'érosion ? Il faut éviter ce raccourci »), pas une consigne interne. Signalé par transparence |

### Constat technique, hors texte

`https://drfranckmoyal.fr/default.php` répondait **200** : c'était la « Page par défaut »
d'Hostinger, déposée à la création de l'hébergement le 22 septembre et jamais retirée. Elle n'était
liée nulle part et ne contenait aucune information du cabinet, mais elle restait publiquement
accessible. **Retirée le 25/09/2026 sur décision de Franck** : le fichier est à la corbeille du
serveur (récupérable), et l'adresse répond désormais `404`. Le reste du site est inchangé,
vérifié page par page.

---

## Contrôle automatique — familles de marqueurs recherchées

Recherche menée sur **tout le HTML envoyé au navigateur** : texte visible, en-tête, pied de page,
`title`, toutes les balises `meta` (dont OpenGraph et Twitter), attributs `alt`, `aria-label`,
`title=`, données structurées JSON-LD, et **commentaires HTML**.

| Famille | Marqueurs | Résultat |
|---|---|---|
| Prompt et assistants | `prompt`, `instruction(s)`, `Claude`, `Claude Code`, `ChatGPT`, `GPT`, `LLM` | **0** |
| Marqueurs de développement | `TODO`, `FIXME`, `placeholder`, `brouillon`, `draft`, `version finale` | **0** (la classe CSS `.placeholder-text` subsiste dans la feuille de style : c'est un nom de classe, aucun texte) |
| Attentes de contenu | `à compléter`, `à fournir`, `à vérifier`, `à confirmer`, `à trancher`, `ajouter ici`, `insérer` | **0** |
| Interdictions de rédaction | `ne pas inventer`, `ne pas mentionner`, `ne pas dire`, `ne pas écrire`, `ne pas utiliser` | **0** |
| Vocabulaire de production | `consigne`, `note interne`, `cahier des charges`, `source de vérité`, `verrouillé`, `brief` | **0** |
| Vocabulaire SEO/GEO | `SEO`, `GEO`, `mot-clé`, `keyword`, `canonical`, `indexable`, `maillage`, `sitemap`, `balise`, `H1` | **0** dans le texte ; `schema.org` apparaît 31 fois, uniquement comme `@context` des données structurées — normal |
| Cible « moteurs » | `moteurs génératifs`, `moteurs de recherche`, `intelligence artificielle`, `IA` | **2 avant correction** (fuite n° 1 et suspect n° 1) |
| Tournures d'instruction | « cette page doit… », « l'objectif de cette page… », « le lecteur doit comprendre… », « pour le SEO/GEO », « conserver/utiliser/éviter ce texte », « ne pas… », « il faut… », « mot pour mot », « faits validés » | **3 occurrences**, toutes analysées en contexte et légitimes (« il faut éviter ce raccourci », « rapport entre impact esthétique et préservation », « symptômes rapportés ») |

La recherche a aussi porté sur les **sources non rendues** : les 28 fichiers du pack, les fichiers
de `src/content/`, les composants et les gabarits. Les seules occurrences de « ChatGPT » y sont des
**étiquettes de traçabilité en commentaire de code** (`const EDITO = "audit éditorial de ChatGPT"`),
utilisées par les rapports de contrôle et jamais envoyées au navigateur — vérifié.

---

## Contrôle du build et de la production

1. Site refabriqué après correction : 28 pages.
2. **Rebalayage complet du HTML fabriqué** : 0 fuite, 3 faux positifs expliqués ci-dessus.
3. Paquet déposé chez Hostinger, archive retirée.
4. **Rebalayage complet du site EN LIGNE**, page par page : **0 alerte sur 28 pages**.
5. Les 28 pages en ligne sont identiques, octet pour octet, à la version fabriquée.
6. Inventaire du serveur : aucun fichier en double, aucune archive oubliée, aucune ancienne page.

### État de `/medias-interviews/` après correction

| | |
|---|---|
| Title | « Médias et interviews \| Dr Franck Moyal » — inchangé |
| Meta description | inchangée |
| Canonical | `https://drfranckmoyal.fr/medias-interviews/`, auto-référente |
| Indexable | oui, aucune balise `robots` |
| H1 | « Médias et interviews — Dr Franck Moyal » — inchangé |
| Structure | 7 H2, 5 H3 — inchangée |
| Données structurées | `WebSite`, `CollectionPage`, `BreadcrumbList`, `Person`, `Dentist` — inchangées |
| Maillage | 7 liens internes, 8 liens externes — inchangés |
| Contenu | 511 mots ; seule la dernière phrase de la dernière section a disparu |

---

## Résultat final

```
Fuites certaines restantes : 0 / 2
Éléments suspects restant à valider : 5
Constat technique : réglé — /default.php retiré, l'adresse répond 404
Pages contrôlées : 28 / 28
```

Les 28 pages du site, leurs métadonnées, leurs données structurées et leurs commentaires HTML ont
été réellement examinés, sur le build **et** en production. Aucun prompt, aucune instruction
destinée à Claude ou à ChatGPT, aucune note de travail n'est publiée. Les deux phrases retirées
étaient des passages du pack éditorial rédigés pour l'équipe du site et non pour son lecteur.

*Rien d'autre n'a été modifié : ni les textes validés, ni les titres, ni les adresses, ni le
design, ni l'architecture. Aucune page créée.*
