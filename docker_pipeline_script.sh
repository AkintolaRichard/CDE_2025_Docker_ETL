#!/bin/bash

chmod +x export_var.sh

source export_var.sh

docker pull postgres

docker network create ntwork

docker run -d \
  --name $POSTGRES_HOST \
  --network ntwork \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=$POSTGRES_DB \
  -v postgres_data:/var/lib/postgresql/data \
  postgres

docker build -t cdedocker .

docker run --name cdedock \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_PORT=$POSTGRES_PORT \
  -e POSTGRES_HOST=$POSTGRES_HOST \
  -e POSTGRES_DB=$POSTGRES_DB \
  -e CSV_URL=$CSV_URL \
  --network ntwork \
  cdedocker
