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
            case 'cantidad_de_aguas_residuales_domesticas':
                loader(
                    db=db,
                    model=models.RES_AGU_ST_cantidad_de_aguas_residuales_domesticas, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                    
            case 'cantidad_de_aguas_residuales_industriales':
                loader(
                    db=db, 
                    model=models.RES_AGU_ST_cantidad_de_aguas_residuales_industriales, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas':
                loader(
                    db=db,
                    model=models.RES_AGU_ST_est_tratam_aguas_res_municipales_extraccion_biogas, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
                    
            case 'estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas':
                loader(
                    db=db, 
                    model=models.RES_AGU_ST_est_tratamiento_aguas_res_ind_extraccion_biogas, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
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
        case schemas.ST_name.cantidad_de_aguas_residuales_domesticas:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_ST_cantidad_de_aguas_residuales_domesticas,
                topic='cantidad_de_aguas_residuales_domesticas',
                **filter
                )
                
        case schemas.ST_name.cantidad_de_aguas_residuales_industriales:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_ST_cantidad_de_aguas_residuales_industriales,
                topic='cantidad_de_aguas_residuales_industriales',
                **filter
                )
        
        case schemas.ST_name.estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_ST_est_tratam_aguas_res_municipales_extraccion_biogas,
                topic='estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas',
                **filter
                )
                
        case schemas.ST_name.estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_ST_est_tratamiento_aguas_res_ind_extraccion_biogas,
                topic='estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas',
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
    
    prune(db=db, model=models.RES_AGU_ST_cantidad_de_aguas_residuales_domesticas)
    prune(db=db, model=models.RES_AGU_ST_cantidad_de_aguas_residuales_industriales)
    prune(db=db, model=models.RES_AGU_ST_est_tratam_aguas_res_municipales_extraccion_biogas)
    prune(db=db, model=models.RES_AGU_ST_est_tratamiento_aguas_res_ind_extraccion_biogas)

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
            case 'dbo_por_m3_de_agua_residual_domestica_tratada':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_tratada, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'dbo_por_m3_de_agua_residual_domestica_no_tratada':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_no_tratada, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                
            case 'dbo_por_m3_de_agua_residual_industrial_tratada':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_tratada, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                
            case 'dbo_por_m3_de_agua_residual_industrial_no_tratada':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_no_tratada, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
            
            case 'generacion_de_ch4_por_kg_dbo_tratado':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_generacion_de_ch4_por_kg_dbo_tratado, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
            
            case 'generacion_de_ch4_por_kg_dbo_no_tratado':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_generacion_de_ch4_por_kg_dbo_no_tratado, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                
            case 'datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_generacion_energetica_estaciones_tratamiento, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
            
            case 'consumo_energetico_medio_por_tratamiento':
                loader(
                    db=db, 
                    model=models.RES_AGU_SF_consumo_energetico_medio_por_tratamiento, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
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
        'dbo_por_m3_de_agua_residual_domestica_tratada'                      : models.RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_tratada,
        'dbo_por_m3_de_agua_residual_domestica_no_tratada'                   : models.RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_no_tratada,
        'dbo_por_m3_de_agua_residual_industrial_tratada'                     : models.RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_tratada,
        'dbo_por_m3_de_agua_residual_industrial_no_tratada'                  : models.RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_no_tratada,
        'generacion_de_ch4_por_kg_dbo_tratado'                               : models.RES_AGU_SF_generacion_de_ch4_por_kg_dbo_tratado,
        'generacion_de_ch4_por_kg_dbo_no_tratado'                            : models.RES_AGU_SF_generacion_de_ch4_por_kg_dbo_no_tratado,
        'datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento' : models.RES_AGU_SF_generacion_energetica_estaciones_tratamiento,
        'consumo_energetico_medio_por_tratamiento'                           : models.RES_AGU_SF_consumo_energetico_medio_por_tratamiento
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
    
    prune(db=db, model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_tratada)
    prune(db=db, model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_no_tratada)
    prune(db=db, model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_tratada)
    prune(db=db, model=models.RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_no_tratada)
    prune(db=db, model=models.RES_AGU_SF_generacion_de_ch4_por_kg_dbo_tratado)
    prune(db=db, model=models.RES_AGU_SF_generacion_de_ch4_por_kg_dbo_no_tratado)
    prune(db=db, model=models.RES_AGU_SF_generacion_energetica_estaciones_tratamiento)
    prune(db=db, model=models.RES_AGU_SF_consumo_energetico_medio_por_tratamiento)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas/energia_consumida', 
        response_model=schemas.RES_AGU_SALIDAS_energia_consumida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_consumida(
    data: schemas.RES_AGU_SALIDAS_energia_consumida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.RES_AGU_SALIDAS_energia_consumida, 
        obj_in=jdata['salida_energia_consumida'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    
    return jdata


@router.post(
        path='/salidas/energia_producida', 
        response_model=schemas.RES_AGU_SALIDAS_energia_producida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_producida(
    data: schemas.RES_AGU_SALIDAS_energia_producida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.RES_AGU_SALIDAS_energia_producida, 
        obj_in=jdata['salida_energia_producida'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    
    return jdata


@router.get('/salidas/{module}')
def read_salidas_module(
    module: schemas.Salidas_name,
    medida_res_agu_1: schemas.Trayectoria,
    medida_res_agu_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_res_agu_1, 'medida_2' : medida_res_agu_2}

    match module:
        case schemas.Salidas_name.salida_energia_consumida:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_SALIDAS_energia_consumida,
                topic='energia_producida_y_requerida',
                **filter
                )
                
        case schemas.Salidas_name.salida_energia_producida:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_SALIDAS_energia_producida,
                topic='energia_producida_y_requerida',
                **filter
                )

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SALIDAS, status_code=status.HTTP_200_OK)
def delete_Salidas(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.RES_AGU_SALIDAS_energia_consumida)
    prune(db=db, model=models.RES_AGU_SALIDAS_energia_producida)

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
        model=models.RES_AGU_emisiones, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1', 'medida_2']
    )
    return jdata

@router.get('/emisiones')
def read_Emisiones_module(
    module: schemas.Emisiones_name,
    medida_res_agu_1: schemas.Trayectoria,
    medida_res_agu_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_res_agu_1, 'medida_2' : medida_res_agu_2}

    match module:
        case schemas.Emisiones_name.emisiones_de_gases_de_efecto_invernadero_aguas_residuales:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_emisiones,
                topic='emisiones_de_gases_de_efecto_invernadero_aguas_residuales',
                **filter
                )
        
        case schemas.Emisiones_name.emisiones_de_gases_de_efecto_invernadero_energia:
            rd = downloader(
                db=db, 
                model=models.RES_AGU_emisiones,
                topic='emisiones_de_gases_de_efecto_invernadero_energia',
                **filter
                )

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)



@router.delete(URI_EMISIONES, status_code=status.HTTP_200_OK)
def delete_Emisiones(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.RES_AGU_emisiones)

    return {'msg': 'Deleted successfully'}
