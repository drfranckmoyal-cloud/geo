#!/usr/bin/env python3
"""Fabrique les deux pages d'atterrissage, espace patients et espace pro.

Ce sont des sommaires, pas des articles : une seule sorte de carte, répétée,
rangée sous des sections numérotées. C'est la règle que Franck a posée le
17/10/2026 — cohérence et hiérarchie — après avoir trouvé la première version
« le bazar » : on y tombait sur un cas d'usure sans savoir où l'on était.
Le menu, le pied de page et la signature du style sont posés par generer.py
au passage suivant : rien n'est recopié ici.
"""
import html as H
import os
import re

SORTIE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
PHOTOS = "../../../../src/assets/photos/cas/"


def e(t):
    return H.escape(t, quote=False)


def acte(titre, quoi, lien, photo="", cadrage="", alt=""):
    """La carte d'un acte : allongée, peu haute, le nom en grand à gauche et la
    photographie à droite, fondue dans la carte par un dégradé — elle illustre
    sans jamais passer sous le texte."""
    visuel = ""
    if photo:
        pos = f" style=\"object-position:{cadrage}\"" if cadrage else ""
        visuel = (f'\n          <span class="tuile__visuel">'
                  f'<img src="{PHOTOS}{photo}" alt="{H.escape(alt)}" loading="lazy"{pos}>'
                  f'</span>')
    return f'''        <a class="tuile tuile--acte" href="{lien}.html">{visuel}
          <span class="tuile__dit">
            <h3 class="tuile__acte">{e(titre)}</h3>
            <p class="tuile__quoi">{e(quoi)}</p>
            <span class="tuile__fleche">L’acte en détail <span>→</span></span>
          </span>
        </a>'''


def tuile(titre, quoi, lien, verbe="Lire", externe=False, longue=False):
    classe = "tuile tuile--long" if longue else "tuile"
    corps = (f'<h3 class="tuile__{"acte" if longue else "titre"}">{e(titre)}'
             f'{" <span class=\'ext\'>↗</span>" if externe else ""}</h3>\n'
             f'            <p class="tuile__quoi">{e(quoi)}</p>\n'
             f'            <span class="tuile__fleche">{e(verbe)} <span>→</span></span>')
    cible = (f'href="{lien}" target="_blank" rel="noopener"' if externe
             else f'href="{lien}.html"')
    if longue:
        return (f'        <a class="{classe}" {cible}>\n'
                f'          <span class="tuile__dit">\n            {corps}\n'
                f'          </span>\n        </a>')
    return f'        <a class="{classe}" {cible}>\n            {corps}\n        </a>' 


def paire(titre, quoi, lien, avant, apres):
    return f'''        <a class="tuile tuile--cas" href="{lien}.html">
          <span class="tuile__paire">
            <img src="{PHOTOS}{avant}" alt="Avant" loading="lazy"><img src="{PHOTOS}{apres}" alt="Après" loading="lazy">
          </span>
          <h3 class="tuile__titre">{e(titre)}</h3>
          <p class="tuile__quoi">{e(quoi)}</p>
          <span class="tuile__fleche">Voir le cas <span>→</span></span>
        </a>'''


def section(rang, titre, tuiles, zone=False):
    classe = "sect sect--zone" if zone else "sect"
    return f'''  <section class="{classe}">
    <div class="contenu">
      <div class="tete-rang">
        <p class="rang">{rang}</p>
        <h2>{e(titre)}</h2>
      </div>
      <div class="tuiles">
{chr(10).join(tuiles)}
      </div>
    </div>
  </section>'''


def page(slug, titre, description, ariane, eyebrow, h1, sections, jsonld=""):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titre)}</title>
<meta name="description" content="{H.escape(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap">
<link rel="stylesheet" href="style.css?v=0">
{jsonld}
</head>
<body>

<header class="entete"></header>

