#!/bin/sh -e

if [ -n "$CI" ]; then
  echo "Running tests with coverage..."
  docker compose up db -d
  sleep 10
  poetry run pytest --cov=. --cov-report=xml
else
  echo "Running tests without coverage..."
  poetry run pytest
fi
