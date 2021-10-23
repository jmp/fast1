#!/bin/sh -e

echo "Checking code with black..."
poetry run black --check .

echo "Checking imports with isort..."
poetry run isort --check .

echo "Checking code with flake8..."
poetry run flake8 .

echo "Checking types with mypy..."
poetry run mypy --strict .
