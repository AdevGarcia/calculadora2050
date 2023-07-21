#! /usr/bin/env bash
set -e  # hace que se salga de tu script inmediatamente cuando un comando falla

./install.sh

export PYTHONPATH=$PWD
echo "The PYTHONPATH is: $PYTHONPATH" # Check

# Let the DB start
sleep 3;

cd ./app
# Run migrations
# alembic init alembic
# alembic revision --autogenerate -m "init"
alembic -c ./alembic.ini upgrade head

cd ./src
# Create initial data in DB
# python backend_pre_start.py

python initial_data.py

uvicorn main:app --host 0.0.0.0 --port 8000