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
            case 'cantidad_de_residuos_generada_anual':
                loader(
                    db=db,
                    model=models.RES_SOL_ST_cantidad_de_residuos_generada_anual, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                    
            case 'tipo_de_gestion':
                loader(
                    db=db, 
                    model=models.RES_SOL_ST_tipo_de_gestion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios':
                loader(
                    db=db,
                    model=models.RES_SOL_ST_cap_inst_sist_recup_aprov_biogas_rellenos_sanit, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
                    
            case 'capacidad_instalada_para_los_sistemas_de_incineracion':
                loader(
                    db=db, 
                    model=models.RES_SOL_ST_capacidad_instalada_sistemas_incineracion, 
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
    """READ ALL
    """
    filter = {'trayectoria' : trayectoria}

    match module:
        case schemas.ST_name.cantidad_de_residuos_generada_anual:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_ST_cantidad_de_residuos_generada_anual,
                topic='cantidad_de_residuos_generada_anual',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.ST_name.tipo_de_gestion:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_ST_tipo_de_gestion,
                topic='tipo_de_gestion',
                **filter
                )
            result = jsonable_encoder(rd)
        
        case schemas.ST_name.capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_ST_cap_inst_sist_recup_aprov_biogas_rellenos_sanit,
                topic='capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.ST_name.capacidad_instalada_para_los_sistemas_de_incineracion:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_ST_capacidad_instalada_sistemas_incineracion,
                topic='capacidad_instalada_para_los_sistemas_de_incineracion',
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
    
    prune(db=db, model=models.RES_SOL_ST_cantidad_de_residuos_generada_anual)
    prune(db=db, model=models.RES_SOL_ST_tipo_de_gestion)
    prune(db=db, model=models.RES_SOL_ST_cap_inst_sist_recup_aprov_biogas_rellenos_sanit)
    prune(db=db, model=models.RES_SOL_ST_capacidad_instalada_sistemas_incineracion)

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
            case 'rellenos_sanitarios_con_captacion_aprovechamiento':
                loader(db=db, model=models.RES_SOL_SF_rellenos_sanitarios_con_captacion_aprovechamiento, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                    
            case 'distribucion_de_los_residuos_por_zona_climatica':
                loader(db=db, model=models.RES_SOL_SF_distribucion_de_los_residuos_por_zona_climatica, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'caracterizacion_por_tipo_de_residuos_generados':
                loader(db=db, model=models.RES_SOL_SF_caracterizacion_por_tipo_de_residuos_generados, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'generacion_de_metano_por_tipologia_de_residuo':
                loader(db=db, model=models.RES_SOL_SF_generacion_de_metano_por_tipologia_de_residuo, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'datos_de_la_generacion_energetica_mediante_incineracion':
                loader(db=db, model=models.RES_SOL_SF_generacion_energetica_mediante_incineracion, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'consumo_energetico_medio_por_tratamiento':
                loader(db=db, model=models.RES_SOL_SF_consumo_energetico_medio_por_tratamiento, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'datos_para_la_estimacion_de_las_emisiones_de_incineracion':
                loader(db=db, model=models.RES_SOL_SF_estimacion_emisiones_incineracion, obj_in=jdata[key], 
                       filters=['topic', 'bloque', 'tipo', 'unidad'])
            
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
    """READ ALL
    """
    
    d = {
        'rellenos_sanitarios_con_captacion_aprovechamiento'         : models.RES_SOL_SF_rellenos_sanitarios_con_captacion_aprovechamiento,
        'distribucion_de_los_residuos_por_zona_climatica'           : models.RES_SOL_SF_distribucion_de_los_residuos_por_zona_climatica,
        'caracterizacion_por_tipo_de_residuos_generados'            : models.RES_SOL_SF_caracterizacion_por_tipo_de_residuos_generados,
        'generacion_de_metano_por_tipologia_de_residuo'             : models.RES_SOL_SF_generacion_de_metano_por_tipologia_de_residuo,
        'datos_de_la_generacion_energetica_mediante_incineracion'   : models.RES_SOL_SF_generacion_energetica_mediante_incineracion,
        'consumo_energetico_medio_por_tratamiento'                  : models.RES_SOL_SF_consumo_energetico_medio_por_tratamiento,
        'datos_para_la_estimacion_de_las_emisiones_de_incineracion' : models.RES_SOL_SF_estimacion_emisiones_incineracion
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
    
    prune(db=db, model=models.RES_SOL_SF_rellenos_sanitarios_con_captacion_aprovechamiento)
    prune(db=db, model=models.RES_SOL_SF_distribucion_de_los_residuos_por_zona_climatica)
    prune(db=db, model=models.RES_SOL_SF_caracterizacion_por_tipo_de_residuos_generados)
    prune(db=db, model=models.RES_SOL_SF_generacion_de_metano_por_tipologia_de_residuo)
    prune(db=db, model=models.RES_SOL_SF_generacion_energetica_mediante_incineracion)
    prune(db=db, model=models.RES_SOL_SF_consumo_energetico_medio_por_tratamiento)
    prune(db=db, model=models.RES_SOL_SF_estimacion_emisiones_incineracion)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas/energia_consumida', 
        response_model=schemas.RES_SOL_SALIDAS_energia_consumida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_consumida(
    data: schemas.RES_SOL_SALIDAS_energia_consumida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.RES_SOL_SALIDAS_energia_consumida, 
        obj_in=jdata['salida_energia_consumida'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1']
    )
    
    return jdata


@router.post(
        path='/salidas/energia_producida', 
        response_model=schemas.RES_SOL_SALIDAS_energia_producida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_producida(
    data: schemas.RES_SOL_SALIDAS_energia_producida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.RES_SOL_SALIDAS_energia_producida, 
        obj_in=jdata['salida_energia_producida'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1']
    )
    
    return jdata


@router.get('/salidas/{module}')
def read_salidas_module(
    module: schemas.Salidas_name,
    medida_res_sol_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL
    """
    filter = {'medida_1' : medida_res_sol_1}

    match module:
        case schemas.Salidas_name.salida_energia_consumida:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_SALIDAS_energia_consumida,
                topic='energia_producida_y_requerida',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.Salidas_name.salida_energia_producida:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_SALIDAS_energia_producida,
                topic='energia_producida_y_requerida',
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
    
    prune(db=db, model=models.RES_SOL_SALIDAS_energia_consumida)
    prune(db=db, model=models.RES_SOL_SALIDAS_energia_producida)

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
        model=models.RES_SOL_emisiones, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'bloque', 'grupo', 'tipo', 'medida_1']
    )
    return jdata


@router.get('/emisiones')
def read_Emisiones_module(
    module: schemas.Emisiones_name,
    medida_res_sol_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL
    """
    filter = {'medida_1' : medida_res_sol_1}

    match module:
        case schemas.Emisiones_name.emisiones_de_gases_de_efecto_invernadero_residuos:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_emisiones,
                topic='emisiones_de_gases_de_efecto_invernadero_residuos',
                **filter
                )
            result = jsonable_encoder(rd)
        
        case schemas.Emisiones_name.emisiones_de_gases_de_efecto_invernadero_energia:
            rd = downloader(
                db=db, 
                model=models.RES_SOL_emisiones,
                topic='emisiones_de_gases_de_efecto_invernadero_energia',
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
    
    prune(db=db, model=models.RES_SOL_emisiones)

    return {'msg': 'Deleted successfully'}
