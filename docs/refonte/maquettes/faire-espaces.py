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


def aussi(liens):
    """Les pages de contexte, sous la carte. Ce sont de vrais liens : la carte
    n'est donc pas un <a>, c'est le titre qui l'est, et son ::after couvre la
    carte entière pour qu'elle reste cliquable d'un bout à l'autre."""
    if not liens:
        return '<span class="tuile__fleche">En détail <span>→</span></span>'
    corps = " <span>·</span> ".join(
        f'<a href="{sl}.html">{e(l)}</a>' for l, sl in liens)
    return f'<span class="tuile__aussi">{corps}</span>'


def acte(titre, quoi, lien, photo="", cadrage="", alt="", liens=()):
    """La carte d'un acte : allongée, peu haute, le nom en grand à gauche et la
    photographie à droite, fondue dans la carte par un dégradé — elle illustre
    sans jamais passer sous le texte."""
    visuel = ""
    if photo:
        pos = f" style=\"object-position:{cadrage}\"" if cadrage else ""
        visuel = (f'\n          <span class="tuile__visuel">'
                  f'<img src="{PHOTOS}{photo}" alt="{H.escape(alt)}" loading="lazy"{pos}>'
                  f'</span>')
    return f'''        <article class="tuile tuile--acte">{visuel}
          <span class="tuile__dit">
            <h3 class="tuile__acte"><a class="tuile__lien" href="{lien}.html">{e(titre)}</a></h3>
            <p class="tuile__quoi">{e(quoi)}</p>
            {aussi(liens)}
          </span>
        </article>'''


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


def section(titre, tuiles, zone=False):
    """Pas de numéro : une page n'est pas un exposé. Un titre, un filet, la
    grille — c'est ce que font les sites de référence."""
    classe = "sect sect--zone" if zone else "sect"
    return f'''  <section class="{classe}">
    <div class="contenu">
      <h2 class="tete-bande">{e(titre)}</h2>
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
# Une seule grille. La coupure « l'acte » d'un côté, « le sujet » de l'autre
# faisait lire deux fois la même chose : l'usure et sa réhabilitation, les taches
# et leur infiltration, la couleur et l'éclaircissement. Chaque soin porte donc
# maintenant son acte en titre, et les pages de contexte passent en dessous,
# en liens. Franck, 18/10/2026 : « c'est très redondant entre le 1 et le 2,
# il faut les fondre ».
#
# L'ordre suit le gradient d'économie tissulaire — on regarde, puis on traite
# du plus léger au plus engageant. C'est la doctrine du cabinet, elle devient
# lisible dès la première page.
SOINS = [
    ("Bilan esthétique",
     "Photographies, simulation 2D, 3D ou dynamique.",
     "bilan-esthetique-personnalise", "bilan-esthetique-projet.jpg", "",
     "Projet esthétique dessiné avant traitement",
     [("Dentisterie esthétique : la vue d’ensemble", "dentisterie-esthetique-paris")]),
    ("Éclaircissement",
     "Gouttières personnalisées, peroxyde de carbamide, port nocturne.",
     "eclaircissement-dentaire-paris", "eclaircissement-ambulatoire-apres.jpg", "",
     "Sourire après un éclaircissement ambulatoire",
     [("Un cas documenté", "cas-mih-eclaircissement-erosion-infiltration")]),
    ("Infiltration ICON",
     "Infiltration de résine ou microabrasion, selon la profondeur.",
     "taches-dentaires-dyschromies-icon", "mih-erosion-infiltration-apres.jpg", "",
     "Dents après infiltration de taches de MIH",
     [("Un cas documenté", "cas-mih-eclaircissement-erosion-infiltration")]),
    ("Composite bonding",
     "Résine stratifiée couche après couche, directement sur la dent.",
     "composite-bonding-paris", "composite-bonding-six-dents-anterieures.jpg",
     "center 78%", "Sourire après un composite bonding sur six dents",
     [("Facettes ou composite ?", "facettes-ou-composite")]),
    ("Facettes",
     "Céramique collée, préparation minimale.",
     "facettes-dentaires-paris", "facettes-ceramique-apres.jpg", "",
     "Sourire après la pose de facettes en céramique",
     [("Facettes ou composite ?", "facettes-ou-composite"),
      ("Un cas documenté", "cas-planification-facettes-ceramique")]),
    ("Réhabilitation des dents usées",
     "Composite ou céramique : le matériau vient après le projet.",
     "rehabilitation-dents-usees", "rehabilitation-usure-apres.jpg", "",
     "Sourire après la réhabilitation de dents usées",
     [("Usure dentaire", "usures-dentaires"),
      ("Érosion", "erosion-dentaire"),
      ("Bruxisme", "bruxisme-usure-dentaire"),
      ("Dents courtes", "dents-courtes-usees")]),
    # Pas de photographie ici : le registre des cas n'en documente aucune comme
    # venant d'un patient souffrant d'un trouble du comportement alimentaire.
    # En emprunter une à un autre cas ferait porter un diagnostic psychiatrique
    # à quelqu'un qui ne l'a pas.
    ("Troubles des conduites alimentaires",
     "Dépistage, prévention, coordination, moment restaurateur.",
     "tca-dents", "", "", "",
     [("Anorexie restrictive : érosion sans vomissements",
       "anorexie-erosion-dentaire-sans-vomissements")]),
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
        section("Mon expertise", [acte(*a) for a in SOINS]),
        section("Les cas", [paire(*c) for c in CAS], zone=True),
        f'''  <section class="sect">
    <div class="contenu">
      <h2 class="tete-bande">Le praticien</h2>
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
     "Dépistage, prévention, coordination, moment restaurateur.", "tca-dents", "Lire"),
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
        section("Enseignement et publications",
                [tuile(*t, longue=True) for t in PRO_ENSEIGNEMENT + PRO_TRAVAUX]),
        section("Activité hospitalière",
                [tuile(*t, longue=True) for t in PRO_HOSPITALIER], zone=True),
        section("Les cas", [paire(*c) for c in CAS]),
        f'''  <section class="sect sect--zone">
    <div class="contenu">
      <h2 class="tete-bande">Le praticien</h2>
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
