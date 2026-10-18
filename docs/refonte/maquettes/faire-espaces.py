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
import json
import os
import re

SORTIE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
PHOTOS = "../../../../src/assets/photos/cas/"


def e(t):
    return H.escape(t, quote=False)


def phrases(prefixe):
    """Les phrases que Franck écrit lui-même, dans phrases.txt. Ce fichier est la
    source : ce qui est écrit ici en dur n'est qu'un point de départ, et toute
    ligne du fichier le remplace. Format : « carte.slug = la phrase »."""
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phrases.txt")
    trouvees = {}
    if not os.path.exists(chemin):
        return trouvees
    for ligne in open(chemin, encoding="utf-8"):
        ligne = ligne.rstrip("\n")
        if not ligne.strip() or ligne.lstrip().startswith("#") or "=" not in ligne:
            continue
        cle, _, valeur = ligne.partition("=")
        cle = cle.strip()
        if cle.startswith(prefixe + "."):
            trouvees[cle[len(prefixe) + 1:]] = valeur.strip()
    return trouvees


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
    quoi = phrases("carte").get(lien, quoi)
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


def section(titre, tuiles, zone=False, premier=False):
    """Pas de numéro : une page n'est pas un exposé. Un titre, un filet, la
    grille — c'est ce que font les sites de référence. La première section
    porte le H1 : la page n'a plus de grand titre au-dessus, il faisait
    doublon avec le fil d'Ariane et le menu."""
    classe = "sect sect--zone" if zone else "sect"
    balise = "h1" if premier else "h2"
    tete = f'<{balise} class="tete-bande{" tete-bande--haut" if premier else ""}">{e(titre)}</{balise}>'
    return f'''  <section class="{classe}">
    <div class="contenu">
      {tete}
      <div class="tuiles">
{chr(10).join(tuiles)}
      </div>
    </div>
  </section>'''


def page(slug, titre, description, ariane, sections, jsonld=""):
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

  <p class="ariane ariane--seule"><a href="index.html">Accueil</a> › {e(ariane)}</p>

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
     "Photographies, analyse du sourire, projet.",
     "bilan-esthetique-personnalise", "bilan-esthetique-projet.jpg", "",
     "Projet esthétique dessiné avant traitement",
     [("Dentisterie esthétique : la vue d’ensemble", "dentisterie-esthetique-paris")]),
    ("Éclaircissement",
     "Gouttières à domicile, suivi au cabinet.",
     "eclaircissement-dentaire-paris", "eclaircissement-ambulatoire-apres.jpg", "",
     "Sourire après un éclaircissement ambulatoire",
     [("Un cas documenté", "cas-mih-eclaircissement-erosion-infiltration")]),
    ("Infiltration ICON",
     "Taches blanches, MIH, fluorose. Sans fraise.",
     "taches-dentaires-dyschromies-icon", "mih-erosion-infiltration-apres.jpg", "",
     "Dents après infiltration de taches de MIH",
     [("Un cas documenté", "cas-mih-eclaircissement-erosion-infiltration")]),
    ("Composite bonding",
     "Résine stratifiée sur la dent, en une séance.",
     "composite-bonding-paris", "composite-bonding-six-dents-anterieures.jpg",
     "center 78%", "Sourire après un composite bonding sur six dents",
     [("Facettes ou composite ?", "facettes-ou-composite")]),
    ("Facettes",
     "Céramique collée sur la face visible de la dent.",
     "facettes-dentaires-paris", "facettes-ceramique-apres.jpg", "",
     "Sourire après la pose de facettes en céramique",
     [("Facettes ou composite ?", "facettes-ou-composite"),
      ("Un cas documenté", "cas-planification-facettes-ceramique")]),
    ("Réhabilitation des dents usées",
     "Rendre la hauteur et la fonction.",
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
     "Ce que le chirurgien-dentiste repère en premier.",
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
        section("Mes expertises", [acte(*a) for a in SOINS], premier=True),
        section("Cas cliniques", [paire(*c) for c in CAS], zone=True),
        f'''  <section class="sect">
    <div class="contenu">
      <h2 class="tete-bande">Me rencontrer</h2>
{PRATICIEN}
    </div>
  </section>''',
    ]
    return page(
        "espace-patients",
        "Espace patients | Dr Franck Moyal — dentisterie esthétique à Paris",
        "Facettes, composite bonding, éclaircissement, infiltration ICON, réhabilitation des "
        "dents usées, bilan esthétique : chaque acte a sa page. Dr Franck Moyal, Paris 9e.",
        "Espace patients",
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
        section("Enseignement et publications",
                [tuile(*t, longue=True) for t in PRO_ENSEIGNEMENT + PRO_TRAVAUX],
                premier=True),
        section("Activité hospitalière",
                [tuile(*t, longue=True) for t in PRO_HOSPITALIER], zone=True),
        section("Cas cliniques", [paire(*c) for c in CAS]),
        f'''  <section class="sect sect--zone">
    <div class="contenu">
      <h2 class="tete-bande">Me rencontrer</h2>
{PRO_PRATICIEN}
    </div>
  </section>''',
    ]
    return page(
        "espace-pro",
        "Espace pro | Formations, publications et activité hospitalière — Dr Franck Moyal",
        "Conférences et formations, publications, activité hospitalière à la Pitié-Salpêtrière "
        "et à la CMME de Sainte-Anne, cas documentés : l’espace professionnel du Dr Franck Moyal.",
        "Espace pro",
        sections, garder_jsonld("espace-pro.html"))


