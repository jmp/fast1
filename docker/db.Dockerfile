FROM mariadb AS build
ARG DUMP_URL=https://ergast.com/downloads/f1db.sql.gz
RUN apt-get update && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/* && \
    wget -O /db.sql.gz $DUMP_URL

FROM mariadb
COPY --from=build /db.sql.gz /docker-entrypoint-initdb.d/
