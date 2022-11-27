#!/usr/bin/env bash
set -o errexit

python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py collectstatic --no-input
python3 manage.py migrate
python3 manage.py setdefaultsuperuser
python3 manage.py seedlanguages
