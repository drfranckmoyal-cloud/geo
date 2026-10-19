#!/usr/bin/env python3
"""
Génère les maquettes de la refonte à partir du site actuel.

Le principe : on ne réécrit aucun texte. On relit les pages construites dans dist/,
on en extrait les titres, les paragraphes, les listes, les questions, les sources et
les photographies, et on les réimprime dans la mise en page de la direction « Revue ».

Ce que le générateur fait de lui-même :
  · les listes passent en encadré, à côté du texte, au lieu de s'empiler dessous ;
  · les sections alternent fond clair et fond teinté, pour donner un rythme ;
  · les questions se mettent sur deux colonnes ;
  · les sources se resserrent en bas de page.

Ce qu'il NE fait PAS : regrouper les douze chapitres en cinq. Ce regroupement demande
de décider ce qu'on garde et ce qu'on fond, c'est-à-dire du texte — cela revient à
ChatGPT. La page Usures, faite à la main, montre ce que ça donne quand c'est fait.

    python3 docs/refonte/maquettes/generer.py
"""
import html as H
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DIST = os.path.join(RACINE, "dist")
SORTIE = os.path.join(RACINE, "docs", "refonte", "maquettes", "site")
# le portrait change de fichier : on le signe pour contourner le cache
PORTRAIT = "img/portrait-fm.png?v=" + str(int(os.path.getmtime(
    os.path.join(SORTIE, "img", "portrait-fm.png"))))
# la feuille de style est signée par sa date, pour contourner le cache du navigateur
VERSION = str(int(os.path.getmtime(os.path.join(SORTIE, "style.css"))))

# ── l'arborescence décidée le 16 octobre ──────────────────────────────────────
# Le menu porte les mêmes mots que les pages : le nom de l'acte d'un côté,
# le nom clinique du sujet de l'autre. Plus de « mes dents s'usent ».
ACTES = [
    ("Facettes", "facettes-dentaires-paris"),
    ("Composite bonding", "composite-bonding-paris"),
    ("Éclaircissement dentaire", "eclaircissement-dentaire-paris"),
    ("Infiltration ICON", "taches-dentaires-dyschromies-icon"),
    ("Réhabilitation des dents usées", "rehabilitation-dents-usees"),
    ("Bilan esthétique", "bilan-esthetique-personnalise"),
]
# Ni des actes ni des sujets : elles aident à choisir entre les actes.
# Elles ont leur propre colonne, sinon elles tombent du menu — c'est arrivé,
# et la page pilier du site avec elles.
POUR_CHOISIR = [
    ("Dentisterie esthétique", "dentisterie-esthetique-paris"),
    ("Facettes ou composite ?", "facettes-ou-composite"),
]
SUJETS = [
    ("Usure dentaire", "usures-dentaires"),
    ("Érosion dentaire", "erosion-dentaire"),
    ("Bruxisme", "bruxisme-usure-dentaire"),
    ("Dents courtes ou usées", "dents-courtes-usees"),
    ("Troubles des conduites alimentaires", "tca-dents"),
    ("Anorexie restrictive", "anorexie-erosion-dentaire-sans-vomissements"),
]
CONFRERES = [
    ("Conférences et formations", "conferences-formations"),
    ("Publications", "publications"),
    ("Activité hospitalière", "activite-hospitaliere"),
    ("Médias et interviews", "medias-interviews"),
]
# surtitre affiché en haut de chaque page, et fil d'Ariane
PUBLIC = {}
for lib, slug in ACTES:
    PUBLIC[slug] = ("L’acte", "Patient", lib)
for lib, slug in SUJETS:
    PUBLIC.setdefault(slug, ("Le sujet", "Patient", lib))
# deux pages qui ne sont ni un acte ni un sujet : elles aident à choisir entre les actes
PUBLIC["dentisterie-esthetique-paris"] = ("Pour choisir", "Patient", "Dentisterie esthétique")
PUBLIC["facettes-ou-composite"] = ("Pour choisir", "Patient", "Facettes ou composite ?")
PUBLIC["bilan-esthetique-personnalise"] = ("La consultation", "Patient", "Bilan esthétique")
for _slug, _lib in (
        ("cas-usures-dentaires-facettes-minimalement-invasives", "Usures et facettes"),
        ("cas-planification-rehabilitation-facettes", "Réhabilitation par facettes"),
        ("cas-planification-facettes-ceramique", "Facettes céramique"),
        ("cas-mih-eclaircissement-erosion-infiltration", "MIH et infiltration")):
    PUBLIC[_slug] = ("Cas clinique", "Patient", _lib)
for lib, slug in CONFRERES:
    PUBLIC[slug] = ("Pour les chirurgiens-dentistes", "Chirurgien-dentiste", lib)
# Pages hors menu mais qui appartiennent bien à un axe : l'anorexie prolonge les TCA,
# les cas cliniques illustrent les traitements.
PUBLIC["anorexie-erosion-dentaire-sans-vomissements"] = (
    "Le sujet", "Patient", "Anorexie restrictive")
PUBLIC["diagnostic-usures-dentaires"] = ("Le sujet", "Patient", "Diagnostic des usures")
PUBLIC["franck-moyal"] = ("Mon parcours", None, "Dr Franck Moyal")
PUBLIC["chirurgien-dentiste-paris-9"] = ("Le cabinet", None, "Paris 9ᵉ")
PUBLIC["contact"] = ("Le cabinet", None, "Contact")
PUBLIC["mentions-legales"] = ("Informations", None, "Mentions légales")

