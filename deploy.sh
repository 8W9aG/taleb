#!/bin/sh

set -e

git push origin main
python setup.py sdist
twine upload dist/* --verbose
