#!/bin/bash
set -e 

echo "killing old docker processes"
docker-compose rm -fs

echo "building docker containers"
docker-compose up -d

echo "load data start in 40 seconds"
sleep 30

echo "10"
sleep 1
echo "9"
sleep 1
echo "8"
sleep 1
echo "7"
sleep 1
echo "6"
sleep 1
echo "5"
sleep 1
echo "4"
sleep 1
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"

echo "load data"
export PYTHONPATH=$PWD
python app/load_data.py
echo "Ok all data update"