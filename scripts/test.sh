#!/bin/sh -e

if [ -n "$CI" ]; then
  echo "Running tests with coverage..."
  docker compose up db -d
  while ! mysqladmin ping -h 127.0.0.1 -u db --password=db 2> /dev/null; do
    sleep 0.1
  done
  poetry run pytest --cov=. --cov-report=xml
else
  echo "Running tests without coverage..."
  poetry run pytest
fi
