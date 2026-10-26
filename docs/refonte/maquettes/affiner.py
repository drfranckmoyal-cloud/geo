"""Affine la version en ligne, page par page, au moment de la publication (appelé par publier.py).

Audit du 25/10/2026, cinq points demandés par Franck « en un coup » :

1. les images, servies à la taille d'affichage et au format WebP (le JPEG ou le PNG
   restent pour les navigateurs qui ne le lisent pas) — le portrait de la signature,
   affiché en 54 px, pesait 811 Ko sur 34 pages ;
2. un aperçu de partage par page (LinkedIn, WhatsApp…), avec une image à son titre ;
3. les fiches du cabinet et du praticien complétées pour les moteurs et les IA ;
4. (l'accessibilité se règle dans la maquette : couleurs, niveaux de titres, pied de page) ;
5. une date de révision sur chaque page.

La maquette n'est pas touchée : tout se fait sur la copie déposée.
"""
import hashlib
import html as H
import json
import os
import re
import textwrap

from PIL import Image, ImageDraw, ImageFont

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
CACHE = os.path.join(DEPOT, ".cache-images.nosync")      # ignoré d'iCloud et de git
RACINE = "https://drfranckmoyal.fr"
REVISION_REFONTE = "2026-10-25"                           # mise en ligne de la refonte
# pages réécrites depuis, avec leur date (D100 : questions/réponses du 26/10/2026)
REVISIONS = {u: "2026-10-26" for u in (
    "/erosion-dentaire/", "/anorexie-erosion-dentaire-sans-vomissements/", "/composite-bonding-paris/",
    "/facettes-dentaires-paris/", "/taches-dentaires-dyschromies-icon/", "/bruxisme-usure-dentaire/",
    "/dents-courtes-usees/", "/eclaircissement-dentaire-paris/", "/bilan-esthetique-personnalise/",
    "/chirurgien-dentiste-paris-9/", "/franck-moyal/", "/facettes-ou-composite/",
    "/dentisterie-esthetique-paris/")}
LARGEURS = (400, 800, 1200, 1600)

# ── 1. les images ─────────────────────────────────────────────────────────
# taille d'affichage selon l'endroit où l'image est posée (la classe la plus proche)
TAILLES = [
    ("signature", None),                                   # vignette ronde de 54 px
    ("tuile__portrait", "(max-width: 720px) 118px, 190px"),
    ("espaces__portrait", "(max-width: 720px) 92vw, 780px"),
    ("vignette-video__image", "120px"),
    ("carte-video", "(max-width: 560px) 46vw, 280px"),
    ("tuile__visuel", "(max-width: 720px) 45vw, 320px"),
    ("tuile__paire", "(max-width: 720px) 46vw, 300px"),
    ("guide__apercu", None),                               # déjà petit
    ("parcours", "(max-width: 1180px) 92vw, 1100px"),
    ("une", "(max-width: 900px) 92vw, 540px"),
    ("cote", "(max-width: 900px) 92vw, 400px"),
]
DEFAUT = "(max-width: 900px) 92vw, 700px"


def _cache(source, largeur, fmt):
    os.makedirs(CACHE, exist_ok=True)
    cle = hashlib.sha1(f"{os.path.getmtime(source)}:{os.path.getsize(source)}:{source}".encode()).hexdigest()[:16]
    return os.path.join(CACHE, f"{cle}-{largeur}.{fmt}")


def _variante(source, largeur, fmt, sortie):
    """Une version de l'image à cette largeur, depuis le cache si elle y est."""
    cache = _cache(source, largeur, fmt)
    if not os.path.exists(cache):
        im = Image.open(source)
        transparent = im.mode in ("RGBA", "LA", "P") and fmt != "jpg"
        im = im.convert("RGBA" if transparent else "RGB")
        if im.width > largeur:
            im = im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS)
        if fmt == "webp":
            im.save(cache, "WEBP", quality=78, method=6)
        elif fmt == "png":
            im.save(cache, "PNG", optimize=True)
        else:
            im.save(cache, "JPEG", quality=80, optimize=True, progressive=True)
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    with open(cache, "rb") as a, open(sortie, "wb") as b:
        b.write(a.read())


