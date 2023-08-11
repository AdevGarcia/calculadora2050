from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
import logging

from app.src.crud.base import loader, prune, downloader, downloader_batch
from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# URI_ST = '/supuestos_trayectoria'
# URI_SF = '/supuestos_fijos'
# URI_SALIDAS   = '/salidas'
# URI_EMISIONES = '/emisiones'

# SCHEMAS_ST  = schemas.SUPUESTOS_TRAYECTORIA
# SCHEMAS_SF  = schemas.SUPUESTOS_FIJOS
# SCHEMAS_SALIDAS    = schemas.SALIDAS
# SCHEMAS_EMISIONES  = schemas.EMISIONES

DEBUG = False

router = APIRouter()


####################################################################################
#######                              Entradas                                #######
####################################################################################

@router.get('/entradas')
def read_entradas(
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    rd = downloader(
        db=db, 
        model=models.ENER_CombFosil_ST_eficiencia_energetica_en_la_refinacion_de_crudo,
        topic='eficiencia_energetica_en_la_refinacion_de_crudo',
        **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)