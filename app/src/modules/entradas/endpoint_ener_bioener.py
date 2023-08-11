from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder

import pandas as pd
import logging

from app.src.crud.base import loader, prune, downloader, downloader_batch

from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()

def db_to_df(rd: dict, debug: bool=False)-> pd.DataFrame:
    years = ["y2018","y2020","y2025", "y2030", "y2035", "y2040", "y2045", "y2050"]
    d = jsonable_encoder(rd)

    if debug:
        print('### db_to_df\n', d)
    return pd.DataFrame(d[list(d.keys())[0]])[years]

def db_to_dict(rd: dict)-> dict:
    return db_to_df(rd=rd).to_dict(orient='records')[0]


def fvalue(rd: dict, topic: str, bloque: str, tipo: str, unidad:str)-> dict:
    
    d = db_to_dict(rd=rd)
    d["topic"]    = topic
    d["bloque"]   = bloque
    d["tipo"]     = tipo
    d["unidad"]   = unidad

    return d


def fcero(topic: str, tipo: str, unidad:str)-> dict:
        dcero = {
            'y2018'  : 0.0, 
            'y2020'  : 0.0, 
            'y2025'  : 0.0, 
            'y2030'  : 0.0, 
            'y2035'  : 0.0, 
            'y2040'  : 0.0, 
            'y2045'  : 0.0, 
            'y2050'  : 0.0,
            'topic'  : topic, 
            'tipo'   : tipo, 
            'unidad' : unidad
        }
        return dcero


####################################################################################
#######                              Entradas                                #######
####################################################################################

@router.get('/energia_bioenergia')
def read_entradas_energia_bioenergia(
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ###
    filter={"tipo": "biodiesel_palma_de_aceite", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='biocombustibles',
        model=models.AGRO_SALIDAS_biocombustibles,
        **filter)

    df1 = db_to_df(rd=rd)

    ###
    filter={"tipo": "bioetanol_cana_de_azucar", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='biocombustibles',
        model=models.AGRO_SALIDAS_biocombustibles,
        **filter)

    df2 = db_to_df(rd=rd)

    agricultura = pd.concat([df1, df2]).sum().to_dict()
    agricultura["topic"]    = "produccion"
    agricultura["tipo"]     = "agricultura"
    agricultura["unidad"]   = "TWh"

    #### 

    combustibles_fosiles = fcero(topic='produccion', tipo='combustibles_fosiles', unidad='TWh')
    energia              = fcero(topic='produccion', tipo='energia',              unidad='TWh')
    industria            = fcero(topic='produccion', tipo='industria',            unidad='TWh')
    residuos             = fcero(topic='produccion', tipo='residuos',             unidad='TWh')
    edificaciones        = fcero(topic='produccion', tipo='edificaciones',        unidad='TWh')
    transporte           = fcero(topic='produccion', tipo='transporte',           unidad='TWh')
    # agricultura          = fcero(topic='produccion', tipo='agricultura',          unidad='TWh')
    ganaderia            = fcero(topic='produccion', tipo='ganaderia',            unidad='TWh')
    bosques              = fcero(topic='produccion', tipo='bosques',              unidad='TWh')

    resultado = {
        "produccion": [
            combustibles_fosiles, 
            energia, 
            industria, 
            residuos, 
            edificaciones, 
            transporte, 
            agricultura, 
            ganaderia, 
            bosques
        ]
    }

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)