# pages déjà faites à la main, qu'on n'écrase pas
# Pages dont les chapitres sont regroupés : composer.py les écrit, pas celui-ci.
# On lit ses plans plutôt que de tenir une seconde liste à jour — elles divergeaient.
def _pages_composees():
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), "composer.py")
    if not os.path.exists(chemin):
        return set()
    src = open(chemin, encoding="utf-8").read()
    bloc = src[src.index("PLANS = {"):] if "PLANS = {" in src else ""
    return set(re.findall(r'^  "([a-z0-9-]+)":', bloc, re.M))


# Écrites entièrement à la main, avant que le composeur n'existe.
A_LA_MAIN = {"usures-dentaires", "facettes-ou-composite",
             "dentisterie-esthetique-paris", "index",
             "contact"} | _pages_composees()
# le diagnostic est fondu dans les usures (D77) : plus de page à lui,
# et tout lien qui le visait mène désormais à celle qui l'a absorbé
FONDUES = {"diagnostic-usures-dentaires"}
FONDUES_VERS = {"diagnostic-usures-dentaires": "usures-dentaires"}


# ── extraction ────────────────────────────────────────────────────────────────
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


def texte(frag):
    """Garde le gras et les liens d'appel, jette le reste du balisage."""
    frag, gardes = _mettre_de_cote(frag)
    f = re.sub(r"<(script|style)\b.*?</\1>", "", frag, flags=re.S)
    f = re.sub(r"<sup[^>]*class=\"cite\"[^>]*>.*?</sup>", "", f, flags=re.S)
    f = re.sub(r"<span[^>]*visually-hidden[^>]*>.*?</span>", "", f, flags=re.S)
    f = re.sub(r"<(?!/?(strong|em|b|i)\b)[^>]+>", " ", f)
    f = re.sub(r"\s+", " ", f)
    return _remettre(f.strip(), gardes)


# Chemin du dossier de la maquette jusqu'à la racine du dépôt. Les photos sont
# appelées en relatif et non en absolu : la maquette s'ouvre alors d'un double-clic,
# sans serveur, tout en marchant aussi derrière le serveur local.
VERS_DEPOT = "../../../../"


def locale(src):
    """/_astro/nom.hash_hash.webp → le fichier d'origine dans le dépôt."""
    nom = re.sub(r"\.[A-Za-z0-9_-]+_[A-Za-z0-9_-]+\.(?:webp|jpg|png)$", ".jpg",
                 os.path.basename(src))
    if os.path.exists(os.path.join(RACINE, "src", "assets", "photos", "cas", nom)):
        return VERS_DEPOT + "src/assets/photos/cas/" + nom
    return VERS_DEPOT + "dist" + src


