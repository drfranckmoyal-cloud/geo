#!/usr/bin/env python3
"""
Compose une page de la refonte en chapitres, à partir du site actuel.

Le générateur voisin (generer.py) refait la mise en page sans toucher au découpage :
une page à douze titres en garde douze. Ce composeur-ci va plus loin — il regroupe
les sections en quatre ou cinq chapitres — mais il a besoin qu'on lui dise lesquelles
vont ensemble. Ce jugement est dans PLANS, en bas du fichier.

Ce qu'il fait tout seul, et qui m'avait échappé à la main sur les deux premières pages :

  · il repère les phrases qui annoncent une liste (« L'esthétique dépend notamment : »)
    et les garde collées à leur liste, où qu'elle aille ;
  · il apparie les sous-titres d'une section avec leurs paragraphes ;
  · il récupère les tableaux, que l'extraction par paragraphes ignorait ;
  · il reprend la description pour Google, les sources avec leurs DOI, et les liens ;
  · il compare ensuite, mot à mot, sa page à la page d'origine, et signale ce qui
    manque. C'est ce contrôle qui compte : sans lui, on perd du texte sans le voir.

    python3 docs/refonte/maquettes/composer.py            toutes les pages prévues
    python3 docs/refonte/maquettes/composer.py erosion-dentaire
"""
import html as H
import importlib.util
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DIST = os.path.join(RACINE, "dist")
SORTIE = os.path.join(RACINE, "docs", "refonte", "maquettes", "site")
# le portrait change de fichier : on le signe pour contourner le cache
PORTRAIT = "img/portrait-fm.png?v=" + str(int(os.path.getmtime(
    os.path.join(SORTIE, "img", "portrait-fm.png"))))

spec = importlib.util.spec_from_file_location(
    "gen", os.path.join(os.path.dirname(os.path.abspath(__file__)), "generer.py"))
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

MEUBLE = ("dr franck moyal — chirurgien", "mis à jour le", "voir les ", "dentisterie esthétique et adhésive, usures")

# Le diagnostic des usures a été fondu dans la page Usures (D77) : tout lien qui
# le visait doit mener là, sinon il tombe sur une page qui n'existe plus.
FONDUES = {"diagnostic-usures-dentaires": "usures-dentaires"}


# ── lecture ───────────────────────────────────────────────────────────────────
# Un numéro de téléphone et une adresse e-mail doivent rester cliquables : sur
# un téléphone, c'est la seule façon d'appeler le cabinet d'un geste. Le site en
# ligne les porte ; la mise en page les effaçait avec le reste du balisage.
_APPEL = re.compile(r'<a\b[^>]*href="((?:tel|mailto):[^"]+)"[^>]*>(.*?)</a>', re.S)


def _mettre_de_cote(frag):
    gardes = []

    def prendre(m):
        gardes.append((m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()))
        return "\x00%d\x00" % (len(gardes) - 1)

    return _APPEL.sub(prendre, frag), gardes


def _remettre(frag, gardes):
    for i, (ou, quoi) in enumerate(gardes):
        frag = frag.replace("\x00%d\x00" % i, '<a href="%s">%s</a>' % (ou, quoi))
    return frag


def nu(x, garder_gras=True):
    gardes = []
    if garder_gras:                      # on ne protège pas pour le contrôle de texte
        x, gardes = _mettre_de_cote(x)
    x = re.sub(r"<(script|style)\b.*?</\1>", "", x, flags=re.S)
    x = re.sub(r'<sup[^>]*class="cite"[^>]*>.*?</sup>', "", x, flags=re.S)
    x = re.sub(r"<span[^>]*visually-hidden[^>]*>.*?</span>", "", x, flags=re.S)
    x = re.sub(r"<(?!/?(strong|em)\b)[^>]+>", " ", x) if garder_gras else re.sub(r"<[^>]+>", " ", x)
    x = re.sub(r"\s+data-astro-cid-\w+", "", x)
    return _remettre(re.sub(r"\s+", " ", x).strip(), gardes)


