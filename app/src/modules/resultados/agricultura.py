from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
import logging

from app.src.crud.base import downloader

from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

from .util.util import db_to_df

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######     Evolución de las emisiones del sector Agricultura                #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_agricultura')
def resultados_evolucion_de_las_emisiones_del_sector_agricultura(
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   cultivo_de_biocombustible   ##############
    filter={"bloque": "cultivo", "tipo": "total", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='emisiones_cultivo_biocombustibles',
        model=models.AGRO_EMISIONES,
        skip=skip, limit=limit,
        **filter)
    
    cultivo_de_biocombustible = db_to_df(rd=rd).to_dict(orient='records')[0]
    cultivo_de_biocombustible["topic"]    = "resultados"
    cultivo_de_biocombustible["bloque"]   = "agricultura"
    cultivo_de_biocombustible["tipo"]     = "cultivo_de_biocombustible"
    cultivo_de_biocombustible["unidad"]   = "Mt_CO2_e"

    ##########   mejores_practicas   ##############
    filter={"tipo": "potencial_de_reduccion_de_emisiones_de_las_medidas", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='implementacion_de_mejores_practicas_agricolas',
        model=models.AGRO_EMISIONES,
        skip=skip, limit=limit,
        **filter)

    mejores_practicas = db_to_df(rd=rd).to_dict(orient='records')[0]
    mejores_practicas["topic"]    = "resultados"
    mejores_practicas["bloque"]   = "agricultura"
    mejores_practicas["tipo"]     = "mejores_practicas"
    mejores_practicas["unidad"]   = "Mt_CO2_e"


    resultado = {"resultados": [cultivo_de_biocombustible, mejores_practicas]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######     Evolución del potencial energético para                          #######
#######     el aprovechamiento de residuos agrícolas y de biocombustibles    #######
####################################################################################
@router.get('/evolucion_del_potencial_energetico_para_aprovechamiento_de_residuos')
def resultados_evolucion_del_potencial_energetico_para_aprovechamiento_de_residuos(
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   cultivos   ##############
    filter={"bloque": "total_cultivos", "tipo": "total_cultivos", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='cultivos',
        model=models.AGRO_SALIDAS_cultivos,
        skip=skip, limit=limit,
        **filter)
    
    cultivos = db_to_df(rd=rd).to_dict(orient='records')[0]
    cultivos["topic"]    = "resultados"
    cultivos["bloque"]   = "agricultura"
    cultivos["tipo"]     = "cultivos"
    cultivos["unidad"]   = "TWh"

    ##########   biocombustibles   ##############
    filter={"tipo": "total", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='biocombustibles',
        model=models.AGRO_SALIDAS_biocombustibles,
        skip=skip, limit=limit,
        **filter)
    
    biocombustibles = db_to_df(rd=rd).to_dict(orient='records')[0]
    biocombustibles["topic"]    = "resultados"
    biocombustibles["bloque"]   = "agricultura"
    biocombustibles["tipo"]     = "biocombustibles"
    biocombustibles["unidad"]   = "TWh"


    resultado = {"entradas": [cultivos, biocombustibles]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                  Tierras dedicada a Biocombustibles                  #######
####################################################################################
@router.get('/tierras_dedicada_a_biocombustibles')
def resultados_tierras_dedicada_a_biocombustibles(
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    
    filter={"tipo": "palma_de_aceite",'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='tierra_dedicada_para_biocombustibles',
        model=models.AGRO_Metodologia_tierra_dedicada_para_biocombustibles,
        skip=skip, limit=limit,
        **filter)
    
    palma_de_aceite = db_to_df(rd=rd).to_dict(orient='records')[0]
    palma_de_aceite["topic"]    = "resultados"
    palma_de_aceite["bloque"]   = "agricultura"
    palma_de_aceite["tipo"]     = "palma_de_aceite"
    palma_de_aceite["unidad"]   = "TWh"


    filter={"tipo": "cana_de_azucar",'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='tierra_dedicada_para_biocombustibles',
        model=models.AGRO_Metodologia_tierra_dedicada_para_biocombustibles,
        skip=skip, limit=limit,
        **filter)
    
    cana_de_azucar = db_to_df(rd=rd).to_dict(orient='records')[0]
    cana_de_azucar["topic"]    = "resultados"
    cana_de_azucar["bloque"]   = "agricultura"
    cana_de_azucar["tipo"]     = "cana_de_azucar"
    cana_de_azucar["unidad"]   = "TWh"


    resultado = {"entradas": [palma_de_aceite, cana_de_azucar]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
 