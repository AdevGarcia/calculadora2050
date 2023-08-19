#!/bin/bash
set -e 

echo "killing old docker processes"
docker-compose rm -fs

# docker system prune -a

echo "building docker containers"
docker-compose build --no-cache
echo "run docker containers"
docker-compose up -d

echo "load data start in 40 seconds"

for i in {1..30}
do
   echo "Wait $i/40 times"
   sleep 1
done

echo "load data"
export PYTHONPATH=$PWD

# Postgres
export $(grep POSTGRES_SERVER .env)
export $(grep POSTGRES_PORT .env)
export $(grep POSTGRES_USER .env)
export $(grep POSTGRES_PASSWORD .env)
export $(grep POSTGRES_DB .env)


# python app/load_data.py
python app/load.py
echo "Ok all data update"