VIDES = {"img", "br", "hr", "meta", "link", "source", "input", "wbr", "path", "stop", "circle", "rect", "use"}


def _contexte(page, pos, balise):
    """La taille d'affichage de l'image, d'après sa propre classe puis celles de ses ancêtres,
    du plus proche au plus lointain. (Une première version prenait la classe la plus proche
    dans le texte : l'image d'en-tête, posée juste après la signature, passait pour elle.)"""
    debut = page.find("<body")
    pile = []
    for m in re.finditer(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>", page[debut:pos]):
        ferme, nom, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if nom in VIDES or attrs.rstrip().endswith("/"):
            continue
        if ferme:
            while pile and pile.pop()[0] != nom:
                pass
        else:
            classe = re.search(r'\bclass="([^"]*)"', attrs)
            pile.append((nom, classe.group(1).split() if classe else []))
    propre = re.search(r'\bclass="([^"]*)"', balise)
    niveaux = [propre.group(1).split() if propre else []] + [c for _, c in reversed(pile)]
    for classes in niveaux:
        for cle, tailles in TAILLES:
            if cle in classes:
                return cle, tailles
    return None


def images(page, a_copier, sortie, problemes):
    """Chaque image servie à sa taille d'affichage, en WebP avec repli JPEG ou PNG."""
    def une(m):
        balise, src = m.group(0), m.group(1)
        source = a_copier.get(src)
        if not source or not os.path.exists(source) or not src.lower().endswith((".jpg", ".jpeg", ".png")):
            return balise
        ctx = _contexte(page, m.start(), balise)
        base, ext = os.path.splitext(src)
        repli = "png" if ext.lower() == ".png" else "jpg"
        largeur_origine = Image.open(source).width
        if ctx and ctx[0] == "guide__apercu":
            return balise
        if ctx and ctx[0] == "signature":
            for fmt in ("webp", repli):
                _variante(source, 160, fmt, os.path.join(sortie, f"{base}-160.{fmt}".lstrip("/")))
            img = balise.replace(f'src="{src}', f'src="{base}-160.{repli}')
            return f'<picture><source type="image/webp" srcset="{base}-160.webp">{img}</picture>'
        largeurs = [w for w in LARGEURS if w < largeur_origine] + [min(largeur_origine, 2000)]
        largeurs = sorted(set(largeurs))
        for w in largeurs:
            for fmt in ("webp", repli):
                _variante(source, w, fmt, os.path.join(sortie, f"{base}-{w}.{fmt}".lstrip("/")))
        tailles = (ctx[1] if ctx and ctx[1] else DEFAUT)
        srcset = lambda fmt: ", ".join(f"{base}-{w}.{fmt} {w}w" for w in largeurs)
        moyenne = min(largeurs, key=lambda w: abs(w - 800))
        img = re.sub(r'\bsrc="[^"]*"', f'src="{base}-{moyenne}.{repli}" srcset="{srcset(repli)}" sizes="{tailles}"', balise, count=1)
        if ctx and ctx[0] == "espaces__portrait":         # l'image principale de l'accueil
            img = img.replace("<img ", '<img fetchpriority="high" ', 1).replace(' loading="lazy"', "")
        return f'<picture><source type="image/webp" srcset="{srcset("webp")}" sizes="{tailles}">{img}</picture>'
    return re.sub(r'<img\b[^>]*\bsrc="(/assets/(?:photos|img|videos)/[^"?]+)(?:\?[^"]*)?"[^>]*>', une, page)


# ── 2. l'aperçu de partage ────────────────────────────────────────────────
def _police(fichiers, taille):
    for f in fichiers:
        try:
            return ImageFont.truetype(f, taille)
        except OSError:
            continue
    return ImageFont.load_default()


SERIF = [os.path.join(DEPOT, "src/assets/fonts/source-serif-4-latin.woff2"),
         "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"]
SANS = [os.path.join(DEPOT, "src/assets/fonts/archivo-latin.woff2"),
        "/System/Library/Fonts/Supplemental/Arial.ttf"]
SANS_GRAS = ["/System/Library/Fonts/Supplemental/Arial Bold.ttf"]


def image_de_partage(titre, nom, portrait, sortie):
    """1200 × 630 : le titre de la page à gauche, le portrait à droite, aux couleurs du site."""
    chemin = os.path.join(sortie, "assets", "partage", f"{nom}.jpg")
    cle = hashlib.sha1(f"v2:{titre}:{os.path.getmtime(portrait)}".encode()).hexdigest()[:16]
    cache = os.path.join(CACHE, f"partage-{cle}.jpg")
    os.makedirs(CACHE, exist_ok=True)
    if not os.path.exists(cache):
        toile = Image.new("RGB", (1200, 630), (250, 248, 243))
        p = Image.open(portrait).convert("RGBA")
        h = 600
        p = p.resize((round(p.width * h / p.height), h), Image.LANCZOS)
        toile.paste(p, (1200 - p.width + 40, 630 - h), p)
        d = ImageDraw.Draw(toile)
        d.rectangle((70, 92, 130, 96), fill=(31, 34, 31))
        d.text((70, 112), "DR FRANCK MOYAL · CHIRURGIEN-DENTISTE, PARIS 9E", font=_police(SANS_GRAS, 20),
               fill=(88, 93, 90))
        # typographie française : pas de « : » ni de « 9e » seuls en début de ligne
        titre = titre.replace(" :", "\u00a0:").replace(" 9e", "\u00a09e").replace(" ?", "\u00a0?")
        taille = 64
        while taille > 40:
            police = _police(SERIF, taille)
            try:
                police.set_variation_by_name("Bold")           # le gras des titres du site
            except (OSError, ValueError, AttributeError):
                pass
            lignes = textwrap.wrap(titre, width=max(10, int(520 / (taille * 0.55))))
            if len(lignes) <= 4 and all(d.textlength(l, font=police) <= 600 for l in lignes):
                break
            taille -= 4
        y = 165
        for l in lignes:
            d.text((68, y), l, font=police, fill=(26, 28, 25))
            y += int(taille * 1.16)
        d.text((70, 560), "drfranckmoyal.fr", font=_police(SANS, 26), fill=(88, 93, 90))
        toile.save(cache, "JPEG", quality=86, optimize=True, progressive=True)
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(cache, "rb") as a, open(chemin, "wb") as b:
        b.write(a.read())
    return f"/assets/partage/{nom}.jpg"


def partage(page, url, portrait, sortie):
    """Les balises lues par LinkedIn, WhatsApp, Facebook et X quand on partage la page."""
    titre = H.unescape(re.search(r"<title>(.*?)</title>", page, re.S).group(1).strip())
    desc = re.search(r'<meta name="description" content="([^"]*)"', page)
    desc = H.unescape(desc.group(1)) if desc else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S)
    sujet = H.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else titre
    if url == "/":
        sujet = "Dentisterie esthétique et adhésive à Paris 9e"
    nom = "accueil" if url == "/" else url.strip("/").replace("/", "-")
    image = image_de_partage(sujet, nom, portrait, sortie)
    voulues = {
        "og:type": "video.other" if url.startswith("/videos/") and url != "/videos/" else
                   ("website" if url in ("/", "/espace-patients/", "/espace-pro/", "/videos/", "/articles/") else "article"),
        "og:site_name": "Dr Franck Moyal",
        "og:locale": "fr_FR",
        "og:title": titre,
        "og:description": desc,
        "og:url": RACINE + url,
        "og:image": RACINE + image,
        "og:image:width": "1200",
        "og:image:height": "630",
        "og:image:alt": f"{sujet} — Dr Franck Moyal, chirurgien-dentiste à Paris 9e",
    }
    ajout = []
    for prop, val in voulues.items():
        if f'property="{prop}"' not in page:
            ajout.append(f'<meta property="{prop}" content="{H.escape(val)}">')
    if 'name="twitter:card"' not in page:
        ajout.append('<meta name="twitter:card" content="summary_large_image">')
    if ajout:
        page = page.replace("</head>", "\n".join(ajout) + "\n</head>", 1)
    return page


