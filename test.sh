#!/bin/sh

python setup.py install
rm -rf tests/__pycache__
pytest -s tests/*
