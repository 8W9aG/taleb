#!/bin/sh

set -e

echo "Formatting..."
echo "--- Ruff ---"
ruff format taleb
echo "--- isort ---"
isort taleb

echo "Checking..."
echo "--- Flake8 ---"
flake8 taleb
echo "--- pylint ---"
pylint taleb
echo "--- mypy ---"
mypy taleb
echo "--- Ruff ---"
ruff check taleb
echo "--- pyright ---"
pyright taleb
