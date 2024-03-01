#!/bin/sh

set -e

python setup.py sdist
twine upload dist/* --verbose
