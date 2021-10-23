# fast1

This is a an experimental read-only API for F1 data.

## Requirements

* [Docker](docker)
* [Python](python)
* [Poetry](poetry)

## Installing dependencies

    poetry install

## Running with Docker Compose

This starts both the app and the database:

    docker compose up

The application can then be accessed at http://localhost:8080.

If you want to run the database in the background, you can run:

    docker compose up db -d

Then you can run/debug the actual application in your IDE.

## Linting and tests

    ./scripts/lint.sh
    ./scripts/test.sh

[python]: https://python.org
[poetry]: https://python-poetry.org
[docker]: https://docker.com
