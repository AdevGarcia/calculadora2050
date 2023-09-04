from typing import Any
from fastapi.responses import FileResponse

from fastapi import APIRouter, Depends, HTTPException, status
from db import deps
import logging
from app.src.modules.user import models as models_user

from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()

@router.get('/')
def download(
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:

    media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    
    file_name = 'Calculadora_Colombiana_de_Carbono_2050.xlsx'
    file_location = Path(__file__).parents[3] / f'data/{file_name}'
    
    logger.info(f'Download Excel')
  
    return FileResponse(path=file_location, media_type=media_type, filename=file_name)