# ── 3 et 5. les données pour les moteurs et les IA ───────────────────────
CABINET = {
    "image": RACINE + "/assets/img/portrait-franck.jpg",
    "geo": {"@type": "GeoCoordinates", "latitude": 48.8770687, "longitude": 2.3417544},
    "hasMap": "https://www.google.com/maps?cid=151850546430860136",
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["https://schema.org/Tuesday", "https://schema.org/Friday"],
                                   "opens": "09:00", "closes": "19:00"}],
    "areaServed": {"@type": "City", "name": "Paris"},
    "sameAs": ["https://www.google.com/maps?cid=151850546430860136",
               "https://www.doctolib.fr/dentiste/paris/franck-moyal"],
    "founder": {"@id": RACINE + "/#franck-moyal"},
}
PRATICIEN = {
    "description": ("Chirurgien-dentiste à Paris 9e, exercice exclusif en dentisterie esthétique et adhésive. "
                    "Praticien hospitalier à la Pitié-Salpêtrière et praticien attaché à la CMME de l'hôpital "
                    "Sainte-Anne ; prise en charge des usures dentaires et des atteintes dentaires des troubles "
                    "des conduites alimentaires."),
    "knowsAbout": ["Dentisterie esthétique", "Dentisterie adhésive", "Usure dentaire", "Érosion dentaire",
                   "Troubles des conduites alimentaires et santé bucco-dentaire", "Réhabilitation des dents usées",
                   "Facettes dentaires", "Composite stratifié", "Composite bonding", "Éclaircissement dentaire",
                   "Infiltration de résine (ICON)", "MIH", "Bruxisme"],
    "affiliation": [
        {"@type": "Hospital", "name": "Hôpital Pitié-Salpêtrière (AP-HP)",
         "url": "https://pitiesalpetriere.aphp.fr/"},
        {"@type": "Hospital", "name": "CMME, hôpital Sainte-Anne (GHU Paris psychiatrie & neurosciences)",
         "url": "https://www.ghu-paris.fr/"},
    ],
    "memberOf": [{"@type": "Organization", "name": "DenTCA", "url": "https://dentca-asso.com/",
                  "description": "Association pour la prévention et les soins des troubles dentaires liés aux "
                                 "troubles des conduites alimentaires, fondée et présidée par le Dr Franck Moyal."}],
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Université Paris Diderot (Paris VII)"},
    "worksFor": {"@id": RACINE + "/#practice"},
}
PROFILS_EN_PLUS = ["https://www.doctolib.fr/dentiste/paris/franck-moyal", "https://smileclubformations.com/",
                   "https://www.youtube.com/@drfranckmoyal"]
