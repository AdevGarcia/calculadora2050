#!/bin/bash
set -e 

echo "killing old docker processes"
docker-compose rm -fs

echo "building docker containers"
docker-compose up -d

echo "load data start in 40 seconds"
sleep 30

for i in {1..10}
do
   echo "Wait $i/10 times"
   sleep 1
done

echo "load data"
export PYTHONPATH=$PWD
python app/load_data.py
echo "Ok all data update"