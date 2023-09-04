#! /usr/bin/env bash
set -e 


cd ./app
alembic init alembic

cd ..
cp alembic_env.py app/alembic/env.py

cd ./app
alembic revision --autogenerate -m "init"
alembic -c ./alembic.ini upgrade head
