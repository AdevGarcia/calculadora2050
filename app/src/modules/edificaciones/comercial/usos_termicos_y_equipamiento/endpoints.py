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

URI_ST = '/supuestos_trayectoria'
URI_SF = '/supuestos_fijos'
URI_SALIDAS   = '/salidas'
URI_EMISIONES = '/emisiones'

SCHEMAS_ST  = schemas.SUPUESTOS_TRAYECTORIA
SCHEMAS_SF  = schemas.SUPUESTOS_FIJOS
SCHEMAS_SALIDAS    = schemas.SALIDAS
SCHEMAS_EMISIONES  = schemas.EMISIONES

DEBUG = False

router = APIRouter()


####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################
@router.post(URI_ST, response_model=SCHEMAS_ST, status_code=status.HTTP_201_CREATED)
def create_ST(
    data: SCHEMAS_ST, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'reduccion_por_eficiencia_en_la_iluminacion':
                loader(
                    db=db,
                    model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_iluminacion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'reduccion_por_eficiencia_en_refrigeracion':
                loader(
                    db=db,
                    model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_refrigeracion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'reduccion_por_eficiencia_en_usos_termicos':
                loader(
                    db=db,
                    model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_usos_termicos, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )

            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get('/supuestos_trayectoria/{module}')
def read_ST_module(
    module: schemas.ST_name,
    trayectoria: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'trayectoria' : trayectoria}

    match module:        
        case schemas.ST_name.reduccion_por_eficiencia_en_la_iluminacion:
            rd = downloader(
                db=db, 
                model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_iluminacion,
                topic='reduccion_por_eficiencia_en_la_iluminacion',
                **filter
                )
        
        case schemas.ST_name.reduccion_por_eficiencia_en_refrigeracion:
            rd = downloader(
                db=db, 
                model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_refrigeracion,
                topic='reduccion_por_eficiencia_en_refrigeracion',
                **filter
                )
        
        case schemas.ST_name.reduccion_por_eficiencia_en_usos_termicos:
            rd = downloader(
                db=db, 
                model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_usos_termicos,
                topic='reduccion_por_eficiencia_en_usos_termicos',
                **filter
                )

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_ST, status_code=status.HTTP_200_OK)
def delete_ST(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_iluminacion)
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_refrigeracion)
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_usos_termicos)

    return {'msg': 'Deleted successfully'}


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################
@router.post(URI_SF, response_model=SCHEMAS_SF, status_code=status.HTTP_201_CREATED)
def create_SF(
    data: SCHEMAS_SF, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'consumo_total_de_energia_por_uso':
                loader(
                    db=db, 
                    model=models.EDIF_COM_USOS_TERM_EQUIP_SF_consumo_total_de_energia_por_uso, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'participacion_usos_en_equipamiento':
                loader(
                    db=db, 
                    model=models.EDIF_COM_USOS_TERM_EQUIP_SF_participacion_usos_en_equipamiento, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
            
            case 'participacion_de_los_energeticos_en_los_usos_termicos':
                loader(
                    db=db, 
                    model=models.EDIF_COM_USOS_TERM_EQUIP_SF_part_energeticos_usos_termicos, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'participacion_de_los_energeticos_en_equipamiento':
                loader(
                    db=db, 
                    model=models.EDIF_COM_USOS_TERM_EQUIP_SF_participacion_energ_equipamiento, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
            
            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get(URI_SF, response_model=SCHEMAS_SF)
def read_SF(
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""
    
    d = {
        'consumo_total_de_energia_por_uso'                      : models.EDIF_COM_USOS_TERM_EQUIP_SF_consumo_total_de_energia_por_uso,
        'participacion_usos_en_equipamiento'                    : models.EDIF_COM_USOS_TERM_EQUIP_SF_participacion_usos_en_equipamiento,
        'participacion_de_los_energeticos_en_los_usos_termicos' : models.EDIF_COM_USOS_TERM_EQUIP_SF_part_energeticos_usos_termicos,
        'participacion_de_los_energeticos_en_equipamiento'      : models.EDIF_COM_USOS_TERM_EQUIP_SF_participacion_energ_equipamiento,
        }
    
    rd = downloader_batch(db=db, **d)
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SF, status_code=status.HTTP_200_OK)
def delete_SF(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""

    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_SF_consumo_total_de_energia_por_uso)
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_SF_participacion_usos_en_equipamiento)
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_SF_part_energeticos_usos_termicos)
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_SF_participacion_energ_equipamiento)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas', 
        response_model=schemas.SALIDAS, 
        status_code=status.HTTP_201_CREATED)
def create_salidas(
    data: schemas.SALIDAS, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS, 
        obj_in=jdata['salidas'], 
        filters=['topic', 'tipo', 'medida_1']
    )
    return jdata


@router.get('/salidas')
def read_salidas_module(
    medida_edi_com_ute_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_edi_com_ute_1}

    rd = downloader(
        db=db, 
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        topic='energia_producida_y_requerida',
        **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SALIDAS, status_code=status.HTTP_200_OK)
def delete_Salidas(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS)

    return {'msg': 'Deleted Salidas successfully'}

####################################################################################
#######                               Emisiones                              #######
####################################################################################

@router.post(
        path='/emisiones', 
        response_model=schemas.EMISIONES, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones(
    data: schemas.EMISIONES, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.EDIF_COM_USOS_TERM_EQUIP_EMISIONES, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'tipo', 'medida_1']
    )
    return jdata


@router.get('/emisiones')
def read_Emisiones_module(
    medida_edi_com_ute_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_edi_com_ute_1}

    rd = downloader(
            db=db, 
            model=models.EDIF_COM_USOS_TERM_EQUIP_EMISIONES,
            topic='emisiones_de_gases_efecto_invernadero',
            **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_EMISIONES, status_code=status.HTTP_200_OK)
def delete_Emisiones(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.EDIF_COM_USOS_TERM_EQUIP_EMISIONES)

    return {'msg': 'Deleted successfully'}
