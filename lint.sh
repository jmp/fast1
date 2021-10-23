#!/bin/sh -e

echo "Checking code with black..."
black --check .

echo "Checking imports with isort..."
isort --check .

echo "Checking code with flake8..."
flake8 .

echo "Checking types with mypy..."
mypy --strict .
