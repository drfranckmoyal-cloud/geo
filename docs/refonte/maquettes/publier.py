#!/usr/bin/env python3
"""Fabrique la version en ligne de la refonte, à partir de la maquette.

La maquette (site/) reste telle quelle : on la regarde sur le Mac, ses pages
s'appellent usures-dentaires.html et ses photos sont prises dans le dépôt. Ce
programme en tire, dans dist-refonte/ à la racine du dépôt, un site prêt à
déposer chez Hostinger (plan de mise en ligne, livrables/mise-en-ligne/) :

- chaque page à son adresse propre, celle du site en ligne : /usures-dentaires/,
  les cas cliniques sous /cas-cliniques/, les vidéos sous /videos/, les articles
  sous /articles/ ;
- photos, vidéos, documents et images sous /assets/, seulement ceux qui servent ;
- les polices hébergées sur le site, et plus chez Google Fonts (RGPD) ;
- une adresse de référence (canonical) sur chaque page, les icônes, le pied de
  page définitif ;
- le plan du site sous les mêmes noms qu'aujourd'hui, robots.txt, et un
  .htaccess qui redirige les pages fondues et sert une page 404 ;

puis il contrôle le résultat et s'arrête en erreur au moindre problème.

    python3 docs/refonte/maquettes/publier.py        (après construire.sh)
"""
import datetime
import html as H
import json
import os
import re
import shutil
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
SITE = os.path.join(ICI, "site")
# Le Bureau est synchronisé par iCloud : un dossier effacé puis refait aussitôt y laisse des
# copies « cas-cliniques 2 », « assets 2 »… (constaté le 25/10/2026). Un dossier en « .nosync »
# est ignoré d'iCloud ; dist-refonte n'en est qu'un raccourci, que tout le reste utilise.
SORTIE = os.path.join(DEPOT, "dist-refonte.nosync")
RACCOURCI = os.path.join(DEPOT, "dist-refonte")
PUBLIC = os.path.join(DEPOT, "public")
POLICES = os.path.join(DEPOT, "src", "assets", "fonts")
RACINE = "https://drfranckmoyal.fr"

# pages de travail de la maquette, jamais publiées
INTERNES = {"sommaire", "polices"}
# pages fondues dans une autre (D77, D95) : leur adresse redirige
FONDUES = {"diagnostic-usures-dentaires": "usures-dentaires",
           "rehabilitation-dents-usees": "usures-dentaires"}
# hors du plan du site, comme aujourd'hui
HORS_PLAN = {"mentions-legales"}
# ressources de la maquette → leur place en ligne
MEDIAS = [("../../../../src/assets/photos/cas/", "/assets/photos/"),
          ("../../../../src/assets/videos/", "/assets/videos/"),
          ("../../../../src/assets/documents/", "/assets/documents/"),
          ("img/", "/assets/img/")]
FICHIERS_SITE = {"style.css": "/assets/style.css", "menu.js": "/assets/menu.js"}

# Les données structurées reprises du site Astro citent des images de son dossier /_astro/,
# effacé à la mise en ligne de la refonte : on les remplace par leur équivalent publié ici.
ANCIENNES_IMAGES = [(r"https://drfranckmoyal\.fr/_astro/portrait-franck\.[^\"]+",
                     "/assets/img/portrait-franck.jpg", "img/portrait-franck.jpg")]

PIED_MAQUETTE = "Maquette de refonte — rien n’est en ligne. Mentions légales."
PIED_EN_LIGNE = '© 2026 Dr Franck Moyal · <a href="/mentions-legales/">Mentions légales</a>'
ICONES = ('<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
          '<link rel="icon" href="/favicon-48.png" type="image/png" sizes="48x48">\n'
          '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
          '<meta name="theme-color" content="#faf8f3">')
# les deux fichiers de police du texte courant, demandés dès l'en-tête
PRECHARGE = ('<link rel="preload" href="/assets/fonts/source-serif-4-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
             '<link rel="preload" href="/assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>')

problemes = []


def adresse(slug):
    """L'adresse en ligne d'une page de la maquette, celle du site actuel quand elle existe."""
    slug = FONDUES.get(slug, slug)
    if slug == "index":
        return "/"
    for prefixe, dossier in (("cas-", "cas-cliniques"), ("video-", "videos"), ("article-", "articles")):
        if slug.startswith(prefixe):
            return f"/{dossier}/{slug[len(prefixe):]}/"
    return f"/{slug}/"