def lire(slug):
    chemin = slug.replace("cas-", "cas-cliniques/", 1) if slug.startswith("cas-") else slug
    brut = open(os.path.join(DIST, chemin, "index.html"), encoding="utf-8").read()
    main = re.search(r"<main.*?</main>", brut, re.S).group(0)
    p = {"slug": slug, "main": main, "brut": brut}
    p["titre"] = H.unescape(re.search(r"<title>(.*?)</title>", brut, re.S).group(1).strip())
    d = re.search(r'<meta name="description" content="([^"]*)"', brut)
    p["description"] = H.unescape(d.group(1)) if d else ""
    p["h1"] = nu(re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S).group(1))

    # où mène chaque libellé de lien, pour les refaire pointer dans la maquette
    p["liens"] = {}
    for href, lib in re.findall(r'<a[^>]*href="(/[^"#?]+/)"[^>]*>(.*?)</a>', main, re.S):
        lib = nu(lib, False)
        if lib and len(lib) < 90:
            cible = href.strip("/").replace("cas-cliniques/", "cas-")
            p["liens"].setdefault(lib, FONDUES.get(cible, cible))

    # Le bandeau d'ouverture n'est pas une <section> : son paragraphe de réponse,
    # qui est le vrai chapô de la page, n'était lu nulle part.
    tete = main.split("<section", 1)[0]
    p["tete"] = [x for x in (nu(y) for y in re.findall(r"<p[^>]*>(.*?)</p>", tete, re.S))
                 if len(x) > 18 and not any(x.lower().startswith(m) for m in MEUBLE)]
    # Le bloc « answer » — la réponse directe à la question du titre — est un div
    # posé entre deux <section>. Ni la tête ni les sections ne le voyaient.
    dans_sections = "".join(re.findall(r"<section[^>]*>.*?</section>", main, re.S))
    p["figures_libres"] = []
    for fig in re.findall(r"<figure.*?</figure>", main, re.S):
        if fig in dans_sections:
            continue
        srcs = re.findall(r'\bsrc="(/_astro/[^"]+\.(?:webp|jpg|png))"', fig)
        alts = re.findall(r'\balt="([^"]*)"', fig)
        cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", fig, re.S)
        if srcs:
            p["figures_libres"].append({"src": [gen.locale(x) for x in srcs[:2]],
                                        "alt": [H.unescape(a) for a in alts[:2]] or [""],
                                        "legende": nu(cap.group(1), False) if cap else ""})

    men = re.search(r'<div[^>]*class="[^"]*pack-mention[^"]*"[^>]*>(.*?)</div>', main, re.S)
    p["mention"] = nu(men.group(1)) if men else ""

    for rep in re.findall(r'<div[^>]*class="answer"[^>]*>(.*?)</div>', main, re.S):
        t = nu(rep)
        if len(t) > 40 and t not in p["tete"]:
            p["tete"].append(t)

    p["sections"] = []
    for sec in re.findall(r"<section[^>]*>.*?</section>", main, re.S):
        ti = re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S)
        # L'encart de l'ancien site qui annonçait un cas clinique (vignettes, titre, phrase,
        # lien) s'aplatissait en deux phrases orphelines et perdait son lien, trop long pour
        # « À lire aussi ». Il devient une ligne de renvoi vers la page du cas.
        annonces = [{"titre": nu(m.group(1)), "texte": nu(m.group(2)),
                     "cible": m.group(3).strip("/").replace("cas-cliniques/", "cas-")}
                    for m in re.finditer(r'<p class="annonce__probleme"[^>]*>(.*?)</p>\s*'
                                         r'<p class="annonce__approche"[^>]*>(.*?)</p>\s*'
                                         r'<a href="([^"]+)"', sec, re.S)]
        sans_annonce = re.sub(r'<p class="annonce__(?:probleme|approche)"[^>]*>.*?</p>', "", sec, flags=re.S)
        paras = [nu(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", sans_annonce, re.S)]
        paras = [x for x in paras if len(x) > 18 and not any(x.lower().startswith(m) for m in MEUBLE)]
        lis = [nu(x) for x in re.findall(r"<li[^>]*>(.*?)</li>", sec, re.S)]
        lis = [x for x in lis if 8 < len(x) < 240]
        tbl = re.search(r"<table.*?</table>", sec, re.S)
        figures = []
        for fig in re.findall(r"<figure.*?</figure>", sec, re.S):
            srcs = re.findall(r'\bsrc="(/_astro/[^"]+\.(?:webp|jpg|png))"', fig)
            alts = re.findall(r'\balt="([^"]*)"', fig)
            cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", fig, re.S)
            if srcs:
                figures.append({"src": [gen.locale(x) for x in srcs[:2]],
                                "alt": [H.unescape(a) for a in alts[:2]] or [""],
                                "legende": nu(cap.group(1), False) if cap else ""})
        p["sections"].append({
            "titre": nu(ti.group(1)) if ti else "",
            "p": paras,
            "li": [x for x in lis if x not in p["liens"]],
            "renvois": [x for x in lis if x in p["liens"]],
            "h3": [nu(x) for x in re.findall(r"<h3[^>]*>(.*?)</h3>", sec, re.S)],
            "table": tbl.group(0) if tbl else None,
            "figures": figures,
            "annonces": annonces,
            "faq": "faq__item" in sec,
            "sources": "source__ref" in sec or "source__n" in sec,
        })
    return p


# ── fabrication ───────────────────────────────────────────────────────────────
def e(s):
    out = H.escape(s, quote=False)
    for t in ("strong", "em"):
        out = out.replace(f"&lt;{t}&gt;", f"<{t}>").replace(f"&lt;/{t}&gt;", f"</{t}>")
    # Les liens d'appel portent un attribut : la liste blanche ci-dessus, qui ne
    # connaît que les balises nues, les laissait échappés et donc affichés en clair.
    out = re.sub(r'&lt;a href="((?:tel|mailto):[^"]+)"&gt;(.*?)&lt;/a&gt;',
                 lambda m: '<a href="%s">%s</a>' % (m.group(1).replace("&amp;", "&"),
                                                    m.group(2)),
                 out, flags=re.S)
    return out


def amorce(sec):
    """La phrase qui annonce une liste doit rester collée à elle."""
    for x in sec["p"]:
        if x.rstrip().endswith(":") and len(x) < 110:
            return x
    return None


def renvois(p, sec):
    if not sec["renvois"]:
        return ""
    liens = " · ".join(f'<a href="{p["liens"][l]}.html">{e(l)}</a>' for l in sec["renvois"])
    return f'\n          <p class="suite">{liens}</p>'


def bloc(p, i, avec_liste, titre=None):
    """Une section devient un bloc : son titre en sous-partie, ses paragraphes,
       ses sous-titres appariés, et sa liste si elle ne part pas en encadré."""
    s = p["sections"][i]
    # La phrase d'annonce ne suit sa liste que si celle-ci part en encadré ;
    # sinon elle reste dans le texte, sans quoi elle disparaissait purement.
    a = amorce(s) if (s["li"] and not avec_liste) else None
    tete = f'<h3>{e(titre if titre is not None else s["titre"])}</h3>\n          ' if (titre or s["titre"]) else ""
    morceaux = []
    if s["h3"] and len(s["h3"]) <= len(s["p"]):
        # sous-titres appariés à leurs paragraphes
        reste = [x for x in s["p"] if x != a]
        for k, t3 in enumerate(s["h3"]):
            txt = reste[k] if k < len(reste) else ""
            if txt.startswith(t3):
                txt = txt[len(t3):].strip()
            morceaux.append(f'<h4 style="font-family:var(--serif);font-size:.95rem;margin:.7rem 0 .25rem">{e(t3)}</h4><p>{e(txt)}</p>')
        for x in reste[len(s["h3"]):]:
            morceaux.append(f"<p>{e(x)}</p>")
    else:
        morceaux = [f"<p>{e(x)}</p>" for x in s["p"] if x != a]
    corps = "\n          ".join(morceaux)
    liste = ""
    if avec_liste and s["li"]:
        puces = "\n              ".join(f"<li>{e(x)}</li>" for x in s["li"])
        intro = f'<p>{e(a)}</p>\n          ' if a else ""
        liste = f'\n          {intro}<ul class="puces">\n              {puces}\n          </ul>'
    photos = ""
    if s["figures"]:
        cartes = []
        for fg in s["figures"]:
            alts = fg["alt"] + [""] * 2
            if len(fg["src"]) >= 2:
                im = "".join(f'<img src="{x}" alt="{H.escape(alts[k])}" loading="lazy">'
                             for k, x in enumerate(fg["src"][:2]))
                dedans, cls = f'<div class="paire">{im}</div>', "paire"
            else:
                dedans, cls = (f'<img src="{fg["src"][0]}" alt="{H.escape(alts[0])}" loading="lazy">', "solo")
            leg = f'<figcaption>{e(fg["legende"])}</figcaption>' if fg["legende"] else ""
            cartes.append(f'<figure class="{cls}">{dedans}{leg}</figure>')
        photos = f'\n          <div class="cas">{"".join(cartes)}</div>'

    tableau = ""
    if s["table"]:
        cols = len(re.findall(r"<th[^>]*>", s["table"].split("</thead>")[0])) if "</thead>" in s["table"] else 3
        t = re.sub(r'<span[^>]*class="cmp__col"[^>]*>.*?</span>', "", s["table"], flags=re.S)
        t = re.sub(r"\s+data-astro-cid-\w+", "", t)
        tableau = f'\n          <div class="tableau{" tableau--duo" if cols <= 2 else ""}">{t}</div>'
    cas = "".join(
        f'\n          <p class="renvoi-cas"><span class="renvoi-cas__eti">Cas clinique</span>'
        f'<a href="{x["cible"]}.html">{e(x["titre"])}</a>'
        f'<span class="renvoi-cas__txt">{e(x["texte"])}</span></p>'
        for x in s.get("annonces", []))
    return f'        <div class="bloc">\n          {tete}{corps}{liste}{tableau}{photos}{cas}{renvois(p, p["sections"][i])}\n        </div>'


def fiche(p, sections):
    morceaux = []
    for i in sections:
        s = p["sections"][i]
        if not s["li"]:
            continue
        a = amorce(s)
        court = a and len(a.rstrip(" :")) <= 52
        titre = (a.rstrip(" :") if court else s["titre"])[:52]
        annonce = f'        <p style="margin:0 0 .5rem">{e(a)}</p>\n' if (a and not court) else ""
        puces = "\n            ".join(f"<li>{e(x)}</li>" for x in s["li"])
        morceaux.append(f'        <h4{" style=\"margin-top:1rem\"" if morceaux else ""}>{e(titre)}</h4>\n'
                        f'{annonce}        <ul>\n            {puces}\n        </ul>')
    return "\n".join(morceaux)



# ── parcours en images ────────────────────────────────────────────────────
# Une suite de photographies légendées, posée entre deux chapitres. Les légendes
# sont celles que Franck a écrites dans les noms de fichiers (orthographe reprise),
# les photographies celles du dossier « PHOTOS SITE - par theme » (19/10/2026).
SEQUENCES = {
    # Trois cas d'éclaircissement, en montages avant/après pleine largeur.
    "eclaircissement-dentaire-paris": {
        "titre": "Avant / après",
        "apres_chapitre": 2,
        "large": True,
        "etapes": [
            ("eclaircissement-cas-1-avant-apres.jpg",
             "Cas 1 — éclaircissement préalable au traitement d’une tache blanche sur l’incisive centrale",
             "Avant et après éclaircissement préalable au traitement d’une tache blanche, sourire de face",
             ("tache blanche", "taches-dentaires-dyschromies-icon")),   # le pont vers ICON
            ("eclaircissement-cas-2-avant-apres.jpg",
             "Cas 2 — éclaircissement avant réhabilitation de l’harmonie du sourire",
             "Avant et après éclaircissement, avant réhabilitation du sourire, vue intra-orale avec écarteurs",
             ("réhabilitation de l’harmonie du sourire", "dentisterie-esthetique-paris")),
            ("eclaircissement-cas-3-avant-apres.jpg",
             "Cas 3 — éclaircissement et remplacement d’une dent manquante due à une agénésie",
             "Avant et après : éclaircissement et remplacement d’une dent manquante, sourire de face"),
        ],
    },
    "taches-dentaires-dyschromies-icon": {"titre": "Avant / après", "apres_chapitre": 3, "large": True, "etapes": [
        ("icon-cas-1-avant-apres.jpg",
         "Cas 1 — plusieurs taches profondes dues à une MIH sévère : résultat après "
         "érosion-infiltration par ICON",
         "Avant et après érosion-infiltration : taches de MIH sur les incisives, puis émail uniforme, sur fond noir"),
        ("icon-cas-2-avant-apres.jpg",
         "Cas 2 — dyschromie après un choc sur 11, associée à une tache blanche de MIH : "
         "résultat après éclaircissement unitaire sur 11 et érosion-infiltration ICON de la tache",
         "Avant et après : incisive assombrie portant une tache blanche, puis teinte et tache corrigées, sur fond noir",
         ("éclaircissement", "eclaircissement-dentaire-paris")),
    ]},
    "composite-bonding-paris": {"titre": "Avant / après", "apres_chapitre": 3, "large": True, "etapes": [
        ("composite-rehabilitation-avant-apres.jpg",
         "Cas 1 — demande de réhabilitation du sourire sans facettes : composite direct sur les six "
         "dents antérieures, sans préparation",
         "Avant et après : dents antérieures usées et colorées, puis reconstruites en composite, sourire de face",
         ("facettes", "facettes-dentaires-paris")),
        ("composite-diasteme-avant-apres.jpg",
         "Cas 2 — demande d’uniformisation et de fermeture naturelle du diastème antérieur : fermeture "
         "du diastème au composite et allongement des incisives latérales",
         "Avant et après : espace entre les incisives centrales, puis fermé en composite, sourire de face"),
    ]},
    # Facettes (25/10/2026) : deux cas vus avec écarteurs, chaque après calé sur son avant.
    "facettes-dentaires-paris": {"titre": "Avant / après", "apres_chapitre": 3, "large": True, "etapes": [
        ("facettes-diastemes-avant-apres.jpg",
         "Cas 1 — espaces entre les dents antérieures, refermés par des facettes : vue avec écarteurs",
         "Avant et après facettes, vue intra-orale avec écarteurs : espaces entre les dents, puis refermés"),
        ("facettes-fractures-avant-apres.jpg",
         "Cas 2 — bords des incisives fracturés et usés : forme et longueur rendues par des facettes",
         "Avant et après facettes, vue avec écarteurs : incisives fracturées et usées, puis reconstruites"),
    ]},
    "_exemple_desactive": {
        "titre": "Le bilan, en quatre étapes",
        "apres_chapitre": 1,
        "etapes": [
            ("bilan-parcours-1-photographies.jpg",
             "Un bilan photographique est réalisé à chaque première consultation.",
             "Le praticien photographie le sourire d’une patiente au cabinet"),
            ("bilan-parcours-2-planification.jpg",
             "La forme des dents du futur sourire est déterminée grâce aux logiciels de planification.",
             "Logiciel de planification : tracé des futures dents sur la photographie du sourire"),
            ("bilan-parcours-3-modelisation-3d.jpg",
             "Une modélisation 3D du projet esthétique est ensuite réalisée.",
             "Modélisation 3D du projet esthétique sur l’empreinte numérique"),
            ("bilan-parcours-4-simulation.jpg",
             "Une simulation en situation réelle est générée en fonction du projet, pour donner "
             "une idée du résultat final à atteindre.",
             "Avant et après simulés sur le visage, yeux masqués"),
        ],
    },
}


SANS_PHOTO_EN_TETE = {"bilan-esthetique-personnalise"}

# ── une couverture choisie, à la place de la première photo de l'ancienne page ──
# Franck, 19/10/2026 : « la photo de couverture ne sert à rien, c'est juste une
# bouche sans intérêt : montre un avant/après (cas 1 par exemple) ».
# Montage carré (avant dessus, après dessous) fabriqué depuis les originaux du
# dossier 02 Eclaircissement, publié par scripts/prepare-photos.mjs.
PHOTO_EN_TETE = {
    "eclaircissement-dentaire-paris": (
        "eclaircissement-cas-1-couverture.jpg",
        "Avant et après éclaircissement — cas 1, préalable au traitement "
        "d’une tache blanche sur l’incisive centrale",
        "Avant et après éclaircissement dentaire, sourire de face"),
    # Franck, 19/10/2026 : « illustrer la page sur le même modèle qu'Éclaircissement ».
    # Le cas d'érosion-infiltration seule, détouré sur fond noir.
    "taches-dentaires-dyschromies-icon": (
        "icon-cas-1-couverture.jpg",
        "Avant et après érosion-infiltration ICON — cas 1, plusieurs taches profondes "
        "dues à une MIH sévère",
        "Avant et après infiltration de résine de taches de MIH sur les incisives, fond noir"),
    # Franck, 20/10/2026 : « fais la même chose avec la page 04 Composite bonding ».
    "composite-bonding-paris": (
        "composite-harmonisation-couverture.jpg",
        "Avant et après — demande d’harmonisation du sourire sans orthodontie : diastème à fermer, "
        "incisive latérale riziforme à remodeler, malpositions à compenser. Résultat uniquement "
        "additif, 100 % conservateur, en composite stratifié réalisé après éclaircissement.",
        "Avant et après : diastème fermé et incisive latérale remodelée en composite, sourire de face",
        [("éclaircissement", "eclaircissement-dentaire-paris")]),
    # Franck, 25/10/2026 : « tu peux fabriquer la page facettes, les photos sont dans le
    # dossier ». Le cas qu'il a rangé dans « cascouverture », sourire sans écarteurs.
    "facettes-dentaires-paris": (
        "facettes-diastemes-couverture.jpg",
        "Avant et après facettes : les espaces entre les dents antérieures sont refermés.",
        "Avant et après facettes : espaces entre les incisives, puis refermés, sourire de face"),
}
# Les photographies de l'ancienne page ICON quittent la page : la tache de MIH et son
# résultat sont désormais montrés par chapitre, avec le traitement entre les deux.
SANS_PHOTOS_SOURCE = {"bilan-esthetique-personnalise", "taches-dentaires-dyschromies-icon",
                      "composite-bonding-paris", "facettes-dentaires-paris"}

# ── une photographie par chapitre ─────────────────────────────────────────
# Posée dans la colonne de droite du chapitre, au-dessus de l'encadré : le texte
# est long, l'image le rythme. Franck, 19/10/2026 : « les dispatcher au fil du
# texte pour le rendre plus lisible et illustré ».
ILLUSTRATIONS = {
    "bilan-esthetique-personnalise": {
        1: ("bilan-parcours-1-photographies.jpg",
            "Un bilan photographique est réalisé à chaque première consultation.",
            "Le praticien photographie le sourire d’une patiente au cabinet"),
        2: ("bilan-parcours-2-planification.jpg",
            "La forme des dents du futur sourire est déterminée grâce aux logiciels de planification.",
            "Logiciel de planification : tracé des futures dents sur la photographie du sourire"),
        3: ("bilan-parcours-3-modelisation-3d.jpg",
            "Une modélisation 3D du projet esthétique est ensuite réalisée.",
            "Modélisation 3D du projet esthétique sur l’empreinte numérique"),
        4: ("bilan-parcours-4-simulation.jpg",
            "Une simulation en situation réelle est générée en fonction du projet, pour donner "
            "une idée du résultat final à atteindre.",
            "Avant et après simulés sur le visage, yeux masqués"),
    },
    # Deux images générées (19/10/2026), pas des photographies de patients :
    # l'alternative textuelle le dit.
    "eclaircissement-dentaire-paris": {
        2: ("eclaircissement-gouttieres.jpg",
            "Gouttières personnalisées et gel de peroxyde de carbamide, portés à domicile.",
            "Illustration : gouttières de blanchiment transparentes et seringue de gel"),
        3: ("eclaircissement-sensibilites.jpg",
            "Le froid est ce qui réveille une sensibilité : elle est transitoire et régresse "
            "après adaptation ou interruption du protocole.",
            "Illustration : verre d’eau glacée, glaçons et condensation"),
        4: ("eclaircissement-colorants.jpg",
            "Café, thé, vin rouge, tabac : ce qui colore les dents.",
            "Illustration : verre de vin rouge, tasse de café, tasse de thé et cigarette"),
    },
    # Photographies du cabinet (19/10/2026). Franck : « utilise le cas que tu as fractionné
    # comme avant/après en illustration du 2/5 » : la tache et son résultat, même zoom ;
    # le traitement sous digue reste au chapitre 3. Les légendes reprennent celles de Franck.
    "taches-dentaires-dyschromies-icon": {
        1: ("icon-fluorose.jpg",
            "Exemple d’atteinte par fluorose grave.",
            "Fluorose sévère : taches brunes et blanches sur l’ensemble des dents, sourire de face"),
        2: ("icon-mih-avant-apres.jpg",
            "Tache blanche de MIH sur une incisive : résultat après éclaircissement, "
            "composite stratifié sur 11 et érosion-infiltration ICON sur 21.",
            "Avant et après : tache blanche de MIH sur une incisive, puis dents éclaircies et tache traitée",
            [("éclaircissement", "eclaircissement-dentaire-paris"),
             ("composite stratifié", "composite-bonding-paris")],
            {"libre": True}),
        3: ("icon-traitement-21.jpg",
            "Le même cas : traitement ICON de la dent 21, sous digue.",
            "Infiltration de résine en cours sur une incisive isolée par une digue et des matrices métalliques"),
    },
    # Composite bonding (20/10/2026) : la vue de profil d'un cas de la bande au chapitre 1,
    # deux avant/après carrés aux chapitres 2 et 4. Légendes de Franck.
    "composite-bonding-paris": {
        1: ("composite-addition-profil.jpg",
            "Le composite, par addition uniquement, ne touche pas aux dents et permet de "
            "restaurer forme et longueur.",
            "Vue de profil des dents antérieures allongées par addition de composite"),
        2: ("composite-microdontie-avant-apres.jpg",
            "Incisives latérales présentant une microdontie, une forme anormale : modification de la "
            "forme par deux composites stratifiés, pour retrouver une forme et une esthétique naturelles.",
            "Avant et après : incisives latérales trop petites, puis remodelées en composite stratifié",
            None, {"libre": True}),
        4: ("composite-usures-avant-apres.jpg",
            "Usures dentaires importantes, la patiente ne souhaitait pas de facettes : composites sur "
            "les six dents antérieures, pour retrouver forme, fonction et esthétique naturelle.",
            "Avant et après : bords des incisives usés, puis reconstruits en composite",
            [("Usures dentaires", "usures-dentaires"), ("facettes", "facettes-dentaires-paris")],
            {"libre": True}),
    },
    # Facettes (25/10/2026) : trois avant/après carrés et les deux photographies de céramiques.
    # La légende du chapitre 4 est celle que Franck a écrite dans les noms de fichiers.
    "facettes-dentaires-paris": {
        1: ("facettes-transformation-avant-apres.jpg",
            "Dents usées et colorées : le sourire redessiné par des facettes, formes, longueurs et teinte.",
            "Avant et après : dents usées et jaunies, puis sourire refait par des facettes",
            None, {"libre": True}),
        2: ("facettes-fractures-sourire-avant-apres.jpg",
            "Le cas 2, sourire : incisives fracturées et usées, puis forme et longueur rendues par des facettes.",
            "Avant et après facettes, sourire : incisives fracturées et usées, puis reconstruites",
            None, {"libre": True}),
        3: ("facettes-pieces-ceramique.jpg",
            "Facettes en céramique, prêtes pour le collage.",
            "Six facettes en céramique posées sur des tiges de préhension orange, fond blanc"),
        4: ("facettes-incisives-eclaircissement-avant-apres.jpg",
            "Une dent dévitalisée et des composites infiltrés : deux facettes réalisées sur les dents "
            "11 et 21, après éclaircissement.",
            "Avant et après : incisive dévitalisée assombrie et anciens composites, puis deux facettes "
            "sur les incisives centrales",
            [("éclaircissement", "eclaircissement-dentaire-paris")],
            {"libre": True}),
        5: ("facettes-modele-ceramique.jpg",
            "Les pièces en céramique sur le modèle, avant le collage.",
            "Modèle de l’arcade supérieure tenu dans une main gantée, pièces en céramique en place"),
    },
}
# Seules les suites d'étapes portent un numéro ; une illustration isolée, non.
ILLUSTRATIONS_NUMEROTEES = {"bilan-esthetique-personnalise"}


# ── une vignette vers la vidéo de la page ──────────────────────────────────
# Franck, 25/10/2026 : « dans la page composite, une vignette photo de couverture
# cliquable qui renvoie vers la page de cette vidéo ». C'est la vidéo qui déclare
# sa page et son chapitre (videos/<slug>.txt) : la page n'a rien à tenir à jour.
def vignettes_video(slug):
    import videos as vid
    trouvees = {}
    for v in vid.toutes():
        for cible, k in vid.cibles(v):
            if cible == slug:
                trouvees.setdefault(k, []).append(vid.vignette(v))
    return trouvees


def lier(texte, liens):
    """Rend cliquables, dans une légende déjà échappée, les mots donnés :
    un couple (mots, page) ou une liste de couples."""
    if not liens:
        return texte
    if isinstance(liens[0], str):
        liens = [liens]
    for mots, cible in liens:
        texte = texte.replace(e(mots), f'<a href="{cible}.html">{e(mots)}</a>', 1)
    return texte


def illustration(slug, k):
    ill = ILLUSTRATIONS.get(slug, {}).get(k)
    if not ill:
        return ""
    fichier, legende, alt = ill[:3]
    options = ill[4] if len(ill) > 4 else {}
    classe = "illus illus--libre" if options.get("libre") else "illus"
    src = gen.VERS_DEPOT + "src/assets/photos/cas/" + fichier
    badge = f'<span class="parcours__num">{k}</span>' if slug in ILLUSTRATIONS_NUMEROTEES else ""
    return (f'        <figure class="{classe}">\n'
            f'          <img src="{src}" alt="{H.escape(alt)}" loading="lazy">\n'
            # le texte dans un seul bloc : la légende est une rangée souple (pastille + texte),
            # et chaque lien en serait sinon devenu une colonne
            f'          <figcaption>{badge}<span>{lier(e(legende), ill[3] if len(ill) > 3 else None)}</span></figcaption>\n'
            f'        </figure>\n')


def sequence(slug):
    seq = SEQUENCES.get(slug)
    if not seq:
        return ""
    figs = []
    large = seq.get("large", False)
    for i, etape in enumerate(seq["etapes"], 1):
        fichier, legende, alt = etape[:3]
        src = gen.VERS_DEPOT + "src/assets/photos/cas/" + fichier
        badge = "" if large else f'<span class="parcours__num">{i}</span>'
        # un quatrième élément (mots, page), ou une liste de couples, rend ces mots cliquables
        texte = lier(e(legende), etape[3] if len(etape) > 3 else None)
        figs.append(f'''        <figure class="parcours__etape">
          <img src="{src}" alt="{H.escape(alt)}" loading="lazy">
          <figcaption>{badge}<span>{texte}</span></figcaption>
        </figure>''')
    classe = "parcours parcours--large" if large else "parcours"
    return f'''  <section class="sect sect--zone">
    <div class="contenu">
      <h2 class="tete-bande">{e(seq["titre"])}</h2>
      <div class="{classe}">
{chr(10).join(figs)}
      </div>
    </div>
  </section>'''


def composer(slug, plan):
    p = lire(slug)
    sec = p["sections"]
    sur, public, lib = gen.PUBLIC.get(slug, ("", None, p["h1"][:40]))
    ariane = '<a href="index.html">Accueil</a>' + (f" › {e(public)}" if public else "") + f" › {e(lib)}"

    # chapô : le paragraphe le plus long de l'ouverture
    # Tout ce qui précède le premier chapitre appartient à l'ouverture : certaines
    # pages ont deux blocs d'en-tête, et le second se perdait.
    premier = min((i for ch in plan["chapitres"] for i in ch["sections"]), default=1)
    ouverture = p["tete"] + [x for s_ in sec[:premier] for x in s_["p"]]
    chapo = max(ouverture, key=len) if ouverture else ""
    # l'ouverture porte souvent deux paragraphes : le chapô et un résumé
    resume = [x for x in ouverture if x != chapo]

    # La photo d'ouverture est prise à la première section qui en porte une,
    # et retirée de celle-ci pour ne pas paraître deux fois.
    photo = ""
    # Franck, 19/10/2026 : les photographies de l'ancien cas ne correspondent
    # plus à la page ; seules ses quatre nouvelles images l'illustrent.
    if slug in SANS_PHOTOS_SOURCE:
        p["figures_libres"] = []
        for s_ in sec:
            s_["figures"] = []
    sources_photo = [p["figures_libres"]] + [s_["figures"] for s_ in sec]
    # Franck, 19/10/2026 : la photo de tête du bilan « ne correspond pas » — retirée.
    if slug in SANS_PHOTO_EN_TETE:
        sources_photo = []
    for lot in sources_photo:
        if lot:
            fg = lot.pop(0)
            leg = f'<figcaption>{e(fg["legende"])}</figcaption>' if fg["legende"] else ""
            photo = (f'      <figure><img src="{fg["src"][0]}" '
                     f'alt="{H.escape((fg["alt"] or [""])[0])}">{leg}</figure>\n')
            break
    if slug in PHOTO_EN_TETE:  # la photo héritée reste consommée, mais c'est celle-ci qui s'affiche
        fichier, leg, alt = PHOTO_EN_TETE[slug][:3]
        liens = PHOTO_EN_TETE[slug][3] if len(PHOTO_EN_TETE[slug]) > 3 else None
        src = gen.VERS_DEPOT + "src/assets/photos/cas/" + fichier
        photo = (f'      <figure><img src="{src}" alt="{H.escape(alt)}">'
                 f'<figcaption>{lier(e(leg), liens)}</figcaption></figure>\n')

    corps = []
    videos_page = vignettes_video(slug)
    n = len(plan["chapitres"])
    for k, ch in enumerate(plan["chapitres"], 1):
        avec_fiche = ch.get("fiche", [])
        blocs = "\n".join(bloc(p, i, avec_liste=i not in avec_fiche,
                               titre=ch.get("titres", {}).get(i))
                          for i in ch["sections"])
        if k == 1 and resume:
            intro = "\n          ".join(f"<p>{e(x)}</p>" for x in resume)
            blocs = f'        <div class="bloc">\n          {intro}\n        </div>\n' + blocs
        zone = ' sect--zone' if k % 2 == 0 else ""
        illus = "".join(videos_page.get(k, [])) + illustration(slug, k)
        droite = ""
        if avec_fiche:
            droite = (f'      <div class="cote">\n{illus}        <div class="fiche">\n'
                      f'{fiche(p, avec_fiche)}\n        </div>\n      </div>\n')
        elif illus:
            droite = f'      <div class="cote">\n{illus}      </div>\n'
        classe = "contenu chapitre" if droite else "contenu chapitre chapitre--plein"
        corps.append(f'''  <section class="sect{zone}">
    <div class="{classe}">
      <div>
        <p class="numero">{k} / {n}</p>
        <h2>{e(ch["titre"])}</h2>
{blocs}
      </div>
{droite}    </div>
  </section>''')
        if SEQUENCES.get(slug, {}).get("apres_chapitre") == k:
            corps.append(sequence(slug))

    # questions — avant « À lire aussi » : elles font partie du contenu, les
    # renvois sont de la navigation. Franck, 19/10/2026 : « un FAQ plus marqué ».
    faq = next((s for s in sec if s["faq"]), None)
    paires = gen.questions(slug)
    if paires is None and faq:
        # un paragraphe d'introduction dans la section décalait toutes les réponses d'un cran
        ps = faq["p"][max(0, len(faq["p"]) - len(faq["h3"])):]
        paires = [{"q": q, "r": r} for q, r in zip(faq["h3"], ps)]
    if paires:
        qs = "".join(f'\n        <div><h3>{e(x["q"])}</h3><p>{e(x["r"])}</p></div>'
                     for x in paires[:8])
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu">
      <h2 class="tete-bande">Questions fréquentes</h2>
      <div class="qa">{qs}
      </div>
    </div>
  </section>''')

    # les liens portés par les sections qu'aucun chapitre ne reprend
    reprises = {i for ch in plan["chapitres"] for i in ch["sections"]}
    poses = set()
    for i in reprises:
        poses.update(sec[i]["renvois"])
    orphelins = [l for l in p["liens"] if l not in poses
                 and p["liens"][l] != slug and len(l) < 60
                 and not l.lower().startswith(("accueil", "prendre"))]
    if orphelins:
        liens = " · ".join(f'<a href="{p["liens"][l]}.html">{e(l)}</a>' for l in orphelins)
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu chapitre chapitre--plein">
      <div>
        <p class="eyebrow">À lire aussi</p>
        <p class="suite">{liens}</p>
      </div>
    </div>
  </section>''')

    if p["figures_libres"]:
        cartes = []
        for fg in p["figures_libres"]:
            alts = fg["alt"] + [""] * 2
            if len(fg["src"]) >= 2:
                im = "".join(f'<img src="{x}" alt="{H.escape(alts[k])}" loading="lazy">'
                             for k, x in enumerate(fg["src"][:2]))
                dedans, cls = f'<div class="paire">{im}</div>', "paire"
            else:
                dedans, cls = (f'<img src="{fg["src"][0]}" alt="{H.escape(alts[0])}" loading="lazy">', "solo")
            leg = f'<figcaption>{e(fg["legende"])}</figcaption>' if fg["legende"] else ""
            cartes.append(f'<figure class="{cls}">{dedans}{leg}</figure>')
        corps.append(f'''  <section class="sect">
    <div class="contenu">
      <p class="eyebrow">Les photographies du cas</p>
      <div class="cas">{"".join(cartes)}</div>
    </div>
  </section>''')

    if p["mention"]:
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu">
      <p class="mention">{e(p["mention"])}</p>
    </div>
  </section>''')

    # appel
    fin = sec[-1]
    corps.append(f'''  <section class="appel">
    <div class="contenu">
      <h2>{e(fin["titre"] or "Faire le point")}</h2>
      {"".join(f"<p>{e(x)}</p>" for x in fin["p"]) or "<p>Un bilan permet de comprendre la situation et les options possibles, avant tout engagement.</p>"}
      <a class="bouton" href="contact.html">Prendre rendez-vous</a>
    </div>
  </section>''')

    # sources
    src = next((s for s in sec if s["sources"]), None)
    if src:
        intro, items, k = "", [], 0
        ps = src["p"]
        if ps and not ps[0].startswith("["):
            intro, k = ps[0], 1
        while k < len(ps):
            ref = ps[k]
            doi = ps[k + 1] if k + 1 < len(ps) and ps[k + 1].startswith("DOI") else ""
            items.append(f"<li>{e(ref)}{(' — ' + e(doi)) if doi else ''}</li>")
            k += 2 if doi else 1
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu sources">
      <p class="eyebrow">Sources scientifiques</p>
      {f'<p style="margin-bottom:.6rem">{e(intro)}</p>' if intro else ""}
      <ol>
        {chr(10).join("        " + i for i in items).strip()}
      </ol>
    </div>
  </section>''')

    version = str(int(os.path.getmtime(os.path.join(SORTIE, "style.css"))))
    page = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p["titre"])}</title>
