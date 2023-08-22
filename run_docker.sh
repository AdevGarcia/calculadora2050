#!/bin/bash
set -e 

echo "killing old docker processes"
docker-compose rm -fs

echo "building docker containers"
docker-compose build --no-cache

echo "run docker containers"
docker-compose up -d


x=300
export $(grep SERVER_HOST .env)
export $(grep API_V1_STR .env)

URL="$SERVER_HOST$API_V1_STR/test"

echo "URL $URL $x"

while [ $x -gt 1 ];
do
    echo "Checking $URL .. $x"
    status_code=$(curl --write-out '%{http_code}' --silent  --output /dev/null "$URL")
    sleep 0.5
    ((x--))

    if [[ $status_code -ge 200 && $status_code -le 299 ]];then
        echo -e "\x1B[32m✅ OK status code: $status_code for domain $URL  \x1B[0m"
        ((x=0))
    fi
done


echo "load data"
export PYTHONPATH=$PWD

python app/load.py
echo "Ok all data update"