def fichier_de(url):
    """Le fichier qui sert une adresse : /usures-dentaires/ → usures-dentaires/index.html."""
    chemin = url.split("#")[0].split("?")[0].lstrip("/")
    return os.path.join(SORTIE, chemin, "index.html") if chemin == "" or chemin.endswith("/") \
        else os.path.join(SORTIE, chemin)


def reecrire(page, slug, a_copier):
    """Les liens et les ressources de la maquette, ramenés aux adresses en ligne."""
    def un(m):
        attr, v = m.group(1), m.group(2)
        if re.match(r"(https?:|mailto:|tel:|#|data:|javascript:)", v):
            return m.group(0)
        chemin, _, fragment = v.partition("#")
        chemin, _, requete = chemin.partition("?")
        suite = (f"?{requete}" if requete else "") + (f"#{fragment}" if fragment else "")
        if chemin.endswith(".html") and "/" not in chemin:
            cible = chemin[:-5]
            if cible in INTERNES:
                problemes.append(f"{slug} : lien vers la page de travail {cible}")
            return f'{attr}="{adresse(cible)}{"#" + fragment if fragment else ""}"'
        for depart, arrivee in MEDIAS:
            if chemin.startswith(depart):
                source = os.path.normpath(os.path.join(SITE, chemin))
                destination = arrivee + chemin[len(depart):]
                a_copier[destination] = source
                return f'{attr}="{destination}{suite}"'
        if chemin in FICHIERS_SITE:
            return f'{attr}="{FICHIERS_SITE[chemin]}{suite}"'
        problemes.append(f"{slug} : chemin inconnu « {v} »")
        return m.group(0)
    return re.sub(r'\b(href|src|poster)="([^"]*)"', un, page)


