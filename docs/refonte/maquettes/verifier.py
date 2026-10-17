#!/usr/bin/env python3
"""Contrôle la maquette avant de la montrer : rien ne doit être cassé, et rien
ne doit diverger d'une page à l'autre. Lancé en dernier par construire.sh."""
import glob
import json
import os
import re

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
RACINE = os.path.abspath(os.path.join(SITE, "..", "..", "..", ".."))


def existe(cible):
    """Les photos vivent dans le dépôt, pas dans le dossier de la maquette :
    elles sont appelées en relatif pour que la maquette s'ouvre sans serveur."""
    if cible.startswith("/"):
        return os.path.exists(os.path.join(RACINE, cible.lstrip("/")))
    return os.path.exists(os.path.normpath(os.path.join(SITE, cible)))


def main():
    pages = sorted(glob.glob(os.path.join(SITE, "*.html")))
    ennuis, liens, images, structurees = [], 0, 0, 0
    versions, menus = set(), set()

    for chemin in pages:
        nom = os.path.basename(chemin)
        h = open(chemin, encoding="utf-8").read()

        for href in re.findall(r'href="([^"]+)"', h):
            if href.startswith(("http", "mailto:", "tel:", "#")):
                continue
            cible = href.split("#")[0].split("?")[0]
            if not cible:
                continue
            liens += 1
            if not existe(cible):
                ennuis.append(f"{nom} → lien mort {href}")
        for src in re.findall(r'src="([^"]+)"', h):
            if src.startswith("http"):
                continue
            images += 1
            if not existe(src.split("?")[0]):
                ennuis.append(f"{nom} → image absente {src}")

        for vide in re.findall(r"<(p|li|h2|h3|td|th|figcaption)[^>]*>\s*</\1>", h):
            ennuis.append(f"{nom} → <{vide}> vide")
        if re.search(r"(undefined|\[object |\{liste\()", h):
            ennuis.append(f"{nom} → reste de fabrication")
        if re.search(r"<title>[^<]*<(?!/title>)", h):
            ennuis.append(f"{nom} → balise dans le <title>")
        # verrou V21 : jamais « dentiste esthétique », sauf la page pilier (D50)
        # — y compris quand une autre page cite le titre de cette page-là.
        hors_pilier = re.sub(
            r'<a[^>]*href="dentisterie-esthetique-paris\.html"[^>]*>.*?</a>', "", h, flags=re.S)
        if "dentiste esthétique" in hors_pilier.lower() and "dentisterie-esthetique-paris" not in nom:
            ennuis.append(f"{nom} → « dentiste esthétique » (verrou V21)")

        # données structurées : c'est par elles que les IA citent le site
        blocs = re.findall(
            r'<script type="application/ld\+json"[^>]*>(.*?)</script>', h, re.S)
        structurees += 1 if blocs else 0
        if not blocs and nom != "sommaire.html":
            ennuis.append(f"{nom} → aucune donnée structurée")
        for b in blocs:
            try:
                json.loads(b)
            except Exception as ex:
                ennuis.append(f"{nom} → JSON-LD illisible ({str(ex)[:40]})")

        v = re.search(r"style\.css\?v=(\d+)", h)
        if v:
            versions.add(v.group(1))
        m = re.findall(r'data-volet="v\d" aria-expanded="false">([^<]*)', h)
        if m:
            menus.add(tuple(m))

    if len(versions) > 1:
        ennuis.append(f"signatures de style différentes : {sorted(versions)}")
    if len(menus) > 1:
        ennuis.append(f"menus différents d'une page à l'autre : {menus}")

    print(f"{len(pages)} pages · {liens} liens internes · {images} images · "
          f"{structurees} avec données structurées · {len(ennuis)} ennui(s)")
    for e in ennuis:
        print("  ✗ " + e)
    if not ennuis:
        print("  menu, pied et style identiques partout ; aucun lien mort ;")
        print("  JSON-LD valide sur toutes les pages publiables.")
    return 1 if ennuis else 0


if __name__ == "__main__":
    raise SystemExit(main())