# ── Contact ───────────────────────────────────────────────────────────────
# Tout vient de la fiche Google du cabinet, relevée le 18/10/2026, et des deux
# stations de métro indiquées par Franck. Rien n'est inventé.
#
# La page a une hiérarchie, pas une grille : le téléphone domine, parce que
# c'est ainsi que les patients prennent rendez-vous ; le lieu et son plan
# occupent la largeur ; les réseaux viennent ensuite, avec leurs logos ; ce
# qu'il faut apporter ferme la page. Franck, 19/10/2026 : « tu es un
# webdesigner pro », après une première version en cinq boîtes identiques.
TEL_AFFICHE = "01 83 75 52 16"
TEL_LIEN = "tel:+33183755216"
COURRIEL = "drfranckmoyal@gmail.com"
COURRIEL_LIEN = ("mailto:drfranckmoyal@gmail.com"
                 "?subject=Demande%20de%20rendez-vous%20-%20Dr%20Franck%20Moyal")
ADRESSE_1, ADRESSE_2 = "2 rue Hippolyte Lebas", "75009 Paris"
LAT, LON = 48.8770687, 2.3417544
ITINERAIRE = f"https://www.google.com/maps/dir/?api=1&destination={LAT},{LON}"
# Plan interactif OpenStreetMap : zoom et déplacement, sans clé et sans cookie
# de pistage — un plan Google exigerait une bannière de consentement.
PLAN_EMBED = ("https://www.openstreetmap.org/export/embed.html"
              f"?bbox={LON-0.006},{LAT-0.0032},{LON+0.006},{LAT+0.0032}"
              f"&layer=mapnik&marker={LAT},{LON}")
HORAIRES = [("Mardi", "9 h – 19 h"), ("Vendredi", "9 h – 19 h")]
ACCES = [("Cadet", "ligne 7"), ("Notre-Dame-de-Lorette", "ligne 12")]

# Logos officiels, tracés monochromes (jeu Simple Icons, licence CC0).
LOGOS = {
    "Instagram": "M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z",
    "LinkedIn": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
    "TikTok": "M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z",
}
RESEAUX = [("Instagram", "@drfranckmoyal", "https://www.instagram.com/drfranckmoyal/"),
           ("LinkedIn", "Franck Moyal", "https://www.linkedin.com/in/franck-moyal-7581b6161/"),
           ("TikTok", "@drfranckmoyal", "https://www.tiktok.com/@drfranckmoyal")]


