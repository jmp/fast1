#!/bin/sh -e

black --check .
isort --check .
flake8 .
mypy --strict .