def lire(slug):
    chemin = os.path.join(DIST, slug, "index.html") if slug else os.path.join(DIST, "index.html")
    if not os.path.exists(chemin):
        return None
    brut = open(chemin, encoding="utf-8").read()
    main = re.search(r"<main.*?</main>", brut, re.S)
    if not main:
        return None
    main = main.group(0)

    page = {"slug": slug}
    t = re.search(r"<title>(.*?)</title>", brut, re.S)
    page["title"] = H.unescape(t.group(1).strip()) if t else slug
    d = re.search(r'<meta name="description" content="([^"]*)"', brut)
    page["description"] = H.unescape(d.group(1)) if d else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    page["h1"] = texte(h1.group(1)) if h1 else page["title"]

    # Le chapô se cache à trois endroits selon les pages : avant la première
    # section, dans un bloc « answer » posé entre deux sections, ou dans la
    # première section elle-même. On les regarde tous les trois.
    candidats = []
    avant = main.split("<section", 1)[0]
    candidats += [texte(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", avant, re.S)]
    candidats += [texte(x) for x in
                  re.findall(r'<div[^>]*class="answer"[^>]*>(.*?)</div>', main, re.S)]
    prem = re.search(r"<section[^>]*>.*?</section>", main, re.S)
    if prem:
        candidats += [texte(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", prem.group(0), re.S)]
    candidats = [c for c in candidats
                 if len(c) > 40 and "Chirurgien-dentiste à Paris" not in c]
    page["chapo"] = max(candidats, key=len) if candidats else ""

    # Données structurées : c'est par elles que les moteurs et les IA
    # comprennent qui parle et de quoi. On les reprend telles quelles —
    # la refonte change la mise en page, pas ce que la page affirme.
    page["jsonld"] = re.findall(
        r'<script type="application/ld\+json"[^>]*>.*?</script>', brut, re.S)

    # photographies de la page
    page["photos"] = []
    for fig in re.findall(r"<figure.*?</figure>", main, re.S):
        imgs = re.findall(r'\bsrc="(/_astro/[^"]+\.(?:webp|jpg|png))"', fig)
        alts = re.findall(r'\balt="([^"]*)"', fig)
        cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", fig, re.S)
        if imgs:
            page["photos"].append({
                "src": [locale(i) for i in imgs[:2]],
                "alt": [H.unescape(a) for a in alts[:2]] or [""],
                "legende": texte(cap.group(1)) if cap else "",
            })

    # sections
    page["sections"] = []
    page["faq"] = []
    page["sources"] = []
    for sec in re.findall(r"<section[^>]*>.*?</section>", main, re.S):
        h2 = re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S)
        titre = texte(h2.group(1)) if h2 else ""

        if "faq__item" in sec:
            # chaque item est <div class="faq__item"><h3>…</h3><p>…</p></div> ;
            # on découpe sur l'ouverture plutôt que de deviner les fermetures.
            for item in sec.split('class="faq__item"')[1:]:
                q = re.search(r"<h3[^>]*>(.*?)</h3>", item, re.S)
                r = re.search(r"<p[^>]*>(.*?)</p>", item, re.S)
                if q and r:
                    page["faq"].append({"q": texte(q.group(1)), "r": texte(r.group(1))})
            continue
        if "source__ref" in sec:
            for s in re.findall(r'<div[^>]*class="source__ref"[^>]*>(.*?)</div>', sec, re.S):
                page["sources"].append(texte(s))
            continue

        paras = [texte(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", sec, re.S)]
        # la ligne d'auteur et le chapô réapparaissent dans la première section
        paras = [p for p in paras
                 if len(p) > 45
                 and "Dr Franck Moyal — Chirurgien" not in p
                 and p != page["chapo"]]
        lis = [texte(x) for x in re.findall(r"<li[^>]*>(.*?)</li>", sec, re.S)]
        lis = [l for l in lis if 10 < len(l) < 240]
        liens = []
        for href, lib in re.findall(r'<a[^>]*href="(/[^"#?]+/)"[^>]*>(.*?)</a>', sec, re.S):
            lib = texte(lib)
            if (lib and len(lib) < 60 and "Franck Moyal" not in lib
                    and href.strip("/") != slug and (href, lib) not in liens):
                liens.append((href, lib))
        if titre or paras:
            page["sections"].append({"titre": titre, "p": paras, "li": lis, "liens": liens[:4]})
    return page


# ── rendu ─────────────────────────────────────────────────────────────────────
AUTORISES = ("strong", "em", "b", "i")


def e(s):
    """Échappe, puis rend leur rôle aux seules balises qu'on a gardées."""
    out = H.escape(s, quote=False)
    for t in AUTORISES:
        out = out.replace(f"&lt;{t}&gt;", f"<{t}>").replace(f"&lt;/{t}&gt;", f"</{t}>")
    # Les liens d'appel portent un attribut : la liste blanche ci-dessus, qui ne
    # connaît que les balises nues, les laissait échappés et donc affichés en clair.
    out = re.sub(r'&lt;a href="((?:tel|mailto):[^"]+)"&gt;(.*?)&lt;/a&gt;',
                 lambda m: '<a href="%s">%s</a>' % (m.group(1).replace("&amp;", "&"),
                                                    m.group(2)),
                 out, flags=re.S)
    return out


def menu(slug):
    def liste(items):
        return "\n".join(
            f'              <li><a href="{s}.html">{e(l)}</a></li>' for l, s in items
        )
    return f'''<header class="entete">
  <div class="entete__barre">
    <a class="marque" href="index.html">Dr Franck Moyal</a>
    <button class="burger" id="burger" aria-expanded="false">Menu</button>
    <nav class="nav" id="nav">
      <div>
        <button data-volet="v1" aria-expanded="false">Espace patients</button>
        <div class="volet volet--trois" id="v1">
          <div>
            <h4>Les actes</h4>
            <ul>
{liste(ACTES)}
            </ul>
          </div>
          <div>
            <h4>Ce que l’on traite</h4>
            <ul>
{liste(SUJETS)}
            </ul>
          </div>
          <div>
            <h4>Pour choisir</h4>
            <ul>
{liste(POUR_CHOISIR)}
              <li><a href="espace-patients.html"><b>Tout l’espace patients</b></a></li>
            </ul>
          </div>
        </div>
      </div>
      <div>
        <button data-volet="v2" aria-expanded="false">Espace pro</button>
        <div class="volet" id="v2">
          <ul>
{liste(CONFRERES)}
            <li><a href="https://smileclubformations.com/" target="_blank" rel="noopener">Smile Club Formations <span class="ext">↗</span></a></li>
            <li><a href="espace-pro.html"><b>Tout l’espace pro</b></a></li>
          </ul>
        </div>
      </div>
      <a class="lien" href="franck-moyal.html">Mon parcours</a>
    </nav>
    <a class="rdv" href="contact.html">Prendre rendez-vous</a>
  </div>
</header>'''


PIED = '''<footer class="pied">
  <div class="contenu">
    <div class="pied__grille">
      <div><h4>Le cabinet</h4><ul><li>2 rue Hippolyte Lebas</li><li>75009 Paris</li><li><a href="tel:+33183755216">01 83 75 52 16</a></li><li>Consultations mardi et vendredi, 9 h – 19 h</li><li>Standard lundi–vendredi, 9 h – 19 h</li></ul></div>
      <div><h4>Les actes</h4><ul><li><a href="facettes-dentaires-paris.html">Facettes</a></li><li><a href="composite-bonding-paris.html">Composite bonding</a></li><li><a href="eclaircissement-dentaire-paris.html">Éclaircissement dentaire</a></li><li><a href="taches-dentaires-dyschromies-icon.html">Infiltration ICON</a></li></ul></div>
      <div><h4>Ce que l’on traite</h4><ul><li><a href="usures-dentaires.html">Usure dentaire</a></li><li><a href="erosion-dentaire.html">Érosion dentaire</a></li><li><a href="bruxisme-usure-dentaire.html">Bruxisme</a></li><li><a href="tca-dents.html">Troubles des conduites alimentaires</a></li></ul></div>
      <div><h4>Mon exercice</h4><ul><li><a href="franck-moyal.html">Parcours</a></li><li><a href="publications.html">Publications</a></li><li><a href="activite-hospitaliere.html">Activité hospitalière</a></li></ul></div>
      <div><h4>Les deux espaces</h4><ul><li><a href="espace-patients.html">Espace patients</a></li><li><a href="espace-pro.html">Espace pro</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    </div>
    <p class="pied__bas">Maquette de refonte — rien n’est en ligne. Mentions légales.</p>
  </div>
  <div class="barre-mobile" aria-label="Contact rapide">
    <a href="mailto:drfranckmoyal@gmail.com?subject=Demande%20de%20rendez-vous%20-%20Dr%20Franck%20Moyal">Écrire</a>
    <a href="tel:+33183755216">Appeler</a>
    <a href="https://www.google.com/maps/dir/?api=1&amp;destination=48.8770687,2.3417544" target="_blank" rel="noopener">Itinéraire</a>
  </div>
</footer>'''


def photo(p, classe="solo"):
    alts = p.get("alt") or [""]
    if len(p["src"]) >= 2:
        imgs = "".join(
            f'<img src="{s}" alt="{H.escape(alts[i] if i < len(alts) else "")}" loading="lazy">'
            for i, s in enumerate(p["src"][:2]))
        bloc = f'<div class="paire">{imgs}</div>'
    else:
        bloc = f'<img src="{p["src"][0]}" alt="{H.escape(alts[0])}" loading="lazy">'
        classe = "solo"
    leg = f'<figcaption>{e(p["legende"])}</figcaption>' if p["legende"] else ""
    return f'<figure class="{classe}">{bloc}{leg}</figure>'


def rendre(page):
    slug = page["slug"]
    surtitre, public, libelle = PUBLIC.get(slug, ("", None, page["h1"][:40]))
    ariane = '<a href="index.html">Accueil</a>'
    if public:
        ariane += f' › {e(public)}'
    ariane += f' › {e(libelle)}'

    corps = []
    photos = list(page["photos"])
    ouverture = photos.pop(0) if photos else None

    # ── la une ──
    fig = ""
    if ouverture:
        src = ouverture["src"][0]
        alt = H.escape((ouverture.get("alt") or [""])[0])
        leg = f'<figcaption>{e(ouverture["legende"])}</figcaption>' if ouverture["legende"] else ""
        fig = f'      <figure><img src="{src}" alt="{alt}">{leg}</figure>\n'
    corps.append(f'''  <div class="contenu">
    <p class="ariane">{ariane}</p>
    <div class="une">
      <div>
        {f'<p class="eyebrow">{e(surtitre)}</p>' if surtitre else ""}
        <h1>{e(grand_titre(slug, page["h1"])[0])}</h1>
{soustitre(grand_titre(slug, page["h1"])[1])}
{f'        <p class="une__chapo">{e(page["chapo"])}</p>' if page["chapo"] else ""}
        <div class="signature">
          <img src="{PORTRAIT}" alt="Dr Franck Moyal">
          <div><b>Dr Franck Moyal</b> — chirurgien-dentiste, Paris 9<sup>e</sup><br>
            Praticien hospitalier, Pitié-Salpêtrière · CMME, Sainte-Anne</div>
        </div>
      </div>
{fig}    </div>
  </div>''')

    # ── les sections ──
    # La première section d'une page n'a pas de titre : c'est le bloc d'ouverture,
    # déjà repris dans la une. L'imprimer une seconde fois répétait le chapô.
    sections = page["sections"]
    if sections and not sections[0]["titre"]:
        sections = sections[1:]
    zone = False
    for i, s in enumerate(sections):
        if not s["titre"] and not s["p"]:
            continue
        zone = not zone
        cls = "sect sect--zone" if zone else "sect"
        titre = f'<h2>{e(s["titre"])}</h2>' if s["titre"].strip() else ""
        paras = "\n        ".join(f"<p>{e(p)}</p>" for p in s["p"][:4])
        liens = ""
        if s["liens"]:
            liens = '\n        <p class="suite">' + " · ".join(
                f'<a href="{FONDUES_VERS.get(h.strip("/"), h.strip("/"))}.html">{e(l)}</a>'
                for h, l in s["liens"]
            ) + "</p>"

        if s["li"]:
            items = "\n            ".join(f"<li>{e(l)}</li>" for l in s["li"][:7])
            corps.append(f'''  <section class="{cls}">
    <div class="contenu chapitre">
      <div>
        {titre}
        {paras}{liens}
      </div>
      <div class="fiche">
        <h4>En bref</h4>
        <ul>
            {items}
        </ul>
      </div>
    </div>
  </section>''')
        else:
            inner = f'<div class="deux-col">{paras}</div>' if len(s["p"]) >= 3 else paras
            img = ""
            if photos and i % 2 == 1:
                img = f'\n      <div class="cas">{photo(photos.pop(0), "paire-ou-solo")}</div>'
            corps.append(f'''  <section class="{cls}">
    <div class="contenu">
      <div class="chapitre chapitre--plein">
        <div>
          {titre}
          {inner}{liens}
        </div>
      </div>{img}
    </div>
  </section>''')

    # ── photographies restantes ──
    if photos:
        figs = "\n        ".join(photo(p) for p in photos)
        corps.append(f'''  <section class="sect">
    <div class="contenu">
      <p class="eyebrow">Cas cliniques</p>
      <h2>Cas du cabinet, photographiés avant et après</h2>
      <div class="cas">
        {figs}
      </div>
    </div>
  </section>''')

    # ── questions ──
    if page["faq"]:
        qs = "\n        ".join(
            f'<div><h3>{e(q["q"])}</h3><p>{e(q["r"])}</p></div>' for q in page["faq"][:8]
        )
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu">
      <h2 class="tete-bande">Questions fréquentes</h2>
      <div class="qa">
        {qs}
      </div>
    </div>
  </section>''')

    # ── appel ──
    # Sur la page contact, « Prendre rendez-vous » renvoyait à la page contact :
    # un bouton qui ne mène nulle part. Elle reçoit les deux vraies actions.
    if slug == "contact":
        corps.append('''  <section class="appel">
    <div class="contenu">
      <h2>Prendre rendez-vous</h2>
      <p>Par téléphone pour un rendez-vous, par courriel pour une question
        avant de venir.</p>
      <p class="appel__duo">
        <a class="bouton" href="tel:+33183755216">Appeler le cabinet</a>
        <a class="bouton bouton--clair" href="mailto:drfranckmoyal@gmail.com?subject=Demande%20de%20rendez-vous%20-%20Dr%20Franck%20Moyal">Écrire au cabinet</a>
      </p>
    </div>
  </section>''')
    else:
        corps.append('''  <section class="appel">
    <div class="contenu">
      <h2>Faire le point</h2>
      <p>Un bilan permet de comprendre l’état des dents et les options possibles,
        avant tout engagement.</p>
      <a class="bouton" href="contact.html">Prendre rendez-vous</a>
    </div>
  </section>''')

    # ── sources ──
    if page["sources"]:
        src = "\n        ".join(f"<li>{e(s)}</li>" for s in page["sources"])
        corps.append(f'''  <section class="sect sect--serre">
    <div class="contenu sources">
      <p class="eyebrow">Sources scientifiques</p>
      <ol>
        {src}
      </ol>
    </div>
  </section>''')

    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(page["title"])}</title>
<meta name="description" content="{H.escape(page["description"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap">
<link rel="stylesheet" href="style.css?v={VERSION}">
{chr(10).join(page.get("jsonld") or [])}
</head>
<body>

{menu(slug)}

<main>

{chr(10).join(corps)}

</main>

{PIED}

<script src="menu.js"></script>
</body>
</html>
'''


# ── exécution ─────────────────────────────────────────────────────────────────
# Les trois pages nouvelles (la porte d'entrée et les deux espaces) n'existent pas
# dans le site en ligne : elles n'ont donc pas de données structurées à reprendre.
# On leur en fabrique, sur le même modèle que les autres, pour que les moteurs et
# les IA sachent qui parle, où, et ce que la page rassemble.
NOUVELLES = {
    "index": {
        "type": "WebPage",
        "chemin": "",
        "nom": "Dr Franck Moyal | Dentisterie esthétique et adhésive à Paris 9e",
        "desc": "Chirurgien-dentiste à Paris 9e, exercice exclusif en dentisterie "
                "esthétique et adhésive. Espace patients et espace professionnel.",
        "fil": [],
    },
    "espace-patients": {
        "type": "CollectionPage",
        "chemin": "espace-patients/",
        "nom": "Espace patients | Dr Franck Moyal",
        "desc": "Les actes un par un — facettes, composite bonding, éclaircissement, "
                "infiltration ICON, réhabilitation des dents usées, bilan esthétique.",
        "fil": [("Espace patients", "espace-patients/")],
    },
    "espace-pro": {
        "type": "CollectionPage",
        "chemin": "espace-pro/",
        "nom": "Espace pro | Dr Franck Moyal",
        "desc": "Conférences et formations, publications, activité hospitalière et "
                "cas documentés, pour les chirurgiens-dentistes.",
        "fil": [("Espace pro", "espace-pro/")],
    },
}
RACINE_WEB = "https://drfranckmoyal.fr/"


def _socle():
    """Les nœuds d'identité (le site, la personne, le cabinet) sont relevés sur une
    page existante plutôt que recopiés à la main : ils ne peuvent pas diverger."""
    for nom in ("contact.html", "franck-moyal.html"):
        chemin = os.path.join(SORTIE, nom)
        if not os.path.exists(chemin):
            continue
        blocs = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',
                           open(chemin, encoding="utf-8").read(), re.S)
        for b in blocs:
            try:
                graphe = json.loads(b).get("@graph", [])
            except Exception:
                continue
            garde = [n for n in graphe
                     if n.get("@type") in ("WebSite", "Person", "Dentist")]
            if len(garde) == 3:
                return garde
    return []


def donnees_structurees(slug):
    fiche = NOUVELLES.get(slug)
    socle = _socle()
    if not fiche or not socle:
        return ""
    url = RACINE_WEB + fiche["chemin"]
    page = {
        "@type": fiche["type"],
        "@id": url + "#page",
        "url": url,
        "name": fiche["nom"],
        "description": fiche["desc"],
        "inLanguage": "fr-FR",
        "isPartOf": {"@id": RACINE_WEB + "#website"},
        "author": {"@id": RACINE_WEB + "#franck-moyal"},
    }
    graphe = [socle[0], page]
    if fiche["fil"]:
        page["breadcrumb"] = {"@id": url + "#fil"}
        elements = [{"@type": "ListItem", "position": 1, "name": "Accueil",
                     "item": RACINE_WEB}]
        for i, (nom, chemin) in enumerate(fiche["fil"], start=2):
            elements.append({"@type": "ListItem", "position": i, "name": nom,
                             "item": RACINE_WEB + chemin})
        graphe.append({"@type": "BreadcrumbList", "@id": url + "#fil",
                       "itemListElement": elements})
    graphe += socle[1:]
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": graphe},
                         ensure_ascii=False)
            + "</script>")


def jsonld_dorigine(slug):
    """Pour une page refaite à la main, les données structurées se relisent
    directement dans le site en ligne : rien n'est réécrit."""
    for chemin in (os.path.join(DIST, slug, "index.html"),):
        if os.path.exists(chemin):
            return "\n".join(re.findall(
                r'<script type="application/ld\+json"[^>]*>.*?</script>',
                open(chemin, encoding="utf-8").read(), re.S))
    return ""


# Le grand titre d'une page, c'est le nom de l'acte — ou, pour un sujet clinique,
# son nom de métier. Franck, 17/10/2026 : « JE VEUX EN GRAND TITRE DE PAGE LES
# ACTES… FACETTES COMPOSITE ETC ! le nom de l'acte ! »
# La phrase qui servait de H1 n'est pas perdue : elle passe en sous-titre, juste
# dessous. Le <title> et la description de la page ne bougent pas : ce sont eux
# que Google affiche dans ses résultats.
TITRES = {
    # les actes
    "facettes-dentaires-paris": ("Facettes", "Céramique collée"),
    "composite-bonding-paris": ("Composite bonding", "Résine stratifiée, en une séance"),
    "eclaircissement-dentaire-paris": ("Éclaircissement dentaire", "Gouttières à domicile"),
    "taches-dentaires-dyschromies-icon": ("Infiltration ICON", "Taches blanches, MIH, fluorose"),
    "rehabilitation-dents-usees": ("Réhabilitation des dents usées", "Technique additive"),
    "bilan-esthetique-personnalise": ("Bilan esthétique", "Première consultation"),
    # pour s'y retrouver
    "dentisterie-esthetique-paris": ("Dentisterie esthétique", "Vue d’ensemble des actes"),
    "facettes-ou-composite": ("Facettes ou composite ?", "Comparatif"),
    # ce que l'on traite
    "usures-dentaires": ("Usure dentaire", "Attrition, érosion, abrasion"),
    "erosion-dentaire": ("Érosion dentaire", "Origines et prévention"),
    "bruxisme-usure-dentaire": ("Bruxisme", "Serrement, grincement, gouttière"),
    "dents-courtes-usees": ("Dents courtes ou usées", "Usure du bord ou excès de gencive"),
    "tca-dents": ("Troubles des conduites alimentaires", "Anorexie, boulimie"),
    "anorexie-erosion-dentaire-sans-vomissements": ("Anorexie restrictive", "Érosion sans vomissements"),
    # le praticien, le cabinet
    "franck-moyal": ("Dr Franck Moyal", "Chirurgien-dentiste, Paris 9ᵉ"),
    "chirurgien-dentiste-paris-9": ("Le cabinet", "2 rue Hippolyte Lebas, Paris 9ᵉ"),
    "contact": ("Contact", "01 83 75 52 16"),
    "conferences-formations": ("Conférences et formations", ""),
    "publications": ("Publications", ""),
    "activite-hospitaliere": ("Activité hospitalière", "Pitié-Salpêtrière, CMME de Sainte-Anne"),
    "medias-interviews": ("Médias et interviews", ""),
}


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


def soustitre(texte):
    if not texte:
        return ""
    return f'        <p class="sous-titre">{e(texte)}</p>'


def grand_titre(slug, h1_dorigine):
    """Rend (titre, sous-titre). Sans entrée dans TITRES, la page garde son H1.
    Une ligne « titre.slug = … » dans phrases.txt l'emporte toujours."""
    titre, sous = TITRES.get(slug, (h1_dorigine, ""))
    return titre, phrases("titre").get(slug, sous)


CAS = [
    ("Usures : facettes minimalement invasives", "cas-usures-dentaires-facettes-minimalement-invasives"),
    ("Planification d’une réhabilitation", "cas-planification-rehabilitation-facettes"),
    ("Planification de facettes céramique", "cas-planification-facettes-ceramique"),
    ("MIH : éclaircissement et infiltration", "cas-mih-eclaircissement-erosion-infiltration"),
]
AUTRES = [
    ("Mon parcours", "franck-moyal"),
    ("Le cabinet, Paris 9ᵉ", "chirurgien-dentiste-paris-9"),
    ("Anorexie et érosion", "anorexie-erosion-dentaire-sans-vomissements"),
    ("Contact", "contact"),
    ("Mentions légales", "mentions-legales"),
]


def sommaire():
    """Le sommaire se fabrique à partir des pages réellement présentes : il ne peut
    plus annoncer un nombre de pages que le dossier ne contient pas."""
    presentes = {n[:-5] for n in os.listdir(SORTIE) if n.endswith(".html")}
    comptees = presentes - {"index", "sommaire"}

    def colonne(titre, items):
        liens = "\n".join(
            '          <li><a href="%s.html">%s</a></li>' % (sl, e(l))
            for l, sl in items if sl in presentes)
        return ('        <div>\n          <h3>%s</h3>\n          <ul>\n%s\n'
                '          </ul>\n        </div>' % (e(titre), liens))

    chapitres, mots = [], 0
    for sl in sorted(comptees):
        h = open(os.path.join(SORTIE, sl + ".html"), encoding="utf-8").read()
        corps = re.search(r"<main.*?</main>", h, re.S)
        if corps:
            mots += len(re.sub(r"<[^>]+>", " ", corps.group(0)).split())
        chapitres.append(len(re.findall(r"<h2", h)))
    med = sorted(chapitres)[len(chapitres) // 2] if chapitres else 0

    corps = "\n".join([
        colonne("La porte d’entrée", [("Page d’accueil — les deux espaces", "index")]),
        colonne("Les deux espaces", [("Espace patients", "espace-patients"),
                                     ("Espace pro", "espace-pro")]),
        colonne("Les actes", ACTES),
        colonne("Ce que l’on traite", SUJETS),
        colonne("Pour choisir", POUR_CHOISIR),
        colonne("Cas documentés", CAS),
        colonne("Pour les confrères", CONFRERES),
        colonne("Mon parcours et le cabinet", AUTRES),
    ])

    gabarit = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "sommaire.gabarit.html"), encoding="utf-8").read()
    return (gabarit.replace("@@STYLE@@", VERSION)
                   .replace("@@PAGES@@", str(len(comptees)))
                   .replace("@@CHAPITRES@@", str(med))
                   .replace("@@MOTS@@", str(mots // 1000))
                   .replace("@@CORPS@@", corps))


# ── maillage interne dans le texte ──────────────────────────────────────────
# Dans chaque page de contenu, la première mention d'un sujet qui a sa page
# devient un lien vers elle — dans les paragraphes et les listes, jamais dans
# les titres, jamais deux fois vers la même page, jamais vers la page elle-même.
# Franck, 19/10/2026 : « recherche un maximum de connexions de ce type ».
# Les motifs vont du plus précis au plus général : « facettes ou composite »
# se décide avant « facettes ».
LIENS_DANS_LE_TEXTE = [
    ("facettes-ou-composite", [r"facettes? ou composites?"]),
    ("facettes-dentaires-paris", [r"facettes? (?:en )?c[ée]ramiques?", r"\bfacettes?\b"]),
    ("composite-bonding-paris", [r"composite bonding", r"composites? stratifi[ée]s?", r"\bcomposites?\b"]),
    ("eclaircissement-dentaire-paris", [r"[ée]claircissement dentaire", r"[ée]claircissement", r"blanchiment dentaire", r"\bblanchiment\b"]),
    ("taches-dentaires-dyschromies-icon", [r"taches? blanches?", r"infiltration de r[ée]sine", r"\bMIH\b", r"\bICON\b"]),
    ("usures-dentaires", [r"usures? dentaires?", r"\busures?\b"]),
    ("erosion-dentaire", [r"[ée]rosion dentaire", r"\b[ée]rosions?\b"]),
    ("bruxisme-usure-dentaire", [r"\bbruxisme\b"]),
    ("dents-courtes-usees", [r"dents courtes"]),
    ("tca-dents", [r"troubles? des conduites alimentaires", r"troubles? du comportement alimentaire", r"\bTCA\b"]),
    ("anorexie-erosion-dentaire-sans-vomissements", [r"anorexie restrictive", r"\banorexie\b"]),
    ("bilan-esthetique-personnalise", [r"bilan esth[ée]tique"]),
    ("rehabilitation-dents-usees", [r"r[ée]habilitation des dents us[ée]es", r"r[ée]habilitation adh[ée]sive"]),
    ("dentisterie-esthetique-paris", [r"dentisterie esth[ée]tique(?: et adh[ée]sive)?"]),
]
SANS_MAILLAGE = {"index", "espace-patients", "espace-pro", "contact", "sommaire",
                 "polices", "mentions-legales"}
MAILLAGE_MAX = 8


def relier_dans_le_texte(page, slug):
    """Pose les liens dans <main>, dans les seuls nœuds de texte des <p> et <li>
    qui ne sont ni dans un lien, ni dans une figure, ni dans un titre."""
    if slug in SANS_MAILLAGE:
        return page, []
    m = re.search(r"<main.*?</main>", page, re.S)
    if not m:
        return page, []
    main = m.group(0)
    deja = set(re.findall(r'<a class="lt" href="([a-z0-9-]+)\.html"', main))
    poses = []

    # découpe en segments : balises / texte ; on sait à tout moment si l'on est
    # dans un lien, une figure ou un titre, et si l'on est dans un <p> ou <li>
    morceaux = re.split(r"(<[^>]+>)", main)
    dans_a = dans_fig = dans_titre = 0
    dans_pli = 0
    exclus = ("ariane", "eyebrow", "sous-titre", "numero", "sig", "tuile", "prise",
              "joindre", "lieu", "reseau", "appel__", "suite", "renvoi", "lire-aussi")
    etat = []  # pour chaque morceau de texte : (index, autorisé ?)
    for i, x in enumerate(morceaux):
        if x.startswith("<"):
            nom = re.match(r"</?([a-zA-Z0-9]+)", x)
            nom = nom.group(1).lower() if nom else ""
            fermant = x.startswith("</")
            if nom == "a": dans_a += -1 if fermant else 1
            elif nom in ("figure", "figcaption"): dans_fig += -1 if fermant else 1
            elif nom in ("h1", "h2", "h3", "h4", "h5"): dans_titre += -1 if fermant else 1
            elif nom in ("p", "li"):
                if fermant: dans_pli = max(0, dans_pli - 1)
                else:
                    cls = re.search(r'class="([^"]*)"', x)
                    ok = not (cls and any(e_ in cls.group(1) for e_ in exclus))
                    dans_pli += 1 if ok else 0
            continue
        etat.append((i, dans_a == 0 and dans_fig == 0 and dans_titre == 0 and dans_pli > 0))

    for cible, motifs in LIENS_DANS_LE_TEXTE:
        if cible == slug or cible in deja or len(poses) >= MAILLAGE_MAX:
            continue
        fait = False
        for motif in motifs:
            rx = re.compile(motif, re.I)
            for i, ok in etat:
                if not ok:
                    continue
                mm = rx.search(morceaux[i])
                if not mm:
                    continue
                txt = morceaux[i]
                morceaux[i] = (txt[:mm.start()] + f'<a class="lt" href="{cible}.html">'
                               + txt[mm.start():mm.end()] + "</a>" + txt[mm.end():])
                poses.append((cible, txt[mm.start():mm.end()]))
                fait = True
                break
            if fait:
                break
    if not poses:
        return page, []
    return page.replace(main, "".join(morceaux), 1), poses


MAILLAGE_JOURNAL = {}


def reharmoniser():
    """Les pages écrites à la main gardaient chacune sa copie du menu et du pied,
    qui prenaient du retard dès qu'on touchait à l'un des deux. Elles vont désormais
    les rechercher ici : une seule source, plus de divergence possible."""
    reprises = []
    for nom in sorted(os.listdir(SORTIE)):
        if not nom.endswith(".html"):
            continue
        chemin = os.path.join(SORTIE, nom)
        page = open(chemin, encoding="utf-8").read()
        avant = page
        # le portail n'a ni menu ni pied : il ne reçoit que la signature du style
        if '<header class="entete">' in page:
            page = re.sub(r'<header class="entete">.*?</header>',
                          lambda _m: menu(nom[:-5]), page, flags=re.S)
        if '<footer class="pied">' in page:
            page = re.sub(r'<footer class="pied">.*?</footer>',
                          lambda _m: PIED, page, flags=re.S)
        # le grand titre : l'acte, pas la phrase (voir TITRES)
        slug = nom[:-5]
        if slug in PUBLIC and PUBLIC[slug][0]:
            page = re.sub(r'<p class="eyebrow">[^<]*</p>',
                          lambda _m: f'<p class="eyebrow">{e(PUBLIC[slug][0])}</p>',
                          page, count=1)
        if slug in TITRES:
            titre, sous = TITRES[slug]
            page = re.sub(r"<h1>.*?</h1>", lambda _m: f"<h1>{e(titre)}</h1>", page,
                          count=1, flags=re.S)
            if sous:
                if '<p class="sous-titre">' in page:
                    page = re.sub(r'<p class="sous-titre">.*?</p>',
                                  lambda _m: f'<p class="sous-titre">{e(sous)}</p>',
                                  page, count=1, flags=re.S)
                else:
                    page = page.replace(f"<h1>{e(titre)}</h1>",
                                        f'<h1>{e(titre)}</h1>\n'
                                        f'        <p class="sous-titre">{e(sous)}</p>', 1)
        page = re.sub(r'style\.css\?v=\d+', f"style.css?v={VERSION}", page)
        page, poses = relier_dans_le_texte(page, slug)
        if poses:
            MAILLAGE_JOURNAL[slug] = poses
        # Une page sans données structurées est muette pour les moteurs et les IA :
        # on les reprend du site en ligne, ou on les fabrique si la page est neuve.
        if "application/ld+json" not in page and nom != "sommaire.html":
            bloc = jsonld_dorigine(nom[:-5]) or donnees_structurees(nom[:-5])
            if bloc:
                page = page.replace("</head>", bloc + "\n</head>", 1)
        if page != avant:
            open(chemin, "w", encoding="utf-8").write(page)
            reprises.append(nom)
    return reprises


def main():
    slugs = sorted(
        d for d in os.listdir(DIST)
        if os.path.isdir(os.path.join(DIST, d))
        and os.path.exists(os.path.join(DIST, d, "index.html"))
        and d not in ("_astro", "cas-cliniques")
    )
    for cas in sorted(os.listdir(os.path.join(DIST, "cas-cliniques"))
                      if os.path.isdir(os.path.join(DIST, "cas-cliniques")) else []):
        if os.path.exists(os.path.join(DIST, "cas-cliniques", cas, "index.html")):
            slugs.append(f"cas-cliniques/{cas}")

    faits, passes = [], []
    for slug in slugs:
        court = slug.replace("cas-cliniques/", "cas-")
        if court in A_LA_MAIN:
            passes.append((court, "faite à la main"))
            continue
        if court in FONDUES:
            passes.append((court, "fondue dans les usures (D77)"))
            continue
        page = lire(slug)
        if not page:
            passes.append((court, "illisible"))
            continue
        page["slug"] = court
        open(os.path.join(SORTIE, f"{court}.html"), "w", encoding="utf-8").write(rendre(page))
        faits.append((court, len(page["sections"]), len(page["faq"]), len(page["photos"])))

    print(f"{len(faits)} page(s) générée(s) dans docs/refonte/maquettes/site/\n")
    print(f"  {'page':44s} {'chapitres':>9s} {'questions':>9s} {'photos':>6s}")
    for c, ns, nf, np_ in faits:
        alerte = "  ← encore trop de chapitres" if ns > 7 else ""
        print(f"  {c:44s} {ns:9d} {nf:9d} {np_:6d}{alerte}")
    if passes:
        print("\n  non générées :")
        for c, pourquoi in passes:
            print(f"    {c:42s} {pourquoi}")
    open(os.path.join(SORTIE, "sommaire.html"), "w", encoding="utf-8").write(sommaire())
    reprises = reharmoniser()
    if MAILLAGE_JOURNAL:
        total = sum(len(v) for v in MAILLAGE_JOURNAL.values())
        print(f"\n  maillage dans le texte : {total} liens posés sur {len(MAILLAGE_JOURNAL)} pages")
        for sl, poses in sorted(MAILLAGE_JOURNAL.items()):
            print(f"    {sl[:40]:40s} " + " · ".join(f"{c.split('-')[0]}←« {m} »" for c, m in poses))
    if reprises:
        print(f"\n  en-tête et pied remis à jour sur {len(reprises)} page(s) :")
        print("    " + ", ".join(r[:-5] for r in reprises))


if __name__ == "__main__":
    main()
