#!/bin/bash

# ./checkurls.sh urlstatus.txt

# url="http://localhost:8000/api/v1"

while read url
do
    echo 'hola'
    urlstatus=$(curl -o /dev/null --silent --head --write-out '%{http_code}' "$url" )
    sleep 1
    echo "$url  $urlstatus" >> urlstatus.txt
done < $1



# curl -Is $url | head -1