<meta name="description" content="{H.escape(p["description"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap">
<link rel="stylesheet" href="style.css?v={version}">
{chr(10).join(re.findall(r"<script type=.application/ld\+json.[^>]*>.*?</script>", p["brut"], re.S))}
</head>
<body>

{gen.menu(slug)}

<main>

  <div class="contenu">
    <p class="ariane">{ariane}</p>
    <div class="une">
      <div>
{f'        <p class="eyebrow">{e(sur)}</p>{chr(10)}' if sur else ""}        <h1>{e(gen.grand_titre(slug, p["h1"])[0])}</h1>
{gen.soustitre(gen.grand_titre(slug, p["h1"])[1])}
        <p class="une__chapo">{e(chapo)}</p>
        <div class="signature">
          <img src="{PORTRAIT}" alt="Dr Franck Moyal">
          <div><b>Dr Franck Moyal</b> — chirurgien-dentiste, Paris 9<sup>e</sup><br>
            Praticien hospitalier, Pitié-Salpêtrière · CMME, Sainte-Anne</div>
        </div>
      </div>
{photo}    </div>
  </div>

{chr(10).join(corps)}

</main>

{gen.PIED}

<script src="menu.js"></script>
</body>
</html>
'''
    open(os.path.join(SORTIE, f"{slug}.html"), "w", encoding="utf-8").write(page)
    return p, page


# ── contrôle : rien ne doit disparaître ───────────────────────────────────────
def controler(p, page):
    ref = nu(p["main"], False).lower()
    fait = nu(re.search(r"<main.*?</main>", page, re.S).group(0), False).lower()
    manque = []
    for tag in ("p", "li"):
        for x in re.findall(rf"<{tag}[^>]*>(.*?)</{tag}>", p["main"], re.S):
            t = nu(x, False)
            if len(t) < 22 or any(t.lower().startswith(m) for m in MEUBLE):
                continue
            mots = re.findall(r"[a-zà-ÿ]{5,}", t.lower())[:5]
            if mots and not all(w in fait for w in mots):
                manque.append(t)
    return manque, len(ref.split()), len(fait.split())


# ── le découpage, décidé page par page ────────────────────────────────────────
PLANS = {
  "erosion-dentaire": {"chapitres": [
    {"titre": "Ce qu’est une érosion", "sections": [1, 2], "fiche": [2]},
    {"titre": "D’où viennent les acides", "sections": [3, 4]},
    {"titre": "Dépister tôt", "sections": [5, 6], "fiche": [6]},
    {"titre": "Protéger au quotidien", "sections": [7, 8, 9], "fiche": [7]},
    {"titre": "Quand faut-il restaurer ?", "sections": [10]},
  ]},
  "tca-dents": {"chapitres": [
    {"titre": "Ce que les TCA font aux dents", "sections": [1, 2], "fiche": [1]},
    {"titre": "Même sans vomissements", "sections": [3]},
    {"titre": "Pourquoi le dépistage compte", "sections": [4, 9], "fiche": [4]},
    {"titre": "Pendant, puis après", "sections": [6, 7, 8], "fiche": [6]},
    {"titre": "Mon engagement sur ce sujet", "sections": [5, 10]},
  ]},
  "rehabilitation-dents-usees": {"chapitres": [
    {"titre": "Pourquoi reconstruire", "sections": [1, 2, 3], "fiche": [3]},
    {"titre": "Avec quoi reconstruire", "sections": [4, 5], "fiche": [5]},
    {"titre": "La dimension verticale", "sections": [6, 7], "fiche": [7]},
    {"titre": "Comment on procède", "sections": [8, 10], "fiche": [8]},
    {"titre": "Et l’esthétique ?", "sections": [9]},
  ]},
  "anorexie-erosion-dentaire-sans-vomissements": {"chapitres": [
    {"titre": "Le risque existe sans vomissements", "sections": [1]},
    {"titre": "Quatre mécanismes", "sections": [2, 3, 4, 5, 6], "fiche": [4]},
    {"titre": "L’anorexie est-elle une cause directe ?", "sections": [7]},
    {"titre": "Pourquoi dépister tôt", "sections": [8], "fiche": [8]},
    {"titre": "Que peut-on faire", "sections": [9, 10], "fiche": [9]},
  ]},
  "composite-bonding-paris": {"chapitres": [
    {"titre": "Une technique conservatrice, mais exigeante", "sections": [1, 2]},
    {"titre": "La stratification", "sections": [3]},
    {"titre": "Quand on l’utilise", "sections": [4, 5], "fiche": [4]},
    {"titre": "Composite ou facettes, et pour combien de temps", "sections": [6, 8]},
    {"titre": "Le déroulement, et ce que je recherche", "sections": [7, 9]},
  ]},
  "facettes-dentaires-paris": {"chapitres": [
    {"titre": "Transformer l’architecture du sourire", "sections": [1, 2]},
    {"titre": "Décider du futur sourire", "sections": [3, 4]},
    {"titre": "La céramique, et la préparation", "sections": [5, 6]},
    {"titre": "Facettes ou composite, et la durée", "sections": [7, 8]},
    {"titre": "À quoi ressemble le parcours", "sections": [9], "fiche": [9]},
  ]},
  "taches-dentaires-dyschromies-icon": {"chapitres": [
    {"titre": "Toutes les taches ne se valent pas", "sections": [1, 3]},
    {"titre": "Les taches de MIH", "sections": [2]},
    {"titre": "L’érosion-infiltration de résine", "sections": [4, 5]},
    {"titre": "Associer les approches", "sections": [6, 7]},
    {"titre": "Pourquoi ne pas poser un composite d’emblée", "sections": [8]},
  ]},
  "bruxisme-usure-dentaire": {"chapitres": [
    {"titre": "Une usure ne prouve pas un bruxisme", "sections": [1, 2], "fiche": [2]},
    {"titre": "Pourquoi les dents s’usent chez un bruxeur", "sections": [3], "fiche": [3]},
    {"titre": "Comment sait-on si l’on bruxe ?", "sections": [4], "fiche": [4]},
    {"titre": "La gouttière, et la part de l’érosion", "sections": [5, 6], "fiche": [6]},
    {"titre": "Reconstruire, et la question des douleurs", "sections": [7, 8], "fiche": [7]},
  ]},
  "dents-courtes-usees": {"chapitres": [
    {"titre": "« Mes dents sont devenues plus petites »", "sections": [1, 2], "fiche": [1]},
    {"titre": "Pourquoi le sourire paraît plus âgé", "sections": [3], "fiche": [3]},
    {"titre": "Faut-il tout reconstruire ?", "sections": [4, 5], "fiche": [4]},
    {"titre": "Quelle longueur, et la dimension verticale", "sections": [6, 7], "fiche": [6]},
    {"titre": "Le résultat qu’on peut rechercher", "sections": [8], "fiche": [8]},
  ]},
  "eclaircissement-dentaire-paris": {"chapitres": [
    {"titre": "Un traitement entièrement conservateur", "sections": [1, 2]},
    {"titre": "L’éclaircissement ambulatoire", "sections": [3, 4], "fiche": [4]},
    {"titre": "Les sensibilités", "sections": [5]},
    {"titre": "Pendant le traitement", "sections": [6]},
    {"titre": "Dans un projet esthétique global", "sections": [7]},
  ]},
  "franck-moyal": {"chapitres": [
    {"titre": "Ma pratique", "sections": [2, 3]},
    {"titre": "Érosion et troubles alimentaires", "sections": [4]},
    {"titre": "Enseigner, et l’hôpital", "sections": [5, 6]},
    {"titre": "Traiter juste", "sections": [7, 8]},
  ]},
  "chirurgien-dentiste-paris-9": {"chapitres": [
    {"titre": "Une pratique orientée", "sections": [1]},
    {"titre": "Pourquoi consulter", "sections": [2], "fiche": [2]},
    {"titre": "La première consultation", "sections": [3], "fiche": [3]},
    {"titre": "Trois principes", "sections": [4]},
    {"titre": "Cabinet et hôpital", "sections": [5]},
  ]},
  "cas-usures-dentaires-facettes-minimalement-invasives": {"chapitres": [
    {"titre": "La demande, et ce que l’examen montre", "sections": [1, 2]},
    {"titre": "Comprendre avant de restaurer", "sections": [3, 4, 5, 6]},
    {"titre": "Planifier, et créer l’espace", "sections": [7, 8]},
    {"titre": "Le traitement", "sections": [9, 10]},
    {"titre": "Le résultat, et ce qu’on en retient", "sections": [11, 12, 13]},
  ]},
  "cas-planification-facettes-ceramique": {"chapitres": [
    {"titre": "La situation initiale", "sections": [1]},
    {"titre": "Définir le projet final", "sections": [2]},
    {"titre": "Une orthodontie guidée par le projet", "sections": [3]},
    {"titre": "Quatre facettes, et le résultat", "sections": [4, 5]},
    {"titre": "Ce que ce cas permet de comprendre", "sections": [6]},
  ]},
  "cas-planification-rehabilitation-facettes": {"chapitres": [
    {"titre": "La situation initiale", "sections": [1]},
    {"titre": "Visualiser avant de traiter", "sections": [2, 3]},
    {"titre": "Une réhabilitation par vingt facettes", "sections": [4]},
    {"titre": "Le résultat", "sections": [5]},
    {"titre": "Ce que ce cas permet de comprendre", "sections": [6]},
  ]},
  "cas-mih-eclaircissement-erosion-infiltration": {"chapitres": [
    {"titre": "Une tache, deux situations", "sections": [1, 2]},
    {"titre": "Premier cas : MIH sur une incisive", "sections": [3]},
    {"titre": "Deuxième cas : MIH sur une dent dyschromiée", "sections": [4]},
    {"titre": "Pourquoi une approche conservatrice", "sections": [5]},
    {"titre": "Ce que ces deux cas permettent de comprendre", "sections": [6]},
  ]},
  "bilan-esthetique-personnalise": {"chapitres": [
    {"titre": "Ce qu’est un bilan esthétique", "sections": [1, 2], "fiche": [2]},
    {"titre": "Du projet au traitement", "sections": [3, 4, 5, 6], "fiche": [6]},
    {"titre": "Voir son futur sourire", "sections": [7, 8], "fiche": [8]},
    {"titre": "Pourquoi planifier, même quand c’est simple", "sections": [9, 11]},
    {"titre": "Sans engagement", "sections": [10]},
  ]},
}


def main():
    voulus = sys.argv[1:] or list(PLANS)
    print(f"{'page':46s} {'chap':>5s} {'s-part':>6s} {'manque':>7s} {'mots'}")
    print("─" * 78)
    for slug in voulus:
        p, page = composer(slug, PLANS[slug])
        manque, mo, mf = controler(p, page)
        alerte = "  ⚠" if manque else ""
        print(f"{slug:46s} {page.count('<h2>'):5d} {page.count('<h3>'):6d} {len(manque):7d}"
              f"   {mf}/{mo}{alerte}")
        for m in manque[:4]:
            print(f"      manquant : {m[:96]}")


if __name__ == "__main__":
    main()
