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
            case 'practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies':
                loader(
                    db=db,
                    model=models.GANA_ST_practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                    
            case 'mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado':
                loader(
                    db=db, 
                    model=models.GANA_ST_mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'produccion_de_estiercol_para_bioenergia':
                loader(
                    db=db, 
                    model=models.GANA_ST_produccion_de_estiercol_para_bioenergia, 
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
        case schemas.ST_name.practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies:
            rd = downloader(
                db=db, 
                model=models.GANA_ST_practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies,
                topic='practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies',
                **filter
                )
            result = jsonable_encoder(rd)
                
        case schemas.ST_name.mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado:
            rd = downloader(
                db=db, 
                model=models.GANA_ST_mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado,
                topic='mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado',
                **filter
                )
            result = jsonable_encoder(rd)
        
        case schemas.ST_name.produccion_de_estiercol_para_bioenergia:
            rd = downloader(
                db=db, 
                model=models.GANA_ST_produccion_de_estiercol_para_bioenergia,
                topic='produccion_de_estiercol_para_bioenergia',
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
    
    prune(db=db, model=models.GANA_ST_practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies)
    prune(db=db, model=models.GANA_ST_mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado)
    prune(db=db, model=models.GANA_ST_produccion_de_estiercol_para_bioenergia)

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
            case 'uso_actual_de_la_tierra_sector_agropecuario_en_colombia':
                loader(db=db, model=models.GANA_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
                    
            case 'hato_ganadero_colombiano':
                loader(db=db, model=models.GANA_SF_hato_ganadero_colombiano, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'factor_de_emision_de_metano_ch4_por_genero':
                loader(db=db, model=models.GANA_SF_factor_de_emision_de_metano_ch4_por_genero, obj_in=jdata[key], 
                       filters=['topic', 'fuente'])
                
            case 'areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos':
                loader(db=db, model=models.GANA_SF_areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones':
                loader(db=db, model=models.GANA_SF_factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones, obj_in=jdata[key], 
                       filters=['topic', 'fuente'])
            
            case 'potencial_energetico_del_estiercol':
                loader(db=db, model=models.GANA_SF_potencial_energetico_del_estiercol, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
                
            case 'potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos':
                loader(db=db, model=models.GANA_SF_potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos, obj_in=jdata[key], 
                       filters=['topic', 'tipo'])
            
            case 'coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual':
                loader(db=db, model=models.GANA_SF_coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual, obj_in=jdata[key], 
                       filters=['topic', 'tipo', 'fuente'])
                
            case 'potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias':
                loader(db=db, model=models.GANA_SF_potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias, obj_in=jdata[key], 
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
        'uso_actual_de_la_tierra_sector_agropecuario_en_colombia'                                : models.GANA_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia,
        'hato_ganadero_colombiano'                                                               : models.GANA_SF_hato_ganadero_colombiano,
        'factor_de_emision_de_metano_ch4_por_genero'                                             : models.GANA_SF_factor_de_emision_de_metano_ch4_por_genero,
        'areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos'       : models.GANA_SF_areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos,
        'factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones'                        : models.GANA_SF_factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones,
        'potencial_energetico_del_estiercol'                                                     : models.GANA_SF_potencial_energetico_del_estiercol,
        'potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos'          : models.GANA_SF_potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos,
        'coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual' : models.GANA_SF_coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual,
        'potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias'                     : models.GANA_SF_potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias
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
    
    prune(db=db, model=models.GANA_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia)
    prune(db=db, model=models.GANA_SF_hato_ganadero_colombiano)
    prune(db=db, model=models.GANA_SF_factor_de_emision_de_metano_ch4_por_genero)
    prune(db=db, model=models.GANA_SF_areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos)
    prune(db=db, model=models.GANA_SF_factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones)
    prune(db=db, model=models.GANA_SF_potencial_energetico_del_estiercol)
    prune(db=db, model=models.GANA_SF_potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos)
    prune(db=db, model=models.GANA_SF_coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual)
    prune(db=db, model=models.GANA_SF_potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas', 
        response_model=schemas.GANA_SALIDAS, 
        status_code=status.HTTP_201_CREATED)
def create_salidas(
    data: schemas.GANA_SALIDAS, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.GANA_SALIDAS, 
        obj_in=jdata['salidas'], 
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
        case schemas.Salidas_name.salidas:
            rd = downloader(
                db=db, 
                model=models.GANA_SALIDAS,
                topic='salidas',
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
    
    prune(db=db, model=models.GANA_SALIDAS)

    return {'msg': 'Deleted Salidas successfully'}

####################################################################################
#######                               Emisiones                              #######
####################################################################################

@router.post(
        path='/emisiones', 
        response_model=schemas.GANA_EMISIONES, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones(
    data: schemas.GANA_EMISIONES, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE
    """

    jdata = jsonable_encoder(data)

    loader(
        db=db, 
        model=models.GANA_EMISIONES, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2', 'medida_3']
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
    
    prune(db=db, model=models.GANA_EMISIONES)

    return {'msg': 'Deleted SC successfully'}
