#!/bin/sh -e

if [ -n "$CI" ]; then
  echo "Running tests with coverage..."
  poetry run pytest --cov=. --cov-report=xml
else
  echo "Running tests without coverage..."
  poetry run pytest
fi
