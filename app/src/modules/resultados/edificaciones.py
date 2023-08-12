from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder

import pandas as pd
import logging

from app.src.crud.base import downloader

from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

from .util.util import db_to_df, db_to_dict, get_item, set_zeros, set_suma_total, not_negative

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######     Evolución de las emisiones del sector Edificaciones              #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_edificaciones')
def resultados_evolucion_de_las_emisiones_del_sector_edificaciones(
    medida_edi_res_acond_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    medida_edi_com_acond_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios   ############## Mt_CO2_e
    
    
    ##########   eficiencia_energetica_y_equipos_eficientes_en_viviendas   ############## Mt_CO2_e
    

    ##########   eficiencia_energetica_para_viviendas_rurales   ############## Mt_CO2_e
    

    ##########   acondicionamiento_de_espacios_comerciales_y_de_servicio   ############## Mt_CO2_e



    ##########   usos_termicos_y_equipamiento_comercial_y_de_servicio   ############## Mt_CO2_e
    
    

    resultado = {"resultados": [
        diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios, 
        eficiencia_energetica_y_equipos_eficientes_en_viviendas, 
        eficiencia_energetica_para_viviendas_rurales, 
        acondicionamiento_de_espacios_comerciales_y_de_servicio,
        usos_termicos_y_equipamiento_comercial_y_de_servicio
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de la demanda energetica del sector edificaciones   #######
#######                      por combustible                                 #######
####################################################################################
@router.get('/evolucion_demanda_energetica_por_combustible')
def resultados_evolucion_demanda_energetica_por_combustible(
    medida_edi_res_acond_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    medida_edi_com_acond_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   electricidad   ############## TWh
    
    
    ##########   gas_natural   ############## TWh
    
    
    ##########   glp   ############## TWh
    

    ##########   petroleo   ############## TWh


    ##########   queroseno   ############## TWh
    
    
    ##########   diesel   ############## TWh
    
    
    ##########   fuel_oil   ############## TWh
    

    ##########   biomansa_seca_y_residuos   ############## TWh
    
    

    resultado = {"resultados": [
        electricidad, 
        gas_natural, 
        glp, 
        petroleo,
        queroseno, 
        diesel, 
        fuel_oil, 
        biomansa_seca_y_residuos
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución del consumo energetico del sector edificaciones     #######
#######                      por sector                                      #######
####################################################################################
@router.get('/evolucion_consumo_energetico_por_sector')
def resultados_evolucion_consumo_energetico_por_sector(
    medida_edi_res_acond_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    medida_edi_com_acond_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   edificaciones_residenciales_urbanas   ############## TWh
    
    
    ##########   edificaciones_residenciales_rurales   ############## TWh
    

    ##########   edificaciones_comerciales_y_de_servicio   ############## TWh
    
    
    

    resultado = {"resultados": [
        edificaciones_residenciales_urbanas, 
        edificaciones_residenciales_rurales,
        edificaciones_comerciales_y_de_servicio
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######   Evolución de la generacion energetica del sector edificaciones     #######
####################################################################################
@router.get('/evolucion_generacion_energetica_sector_edificaciones')
def resultados_evolucion_generacion_energetica_sector_edificaciones(
    medida_edi_res_acond_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    medida_edi_com_acond_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""    
    
    ##########   edificaciones_residenciales_rurales   ############## TWh
    
    
    

    resultado = {"resultados": [edificaciones_residenciales_rurales]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)