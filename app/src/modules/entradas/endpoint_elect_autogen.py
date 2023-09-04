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

from .util.util import db_to_df, db_to_dict, get_item, set_zeros, set_suma_total

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######                               produccion                             #######
####################################################################################

@router.get('/autogeneracion/produccion')
def read_entradas_produccion(
    medida_ind_1: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    medida_res_irco_1: schemas.Trayectoria=1,
    medida_res_irco_2: schemas.Trayectoria=1,
    medida_res_irco_3: schemas.Trayectoria=1,
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    medida_gana_1: schemas.Trayectoria=1,
    medida_gana_2: schemas.Trayectoria=1,
    medida_gana_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   industria   ##############
    filter={'medida_1': medida_ind_1}
    rd = downloader(db=db, topic='energia_producida_por_autogeneracion_y_cogeneracion',
        model=models.INDU_SALIDAS_por_comb_ener_prod_autogeneracion_cogeneracion,
        skip=skip, limit=limit,
        **filter)

    industria = db_to_df(rd).sum().to_dict()
    industria["topic"]    = "entradas"
    industria["bloque"]   = "produccion"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"
    
    ##########   residuos   ##############
    ### residuos solidos
    filter={"tipo": "total_producido", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    ### aguas residuales
    filter={"tipo": "total_generacion", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    residuos = pd.concat([df1, df2]).sum().to_dict()
    residuos["topic"]    = "entradas"
    residuos["bloque"]   = "produccion"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "TWh"

    ##########   edificaciones   ##############    
    filter={"tipo": "solar_fotovoltaica", 'medida_1': medida_res_irco_1, 'medida_2': medida_res_irco_2, 'medida_3': medida_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    edificaciones = db_to_dict(rd=rd)
    edificaciones["topic"]    = "entradas"
    edificaciones["bloque"]   = "produccion"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"

    ##########   agricultura   ##############
    filter={'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='cultivos',
        model=models.AGRO_SALIDAS_cultivos,
        skip=skip, limit=limit,
        **filter)
    
    agricultura = db_to_df(rd=rd).sum().to_dict()
    agricultura["topic"]    = "entradas"
    agricultura["bloque"]   = "produccion"
    agricultura["tipo"]     = "agricultura"
    agricultura["unidad"]   = "TWh"

    ##########   ganaderia   ##############
    filter={"tipo": "total", 'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    ganaderia = get_item(db=db, 
        model=models.GANA_SALIDAS,
        topic='produccion_de_estiercol_para_bioenergia',
        filter=filter,
        topic_item='entradas',
        bloque="produccion",
        tipo='ganaderia',
        unidad='TWh')

    ##############################
    combustibles_fosiles = set_zeros(topic_item='entradas', bloque='produccion', tipo='combustibles_fosiles', unidad='TWh')
    transporte           = set_zeros(topic_item='entradas', bloque='produccion', tipo='transporte',           unidad='TWh')
    bosques              = set_zeros(topic_item='entradas', bloque='produccion', tipo='bosques',              unidad='TWh')

    total = set_suma_total(items=[combustibles_fosiles, industria, residuos, edificaciones, transporte, agricultura, ganaderia, bosques],
                   topic="entradas", 
                   bloque="produccion", tipo="total", unidad="TWh")

    resultado = {"entradas": [
            combustibles_fosiles,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            bosques,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
