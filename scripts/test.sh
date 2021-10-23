#!/bin/sh -e

if [ -n "$CI" ]; then
  poetry run pytest --cov=. --cov-report=xml
else
  poetry run pytest
fi
