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

from .util.util import db_to_df

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######                               produccion                             #######
####################################################################################

@router.get('/cultivos')
def read_entradas_produccion(
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   agricultura   ##############
    filter={'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='cultivos',
        model=models.AGRO_SALIDAS_cultivos,
        **filter)
    
    agricultura = db_to_df(rd=rd).sum().to_dict()
    agricultura["topic"]    = "entradas"
    agricultura["bloque"]   = "cultivos"
    agricultura["tipo"]     = "bagazo_y_otros"
    agricultura["unidad"]   = "TWh"


    resultado = {"entradas": [agricultura]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
