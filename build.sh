#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py setdefaultsuperuser
python3 manage.py seedlanguages
