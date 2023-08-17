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

from .util.util import db_to_df, set_zeros

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


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

    combustibles_fosiles = set_zeros(topic_item='produccion', tipo='combustibles_fosiles', unidad='TWh')
    energia              = set_zeros(topic_item='produccion', tipo='energia',              unidad='TWh')
    industria            = set_zeros(topic_item='produccion', tipo='industria',            unidad='TWh')
    residuos             = set_zeros(topic_item='produccion', tipo='residuos',             unidad='TWh')
    edificaciones        = set_zeros(topic_item='produccion', tipo='edificaciones',        unidad='TWh')
    transporte           = set_zeros(topic_item='produccion', tipo='transporte',           unidad='TWh')
    # agricultura          = set_zeros(topic_item='produccion', tipo='agricultura',          unidad='TWh')
    ganaderia            = set_zeros(topic_item='produccion', tipo='ganaderia',            unidad='TWh')
    bosques              = set_zeros(topic_item='produccion', tipo='bosques',              unidad='TWh')

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