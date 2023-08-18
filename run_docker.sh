#!/bin/bash
set -e 

echo "killing old docker processes"
docker-compose rm -fs

# docker system prune -a

echo "building docker containers"
docker-compose up -d

echo "load data start in 40 seconds"

for i in {1..30}
do
   echo "Wait $i/40 times"
   sleep 1
done

echo "load data"
export PYTHONPATH=$PWD

# python app/load_data.py
python app/load.py
echo "Ok all data update"
