#!/bin/bash
# Reconstruit la maquette entière, dans le seul ordre qui marche :
#   0. faire-espaces.py réécrit les deux sommaires (patients et pro)
#   1. generer.py  remet en page les pages mécaniques
#   2. composer.py regroupe en chapitres celles qui ont un plan
#   3. generer.py  repasse pour aligner en-tête, pied et signature du style
#      sur TOUTES les pages, y compris celles écrites à la main.
set -e
cd "$(dirname "$0")"
python3 faire-espaces.py
python3 generer.py  | tail -3
python3 composer.py | tail -3
python3 generer.py  | tail -3
echo
python3 verifier.py
