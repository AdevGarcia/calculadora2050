#! /usr/bin/env bash
set -e 

export PYTHONPATH=$PWD
export $(grep API_ENV .env)
export $(grep DEBUG .env)

echo "The PYTHONPATH is: $PYTHONPATH" # Check
echo "API_ENV          : $API_ENV" 
echo "DEBUG            : $DEBUG" 

DIRECTORIO=app/alembic
SQLITE=app/app.sqlite

if [ -d "$DIRECTORIO" ]
then
   rm -rf $DIRECTORIO
   echo "El directorio ${DIRECTORIO} ha sido eliminado"
else
   echo "El directorio ${DIRECTORIO} no existe"
fi

if [ -f "$SQLITE" ]
then
   rm $SQLITE
   echo "La ddbb ${SQLITE} ha sido eliminado"
else
   echo "La ddbb ${SQLITE} no existe"
fi

cd ./app
echo "Alembic INIT"
alembic init alembic

cd ..
echo "Alembic env copy"
cp alembic_env.py app/alembic/env.py


cd ./app
echo "Alembic autogenerate"
alembic revision --autogenerate -m "init"

alembic -c ./alembic.ini upgrade head
echo "Done"
