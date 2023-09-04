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
            case 'transporte_urbano_distribucion_modal':
                loader(
                    db=db,
                    model=models.TRANS_PAS_ST_transporte_urbano_distribucion_modal, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'transporte_urbano_distancia_promedio_por_viaje_por_modo':
                loader(
                    db=db,
                    model=models.TRANS_PAS_ST_transp_urbano_dist_promedio_viaje_modo, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'transporte_urbano_distribucion_por_tecnologia':
                loader(
                    db=db,
                    model=models.TRANS_PAS_ST_transporte_urbano_distribucion_por_tecnologia, 
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
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'trayectoria' : trayectoria}

    match module:        
        case schemas.ST_name.transporte_urbano_distribucion_modal:
            rd = downloader(
                db=db, 
                model=models.TRANS_PAS_ST_transporte_urbano_distribucion_modal,
                topic='transporte_urbano_distribucion_modal',
                skip=skip, limit=limit,
                **filter
                )
        
        case schemas.ST_name.transporte_urbano_distancia_promedio_por_viaje_por_modo:
            rd = downloader(
                db=db, 
                model=models.TRANS_PAS_ST_transp_urbano_dist_promedio_viaje_modo,
                topic='transporte_urbano_distancia_promedio_por_viaje_por_modo',
                skip=skip, limit=limit,
                **filter
                )
        
        case schemas.ST_name.transporte_urbano_distribucion_por_tecnologia:
            rd = downloader(
                db=db, 
                model=models.TRANS_PAS_ST_transporte_urbano_distribucion_por_tecnologia,
                topic='transporte_urbano_distribucion_por_tecnologia',
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
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.TRANS_PAS_ST_transporte_urbano_distribucion_modal)
    prune(db=db, model=models.TRANS_PAS_ST_transp_urbano_dist_promedio_viaje_modo)
    prune(db=db, model=models.TRANS_PAS_ST_transporte_urbano_distribucion_por_tecnologia)

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
            case 'n_viajes_por_habitante_por_dia':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_n_viajes_por_habitante_por_dia, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'uso_de_combustibles_fosiles_en_vehiculos_hibridos':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_uso_de_combustibles_fosiles_en_vehiculos_hibridos, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'unidad']
                )
            
            case 'rendimiento_modo_tecnologia_transporte_urbano_vehiculos_nuevos':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_nuevos, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'rendimiento_modo_tecnologia_transporte_urbano_vehiculos_existentes':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_existentes, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
            
            case 'rendimiento_modo_tecnologia_transporte_urbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_rendimiento_modo_tecnologia_transporte_urbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'rendimiento_modo_tecnologia_transporte_urbano_electrico':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_rend_modo_tec_transp_urbano_electrico, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'gas_natural_vehicular':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_gas_natural_vehicular, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'porcentaje_de_vehiculos_nuevos_transporte_urbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_porcentaje_de_vehiculos_nuevos_transporte_urbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'kilometros_totales_modo_carretero_transporte_interurbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_km_tot_modo_carretero_transp_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'demanda_de_energia_otros_modos_transporte_interurbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_demanda_ener_otros_modos_transp_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'porcentaje_de_demanda_electrica_para_el_modo_ferreo':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_demanda_electrica_modo_ferreo, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'distribucion_por_modo_carretero_transporte_interurbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_distr_modo_carretero_trans_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'rendimiento_modo_tecnologia_transporte_interurbano_vehiculos_existentes':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_rend_modo_tec_trans_interurbano_vehic_existentes, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'porcentaje_de_vehiculos_nuevos_transporte_interurbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_vehiculos_nuevos_transp_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'distancia_tipica_viajada_por_modo_transporte_urbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_dist_tip_viajada_por_modo_transp_urbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'distancia_tipica_viajada_por_modo_transporte_interurbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_dist_tip_viajada_modo_transp_interurbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'total_viajes_anuales':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_total_viajes_anuales, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'vida_util':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_vida_util, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo', 'unidad']
                )
                    
            case 'numero_de_vehiculos_transporte_urbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_numero_de_vehiculos_transporte_urbano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                    
            case 'numero_de_vehiculos_transporte_interurbano':
                loader(
                    db=db, 
                    model=models.TRANS_PAS_SF_numero_de_vehiculos_transporte_interurbano, 
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
        'n_viajes_por_habitante_por_dia'                                          : models.TRANS_PAS_SF_n_viajes_por_habitante_por_dia,
        'uso_de_combustibles_fosiles_en_vehiculos_hibridos'                       : models.TRANS_PAS_SF_uso_de_combustibles_fosiles_en_vehiculos_hibridos,
        'rendimiento_modo_tecnologia_transporte_urbano_vehiculos_nuevos'          : models.TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_nuevos,
        'rendimiento_modo_tecnologia_transporte_urbano_vehiculos_existentes'      : models.TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_existentes,
        'rendimiento_modo_tecnologia_transporte_urbano'                           : models.TRANS_PAS_SF_rendimiento_modo_tecnologia_transporte_urbano,
        'rendimiento_modo_tecnologia_transporte_urbano_electrico'                 : models.TRANS_PAS_SF_rend_modo_tec_transp_urbano_electrico,
        'gas_natural_vehicular'                                                   : models.TRANS_PAS_SF_gas_natural_vehicular,
        'porcentaje_de_vehiculos_nuevos_transporte_urbano'                        : models.TRANS_PAS_SF_porcentaje_de_vehiculos_nuevos_transporte_urbano,
        'kilometros_totales_modo_carretero_transporte_interurbano'                : models.TRANS_PAS_SF_km_tot_modo_carretero_transp_interurbano,
        'demanda_de_energia_otros_modos_transporte_interurbano'                   : models.TRANS_PAS_SF_demanda_ener_otros_modos_transp_interurbano,
        'porcentaje_de_demanda_electrica_para_el_modo_ferreo'                     : models.TRANS_PAS_SF_demanda_electrica_modo_ferreo,
        'distribucion_por_modo_carretero_transporte_interurbano'                  : models.TRANS_PAS_SF_distr_modo_carretero_trans_interurbano,
        'rendimiento_modo_tecnologia_transporte_interurbano_vehiculos_existentes' : models.TRANS_PAS_SF_rend_modo_tec_trans_interurbano_vehic_existentes,
        'porcentaje_de_vehiculos_nuevos_transporte_interurbano'                   : models.TRANS_PAS_SF_vehiculos_nuevos_transp_interurbano,
        'distancia_tipica_viajada_por_modo_transporte_urbano'                     : models.TRANS_PAS_SF_dist_tip_viajada_por_modo_transp_urbano,
        'distancia_tipica_viajada_por_modo_transporte_interurbano'                : models.TRANS_PAS_SF_dist_tip_viajada_modo_transp_interurbano,
        'total_viajes_anuales'                                                    : models.TRANS_PAS_SF_total_viajes_anuales,
        'vida_util'                                                               : models.TRANS_PAS_SF_vida_util,
        'numero_de_vehiculos_transporte_urbano'                                   : models.TRANS_PAS_SF_numero_de_vehiculos_transporte_urbano,
        'numero_de_vehiculos_transporte_interurbano'                              : models.TRANS_PAS_SF_numero_de_vehiculos_transporte_interurbano
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

    prune(db=db, model=models.TRANS_PAS_SF_n_viajes_por_habitante_por_dia)
    prune(db=db, model=models.TRANS_PAS_SF_uso_de_combustibles_fosiles_en_vehiculos_hibridos)
    prune(db=db, model=models.TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_nuevos)
    prune(db=db, model=models.TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_existentes)
    prune(db=db, model=models.TRANS_PAS_SF_rendimiento_modo_tecnologia_transporte_urbano)
    prune(db=db, model=models.TRANS_PAS_SF_rend_modo_tec_transp_urbano_electrico)
    prune(db=db, model=models.TRANS_PAS_SF_gas_natural_vehicular)
    prune(db=db, model=models.TRANS_PAS_SF_porcentaje_de_vehiculos_nuevos_transporte_urbano)
    prune(db=db, model=models.TRANS_PAS_SF_km_tot_modo_carretero_transp_interurbano)
    prune(db=db, model=models.TRANS_PAS_SF_demanda_ener_otros_modos_transp_interurbano)
    prune(db=db, model=models.TRANS_PAS_SF_demanda_electrica_modo_ferreo)
    prune(db=db, model=models.TRANS_PAS_SF_distr_modo_carretero_trans_interurbano)
    prune(db=db, model=models.TRANS_PAS_SF_rend_modo_tec_trans_interurbano_vehic_existentes)
    prune(db=db, model=models.TRANS_PAS_SF_vehiculos_nuevos_transp_interurbano)
    prune(db=db, model=models.TRANS_PAS_SF_dist_tip_viajada_por_modo_transp_urbano)
    prune(db=db, model=models.TRANS_PAS_SF_dist_tip_viajada_modo_transp_interurbano)
    prune(db=db, model=models.TRANS_PAS_SF_total_viajes_anuales)
    prune(db=db, model=models.TRANS_PAS_SF_vida_util)
    prune(db=db, model=models.TRANS_PAS_SF_numero_de_vehiculos_transporte_urbano)
    prune(db=db, model=models.TRANS_PAS_SF_numero_de_vehiculos_transporte_interurbano)

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
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros, 
        obj_in=jdata['salidas'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    return jdata


@router.get('/salidas')
def read_salidas_module(
    medida_trans_pas_1: schemas.Trayectoria,
    medida_trans_pas_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_trans_pas_1, 'medida_2' : medida_trans_pas_2}

    rd = downloader(
        db=db, 
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        topic='energia_requerida_transporte_pasajeros',
        skip=skip, limit=limit,
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
    
    prune(db=db, model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros)

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
        model=models.TRANS_PAS_emisiones_de_gases_efecto_invernadero, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2']
    )
    return jdata


@router.get('/emisiones')
def read_Emisiones_module(
    medida_trans_pas_1: schemas.Trayectoria,
    medida_trans_pas_2: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_trans_pas_1, 'medida_2' : medida_trans_pas_2}

    rd = downloader(
            db=db, 
            model=models.TRANS_PAS_emisiones_de_gases_efecto_invernadero,
            topic='emisiones_de_gases_efecto_invernadero',
            skip=skip, limit=limit,
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
    
    prune(db=db, model=models.TRANS_PAS_emisiones_de_gases_efecto_invernadero)

    return {'msg': 'Deleted successfully'}
