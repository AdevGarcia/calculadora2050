#!/bin/bash
set -e 

echo "killing old docker processes"
docker-compose rm -fs

echo "building docker containers"
docker-compose up -d

echo "load data start in 40 seconds"
# sleep 30

for i in {1..30}
do
   echo "Wait $i/30 times"
   sleep 1
done


echo "load data"
export PYTHONPATH=$PWD

# python app/load_data.py
python app/load.py
echo "Ok all data update"