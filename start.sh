#! /usr/bin/env bash
set -e  # hace que se salga de tu script inmediatamente cuando un comando falla


echo "########  START.sh  ########"

echo "########  init INSTALL.sh  ########"
./install.sh
echo "########  end INSTALL.sh  ########"

export PYTHONPATH=$PWD
echo "The PYTHONPATH is: $PYTHONPATH" # Check

echo "The POSTGRES_SERVER is   : $POSTGRES_SERVER"   # Check
echo "The POSTGRES_PORT is     : $POSTGRES_PORT"     # Check
echo "The POSTGRES_USER is     : $POSTGRES_USER"     # Check
echo "The POSTGRES_PASSWORD is : $POSTGRES_PASSWORD" # Check
echo "The POSTGRES_DB is       : $POSTGRES_DB"       # Check

# Let the DB start
echo "### Let the DB start - sleep 5s"
sleep 5;

cd ./app
# Run migrations
# alembic init alembic
# alembic revision --autogenerate -m "init"
# alembic -c ./alembic.ini upgrade head

cd ./src
# Create initial data in DB
# python backend_pre_start.py

echo "########  init initial_data.py  ########"
python initial_data.py
echo "########  end initial_data.py  ########"

echo "########  run uvicorn  ########"

uvicorn main:app --host 0.0.0.0 --port 8000