PAGES = {"WebPage", "MedicalWebPage", "CollectionPage", "ProfilePage", "ContactPage", "AboutPage", "Blog"}


def donnees(page, url):
    def enrichir(bloc):
        d = json.loads(bloc)
        noeuds = d.get("@graph") if isinstance(d, dict) and "@graph" in d else [d]
        for n in noeuds:
            t = n.get("@type")
            types = set(t if isinstance(t, list) else [t])
            if "Dentist" in types:
                for k, v in CABINET.items():
                    if k == "sameAs":
                        n["sameAs"] = list(dict.fromkeys((n.get("sameAs") or []) + v))
                    else:
                        n.setdefault(k, v)
            if "Person" in types and str(n.get("@id", "")).endswith("#franck-moyal"):
                for k, v in PRATICIEN.items():
                    n.setdefault(k, v)
                n["sameAs"] = list(dict.fromkeys((n.get("sameAs") or []) + PROFILS_EN_PLUS))
            if types & PAGES and str(n.get("@id", "")).startswith(RACINE + url):
                if url in REVISIONS:  # le texte a changé depuis : la date suit, même si la page en portait une
                    n["dateModified"] = REVISIONS[url]
                else:
                    n.setdefault("dateModified", REVISION_REFONTE)
        return json.dumps(d, ensure_ascii=False)
    return re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',
                  lambda m: m.group(1) + enrichir(m.group(2)) + m.group(3), page, flags=re.S)
