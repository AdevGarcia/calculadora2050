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
            case 'uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_uso_ener_trans_ferreo_transp_carga_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
            
            case 'distancia_modo_ferreo':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_distancia_modo_ferreo, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
            
            case 'distancia_para_el_transporte_carretero_transporte_de_carga_interurbano':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_dist_trans_carretero_transp_carga_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
            
            case 'uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_uso_ener_trans_fluvial_transp_carga_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
            
            case 'uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_uso_de_ener_trans_aereo_trans_carga_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
            
            case 'carga_sustituida_por_modo_transporte_de_carga_interurbano':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_carga_sustituida_modo_trans_carga_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'distribucion_por_tecnologia_transporte_de_carga_urbano':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_distr_tecnologia_transporte_carga_urbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'distribucion_por_tecnologia_transporte_de_carga_interurbano':
                loader(
                    db=db,
                    model=models.TRANS_CAR_ST_dist_tecn_transporte_carga_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo', 'trayectoria']
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
        case schemas.ST_name.uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_uso_ener_trans_ferreo_transp_carga_interurbano,
                topic='uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano',
                **filter
                )
        
        case schemas.ST_name.distancia_modo_ferreo:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_distancia_modo_ferreo,
                topic='distancia_modo_ferreo',
                **filter
                )
        
        case schemas.ST_name.distancia_para_el_transporte_carretero_transporte_de_carga_interurbano:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_dist_trans_carretero_transp_carga_interurbano,
                topic='distancia_para_el_transporte_carretero_transporte_de_carga_interurbano',
                **filter
                )
        
        case schemas.ST_name.uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_uso_ener_trans_fluvial_transp_carga_interurbano,
                topic='uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano',
                **filter
                )
        
        case schemas.ST_name.uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_uso_de_ener_trans_aereo_trans_carga_interurbano,
                topic='uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano',
                **filter
                )
        
        case schemas.ST_name.carga_sustituida_por_modo_transporte_de_carga_interurbano:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_carga_sustituida_modo_trans_carga_interurbano,
                topic='carga_sustituida_por_modo_transporte_de_carga_interurbano',
                **filter
                )
        
        case schemas.ST_name.distribucion_por_tecnologia_transporte_de_carga_urbano:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_distr_tecnologia_transporte_carga_urbano,
                topic='distribucion_por_tecnologia_transporte_de_carga_urbano',
                **filter
                )
        
        case schemas.ST_name.distribucion_por_tecnologia_transporte_de_carga_interurbano:
            rd = downloader(
                db=db, 
                model=models.TRANS_CAR_ST_dist_tecn_transporte_carga_interurbano,
                topic='distribucion_por_tecnologia_transporte_de_carga_interurbano',
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
    
    prune(db=db, model=models.TRANS_CAR_ST_uso_ener_trans_ferreo_transp_carga_interurbano)
    prune(db=db, model=models.TRANS_CAR_ST_distancia_modo_ferreo)
    prune(db=db, model=models.TRANS_CAR_ST_dist_trans_carretero_transp_carga_interurbano)
    prune(db=db, model=models.TRANS_CAR_ST_uso_ener_trans_fluvial_transp_carga_interurbano)
    prune(db=db, model=models.TRANS_CAR_ST_uso_de_ener_trans_aereo_trans_carga_interurbano)
    prune(db=db, model=models.TRANS_CAR_ST_carga_sustituida_modo_trans_carga_interurbano)
    prune(db=db, model=models.TRANS_CAR_ST_distr_tecnologia_transporte_carga_urbano)
    prune(db=db, model=models.TRANS_CAR_ST_dist_tecn_transporte_carga_interurbano)

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
            case 'factor_de_actividad_transporte_de_carga_urbano':
                loader(
                    db=db, 
                    model=models.TRANS_CAR_SF_factor_de_actividad_transporte_de_carga_urbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'rendimiento_modo_carretero':
                loader(
                    db=db, 
                    model=models.TRANS_CAR_SF_rendimiento_modo_carretero, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
            
            case 'distancia_tipica_por_modo':
                loader(
                    db=db, 
                    model=models.TRANS_CAR_SF_distancia_tipica_por_modo, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'vida_util':
                loader(
                    db=db, 
                    model=models.TRANS_CAR_SF_vida_util, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'unidad']
                )
            
            case 'numero_de_vehiculos_transporte_de_carga_urbano':
                loader(
                    db=db, 
                    model=models.TRANS_CAR_SF_numero_de_vehiculos_transporte_de_carga_urbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'numero_de_vehiculos_transporte_de_carga_interurbano':
                loader(
                    db=db, 
                    model=models.TRANS_CAR_SF_num_vehiculos_transporte_carga_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
             
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
    """READ ALL"""
    
    d = {
        'factor_de_actividad_transporte_de_carga_urbano'      : models.TRANS_CAR_SF_factor_de_actividad_transporte_de_carga_urbano,
        'rendimiento_modo_carretero'                          : models.TRANS_CAR_SF_rendimiento_modo_carretero,
        'distancia_tipica_por_modo'                           : models.TRANS_CAR_SF_distancia_tipica_por_modo,
        'vida_util'                                           : models.TRANS_CAR_SF_vida_util,
        'numero_de_vehiculos_transporte_de_carga_urbano'      : models.TRANS_CAR_SF_numero_de_vehiculos_transporte_de_carga_urbano,
        'numero_de_vehiculos_transporte_de_carga_interurbano' : models.TRANS_CAR_SF_num_vehiculos_transporte_carga_interurbano
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
    
    prune(db=db, model=models.TRANS_CAR_SF_factor_de_actividad_transporte_de_carga_urbano)
    prune(db=db, model=models.TRANS_CAR_SF_rendimiento_modo_carretero)
    prune(db=db, model=models.TRANS_CAR_SF_distancia_tipica_por_modo)
    prune(db=db, model=models.TRANS_CAR_SF_vida_util)
    prune(db=db, model=models.TRANS_CAR_SF_numero_de_vehiculos_transporte_de_carga_urbano)
    prune(db=db, model=models.TRANS_CAR_SF_num_vehiculos_transporte_carga_interurbano)

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
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera, 
        obj_in=jdata['salidas'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    return jdata


@router.get('/salidas')
def read_salidas_module(
    medida_trans_car_1: schemas.Trayectoria,
    medida_trans_car_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_trans_car_1, 'medida_2' : medida_trans_car_2}

    rd = downloader(
        db=db, 
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        topic='energia_requerida_transporte_de_carretera',
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
    
    prune(db=db, model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera)

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
        model=models.TRANS_CAR_emisiones_de_gases_efecto_invernadero, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    return jdata


@router.get('/emisiones')
def read_Emisiones_module(
    medida_trans_car_1: schemas.Trayectoria,
    medida_trans_car_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_trans_car_1, 'medida_2' : medida_trans_car_2}

    rd = downloader(
            db=db, 
            model=models.TRANS_CAR_emisiones_de_gases_efecto_invernadero,
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
    
    prune(db=db, model=models.TRANS_CAR_emisiones_de_gases_efecto_invernadero)

    return {'msg': 'Deleted successfully'}
