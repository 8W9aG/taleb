#!/bin/sh

rm -rf tests/__pycache__
pytest -s tests/*
