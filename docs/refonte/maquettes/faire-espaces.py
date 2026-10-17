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


def acte(titre, quoi, lien):
    """La carte d'un acte : son nom, en grand, et rien qui le dilue."""
    return f'''        <a class="tuile tuile--acte" href="{lien}.html">
          <h3 class="tuile__acte">{e(titre)}</h3>
          <p class="tuile__quoi">{e(quoi)}</p>
          <span class="tuile__fleche">L’acte en détail <span>→</span></span>
        </a>'''


def tuile(titre, quoi, lien, verbe="Lire", externe=False):
    if externe:
        return f'''        <a class="tuile" href="{lien}" target="_blank" rel="noopener">
          <h3 class="tuile__titre">{e(titre)} <span class="ext">↗</span></h3>
          <p class="tuile__quoi">{e(quoi)}</p>
          <span class="tuile__fleche">{e(verbe)} <span>→</span></span>
        </a>'''
    return f'''        <a class="tuile" href="{lien}.html">
          <h3 class="tuile__titre">{e(titre)}</h3>
          <p class="tuile__quoi">{e(quoi)}</p>
          <span class="tuile__fleche">{e(verbe)} <span>→</span></span>
        </a>'''


def paire(titre, quoi, lien, avant, apres):
    return f'''        <a class="tuile tuile--cas" href="{lien}.html">
          <span class="tuile__paire">
            <img src="{PHOTOS}{avant}" alt="Avant" loading="lazy"><img src="{PHOTOS}{apres}" alt="Après" loading="lazy">
          </span>
          <h3 class="tuile__titre">{e(titre)}</h3>
          <p class="tuile__quoi">{e(quoi)}</p>
          <span class="tuile__fleche">Voir le cas <span>→</span></span>
        </a>'''


def section(rang, titre, phrase, tuiles, zone=False):
    classe = "sect sect--zone" if zone else "sect"
    return f'''  <section class="{classe}">
    <div class="contenu">
      <div class="tete-rang">
        <p class="rang">{rang}</p>
        <div>
          <h2>{e(titre)}</h2>
          <p class="doux">{e(phrase)}</p>
        </div>
      </div>
      <div class="tuiles">
{chr(10).join(tuiles)}
      </div>
    </div>
  </section>'''


def page(slug, titre, description, ariane, eyebrow, h1, chapo, sections, jsonld=""):
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
      <p class="chapo">{e(chapo)}</p>
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
ACTES = [
    ("Facettes",
     "Des céramiques fines, conçues puis collées sur la face visible de la dent.",
     "facettes-dentaires-paris"),
    ("Composite bonding",
     "De la résine stratifiée directement sur la dent, en une séance, sans la tailler.",
     "composite-bonding-paris"),
    ("Éclaircissement",
     "Le protocole en gouttières : la durée, les limites, les précautions.",
     "eclaircissement-dentaire-paris"),
    ("Infiltration ICON",
     "Le traitement des taches blanches, de la MIH et des dyschromies, sans fraise.",
     "taches-dentaires-dyschromies-icon"),
    ("Réhabilitation des dents usées",
     "Rendre la hauteur et la fonction à une bouche usée, en gardant la dent.",
     "rehabilitation-dents-usees"),
    ("Bilan esthétique",
     "La consultation qui précède tout le reste : ce que l’on regarde, et dans quel ordre.",
     "bilan-esthetique-personnalise"),
]

# Deux pages qui ne sont pas des actes mais aident à choisir entre eux.
POUR_CHOISIR = [
    ("Dentisterie esthétique",
     "La vue d’ensemble : comment choisir un praticien, et entre quels actes choisir.",
     "dentisterie-esthetique-paris", "La vue d’ensemble"),
    ("Facettes ou composite ?",
     "Les deux comparés point par point : tenue, teinte, réparabilité, entretien, coût en dent.",
     "facettes-ou-composite", "Comparer"),
]

# Les sujets cliniques : ce que les actes traitent.
SUJETS = [
    ("Usure dentaire",
     "Pourquoi l’usure s’installe, comment on la mesure, et quand il faut agir.",
     "usures-dentaires"),
    ("Érosion dentaire",
     "L’acide dissout l’émail sans que rien ne frotte : origines et prévention.",
     "erosion-dentaire"),
    ("Bruxisme",
     "Serrement et grincement : ce qu’ils usent, et ce qui les calme.",
     "bruxisme-usure-dentaire"),
    ("Dents courtes ou usées",
     "Usure du bord, gencive trop basse, ou les deux : on ne traite pas pareil.",
     "dents-courtes-usees"),
    ("Troubles des conduites alimentaires",
     "Anorexie, boulimie : les atteintes bucco-dentaires, et leur dépistage.",
     "tca-dents"),
    ("Anorexie restrictive",
     "Un mécanisme peu décrit : l’érosion peut s’installer sans vomissements.",
     "anorexie-erosion-dentaire-sans-vomissements"),
]

