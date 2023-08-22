from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder

import pandas as pd
import logging

from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

from .util.constants import YEARS
from .util.util import get_item, get_total, not_negative, abs_negative

from .endpoint_ener_combfosil import (
    read_entradas_energia_combustibles_fosiles_gasolina, 
    read_entradas_energia_combustibles_fosiles_diesel,
    read_entradas_energia_combustibles_fosiles_fuel_oil,
    read_entradas_energia_combustibles_fosiles_glp,
    read_entradas_energia_combustibles_fosiles_queroseno,
    read_entradas_energia_combustibles_fosiles_gas_natural,
    read_entradas_energia_combustibles_fosiles_carbon
    )

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


@router.get('/requerimientos_energeticos')
def read_entradas_requerimientos_energeticos(
    medida_ener_1: schemas.Trayectoria=1,
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ####################################################################################
    #######                              crudo                                   #######
    ####################################################################################

    gasolina = read_entradas_energia_combustibles_fosiles_gasolina(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_trans_car_1=medida_trans_car_1,
        medida_trans_car_2=medida_trans_car_2,
        medida_trans_pas_1=medida_trans_pas_1,
        medida_trans_pas_2=medida_trans_pas_2
        ) 

    diesel = read_entradas_energia_combustibles_fosiles_diesel(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_trans_car_1=medida_trans_car_1,
        medida_trans_car_2=medida_trans_car_2,
        medida_trans_pas_1=medida_trans_pas_1,
        medida_trans_pas_2=medida_trans_pas_2,
        medida_trans_nav_1=medida_trans_nav_1,
        medida_edi_com_ute_1=medida_edi_com_ute_1
    )

    fuel_oil = read_entradas_energia_combustibles_fosiles_fuel_oil(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_edi_com_ute_1=medida_edi_com_ute_1
    )

    glp = read_entradas_energia_combustibles_fosiles_glp(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_edi_com_ute_1=medida_edi_com_ute_1,
        medida_edi_res_irco_1=medida_edi_res_irco_1,
        medida_edi_res_irco_2=medida_edi_res_irco_2,
        medida_edi_res_irco_3=medida_edi_res_irco_3,
        medida_edi_res_rural_1=medida_edi_res_rural_1
    )

    queroseno = read_entradas_energia_combustibles_fosiles_queroseno(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_edi_com_ute_1=medida_edi_com_ute_1
    )

    sum_combustibles = pd.concat(
        [
            get_total(gasolina),
            get_total(diesel), 
            get_total(fuel_oil), 
            get_total(glp), 
            get_total(queroseno)
        ]
        ).sum().to_dict()

    crudo = get_item(db=db, 
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        filter={"tipo": "crudo", 'medida_1': medida_ener_1},
        topic='combustibles_fosiles_producidos')
    
    # Resta de suma de combustibles - crudo, aplicando 0 para valores negativos
    df = pd.concat([pd.json_normalize(sum_combustibles), pd.json_normalize(crudo)[YEARS]])
    df = df.iloc[0] - df.iloc[1]
    result_crudo = df.apply(not_negative).to_dict()


    ####################################################################################
    #######                              gas                                     #######
    ####################################################################################

    gas_natural = read_entradas_energia_combustibles_fosiles_gas_natural(db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_trans_car_1=medida_trans_car_1,
        medida_trans_car_2=medida_trans_car_2,
        medida_trans_pas_1=medida_trans_pas_1,
        medida_trans_pas_2=medida_trans_pas_2,
        medida_edi_com_ute_1=medida_edi_com_ute_1,
        medida_edi_res_irco_1=medida_edi_res_irco_1,
        medida_edi_res_irco_2=medida_edi_res_irco_2,
        medida_edi_res_irco_3=medida_edi_res_irco_3
    )

    gas = get_item(db=db, 
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        filter={"tipo": "gas_natural", 'medida_1': medida_ener_1},
        topic='combustibles_fosiles_producidos')
    
    # Resta de suma de gas_natural - gas, aplicando 0 para valores negativos
    df = pd.concat([get_total(gas_natural), pd.json_normalize(gas)[YEARS]])
    df = df.iloc[0] - df.iloc[1]
    result_gas = df.apply(not_negative).to_dict()


    ####################################################################################
    #######                             carbon                                   #######
    ####################################################################################

    carbon_mineral = read_entradas_energia_combustibles_fosiles_carbon(db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4
    )

    carbon = get_item(db=db, 
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        filter={"tipo": "carbon", 'medida_1': medida_ener_1},
        topic='combustibles_fosiles_producidos')
    
    # Resta de suma de carbon_mineral - carbon, aplicando 0 para valores negativos
    df = pd.concat([get_total(carbon_mineral), pd.json_normalize(carbon)[YEARS]])
    df = df.iloc[0] - df.iloc[1]
    result_carbon = df.apply(not_negative).to_dict()

    ####################################################################################

    result_crudo['topic']  = 'requerimientos_energeticos'
    result_crudo['tipo']   = 'crudo'
    result_crudo['unidad'] = 'TWh'

    result_gas['topic']  = 'requerimientos_energeticos'
    result_gas['tipo']   = 'gas'
    result_gas['unidad'] = 'TWh'

    result_carbon['topic']  = 'requerimientos_energeticos'
    result_carbon['tipo']   = 'carbon'
    result_carbon['unidad'] = 'TWh'

    result = {
        'requerimientos_energeticos' : [result_crudo, result_gas, result_carbon]
    }


    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(result)}')

    return jsonable_encoder(result)


