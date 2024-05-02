#!/bin/bash
python3 manage.py makemigrations example
python3 manage.py migrate example
python3 manage.py runserver 0.0.0.0:8000