def entete(page, slug, url):
    """Polices locales, icônes, adresse de référence."""
    page = re.sub(r'<link rel="preconnect" href="https://fonts\.g(?:oogleapis|static)\.com"[^>]*>\n?', "", page)
    # chaque police que la maquette demandait à Google doit être hébergée sur le site : la
    # porte d'accueil en appelait une troisième, oubliée au premier dépôt (25/10/2026)
    hebergees = open(os.path.join(POLICES, "polices.css"), encoding="utf-8").read()
    for lien in re.findall(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]*)">', page):
        for famille in re.findall(r"family=([^:&]+)", lien):
            nom = famille.replace("+", " ")
            if f"font-family:'{nom}'" not in hebergees:
                problemes.append(f"{slug} : la police « {nom} » n'est pas hébergée sur le site")
    page = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/[^"]*">\n?', "", page)
    vue = re.search(r'<meta name="viewport"[^>]*>\n', page)
    ajout = ICONES + "\n" + PRECHARGE + "\n"
    canon = f"{RACINE}{url}"
    existant = re.search(r'<link rel="canonical" href="([^"]+)">', page)
    if existant:
        if existant.group(1) != canon:
            page = page.replace(existant.group(0), f'<link rel="canonical" href="{canon}">')
    elif slug != "404":
        ajout += f'<link rel="canonical" href="{canon}">\n'
    return page[:vue.end()] + ajout + page[vue.end():]


def page_404(modele):
    """La page des adresses inconnues, avec le menu et le pied du site."""
    page = re.sub(r"<title>.*?</title>", "<title>Page introuvable | Dr Franck Moyal</title>", modele,
                  count=1, flags=re.S)
    page = re.sub(r'<meta name="description" content="[^"]*">',
                  '<meta name="description" content="Cette page n’existe pas ou a changé d’adresse.">\n'
                  '<meta name="robots" content="noindex">', page, count=1)
    page = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", page, flags=re.S)
    page = re.sub(r'<link rel="canonical"[^>]*>\n?', "", page)
    corps = '''<main>

  <section class="sect">
    <div class="contenu">
      <h1 class="tete-bande tete-bande--haut">Page introuvable</h1>
      <p class="videos__intro">Cette page n’existe pas, ou elle a changé d’adresse.</p>
      <p class="videos__toutes"><a href="/">Retour à l’accueil <span>→</span></a></p>
      <p class="videos__toutes"><a href="/espace-patients/">Espace patients <span>→</span></a></p>
      <p class="videos__toutes"><a href="/contact/">Prendre rendez-vous <span>→</span></a></p>
    </div>
  </section>

</main>'''
    return re.sub(r"<main>.*?</main>", lambda _m: corps, page, count=1, flags=re.S)


def htaccess():
    base = open(os.path.join(PUBLIC, ".htaccess"), encoding="utf-8").read().rstrip() + "\n"
    regles = "\n".join(f"RewriteRule ^{a}/?$ {RACINE}/{b}/ [R=301,L]" for a, b in sorted(FONDUES.items()))
    return base + f"""
# Les pages se revalident à chaque visite : le navigateur ne ressert jamais une ancienne
# version gardée en mémoire (l'accueil de l'ancien site, constaté le 25/10/2026).
<IfModule mod_headers.c>
  <FilesMatch "\\.html$">
    Header set Cache-Control "no-cache"
  </FilesMatch>
</IfModule>

# Pages fondues dans une autre lors de la refonte : leur adresse, connue de Google,
# mène définitivement à celle qui les a absorbées (D77, D95).
{regles}

# Les adresses inconnues : une page à l'image du site, plutôt que celle d'Hostinger.
ErrorDocument 404 /404.html

AddType font/woff2 .woff2

# Durée de conservation par le navigateur : longue pour les polices et la feuille de
# style (son adresse change à chaque version), raisonnable pour les images et vidéos.
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 week"
  ExpiresByType image/jpeg "access plus 1 month"
  ExpiresByType image/png "access plus 1 month"
  ExpiresByType image/svg+xml "access plus 1 month"
  ExpiresByType video/mp4 "access plus 1 month"
  ExpiresByType application/pdf "access plus 1 month"
</IfModule>
"""


def plan_du_site(adresses):
    jour = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{RACINE}{u}</loc><lastmod>{jour}</lastmod></url>" for u in adresses)
    plan = ('<?xml version="1.0" encoding="UTF-8"?>'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    index = ('<?xml version="1.0" encoding="UTF-8"?>'
             '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
             f'<sitemap><loc>{RACINE}/sitemap-0.xml</loc><lastmod>{jour}</lastmod></sitemap></sitemapindex>\n')
    return plan, index


def controler(adresses):
    """Tout lien interne mène à un fichier ; rien de la maquette ne subsiste."""
    for racine, _, fichiers in os.walk(SORTIE):
        for nom in fichiers:
            if not nom.endswith(".html"):
                continue
            chemin = os.path.join(racine, nom)
            court = os.path.relpath(chemin, SORTIE)
            h = open(chemin, encoding="utf-8").read()
            for trace in ("../../../../", "fonts.googleapis", "Maquette de refonte", "/_astro/"):
                if trace in h:
                    problemes.append(f"{court} : reste « {trace} »")
            for v in re.findall(r'\b(?:href|src|poster)="(/[^"]*)"', h):
                if not os.path.exists(fichier_de(v)):
                    problemes.append(f"{court} : lien mort {v}")
            for v in re.findall(r'\bhref="([^":#/][^":]*\.html[^"]*)"', h):
                problemes.append(f"{court} : lien de maquette {v}")
            if court != "404.html":
                canons = re.findall(r'<link rel="canonical" href="([^"]+)">', h)
                attendu = RACINE + "/" + os.path.dirname(court).replace(os.sep, "/") + ("/" if os.path.dirname(court) else "")
                if canons != [attendu]:
                    problemes.append(f"{court} : adresse de référence {canons} au lieu de {attendu}")
            for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
                try:
                    json.loads(bloc)
                except ValueError as err:
                    problemes.append(f"{court} : données structurées illisibles ({err})")
    # chaque adresse du site actuel est servie, ou redirigée
    actuel = os.path.join(DEPOT, "dist", "sitemap-0.xml")
    if os.path.exists(actuel):
        for u in re.findall(r"<loc>https://drfranckmoyal\.fr([^<]*)</loc>", open(actuel, encoding="utf-8").read()):
            if u.strip("/") in FONDUES:
                continue
            if not os.path.exists(fichier_de(u)):
                problemes.append(f"adresse du site actuel ni servie ni redirigée : {u}")
    else:
        print("  (dist/sitemap-0.xml absent : contrôle des anciennes adresses sauté)")
    for u in adresses:
        if not os.path.exists(fichier_de(u)):
            problemes.append(f"plan du site : {u} sans page")


def main():
    if os.path.isdir(RACCOURCI) and not os.path.islink(RACCOURCI):
        shutil.rmtree(RACCOURCI)          # l'ancien dossier, synchronisé par iCloud
    if not os.path.lexists(RACCOURCI):
        os.symlink(os.path.basename(SORTIE), RACCOURCI)
    if os.path.exists(SORTIE):
        shutil.rmtree(SORTIE)
    os.makedirs(SORTIE)
    a_copier, adresses, modele = {}, [], None
    for nom in sorted(os.listdir(SITE)):
        if not nom.endswith(".html"):
            continue
        slug = nom[:-5]
        if slug in INTERNES or slug in FONDUES:
            continue
        url = adresse(slug)
        page = open(os.path.join(SITE, nom), encoding="utf-8").read()
        page = reecrire(page, slug, a_copier)
        for motif, en_ligne, source in ANCIENNES_IMAGES:
            if re.search(motif, page):
                page = re.sub(motif, RACINE + en_ligne, page)
                a_copier[en_ligne] = os.path.join(SITE, source)
        page = entete(page, slug, url)
        if PIED_MAQUETTE in page:
            page = page.replace(PIED_MAQUETTE, PIED_EN_LIGNE)
        cible = fichier_de(url)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        open(cible, "w", encoding="utf-8").write(page)
        if slug == "mentions-legales":
            modele = page
        if slug not in HORS_PLAN:
            adresses.append(url)
    open(os.path.join(SORTIE, "404.html"), "w", encoding="utf-8").write(page_404(modele))

    # ressources : seulement celles qui servent
    poids = 0
    for destination, source in sorted(a_copier.items()):
        if not os.path.exists(source):
            problemes.append(f"ressource introuvable : {source}")
            continue
        cible = os.path.join(SORTIE, destination.lstrip("/"))
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        shutil.copy2(source, cible)
        poids += os.path.getsize(cible)
    os.makedirs(os.path.join(SORTIE, "assets", "fonts"), exist_ok=True)
    for nom in os.listdir(POLICES):
        if nom.endswith(".woff2"):
            shutil.copy2(os.path.join(POLICES, nom), os.path.join(SORTIE, "assets", "fonts", nom))
    style = open(os.path.join(POLICES, "polices.css"), encoding="utf-8").read() + "\n" + \
        open(os.path.join(SITE, "style.css"), encoding="utf-8").read()
    open(os.path.join(SORTIE, "assets", "style.css"), "w", encoding="utf-8").write(style)
    shutil.copy2(os.path.join(SITE, "menu.js"), os.path.join(SORTIE, "assets", "menu.js"))
    for nom in ("favicon.svg", "favicon-48.png", "apple-touch-icon.png", "robots.txt"):
        shutil.copy2(os.path.join(PUBLIC, nom), os.path.join(SORTIE, nom))
    # la clé IndexNow : un fichier à la racine qui prouve à Bing que les signalements
    # de pages viennent bien du site (scripts/indexnow.mjs)
    for nom in os.listdir(PUBLIC):
        if re.fullmatch(r"[0-9a-f]{32}\.txt", nom):
            shutil.copy2(os.path.join(PUBLIC, nom), os.path.join(SORTIE, nom))
    open(os.path.join(SORTIE, ".htaccess"), "w", encoding="utf-8").write(htaccess())
    plan, index = plan_du_site(adresses)
    for nom, contenu in (("sitemap-0.xml", plan), ("sitemap.xml", plan), ("sitemap-index.xml", index)):
        open(os.path.join(SORTIE, nom), "w", encoding="utf-8").write(contenu)

    # Tout lisible par le serveur web : un fichier réglé « moi seul » sur le Mac y garderait
    # ce réglage et répondrait 403 (le portrait, le 25/10/2026).
    for racine, dossiers, fichiers in os.walk(SORTIE):
        for d in dossiers:
            os.chmod(os.path.join(racine, d), 0o755)
        for f in fichiers:
            os.chmod(os.path.join(racine, f), 0o644)

    controler(adresses)
    total = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(SORTIE) for f in fs)
    print(f"dist-refonte/ : {len(adresses) + len(HORS_PLAN)} pages publiques et la page 404, "
          f"{len(a_copier)} ressources ({poids / 1e6:.1f} Mo), {total / 1e6:.1f} Mo en tout")
    print(f"  plan du site : {len(adresses)} adresses ; redirections : "
          + ", ".join(f"/{a}/ → /{b}/" for a, b in sorted(FONDUES.items())))
    if problemes:
        print(f"\n{len(problemes)} problème(s) :")
        for p in problemes[:60]:
            print("  -", p)
        sys.exit(1)
    print("  contrôles : aucun lien mort, aucune trace de maquette, une adresse de référence par page,"
          " toutes les anciennes adresses servies ou redirigées")


if __name__ == "__main__":
    main()
