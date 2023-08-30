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
#######     Evolución de las emisiones del sector Bosques                    #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_bosques')
def resultados_evolucion_de_las_emisiones_del_sector_bosques(
    medida_bosq_1: schemas.Trayectoria=1,
    medida_bosq_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   absorciones_por_plantaciones_comerciales   ##############
    filter={"tipo": "absorciones_por_plantaciones_comerciales", 'medida_1': medida_bosq_1, 'medida_2': medida_bosq_2}
    rd = downloader(db=db, topic='total_emisiones',
        model=models.BOSQ_EMISIONES,
        skip=skip, limit=limit,
        **filter)
        
    absorciones_por_plantaciones_comerciales = db_to_df(rd=rd).to_dict(orient='records')[0]
    absorciones_por_plantaciones_comerciales["topic"]    = "resultados"
    absorciones_por_plantaciones_comerciales["bloque"]   = "bosques"
    absorciones_por_plantaciones_comerciales["tipo"]     = "absorciones_por_plantaciones_comerciales"
    absorciones_por_plantaciones_comerciales["unidad"]   = "Mt_CO2_e"

    ##########   emisiones_por_deforestacion   ##############
    filter={"tipo": "emisiones_por_deforestacion", 'medida_1': medida_bosq_1, 'medida_2': medida_bosq_2}
    rd = downloader(db=db, topic='total_emisiones',
        model=models.BOSQ_EMISIONES,
        skip=skip, limit=limit,
        **filter)
        
    emisiones_por_deforestacion = db_to_df(rd=rd).to_dict(orient='records')[0]
    emisiones_por_deforestacion["topic"]    = "resultados"
    emisiones_por_deforestacion["bloque"]   = "bosques"
    emisiones_por_deforestacion["tipo"]     = "emisiones_por_deforestacion"
    emisiones_por_deforestacion["unidad"]   = "Mt_CO2_e"

    resultado = {"resultados": [absorciones_por_plantaciones_comerciales, emisiones_por_deforestacion]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######            Evolución de las hectareas de bosque                      #######
####################################################################################
@router.get('/evolucion_de_las_hectareas_de_bosque')
def resultados_evolucion_de_las_hectareas_de_bosque(
    medida_bosq_1: schemas.Trayectoria=1,
    medida_bosq_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   superficie_total_deforestacion_acumulada   ##############
    filter={"tipo": "total_deforestada_acumulada",'medida_1': medida_bosq_1, 'medida_2': medida_bosq_2}
    rd = downloader(db=db, topic='total_areas_reforestadas',
        model=models.BOSQ_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    superficie_total_deforestacion_acumulada = db_to_df(rd=rd).to_dict(orient='records')[0]
    superficie_total_deforestacion_acumulada["topic"]    = "resultados"
    superficie_total_deforestacion_acumulada["bloque"]   = "bosques"
    superficie_total_deforestacion_acumulada["tipo"]     = "superficie_total_deforestacion_acumulada"
    superficie_total_deforestacion_acumulada["unidad"]   = "ha"

    ##########   superficie_reforestacion_comercial_acumulada   ##############
    filter={"tipo": "reforestacion_comercial_acumulada",'medida_1': medida_bosq_1, 'medida_2': medida_bosq_2}
    rd = downloader(db=db, topic='total_areas_reforestadas',
        model=models.BOSQ_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    superficie_reforestacion_comercial_acumulada = db_to_df(rd=rd).to_dict(orient='records')[0]
    superficie_reforestacion_comercial_acumulada["topic"]    = "resultados"
    superficie_reforestacion_comercial_acumulada["bloque"]   = "bosques"
    superficie_reforestacion_comercial_acumulada["tipo"]     = "superficie_reforestacion_comercial_acumulada"
    superficie_reforestacion_comercial_acumulada["unidad"]   = "ha"


    resultado = {"resultados": [superficie_total_deforestacion_acumulada, superficie_reforestacion_comercial_acumulada]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
 