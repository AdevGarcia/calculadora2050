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
    """CREATE
    """

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'mejores_practicas_agricolas_superficie_de_implementacion':
                loader(
                    db=db,
                    model=models.AGRO_ST_mejores_practicas_agricolas_superficie_de_implementacion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                    
            case 'tierra_dedicada_para_biocombustibles_superficie_de_implementacion':
                loader(
                    db=db, 
                    model=models.AGRO_ST_tierra_dedicada_para_biocombustibles_superficie_de_implementacion, 
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
    """READ ALL
    """
    filter = {'trayectoria' : trayectoria}

    match module:
        case schemas.ST_name.mejores_practicas_agricolas_superficie_de_implementacion:
            rd = downloader(
                db=db, 
                model=models.AGRO_ST_mejores_practicas_agricolas_superficie_de_implementacion,
                topic='mejores_practicas_agricolas_superficie_de_implementacion',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.ST_name.tierra_dedicada_para_biocombustibles_superficie_de_implementacion:
            rd = downloader(
                db=db, 
                model=models.AGRO_ST_tierra_dedicada_para_biocombustibles_superficie_de_implementacion,
                topic='tierra_dedicada_para_biocombustibles_superficie_de_implementacion',
                **filter
                )
            result = jsonable_encoder(rd)

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {result}')

    return result


@router.delete(URI_ST, status_code=status.HTTP_200_OK)
def delete_ST(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL
    """
    
    prune(db=db, model=models.AGRO_ST_mejores_practicas_agricolas_superficie_de_implementacion)
    prune(db=db, model=models.AGRO_ST_tierra_dedicada_para_biocombustibles_superficie_de_implementacion)

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
    """CREATE
    """

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo':
                loader(db=db, model=models.AGRO_SF_factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                    
            case 'produccion_biocombustibles':
                loader(db=db, model=models.AGRO_SF_produccion_biocombustibles, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'porcentaje_del_cultivo_usado_para_biocombustibles':
                loader(db=db, model=models.AGRO_SF_porcentaje_del_cultivo_usado_para_biocombustibles, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'factor_de_emision_de_cultivo_usado_para_biocombustibles':
                loader(db=db, model=models.AGRO_SF_factor_de_emision_de_cultivo_usado_para_biocombustibles, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'uso_actual_de_la_tierra_sector_agropecuario_en_colombia':
                loader(db=db, model=models.AGRO_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
            
            case 'tasas_de_crecimiento_del_pib_sectorial_de_agricultura':
                loader(db=db, model=models.AGRO_SF_tasas_de_crecimiento_del_pib_sectorial_de_agricultura, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'areas_de_implementacion_de_mejores_practicas_agricolas':
                loader(db=db, model=models.AGRO_SF_areas_de_implementacion_de_mejores_practicas_agricolas, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'factor_de_produccion_biomasa_por_cultivo':
                loader(db=db, model=models.AGRO_SF_factor_de_produccion_biomasa_por_cultivo, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'potencial_energetico_por_unidad_de_biomasa':
                loader(db=db, model=models.AGRO_SF_potencial_energetico_por_unidad_de_biomasa, obj_in=jdata[key], 
                       filters=['topic', 'bloque', 'tipo', 'unidad_factor', 'unidad_potencial'])
            
            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get(URI_SF, response_model=SCHEMAS_SF)
def read_SF(
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL
    """
    
    d = {
        'factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo' : models.AGRO_SF_factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo,
        'produccion_biocombustibles'                                           : models.AGRO_SF_produccion_biocombustibles,
        'porcentaje_del_cultivo_usado_para_biocombustibles'                    : models.AGRO_SF_porcentaje_del_cultivo_usado_para_biocombustibles,
        'factor_de_emision_de_cultivo_usado_para_biocombustibles'              : models.AGRO_SF_factor_de_emision_de_cultivo_usado_para_biocombustibles,
        'uso_actual_de_la_tierra_sector_agropecuario_en_colombia'              : models.AGRO_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia,
        'tasas_de_crecimiento_del_pib_sectorial_de_agricultura'                : models.AGRO_SF_tasas_de_crecimiento_del_pib_sectorial_de_agricultura,
        'areas_de_implementacion_de_mejores_practicas_agricolas'               : models.AGRO_SF_areas_de_implementacion_de_mejores_practicas_agricolas,
        'factor_de_produccion_biomasa_por_cultivo'                             : models.AGRO_SF_factor_de_produccion_biomasa_por_cultivo,
        'potencial_energetico_por_unidad_de_biomasa'                           : models.AGRO_SF_potencial_energetico_por_unidad_de_biomasa
        }
    
    rd = downloader_batch(db=db, **d)
    result = jsonable_encoder(rd)
    
    if DEBUG:
        logger.info(f'Read Data: {result}')

    return result


@router.delete(URI_SF, status_code=status.HTTP_200_OK)
def delete_SF(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL
    """
    
    prune(db=db, model=models.AGRO_SF_factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo)
    prune(db=db, model=models.AGRO_SF_produccion_biocombustibles)
    prune(db=db, model=models.AGRO_SF_porcentaje_del_cultivo_usado_para_biocombustibles)
    prune(db=db, model=models.AGRO_SF_factor_de_emision_de_cultivo_usado_para_biocombustibles)
    prune(db=db, model=models.AGRO_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia)
    prune(db=db, model=models.AGRO_SF_tasas_de_crecimiento_del_pib_sectorial_de_agricultura)
    prune(db=db, model=models.AGRO_SF_areas_de_implementacion_de_mejores_practicas_agricolas)
    prune(db=db, model=models.AGRO_SF_factor_de_produccion_biomasa_por_cultivo)
    prune(db=db, model=models.AGRO_SF_potencial_energetico_por_unidad_de_biomasa)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas/salida_cultivos', 
        response_model=schemas.AGRO_SALIDAS_cultivos, 
        status_code=status.HTTP_201_CREATED)
def create_salida_cultivos(
    data: schemas.AGRO_SALIDAS_cultivos, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.AGRO_SALIDAS_cultivos, 
        obj_in=jdata['salida_cultivos'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1', 'medida_2', 'medida_3']
    )
    
    return jdata


@router.post(
        path='/salidas/salidas_biocombustibles', 
        response_model=schemas.AGRO_SALIDAS_biocombustibles, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_biocombustibles(
    data: schemas.AGRO_SALIDAS_biocombustibles, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.AGRO_SALIDAS_biocombustibles, 
        obj_in=jdata['salidas_biocombustibles'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2', 'medida_3']
    )
    
    return jdata


@router.get('/salidas/{module}')
def read_salidas_module(
    module: schemas.Salidas_name,
    medida_1: schemas.Trayectoria,
    medida_2: schemas.Trayectoria,
    medida_3: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL
    """
    filter = {'medida_1' : medida_1, 'medida_2' : medida_2, 'medida_3' : medida_3}

    match module:
        case schemas.Salidas_name.salida_cultivos:
            rd = downloader(
                db=db, 
                model=models.AGRO_SALIDAS_cultivos,
                topic='salida_cultivos',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.Salidas_name.salidas_biocombustibles:
            rd = downloader(
                db=db, 
                model=models.AGRO_SALIDAS_biocombustibles,
                topic='salidas_biocombustibles',
                **filter
                )
            result = jsonable_encoder(rd)

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {result}')

    return result


@router.delete(URI_SALIDAS, status_code=status.HTTP_200_OK)
def delete_Salidas(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL
    """
    
    prune(db=db, model=models.AGRO_SALIDAS_cultivos)
    prune(db=db, model=models.AGRO_SALIDAS_biocombustibles)

    return {'msg': 'Deleted Salidas successfully'}

####################################################################################
#######                               Emisiones                              #######
####################################################################################

@router.post(
        path='/emisiones', 
        response_model=schemas.AGRO_EMISIONES, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones(
    data: schemas.AGRO_EMISIONES, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.AGRO_EMISIONES, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1', 'medida_2', 'medida_3']
    )
    
    return jdata


@router.get('/emisiones')
def read_Emisiones_module(
    module: schemas.Emisiones_name,
    medida_1: schemas.Trayectoria,
    medida_2: schemas.Trayectoria,
    medida_3: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL
    """
    filter = {'medida_1' : medida_1, 'medida_2' : medida_2, 'medida_3' : medida_3}

    match module:
        case schemas.Emisiones_name.emisiones:
            rd = downloader(
                db=db, 
                model=models.EMISIONES,
                topic='emisiones',
                **filter
                )
            result = jsonable_encoder(rd)

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {result}')

    return result


@router.delete(URI_EMISIONES, status_code=status.HTTP_200_OK)
def delete_Emisiones(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL
    """
    
    prune(db=db, model=models.AGRO_EMISIONES)

    return {'msg': 'Deleted SC successfully'}
