FROM python:3.10-slim as build
WORKDIR /tmp
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.10-slim
RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /code
COPY --from=build /tmp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