@router.get('/excedentes_energeticos')
def read_entradas_excedentes_energeticos(
    medida_ener_1: schemas.Trayectoria=1,
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ####################################################################################
    #######                              crudo                                   #######
    ####################################################################################

    gasolina = read_entradas_energia_combustibles_fosiles_gasolina(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_trans_car_1=medida_trans_car_1,
        medida_trans_car_2=medida_trans_car_2,
        medida_trans_pas_1=medida_trans_pas_1,
        medida_trans_pas_2=medida_trans_pas_2
        ) 

    diesel = read_entradas_energia_combustibles_fosiles_diesel(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_trans_car_1=medida_trans_car_1,
        medida_trans_car_2=medida_trans_car_2,
        medida_trans_pas_1=medida_trans_pas_1,
        medida_trans_pas_2=medida_trans_pas_2,
        medida_trans_nav_1=medida_trans_nav_1,
        medida_edi_com_ute_1=medida_edi_com_ute_1
    )

    fuel_oil = read_entradas_energia_combustibles_fosiles_fuel_oil(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_edi_com_ute_1=medida_edi_com_ute_1
    )

    glp = read_entradas_energia_combustibles_fosiles_glp(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_edi_com_ute_1=medida_edi_com_ute_1,
        medida_edi_res_irco_1=medida_edi_res_irco_1,
        medida_edi_res_irco_2=medida_edi_res_irco_2,
        medida_edi_res_irco_3=medida_edi_res_irco_3,
        medida_edi_res_rural_1=medida_edi_res_rural_1
    )

    queroseno = read_entradas_energia_combustibles_fosiles_queroseno(
        db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_edi_com_ute_1=medida_edi_com_ute_1
    )

    sum_combustibles = pd.concat(
        [
            get_total(gasolina),
            get_total(diesel), 
            get_total(fuel_oil), 
            get_total(glp), 
            get_total(queroseno)
        ]
        ).sum().to_dict()

    crudo = get_item(db=db, 
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        filter={"tipo": "crudo", 'medida_1': medida_ener_1},
        topic='combustibles_fosiles_producidos')
    
    # Resta de suma de combustibles - crudo, aplicando 0 para valores positivos
    df = pd.concat([pd.json_normalize(sum_combustibles), pd.json_normalize(crudo)[YEARS]])
    df = df.iloc[0] - df.iloc[1]

    result_crudo = df.apply(abs_negative).to_dict()


    ####################################################################################
    #######                              gas                                     #######
    ####################################################################################

    gas_natural = read_entradas_energia_combustibles_fosiles_gas_natural(db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4,
        medida_trans_car_1=medida_trans_car_1,
        medida_trans_car_2=medida_trans_car_2,
        medida_trans_pas_1=medida_trans_pas_1,
        medida_trans_pas_2=medida_trans_pas_2,
        medida_edi_com_ute_1=medida_edi_com_ute_1,
        medida_edi_res_irco_1=medida_edi_res_irco_1,
        medida_edi_res_irco_2=medida_edi_res_irco_2,
        medida_edi_res_irco_3=medida_edi_res_irco_3
    )

    gas = get_item(db=db, 
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        filter={"tipo": "gas_natural", 'medida_1': medida_ener_1},
        topic='combustibles_fosiles_producidos')
    
    # Resta de suma de gas_natural - gas, aplicando 0 para valores positivos
    df = pd.concat([get_total(gas_natural), pd.json_normalize(gas)[YEARS]])
    df = df.iloc[0] - df.iloc[1]
    result_gas = df.apply(abs_negative).to_dict()


    ####################################################################################
    #######                             carbon                                   #######
    ####################################################################################

    carbon_mineral = read_entradas_energia_combustibles_fosiles_carbon(db=db,
        medida_ind_1=medida_ind_1,
        medida_ind_4=medida_ind_4
    )

    carbon = get_item(db=db, 
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        filter={"tipo": "carbon", 'medida_1': medida_ener_1},
        topic='combustibles_fosiles_producidos')
    
    # Resta de suma de carbon_mineral - carbon, aplicando 0 para valores positivos
    df = pd.concat([get_total(carbon_mineral), pd.json_normalize(carbon)[YEARS]])
    df = df.iloc[0] - df.iloc[1]
    result_carbon = df.apply(abs_negative).to_dict()

    ####################################################################################

    result_crudo['topic']  = 'excedentes_energeticos'
    result_crudo['tipo']   = 'crudo'
    result_crudo['unidad'] = 'TWh'

    result_gas['topic']  = 'excedentes_energeticos'
    result_gas['tipo']   = 'gas'
    result_gas['unidad'] = 'TWh'

    result_carbon['topic']  = 'excedentes_energeticos'
    result_carbon['tipo']   = 'carbon'
    result_carbon['unidad'] = 'TWh'

    result = {
        'excedentes_energeticos' : [result_crudo, result_gas, result_carbon]
    }


    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(result)}')

    return jsonable_encoder(result)
