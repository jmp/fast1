#!/bin/sh -e

if [ -n "$CI" ]; then
  stopdb=
  if ! docker compose ps --filter 'status=running' --services | grep -q db; then
    echo "Starting database..."
    docker compose up db -d
    stopdb=1
  fi
  echo "Waiting for database to be up..."
  while ! mysqladmin ping -h 127.0.0.1 -udb -pdb 2> /dev/null; do
    sleep 0.1
  done
  echo "Running tests with coverage..."
  poetry run pytest --cov=. --cov-report=xml
  if [ -n "$stopdb" ]; then
    echo "Stopping database..."
    docker compose down db
  fi
else
  echo "Running tests without coverage..."
  poetry run pytest
fi
