from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder

import pandas as pd
import logging

from app.src.crud.base import downloader

from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

from .util.util import db_to_df, db_to_dict, get_item, set_zeros, set_suma_total, not_negative

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######     Evolución de las emisiones del sector Ganaderia                  #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_ganaderia')
def resultados_evolucion_de_las_emisiones_del_sector_ganaderia(
    medida_gana_1: schemas.Trayectoria=1,
    medida_gana_2: schemas.Trayectoria=1,
    medida_gana_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   hato_ganadero   ##############
    filter={'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='emisiones_de_hato_ganadero',
        model=models.GANA_EMISIONES,
        **filter)
        
    hato_ganadero = db_to_df(rd=rd).sum().to_dict()
    hato_ganadero["topic"]    = "resultados"
    hato_ganadero["bloque"]   = "ganaderia"
    hato_ganadero["tipo"]     = "hato_ganadero"
    hato_ganadero["unidad"]   = "Mt_CO2_e"

    ##########   practicas_sostenibles   ##############
    filter={'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='practicas_sostenibles_en_suelos_ganaderos',
        model=models.GANA_EMISIONES,
        **filter)
        
    practicas_sostenibles = db_to_df(rd=rd).sum().to_dict()
    practicas_sostenibles["topic"]    = "resultados"
    practicas_sostenibles["bloque"]   = "ganaderia"
    practicas_sostenibles["tipo"]     = "practicas_sostenibles"
    practicas_sostenibles["unidad"]   = "Mt_CO2_e"


    ##########   mejores_practicas_pecuarias   ##############
    filter={'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='mejores_practicas_pecuarias',
        model=models.GANA_EMISIONES,
        **filter)
        
    mejores_practicas_pecuarias = db_to_df(rd=rd).sum().to_dict()
    mejores_practicas_pecuarias["topic"]    = "resultados"
    mejores_practicas_pecuarias["bloque"]   = "ganaderia"
    mejores_practicas_pecuarias["tipo"]     = "mejores_practicas_pecuarias"
    mejores_practicas_pecuarias["unidad"]   = "Mt_CO2_e"


    ##########   manejo_de_estiercol   ##############
    filter={'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='manejo_de_estiercol',
        model=models.GANA_EMISIONES,
        **filter)
        
    manejo_de_estiercol = db_to_df(rd=rd).sum().to_dict()
    manejo_de_estiercol["topic"]    = "resultados"
    manejo_de_estiercol["bloque"]   = "ganaderia"
    manejo_de_estiercol["tipo"]     = "manejo_de_estiercol"
    manejo_de_estiercol["unidad"]   = "Mt_CO2_e"


    resultado = {"resultados": [hato_ganadero, practicas_sostenibles, mejores_practicas_pecuarias, manejo_de_estiercol]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######            Evolución de la produccion de bioenergia                  #######
#######                 a traves del estiercol                               #######
####################################################################################
@router.get('/evolucion_de_produccion_bioenergia_por_estiercol')
def resultados_evolucion_de_produccion_bioenergia_por_estiercol(
    medida_gana_1: schemas.Trayectoria=1,
    medida_gana_2: schemas.Trayectoria=1,
    medida_gana_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   hembras   ##############
    filter={"tipo": "hembras_vacas",'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='produccion_de_estiercol_para_bioenergia',
        model=models.GANA_SALIDAS,
        **filter)
    
    hembras = db_to_df(rd=rd).to_dict(orient='records')[0]
    hembras["topic"]    = "resultados"
    hembras["bloque"]   = "ganaderia"
    hembras["tipo"]     = "hembras"
    hembras["unidad"]   = "TWh"

    ##########   machos   ##############
    filter={"tipo": "machos_reses",'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='produccion_de_estiercol_para_bioenergia',
        model=models.GANA_SALIDAS,
        **filter)
    
    machos = db_to_df(rd=rd).to_dict(orient='records')[0]
    machos["topic"]    = "resultados"
    machos["bloque"]   = "ganaderia"
    machos["tipo"]     = "machos"
    machos["unidad"]   = "TWh"


    resultado = {"resultados": [hembras, machos]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)



 