# Chaque vignette est prise DANS la page vers laquelle elle mène : sinon on
# montre un cas et on en ouvre un autre.
CAS = [
    ("Usures antérieures et facettes",
     "Du diagnostic aux facettes minimalement invasives, étape par étape.",
     "cas-usures-dentaires-facettes-minimalement-invasives",
     "rehabilitation-usure-avant.jpg", "rehabilitation-usure-apres.jpg"),
    ("Réhabilitation par vingt facettes",
     "Un projet dessiné et essayé en bouche avant la moindre préparation.",
     "cas-planification-rehabilitation-facettes",
     "bilan-esthetique-initial.jpg", "bilan-esthetique-resultat.jpg"),
    ("Quatre facettes céramique",
     "La planification numérique, puis le résultat posé.",
     "cas-planification-facettes-ceramique",
     "facettes-planification-initial.jpg", "facettes-planification-resultat.jpg"),
    ("Taches de MIH",
     "Éclaircissement d’abord, infiltration ensuite : rien n’est taillé.",
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
              dentisterie esthétique et adhésive. Praticien hospitalier à la Pitié-Salpêtrière
              depuis 2012 et à la CMME de Sainte-Anne depuis 2024, où il conduit la consultation
              dentaire des troubles du comportement alimentaire.</p>
            <span class="tuile__fleche">Son parcours <span>→</span></span>
          </span>
        </a>
        <a class="tuile" href="chirurgien-dentiste-paris-9.html">
          <h3 class="tuile__titre">Le cabinet, Paris 9<sup>e</sup></h3>
          <p class="tuile__quoi">2 rue Hippolyte Lebas, 75009 Paris. Comment venir, comment se
            passe une première consultation.</p>
          <span class="tuile__fleche">Voir <span>→</span></span>
        </a>
        <a class="tuile" href="contact.html">
          <h3 class="tuile__titre">Prendre rendez-vous</h3>
          <p class="tuile__quoi">Par téléphone au 01 83 75 52 16, ou par courriel. Les horaires
            et ce qu’il faut apporter.</p>
          <span class="tuile__fleche">Nous écrire <span>→</span></span>
        </a>
      </div>'''


def patients():
    sections = [
        section("1", "Les actes",
                "Chaque acte a sa page : ce qu’il fait, ce qu’il coûte en tissu dentaire, "
                "combien de séances, et ce qu’il ne fait pas.",
                [acte(t, q, l) for t, q, l in ACTES] +
                [tuile(*p) for p in POUR_CHOISIR]),
        section("2", "Ce que l’on traite",
                "Les sujets cliniques derrière ces actes. Ce que vous voyez sur vos dents "
                "est expliqué en ouverture de la page qui le concerne.",
                [tuile(t, q, l) for t, q, l in SUJETS], zone=True),
        section("3", "Des cas, en photographies",
                "Quatre cas du cabinet suivis de bout en bout. Photographies réelles, "
                "sans retouche de couleur ni de netteté.",
                [paire(*c) for c in CAS]),
        f'''  <section class="sect sect--zone">
    <div class="contenu">
      <div class="tete-rang">
        <p class="rang">4</p>
        <div>
          <h2>Le praticien et le cabinet</h2>
          <p class="doux">Qui vous recevra, où, et comment le joindre.</p>
        </div>
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
        "Les actes d’abord, parce que c’est ce que l’on cherche. Puis ce qu’ils traitent, "
        "des cas en photographies, et qui vous recevra.",
        sections, garder_jsonld("espace-patients.html"))




# ── Espace pro ────────────────────────────────────────────────────────────
PRO_ENSEIGNEMENT = [
    ("Conférences et formations",
     "Enseignement clinique autour de la dentisterie esthétique, des composites, "
     "de la planification et des usures.", "conferences-formations", "Le détail"),
    ("Smile Club Formations",
     "L’organisme de formation : le calendrier, les sessions et les inscriptions.",
     "https://smileclubformations.com/", "Le site", True),
]

PRO_TRAVAUX = [
    ("Publications et travaux",
     "Articles, ouvrages et travaux académiques : six publications, sept thèses "
     "encadrées, Le Fil Dentaire, les Ouvrages CdP.", "publications", "La liste"),
    ("Médias et interviews",
     "Entretiens, articles et ressources externes permettant de retrouver les "
     "thèmes qui structurent la pratique.", "medias-interviews", "Les parutions"),
]

PRO_HOSPITALIER = [
    ("Activité hospitalière",
     "Pitié-Salpêtrière depuis 2012, CMME de Sainte-Anne depuis 2024 : diagnostic, "
     "prévention, adaptation du soin et coordination.", "activite-hospitaliere", "Le détail"),
    ("TCA et santé bucco-dentaire",
     "Anorexie, boulimie : l’érosion que les complications dentaires révèlent, "
     "et ce que le chirurgien-dentiste peut repérer en premier.", "tca-dents", "Lire"),
    ("Anorexie et érosion sans vomissements",
     "Un mécanisme peu décrit : l’érosion peut s’installer sans conduite de purge.",
     "anorexie-erosion-dentaire-sans-vomissements", "Lire"),
]

PRO_PRATICIEN = '''      <div class="tuiles tuiles--praticien">
        <a class="tuile tuile--large" href="franck-moyal.html">
          <img class="tuile__portrait" src="img/portrait-fm.png?v=0"
               alt="Dr Franck Moyal, chirurgien-dentiste à Paris">
          <span class="tuile__texte">
            <h3 class="tuile__titre">Dr Franck Moyal</h3>
            <p class="tuile__quoi">Chirurgien-dentiste à Paris 9<sup>e</sup>, exercice exclusif en
              dentisterie esthétique et adhésive. Praticien hospitalier à la Pitié-Salpêtrière
              et à la CMME de Sainte-Anne, président de DenTCA. Formation initiale, diplômes,
              responsabilités hospitalières et universitaires.</p>
            <span class="tuile__fleche">Son parcours <span>→</span></span>
          </span>
        </a>
        <a class="tuile" href="contact.html">
          <h3 class="tuile__titre">Échanger sur un cas</h3>
          <p class="tuile__quoi">Pour une question clinique, une intervention ou une
            collaboration : 01 83 75 52 16, ou par courriel.</p>
          <span class="tuile__fleche">Me contacter <span>→</span></span>
        </a>
        <a class="tuile" href="chirurgien-dentiste-paris-9.html">
          <h3 class="tuile__titre">Le cabinet, Paris 9<sup>e</sup></h3>
          <p class="tuile__quoi">2 rue Hippolyte Lebas, 75009 Paris. Le plateau technique et
            l’organisation des séances.</p>
          <span class="tuile__fleche">Voir <span>→</span></span>
        </a>
      </div>'''


def pro():
    sections = [
        section("1", "Enseignement et formation",
                "Ce que j’enseigne, et où.",
                [tuile(*t) for t in PRO_ENSEIGNEMENT]),
        section("2", "Travaux publiés",
                "Articles, ouvrages, thèses encadrées et interventions dans la presse "
                "professionnelle.",
                [tuile(*t) for t in PRO_TRAVAUX], zone=True),
        section("3", "Activité hospitalière et troubles alimentaires",
                "Le sujet sur lequel je travaille à l’hôpital, et que la profession "
                "regarde encore peu.",
                [tuile(*t) for t in PRO_HOSPITALIER]),
        section("4", "Des cas documentés de bout en bout",
                "Diagnostic, planification, exécution et résultat — sans sauter les "
                "étapes intermédiaires.",
                [paire(*c) for c in CAS], zone=True),
        f'''  <section class="sect">
    <div class="contenu">
      <div class="tete-rang">
        <p class="rang">5</p>
        <div>
          <h2>Le praticien et le contact</h2>
          <p class="doux">Qui je suis, où j’exerce, et comment me joindre.</p>
        </div>
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
        "Tout l’espace professionnel, rangé en cinq temps : l’enseignement, les travaux publiés, "
        "l’activité hospitalière, des cas documentés, et comment me joindre.",
        sections, garder_jsonld("espace-pro.html"))


if __name__ == "__main__":
    open(os.path.join(SORTIE, "espace-patients.html"), "w",
         encoding="utf-8").write(patients())
    open(os.path.join(SORTIE, "espace-pro.html"), "w",
         encoding="utf-8").write(pro())
    print("espace-patients.html et espace-pro.html refaits en sommaires")
