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


@router.get('/requerimientos_energeticos')
def read_entradas_requerimientos_energeticos(
    medida_elect_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""
    
    filter={"tipo": "balance_total", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='balance',
        model=models.ELECT_Electricidad_SALIDAS_balance,
        skip=skip, limit=limit,
        **filter)

    df = db_to_df(rd=rd)

    for c in df.columns:
        if df[c].iloc[0] < 0:
            df[c].iloc[0] = 0

    electricidad = df.to_dict(orient='records')[0]
    electricidad["topic"]    = "entradas"
    electricidad["bloque"]   = "requerimientos_energeticos"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    result = {
        'requerimientos_energeticos' : [electricidad]
    }

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(result)}')

    return jsonable_encoder(result)


@router.get('/excedentes_energeticos')
def read_entradas_excedentes_energeticos(
    medida_elect_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""
    
    filter={"tipo": "balance_total", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='balance',
        model=models.ELECT_Electricidad_SALIDAS_balance,
        skip=skip, limit=limit,
        **filter)

    df = db_to_df(rd=rd)

    for c in df.columns:
        if df[c].iloc[0] > 0:
            df[c].iloc[0] = 0
        else:
            df[c].iloc[0] = abs(df[c].iloc[0])

    electricidad = df.to_dict(orient='records')[0]
    electricidad["topic"]    = "entradas"
    electricidad["bloque"]   = "excedentes_energeticos"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    result = {
        'excedentes_energeticos' : [electricidad]
    }

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(result)}')

    return jsonable_encoder(result)