<main>

  <section class="sect sect--tete" style="border-top:0">
    <div class="contenu">
      <p class="ariane"><a href="index.html">Accueil</a> › {e(ariane)}</p>
      <p class="eyebrow">{e(eyebrow)}</p>
      <h1>{e(h1)}</h1>
    </div>
  </section>

{chr(10).join(sections)}

</main>

<footer class="pied"></footer>
<script src="menu.js"></script>
</body>
</html>
'''


def garder_jsonld(nom):
    """On ne refabrique pas les données structurées : on reprend celles de la
    page qu'on remplace, pour ne pas les perdre à chaque refonte."""
    chemin = os.path.join(SORTIE, nom)
    if not os.path.exists(chemin):
        return ""
    trouve = re.findall(r'<script type="application/ld\+json"[^>]*>.*?</script>',
                        open(chemin, encoding="utf-8").read(), re.S)
    return "\n".join(trouve)


# ── Espace patients ───────────────────────────────────────────────────────
# Les actes : c'est eux que le patient cherche, et c'est eux qui portent le
# grand titre de leur page. Ils passent donc en premier, en grand.
# Chaque acte porte une photographie du cabinet. Les trois images de composite
# sont des avant/après montés en carré : on cadre sur le bas, c'est-à-dire sur
# l'après. Les autres sont des vues uniques, cadrées au centre.
ACTES = [
    ("Facettes",
     "Céramique collée sur la face visible de la dent.",
     "facettes-dentaires-paris", "facettes-ceramique-apres.jpg", "",
     "Sourire après la pose de facettes en céramique"),
    ("Composite bonding",
     "Résine stratifiée sur la dent, en une séance.",
     "composite-bonding-paris", "composite-bonding-six-dents-anterieures.jpg",
     "center 78%", "Sourire après un composite bonding sur six dents"),
    ("Éclaircissement",
     "Gouttières à domicile, suivi au cabinet.",
     "eclaircissement-dentaire-paris", "eclaircissement-ambulatoire-apres.jpg", "",
     "Sourire après un éclaircissement ambulatoire"),
    ("Infiltration ICON",
     "Taches blanches, MIH, fluorose. Sans fraise.",
     "taches-dentaires-dyschromies-icon", "mih-erosion-infiltration-apres.jpg", "",
     "Dents après infiltration de taches de MIH"),
    ("Réhabilitation des dents usées",
     "Rendre la hauteur et la fonction.",
     "rehabilitation-dents-usees", "rehabilitation-usure-apres.jpg", "",
     "Sourire après la réhabilitation de dents usées"),
    ("Bilan esthétique",
     "Photographies, analyse du sourire, projet.",
     "bilan-esthetique-personnalise", "bilan-esthetique-projet.jpg", "",
     "Projet esthétique dessiné avant traitement"),
]

# Deux pages qui ne sont pas des actes mais aident à choisir entre eux.
POUR_CHOISIR = [
    ("Dentisterie esthétique",
     "Vue d’ensemble des actes.",
     "dentisterie-esthetique-paris", "La vue d’ensemble"),
    ("Facettes ou composite ?",
     "Tenue, teinte, réparabilité, coût en tissu dentaire.",
     "facettes-ou-composite", "Comparer"),
]

# Les sujets cliniques : ce que les actes traitent.
SUJETS = [
    ("Usure dentaire",
     "Attrition, érosion, abrasion. Mesure BEWE.",
     "usures-dentaires"),
    ("Érosion dentaire",
     "Origines alimentaires, gastriques, professionnelles.",
     "erosion-dentaire"),
    ("Bruxisme",
     "Serrement, grincement, gouttière.",
     "bruxisme-usure-dentaire"),
    ("Dents courtes ou usées",
     "Usure du bord ou excès de gencive.",
     "dents-courtes-usees"),
    ("Troubles des conduites alimentaires",
     "Anorexie, boulimie. Dépistage et prévention.",
     "tca-dents"),
    ("Anorexie restrictive",
     "Érosion sans vomissements.",
     "anorexie-erosion-dentaire-sans-vomissements"),
]

# Chaque vignette est prise DANS la page vers laquelle elle mène : sinon on
# montre un cas et on en ouvre un autre.
CAS = [
    ("Usures antérieures et facettes",
     "Diagnostic, gouttière composite, facettes.",
     "cas-usures-dentaires-facettes-minimalement-invasives",
     "rehabilitation-usure-avant.jpg", "rehabilitation-usure-apres.jpg"),
    ("Réhabilitation par vingt facettes",
     "Projet dessiné, essayé en bouche, puis posé.",
     "cas-planification-rehabilitation-facettes",
     "bilan-esthetique-initial.jpg", "bilan-esthetique-resultat.jpg"),
    ("Quatre facettes céramique",
     "Planification numérique, puis pose.",
     "cas-planification-facettes-ceramique",
     "facettes-planification-initial.jpg", "facettes-planification-resultat.jpg"),
    ("Taches de MIH",
     "Éclaircissement, puis infiltration.",
     "cas-mih-eclaircissement-erosion-infiltration",
     "dyschromie-erosion-infiltration-avant.jpg", "dyschromie-erosion-infiltration-apres.jpg"),
]

PRATICIEN = '''      <div class="tuiles tuiles--praticien">
        <a class="tuile tuile--large" href="franck-moyal.html">
          <img class="tuile__portrait" src="img/portrait-fm.png?v=0"
               alt="Dr Franck Moyal, chirurgien-dentiste à Paris">
          <span class="tuile__texte">
            <h3 class="tuile__titre">Dr Franck Moyal</h3>
            <p class="tuile__quoi">Chirurgien-dentiste à Paris 9<sup>e</sup>, exercice exclusif en
              dentisterie esthétique et adhésive. Praticien hospitalier, Pitié-Salpêtrière et
              CMME de Sainte-Anne.</p>
            <span class="tuile__fleche">Son parcours <span>→</span></span>
          </span>
        </a>
        <a class="tuile" href="chirurgien-dentiste-paris-9.html">
          <h3 class="tuile__titre">Le cabinet, Paris 9<sup>e</sup></h3>
          <p class="tuile__quoi">2 rue Hippolyte Lebas, 75009 Paris.</p>
          <span class="tuile__fleche">Voir <span>→</span></span>
        </a>
        <a class="tuile" href="contact.html">
          <h3 class="tuile__titre">Prendre rendez-vous</h3>
          <p class="tuile__quoi">01 83 75 52 16, ou par courriel.</p>
          <span class="tuile__fleche">Nous écrire <span>→</span></span>
        </a>
      </div>'''


def patients():
    sections = [
        section("1", "Mon expertise",
                [acte(*a) for a in ACTES] + [tuile(*p, longue=True) for p in POUR_CHOISIR]),
        section("2", "Ce que je traite",
                [tuile(t, q, l, longue=True) for t, q, l in SUJETS], zone=True),
        section("3", "Cas cliniques", [paire(*c) for c in CAS]),
        f'''  <section class="sect sect--zone">
    <div class="contenu">
      <div class="tete-rang">
        <p class="rang">4</p>
        <h2>Le praticien</h2>
      </div>
{PRATICIEN}
    </div>
  </section>''',
    ]
    return page(
        "espace-patients",
        "Espace patients | Dr Franck Moyal — dentisterie esthétique à Paris",
        "Facettes, composite bonding, éclaircissement, infiltration ICON, réhabilitation des "
        "dents usées, bilan esthétique : chaque acte a sa page. Dr Franck Moyal, Paris 9e.",
        "Espace patients", "Vous consultez", "Espace patients",
        sections, garder_jsonld("espace-patients.html"))




# ── Espace pro ────────────────────────────────────────────────────────────
PRO_ENSEIGNEMENT = [
    ("Conférences et formations",
     "Esthétique, composites, planification, usures.",
     "conferences-formations", "Le détail"),
    ("Smile Club Formations",
     "Calendrier, sessions, inscriptions.",
     "https://smileclubformations.com/", "Le site", True),
]

PRO_TRAVAUX = [
    ("Publications et travaux",
     "Six publications, sept thèses encadrées.",
     "publications", "La liste"),
    ("Médias et interviews",
     "Entretiens, articles, ressources externes.",
     "medias-interviews", "Les parutions"),
]

PRO_HOSPITALIER = [
    ("Activité hospitalière",
     "Pitié-Salpêtrière 2012, CMME Sainte-Anne 2024.",
     "activite-hospitaliere", "Le détail"),
    ("TCA et santé bucco-dentaire",
     "Ce que le chirurgien-dentiste repère en premier.", "tca-dents", "Lire"),
    ("Anorexie et érosion sans vomissements",
     "Érosion sans conduite de purge.",
     "anorexie-erosion-dentaire-sans-vomissements", "Lire"),
]

PRO_PRATICIEN = '''      <div class="tuiles tuiles--praticien">
        <a class="tuile tuile--large" href="franck-moyal.html">
          <img class="tuile__portrait" src="img/portrait-fm.png?v=0"
               alt="Dr Franck Moyal, chirurgien-dentiste à Paris">
          <span class="tuile__texte">
            <h3 class="tuile__titre">Dr Franck Moyal</h3>
            <p class="tuile__quoi">Chirurgien-dentiste à Paris 9<sup>e</sup>, exercice exclusif en
              dentisterie esthétique et adhésive. Praticien hospitalier, Pitié-Salpêtrière et
              CMME de Sainte-Anne. Président de DenTCA.</p>
            <span class="tuile__fleche">Son parcours <span>→</span></span>
          </span>
        </a>
        <a class="tuile" href="contact.html">
          <h3 class="tuile__titre">Échanger sur un cas</h3>
          <p class="tuile__quoi">Question clinique, intervention, collaboration.
            01 83 75 52 16.</p>
          <span class="tuile__fleche">Me contacter <span>→</span></span>
        </a>
        <a class="tuile" href="chirurgien-dentiste-paris-9.html">
          <h3 class="tuile__titre">Le cabinet, Paris 9<sup>e</sup></h3>
          <p class="tuile__quoi">2 rue Hippolyte Lebas, 75009 Paris.</p>
          <span class="tuile__fleche">Voir <span>→</span></span>
        </a>
      </div>'''


def pro():
    sections = [
        section("1", "Enseignement et formation", [tuile(*t, longue=True) for t in PRO_ENSEIGNEMENT]),
        section("2", "Publications", [tuile(*t, longue=True) for t in PRO_TRAVAUX], zone=True),
        section("3", "Activité hospitalière", [tuile(*t, longue=True) for t in PRO_HOSPITALIER]),
        section("4", "Cas cliniques", [paire(*c) for c in CAS], zone=True),
        f'''  <section class="sect">
    <div class="contenu">
      <div class="tete-rang">
        <p class="rang">5</p>
        <h2>Le praticien</h2>
      </div>
{PRO_PRATICIEN}
    </div>
  </section>''',
    ]
    return page(
        "espace-pro",
        "Espace pro | Formations, publications et activité hospitalière — Dr Franck Moyal",
        "Conférences et formations, publications, activité hospitalière à la Pitié-Salpêtrière "
        "et à la CMME de Sainte-Anne, cas documentés : l’espace professionnel du Dr Franck Moyal.",
        "Espace pro", "Vous exercez", "Espace pro",
        sections, garder_jsonld("espace-pro.html"))


if __name__ == "__main__":
    open(os.path.join(SORTIE, "espace-patients.html"), "w",
         encoding="utf-8").write(patients())
    open(os.path.join(SORTIE, "espace-pro.html"), "w",
         encoding="utf-8").write(pro())
    print("espace-patients.html et espace-pro.html refaits en sommaires")
