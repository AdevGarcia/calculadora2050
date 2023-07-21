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
            case 'reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica':
                loader(
                    db=db,
                    model=models.INDU_ST_reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                    
            case 'eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras':
                loader(
                    db=db, 
                    model=models.INDU_ST_eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
                
            case 'eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion':
                loader(
                    db=db, 
                    model=models.INDU_ST_eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                
            case 'eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras':
                loader(
                    db=db, 
                    model=models.INDU_ST_eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
                
            case 'sustitucion_de_sao_y_hfc':
                loader(
                    db=db, 
                    model=models.INDU_ST_sustitucion_de_sao_y_hfc, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                
            case 'procesos_productivos_sostenibles':
                loader(
                    db=db, 
                    model=models.INDU_ST_procesos_productivos_sostenibles, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )

            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


# @router.get(URI_ST, response_model=SCHEMAS_ST)
# def read_ST(
#     db: Session = Depends(deps.get_db), 
#     # skip: int = 0, 
#     # limit: int = 100,
#     # current_user: models_user.User = Depends(deps.get_current_active_user)
#     ) -> Any:
#     """READ ALL
#     """

#     d = {
#         'reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica' : models.INDU_ST_reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica,
#         'eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras'       : models.INDU_ST_eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras,
#         'eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion'      : models.INDU_ST_eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion,
#         'eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras'         : models.INDU_ST_eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras,
#         'sustitucion_de_sao_y_hfc'                                                : models.INDU_ST_sustitucion_de_sao_y_hfc,
#         'procesos_productivos_sostenibles'                                        : models.INDU_ST_procesos_productivos_sostenibles
#         }
    
#     rd = downloader_batch(db=db, **d)
#     result = jsonable_encoder(rd)
    
#     if DEBUG:
#         logger.info(f'Read Data: {result}')

#     return result


@router.get('/supuestos_trayectoria/{module}')#, response_model=SCHEMAS_ST)
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
        case schemas.ST_name.reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica:
            rd = downloader(
                db=db, 
                model=models.INDU_ST_reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica,
                topic='reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.ST_name.eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras:
            rd = downloader(
                db=db, 
                model=models.INDU_ST_eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras,
                topic='eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.ST_name.eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion:
            rd = downloader(
                db=db, 
                model=models.INDU_ST_eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion,
                topic='eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.ST_name.eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras:
            rd = downloader(
                db=db, 
                model=models.INDU_ST_eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras,
                topic='eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.ST_name.sustitucion_de_sao_y_hfc:
            rd = downloader(
                db=db, 
                model=models.INDU_ST_sustitucion_de_sao_y_hfc,
                topic='sustitucion_de_sao_y_hfc',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.ST_name.procesos_productivos_sostenibles:
            rd = downloader(
                db=db, 
                model=models.INDU_ST_procesos_productivos_sostenibles,
                topic='procesos_productivos_sostenibles',
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
    
    prune(db=db, model=models.INDU_ST_reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica)
    prune(db=db, model=models.INDU_ST_eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras)
    prune(db=db, model=models.INDU_ST_eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion)
    prune(db=db, model=models.INDU_ST_eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras)
    prune(db=db, model=models.INDU_ST_sustitucion_de_sao_y_hfc)
    prune(db=db, model=models.INDU_ST_procesos_productivos_sostenibles)

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
            case 'produccion_anual_de_materiales':
                loader(db=db, model=models.INDU_SF_produccion_anual_de_materiales, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                    
            case 'produccion_de_acido_nitrico':
                loader(db=db, model=models.INDU_SF_produccion_de_acido_nitrico, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'produccion_de_cemento':
                loader(db=db, model=models.INDU_SF_produccion_de_cemento, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'produccion_anual_de_ladrillos':
                loader(db=db, model=models.INDU_SF_produccion_anual_de_ladrillos, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'indice_de_consumo':
                loader(db=db, model=models.INDU_SF_indice_de_consumo, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'distribucion_segun_tipo_de_combustible_ladrilleras':
                loader(db=db, model=models.INDU_SF_distribucion_segun_tipo_de_combustible_ladrilleras, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'uso_energetico_por_combustible':
                loader(db=db, model=models.INDU_SF_uso_energetico_por_combustible, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
            
            case 'factor_de_utilizacion_de_autogeneracion_y_cogeneracion':
                loader(db=db, model=models.INDU_SF_factor_de_utilizacion_de_autogeneracion_y_cogeneracion, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'capacidad_instalada_de_autogeneracion':
                loader(db=db, model=models.INDU_SF_capacidad_instalada_de_autogeneracion, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
            
            case 'excedentes_de_autogeneracion':
                loader(db=db, model=models.INDU_SF_excedentes_de_autogeneracion, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
            
            case 'capacidad_instalada_de_cogeneracion':
                loader(db=db, model=models.INDU_SF_capacidad_instalada_de_cogeneracion, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])

            case 'excedentes_de_cogeneracion':
                loader(db=db, model=models.INDU_SF_excedentes_de_cogeneracion, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
    
            case 'emision_de_sao':
                loader(db=db, model=models.INDU_SF_emision_de_sao, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])

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
        'produccion_anual_de_materiales'                         : models.INDU_SF_produccion_anual_de_materiales,
        'produccion_de_acido_nitrico'                            : models.INDU_SF_produccion_de_acido_nitrico,
        'produccion_de_cemento'                                  : models.INDU_SF_produccion_de_cemento,
        'produccion_anual_de_ladrillos'                          : models.INDU_SF_produccion_anual_de_ladrillos,
        'indice_de_consumo'                                      : models.INDU_SF_indice_de_consumo,
        'distribucion_segun_tipo_de_combustible_ladrilleras'     : models.INDU_SF_distribucion_segun_tipo_de_combustible_ladrilleras,
        'uso_energetico_por_combustible'                         : models.INDU_SF_uso_energetico_por_combustible,
        'factor_de_utilizacion_de_autogeneracion_y_cogeneracion' : models.INDU_SF_factor_de_utilizacion_de_autogeneracion_y_cogeneracion,
        'capacidad_instalada_de_autogeneracion'                  : models.INDU_SF_capacidad_instalada_de_autogeneracion,
        'excedentes_de_autogeneracion'                           : models.INDU_SF_excedentes_de_autogeneracion,
        'capacidad_instalada_de_cogeneracion'                    : models.INDU_SF_capacidad_instalada_de_cogeneracion,
        'excedentes_de_cogeneracion'                             : models.INDU_SF_excedentes_de_cogeneracion,
        'emision_de_sao'                                         : models.INDU_SF_emision_de_sao
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
    
    prune(db=db, model=models.INDU_SF_produccion_anual_de_materiales)
    prune(db=db, model=models.INDU_SF_produccion_de_acido_nitrico)
    prune(db=db, model=models.INDU_SF_produccion_de_cemento)
    prune(db=db, model=models.INDU_SF_produccion_anual_de_ladrillos)
    prune(db=db, model=models.INDU_SF_indice_de_consumo)
    prune(db=db, model=models.INDU_SF_distribucion_segun_tipo_de_combustible_ladrilleras)
    prune(db=db, model=models.INDU_SF_uso_energetico_por_combustible)
    prune(db=db, model=models.INDU_SF_factor_de_utilizacion_de_autogeneracion_y_cogeneracion)
    prune(db=db, model=models.INDU_SF_capacidad_instalada_de_autogeneracion)
    prune(db=db, model=models.INDU_SF_excedentes_de_autogeneracion)
    prune(db=db, model=models.INDU_SF_capacidad_instalada_de_cogeneracion)
    prune(db=db, model=models.INDU_SF_excedentes_de_cogeneracion)
    prune(db=db, model=models.INDU_SF_emision_de_sao)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas/salida_energia_requerida_combustible', 
        response_model=schemas.INDU_SALIDAS_por_combustible_energia_requerida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_requerida_combustible(
    data: schemas.INDU_SALIDAS_por_combustible_energia_requerida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_SALIDAS_por_combustible_energia_requerida, 
        obj_in=jdata['salida_energia_requerida_combustible'], 
        filters=['bloque', 'topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.post(
        path='/salidas/salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible', 
        response_model=schemas.INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible(
    data: schemas.INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion, 
        obj_in=jdata['salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible'], 
        filters=['bloque', 'topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.post(
        path='/salidas/salida_balance_total_de_la_energia_requerida_combustible', 
        response_model=schemas.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_balance_total_de_la_energia_requerida_combustible(
    data: schemas.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida, 
        obj_in=jdata['salida_balance_total_de_la_energia_requerida_combustible'], 
        filters=['bloque', 'topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.post(
        path='/salidas/salida_energia_requerida_industria', 
        response_model=schemas.INDU_SALIDAS_por_tipo_de_industria_energia_requerida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_requerida_industria(
    data: schemas.INDU_SALIDAS_por_tipo_de_industria_energia_requerida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_SALIDAS_por_tipo_de_industria_energia_requerida, 
        obj_in=jdata['salida_energia_requerida_industria'], 
        filters=['bloque', 'topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.post(
        path='/salidas/salida_energia_producida_por_autogeneracion_y_cogeneracion_industria', 
        response_model=schemas.INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion, 
        status_code=status.HTTP_201_CREATED)
def create_salida_energia_producida_por_autogeneracion_y_cogeneracion_industria(
    data: schemas.INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion, 
        obj_in=jdata['salida_energia_producida_por_autogeneracion_y_cogeneracion_industria'], 
        filters=['bloque', 'topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.post(
        path='/salidas/salida_balance_total_de_la_energia_requerida_industria', 
        response_model=schemas.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida, 
        status_code=status.HTTP_201_CREATED)
def create_salida_balance_total_de_la_energia_requerida_industria(
    data: schemas.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida, 
        obj_in=jdata['salida_balance_total_de_la_energia_requerida_industria'], 
        filters=['bloque', 'topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.get('/salidas/{module}')#, response_model=SCHEMAS_SALIDAS)
def read_Salidas_module(
    module: schemas.Salidas_name,
    medida_1: schemas.Trayectoria,
    medida_2: schemas.Trayectoria,
    medida_3: schemas.Trayectoria,
    medida_4: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL
    """
    filter = {'medida_1' : medida_1, 'medida_2' : medida_2, 'medida_3' : medida_3, 'medida_4' : medida_4}

    match module:
        case schemas.Salidas_name.salida_energia_requerida_combustible:
            rd = downloader(
                db=db, 
                model=models.INDU_SALIDAS_por_combustible_energia_requerida,
                topic='energia_requerida',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.Salidas_name.salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible:
            rd = downloader(
                db=db, 
                model=models.INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion,
                topic='energia_producida_por_autogeneracion_y_cogeneracion',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.Salidas_name.salida_balance_total_de_la_energia_requerida_combustible:
            rd = downloader(
                db=db, 
                model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
                topic='balance_total_de_la_energia_requerida',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.Salidas_name.salida_energia_requerida_industria:
            rd = downloader(
                db=db, 
                model=models.INDU_SALIDAS_por_tipo_de_industria_energia_requerida,
                topic='energia_requerida',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.Salidas_name.salida_energia_producida_por_autogeneracion_y_cogeneracion_industria:
            rd = downloader(
                db=db, 
                model=models.INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion,
                topic='energia_producida_por_autogeneracion_y_cogeneracion',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.Salidas_name.salida_balance_total_de_la_energia_requerida_industria:
            rd = downloader(
                db=db, 
                model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
                topic='balance_total_de_la_energia',
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
    
    prune(db=db, model=models.INDU_SALIDAS_por_combustible_energia_requerida)
    prune(db=db, model=models.INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion)
    prune(db=db, model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida)
    prune(db=db, model=models.INDU_SALIDAS_por_tipo_de_industria_energia_requerida)
    prune(db=db, model=models.INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion)
    prune(db=db, model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida)

    return {'msg': 'Deleted Salidas successfully'}

####################################################################################
#######                               Emisiones                              #######
####################################################################################

@router.post(
        path='/emisiones/emisiones_gases_efecto_invernadero', 
        response_model=schemas.INDU_emisiones_gases_efecto_invernadero, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones_gases_efecto_invernadero(
    data: schemas.INDU_emisiones_gases_efecto_invernadero, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_emisiones_gases_efecto_invernadero, 
        obj_in=jdata['emisiones_gases_efecto_invernadero'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.post(
        path='/emisiones/emisiones_por_el_consumo_de_bagazo_y_otros', 
        response_model=schemas.INDU_emisiones_por_el_consumo_de_bagazo_y_otros, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones_por_el_consumo_de_bagazo_y_otros(
    data: schemas.INDU_emisiones_por_el_consumo_de_bagazo_y_otros, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_emisiones_por_el_consumo_de_bagazo_y_otros, 
        obj_in=jdata['emisiones_por_el_consumo_de_bagazo_y_otros'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.post(
        path='/emisiones/emisiones_sao', 
        response_model=schemas.INDU_emisiones_sao, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones_sao(
    data: schemas.INDU_emisiones_sao, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.INDU_emisiones_sao, 
        obj_in=jdata['emisiones_sao'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2', 'medida_3', 'medida_4']
    )
    
    return jdata


@router.get('/emisiones/{module}')#, response_model=SCHEMAS_SALIDAS)
def read_Emisiones_module(
    module: schemas.Emisiones_name,
    medida_1: schemas.Trayectoria,
    medida_2: schemas.Trayectoria,
    medida_3: schemas.Trayectoria,
    medida_4: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL
    """
    filter = {'medida_1' : medida_1, 'medida_2' : medida_2, 'medida_3' : medida_3, 'medida_4' : medida_4}

    match module:
        case schemas.Emisiones_name.emisiones_gases_efecto_invernadero:
            rd = downloader(
                db=db, 
                model=models.INDU_emisiones_gases_efecto_invernadero,
                topic='gases_efecto_invernadero',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.Emisiones_name.emisiones_por_el_consumo_de_bagazo_y_otros:
            rd = downloader(
                db=db, 
                model=models.INDU_emisiones_por_el_consumo_de_bagazo_y_otros,
                topic='gases_efecto_invernadero',
                **filter
                )
            result = jsonable_encoder(rd)
            
        case schemas.Emisiones_name.emisiones_sao:
            rd = downloader(
                db=db, 
                model=models.INDU_emisiones_sao,
                topic='gases_efecto_invernadero',
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
    
    prune(db=db, model=models.INDU_emisiones_gases_efecto_invernadero)
    prune(db=db, model=models.INDU_emisiones_por_el_consumo_de_bagazo_y_otros)
    prune(db=db, model=models.INDU_emisiones_sao)

    return {'msg': 'Deleted SC successfully'}
