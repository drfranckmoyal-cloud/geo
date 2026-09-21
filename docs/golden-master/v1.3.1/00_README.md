# GOLDEN MASTER — DR FRANCK MOYAL
## À lire avant toute exécution

**Commence obligatoirement par `00_PROJECT_CONTEXT.md`.**

Ce dossier ne contient pas simplement trois pages à coder.
Il contient le **prototype de référence du futur site complet** de `drfranckmoyal.fr`.

## Ordre de lecture obligatoire

1. `00_PROJECT_CONTEXT.md` — vision globale, positionnement, architecture, rôles
2. `01_DESIGN_SYSTEM.md` — direction visuelle
3. `02_HOME.md` — contenu homepage
4. `03_FRANCK_MOYAL.md` — page entité
5. `04_USURES_DENTAIRES.md` — page clinique type
6. `05_COMPONENT_MAP.md` — composants à construire
7. `06_PROMPT_CLAUDE_CODE.md` — règles d’exécution
8. `07_ART_DIRECTION.md` — direction artistique verrouillée
9. `08_VISUAL_QA_CLAUDE.md` — critères visuels de validation

## Mission actuelle de Claude Code

Construire **uniquement** :
- `/`
- `/franck-moyal/`
- `/usures-dentaires/`

Ces pages constituent le **golden master visuel et technique**.

Aucune industrialisation du reste du site avant validation humaine.

## Workflow

1. Claude Code construit.
2. Il produit captures desktop + mobile.
3. ChatGPT audite le rendu par rapport aux fichiers de référence.
4. Franck valide ou demande des modifications.
5. Claude corrige.
6. Lorsque le rendu est validé, les composants sont gelés.
7. Le reste du site est ensuite décliné sur cette base.

## Principe fondamental

**Claude Code exécute un système déjà décidé. Il ne doit pas réinventer le projet.**
