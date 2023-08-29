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
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'escenarios_de_deforestacion':
                loader(
                    db=db,
                    model=models.BOSQ_ST_escenarios_de_deforestacion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                    
            case 'desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales':
                loader(
                    db=db, 
                    model=models.BOSQ_ST_plantaciones_forestales_con_fines_comerciales, 
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
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'trayectoria' : trayectoria}

    match module:
        case schemas.ST_name.escenarios_de_deforestacion:
            rd = downloader(
                db=db, 
                model=models.BOSQ_ST_escenarios_de_deforestacion,
                topic='escenarios_de_deforestacion',
                skip=skip, limit=limit,
                **filter
                )
                
        case schemas.ST_name.desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales:
            rd = downloader(
                db=db, 
                model=models.BOSQ_ST_plantaciones_forestales_con_fines_comerciales,
                topic='desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales',
                skip=skip, limit=limit,
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
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.BOSQ_ST_escenarios_de_deforestacion)
    prune(db=db, model=models.BOSQ_ST_plantaciones_forestales_con_fines_comerciales)

    return {'msg': 'Deleted successfully'}


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################
@router.post(URI_SF, response_model=SCHEMAS_SF, status_code=status.HTTP_201_CREATED)
def create_SF(
    data: SCHEMAS_SF, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'area_anual_deforestada_puntual':
                loader(db=db, model=models.BOSQ_SF_area_anual_deforestada_puntual, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                    
            case 'deforestacion_observada_no_acumulada':
                loader(db=db, model=models.BOSQ_SF_deforestacion_observada_no_acumulada, obj_in=jdata[key], 
                       filters=['topic', 'fuente', 'unidad'])
                
            case 'contenidos_de_carbono_por_zonas_naturales':
                loader(db=db, model=models.BOSQ_SF_contenidos_de_carbono_por_zonas_naturales, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'factor_de_conversion_de_biomasa_por_deforestacion':
                loader(db=db, model=models.BOSQ_SF_factor_de_conversion_de_biomasa_por_deforestacion, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'area_para_la_reforestacion_comercial':
                loader(db=db, model=models.BOSQ_SF_area_para_la_reforestacion_comercial, obj_in=jdata[key], 
                       filters=['topic', 'bloque', 'tipo'])
            
            case 'biomasa_aerea_subterranea_reforestacion_comercial':
                loader(db=db, model=models.BOSQ_SF_biomasa_aerea_subterranea_reforestacion_comercial, obj_in=jdata[key], 
                       filters=['topic', 'fuente', 'unidad'])
                
            case 'descuentos_aplicables_a_reforestacion_comercial':
                loader(db=db, model=models.BOSQ_SF_descuentos_aplicables_a_reforestacion_comercial, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
            
            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get(URI_SF, response_model=SCHEMAS_SF)
def read_SF(
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""
    
    d = {
        'area_anual_deforestada_puntual'                    : models.BOSQ_SF_area_anual_deforestada_puntual,
        'deforestacion_observada_no_acumulada'              : models.BOSQ_SF_deforestacion_observada_no_acumulada,
        'contenidos_de_carbono_por_zonas_naturales'         : models.BOSQ_SF_contenidos_de_carbono_por_zonas_naturales,
        'factor_de_conversion_de_biomasa_por_deforestacion' : models.BOSQ_SF_factor_de_conversion_de_biomasa_por_deforestacion,
        'area_para_la_reforestacion_comercial'              : models.BOSQ_SF_area_para_la_reforestacion_comercial,
        'biomasa_aerea_subterranea_reforestacion_comercial' : models.BOSQ_SF_biomasa_aerea_subterranea_reforestacion_comercial,
        'descuentos_aplicables_a_reforestacion_comercial'   : models.BOSQ_SF_descuentos_aplicables_a_reforestacion_comercial
        }
    
    rd = downloader_batch(db=db, skip=skip, limit=limit, **d)
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SF, status_code=status.HTTP_200_OK)
def delete_SF(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.BOSQ_SF_area_anual_deforestada_puntual)
    prune(db=db, model=models.BOSQ_SF_deforestacion_observada_no_acumulada)
    prune(db=db, model=models.BOSQ_SF_contenidos_de_carbono_por_zonas_naturales)
    prune(db=db, model=models.BOSQ_SF_factor_de_conversion_de_biomasa_por_deforestacion)
    prune(db=db, model=models.BOSQ_SF_area_para_la_reforestacion_comercial)
    prune(db=db, model=models.BOSQ_SF_biomasa_aerea_subterranea_reforestacion_comercial)
    prune(db=db, model=models.BOSQ_SF_descuentos_aplicables_a_reforestacion_comercial)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas', 
        response_model=schemas.SALIDAS, 
        status_code=status.HTTP_201_CREATED)
def create_total_areas_reforestadas(
    data: schemas.SALIDAS, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.BOSQ_SALIDAS, 
        obj_in=jdata['salidas'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    return jdata


@router.get('/salidas')
def read_salidas_module(
    medida_bosq_1: schemas.Trayectoria,
    medida_bosq_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_bosq_1, 'medida_2' : medida_bosq_2}

    rd = downloader(
        db=db, 
        model=models.BOSQ_SALIDAS,
        topic='total_areas_reforestadas',
        skip=skip, limit=limit,
        **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SALIDAS, status_code=status.HTTP_200_OK)
def delete_Salidas(
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.BOSQ_SALIDAS)

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
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.BOSQ_EMISIONES, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    return jdata


@router.get('/emisiones')
def read_emisiones_module(
    medida_bosq_1: schemas.Trayectoria,
    medida_bosq_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_bosq_1, 'medida_2' : medida_bosq_2}

    rd = downloader(
        db=db, 
        model=models.BOSQ_EMISIONES,
        topic='total_emisiones',
        skip=skip, limit=limit,
        **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_EMISIONES, status_code=status.HTTP_200_OK)
def delete_Emisiones(
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.BOSQ_EMISIONES)

    return {'msg': 'Deleted successfully'}
