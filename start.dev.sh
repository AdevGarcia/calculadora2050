#! /usr/bin/env bash
set -e


export PYTHONPATH=$PWD
# ./install.sh

cd ./app
alembic -c ./alembic.ini upgrade head

cd ./src
python initial_data.py

uvicorn main:app --host 0.0.0.0 --port 8000 --proxy-headers #--reload
