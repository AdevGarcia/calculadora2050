# Calculadora Colombiana CO2 2050



### Operacion en segundo plano
nohup ./prestart.sh > logs.out 2> logs.err < /dev/null &



# Proceso de creación de modulos

1. Generar Carpeta
2. Create Files:
    - ```__init__.py```
    - ```name_module.py```
    - ```crud.py```
    - ```models.py```
    - ```schemas.py```
3. Add endpoint in ```app/src/api/api.py```
4. Add models in ```app/src/db/base.py```
5. Create models to ddbb
6. Create schemas
7. Define crud
8. Define endpoints
9. Create data.json


### Para inicializar en debugger

```bash
$ set PYTHONPATH=$PWD # Windows
$ export PYTHONPATH=$PWD
$ echo $PYTHONPATH # Check
> /home/angel/calculadora2050 # la carpeta raiz es app
$ source ./venv/bin/activate
$ uvicorn main:app --host localhost --port 8000 --reload
```

```bash
# No olvidar permisos!
chmod +x prestart.sh
```

## Primer proceso de arranque alembic para creaci'on de ddbb
```bash
# Alembic
alembic init alembic
alembic revision --autogenerate -m "init"
# go to where the alembic.ini file is located
alembic upgrade head
```

## Actualizaci'on de las tablas segun los modelos
```bash
alembic revision --autogenerate -m "init"
# go to where the alembic.ini file is located
alembic upgrade head

# Cualquier cambio que se realice se debe ejecutar
alembic revision --autogenerate -m "commit" # Para generar la version que cree las tablas
alembic upgrade head
```