def logo(nom):
    return (f'<svg class="logo" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'<path d="{LOGOS[nom]}"/></svg>')


def jsonld_contact():
    """Les données structurées de la page, enrichies de ce que la fiche Google
    nous a appris : horaires et coordonnées sur le nœud Dentist. C'est ce que
    Google et les IA lisent pour répondre « est-ce ouvert ? où ? »."""
    brut = garder_jsonld("contact.html")
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', brut, re.S)
    if not m:
        return brut
    try:
        d = json.loads(m.group(1))
    except Exception:
        return brut
    for n in d.get("@graph", []):
        if n.get("@type") == "Dentist":
            n["openingHoursSpecification"] = [{
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Tuesday", "Friday"],
                "opens": "09:00", "closes": "19:00"}]
            n["geo"] = {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON}
            n["hasMap"] = ITINERAIRE
            n["sameAs"] = [u for _, _, u in RESEAUX]
    return ('<script type="application/ld+json">'
            + json.dumps(d, ensure_ascii=False) + "</script>")


def contact():
    jours = "".join(f'<span><b>{e(j)}</b> {e(h)}</span>' for j, h in HORAIRES)
    acces = " · ".join(f'{e(s)} <span class="lieu__ligne">{e(l)}</span>' for s, l in ACCES)
    reseaux = "\n".join(
        f'''        <li><a class="reseau" href="{u}" target="_blank" rel="noopener">
          {logo(n)}
          <span class="reseau__nom">{e(n)}</span>
          <span class="reseau__compte">{e(c)}</span>
        </a></li>''' for n, c, u in RESEAUX)

    page_html = f'''  <section class="sect">
    <div class="contenu">
      <h1 class="tete-bande tete-bande--haut">Prendre rendez-vous</h1>

      <div class="prise">
        <div class="prise__appel">
          <p class="prise__sur">Par téléphone, le plus simple</p>
          <a class="prise__numero" href="{TEL_LIEN}">{e(TEL_AFFICHE)}</a>
          <p class="prise__quand">{jours}<span class="prise__ferme">Fermé les autres jours</span></p>
        </div>
        <div class="prise__ecrire">
          <p class="prise__sur">Une question avant de venir</p>
          <a class="prise__mail" href="{COURRIEL_LIEN}">{e(COURRIEL)}</a>
          <p class="prise__note">Pour un rendez-vous, préférez le téléphone : la réponse est
            immédiate.</p>
        </div>
      </div>

      <div class="lieu">
        <div class="lieu__texte">
          <p class="eyebrow">Le cabinet</p>
          <p class="lieu__adresse">{e(ADRESSE_1)}<br>{e(ADRESSE_2)}</p>
          <p class="lieu__acces"><b>Métro</b> {acces}</p>
          <a class="bouton-encre" href="{ITINERAIRE}" target="_blank" rel="noopener">Itinéraire <span class="ext">↗</span></a>
        </div>
        <div class="lieu__plan">
          <iframe src="{PLAN_EMBED}" title="Plan : 2 rue Hippolyte Lebas, Paris 9e"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </div>
  </section>

  <section class="sect sect--zone">
    <div class="contenu">
      <h2 class="tete-bande">Dr Franck Moyal sur les réseaux</h2>
      <ul class="reseaux">
{reseaux}
      </ul>
    </div>
  </section>

  <section class="sect">
    <div class="contenu">
      <h2 class="tete-bande">Avant votre consultation</h2>
      <div class="chapitre chapitre--plein">
        <div>
          <p>Aucun document n’est obligatoire pour demander un premier rendez-vous.
            Selon le motif, il peut être utile d’apporter :</p>
          <ul>
            <li>les radiographies ou examens récents dont vous disposez ;</li>
            <li>d’anciennes photographies du sourire lorsqu’une évolution des usures
              est recherchée ;</li>
            <li>la liste de vos traitements médicaux lorsque cela peut influencer la
              prise en charge.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>'''

    return page(
        "contact",
        "Contact et rendez-vous | Dr Franck Moyal Paris 9",
        "Prendre rendez-vous avec le Dr Franck Moyal : 2 rue Hippolyte Lebas, 75009 "
        "Paris, 01 83 75 52 16. Cabinet ouvert le mardi et le vendredi de 9 h à 19 h.",
        "Contact", [page_html], jsonld_contact())


if __name__ == "__main__":
    # On calcule chaque page AVANT d'ouvrir son fichier : « open(..., "w") »
    # vide le fichier sur-le-champ, et ces fonctions relisent leur propre
    # page pour en garder les données structurées. Dans l'autre ordre, elles
    # relisaient un fichier vide — c'est ainsi que les horaires se perdaient.
    for nom, fabrique in (("espace-patients.html", patients),
                          ("espace-pro.html", pro),
                          ("contact.html", contact)):
        contenu = fabrique()
        with open(os.path.join(SORTIE, nom), "w", encoding="utf-8") as fh:
            fh.write(contenu)
    print("espace-patients, espace-pro et contact refaits")
