#! /usr/bin/env bash
set -e


echo "########  START.sh  ########"
export PYTHONPATH=$PWD
export $(grep API_ENV .env)
export $(grep DEBUG .env)

if [ "$API_ENV" == 'production' ]
then
    echo "Estamos en ${API_ENV}"
    echo "########  init INSTALL.sh  ########"
    ./install.sh
    echo "########  end INSTALL.sh  ########"
    export $(grep POSTGRES_SERVER .env)
    export $(grep POSTGRES_PORT .env)
    export $(grep POSTGRES_USER .env)
    export $(grep POSTGRES_PASSWORD .env)
    export $(grep POSTGRES_DB .env)

    echo "The PYTHONPATH is        : $PYTHONPATH"        # Check
    echo "The POSTGRES_SERVER is   : $POSTGRES_SERVER"   # Check
    echo "The POSTGRES_PORT is     : $POSTGRES_PORT"     # Check
    echo "The POSTGRES_USER is     : $POSTGRES_USER"     # Check
    echo "The POSTGRES_PASSWORD is : $POSTGRES_PASSWORD" # Check
    echo "The POSTGRES_DB is       : $POSTGRES_DB"       # Check
    
else
    echo "Estamos en ${API_ENV}"
fi


# Let the DB start
echo "### Let the DB start - sleep 5s"
sleep 5;

cd ./app/src/ 

echo "########  init initial_data.py  ########"
python initial_data.py
echo "########  end initial_data.py  ########"

echo "########  run uvicorn  ########"

if [ "$API_ENV" == 'production' ]
then
   uvicorn main:app --host 0.0.0.0 --port 8000
else
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
fi

