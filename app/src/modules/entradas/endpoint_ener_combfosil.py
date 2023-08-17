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

from .util.util import db_to_df, get_item, set_item, set_zeros, set_suma_total

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######                              gasolina                                #######
####################################################################################

@router.get('/energia_combustibles_fosiles/gasolina')
def read_entradas_energia_combustibles_fosiles_gasolina(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   industria   ##############
    filter={"tipo": "gasolina", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="gasolina", 
        tipo="industria", 
        unidad="TWh")

    ##########   transporte   ##############
    ###
    filter={"tipo": "gasolina", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)

    df1 = db_to_df(rd=rd)

    ###
    filter={"tipo": "gasolina", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)

    df2 = db_to_df(rd=rd)

    transporte = pd.concat([df1, df2]).sum().to_dict()
    transporte["topic"]    = "consumo_de_combustibles_fosiles"
    transporte["bloque"]   = "gasolina"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "TWh"

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gasolina', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gasolina', tipo='residuos',      unidad='TWh')
    edificaciones = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gasolina', tipo='edificaciones', unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gasolina', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gasolina', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="gasolina", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              diesel                                  #######
####################################################################################

@router.get('/energia_combustibles_fosiles/diesel')
def read_entradas_energia_combustibles_fosiles_diesel(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

     # industria
    filter={"tipo": "diesel", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
     
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="diesel", 
        tipo="industria", 
        unidad="TWh")
    
    # edificaciones
    filter={"tipo": "diesel", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)

    edificaciones = set_item(rd=rd, 
                       topic="consumo_de_combustibles_fosiles", 
                       bloque="diesel", 
                       tipo="edificaciones", 
                       unidad="TWh")
    
    # transporte
    ###
    filter={"tipo": "diesel", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)

    df1 = db_to_df(rd=rd)

    ###
    filter={"tipo": "diesel", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)

    df2 = db_to_df(rd=rd)

    ###
    filter={"tipo": "diesel", 'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_NAV_SALIDAS_energia_requerida,
        **filter)

    df3 = db_to_df(rd=rd)

    transporte = pd.concat([df1, df2, df3]).sum().to_dict()
    transporte["topic"]    = "consumo_de_combustibles_fosiles"
    transporte["bloque"]   = "diesel"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "TWh"

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='diesel', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='diesel', tipo='residuos',      unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='diesel', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='diesel', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="diesel", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              fuel_oil                                #######
####################################################################################

@router.get('/energia_combustibles_fosiles/fuel_oil')
def read_entradas_energia_combustibles_fosiles_fuel_oil(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    # industria
    filter={"tipo": "fuel_oil", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="fuel_oil", 
        tipo="industria", 
        unidad="TWh")
    
    # edificaciones
    filter={"tipo": "fuel_oil", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)

    edificaciones = set_item(rd=rd, 
                       topic="consumo_de_combustibles_fosiles", 
                       bloque="fuel_oil", 
                       tipo="edificaciones", 
                       unidad="TWh")

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='fuel_oil', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='fuel_oil', tipo='residuos',      unidad='TWh')
    transporte    = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='fuel_oil', tipo='transporte',    unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='fuel_oil', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='fuel_oil', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="fuel_oil", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              gas_natural                             #######
####################################################################################

@router.get('/energia_combustibles_fosiles/gas_natural')
def read_entradas_energia_combustibles_fosiles_gas_natural(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    # industria
    filter={"tipo": "gas_natural", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="gas_natural", 
        tipo="industria", 
        unidad="TWh")
    
    # edificaciones
    ###
    filter={"tipo": "gas_natural", "bloque": "demanda", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        **filter)

    df1 = db_to_df(rd=rd)

    ###
    filter={"tipo": "gas_natural", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)

    df2 = db_to_df(rd=rd)

    edificaciones = pd.concat([df1, df2]).sum().to_dict()
    edificaciones["topic"]    = "consumo_de_combustibles_fosiles"
    edificaciones["bloque"]   = "gas_natural"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"

    # transporte
    ###
    filter={"tipo": "gas_gnc", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)

    df1 = db_to_df(rd=rd)

    ###
    filter={"tipo": "gas_gnl", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)

    df2 = db_to_df(rd=rd)

    ###
    filter={"tipo": "gas_natural", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)

    df3 = db_to_df(rd=rd)

    transporte = pd.concat([df1, df2, df3]).sum().to_dict()
    transporte["topic"]    = "consumo_de_combustibles_fosiles"
    transporte["bloque"]   = "gas_natural"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "TWh"

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gas_natural', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gas_natural', tipo='residuos',      unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gas_natural', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='gas_natural', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="gas_natural", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              glp                                     #######
####################################################################################

@router.get('/energia_combustibles_fosiles/glp')
def read_entradas_energia_combustibles_fosiles_glp(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
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

    # industria
    filter={"tipo": "glp", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="glp", 
        tipo="industria", 
        unidad="TWh")
    
    # edificaciones
    ###
    filter={"tipo": "glp", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)

    df1 = db_to_df(rd=rd)

    ###
    filter={"tipo": "hidrocarburos_gaseosos_glp", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        **filter)

    df2 = db_to_df(rd=rd)

    ###
    filter={"tipo": "glp", "bloque": "demanda", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        **filter)

    df3 = db_to_df(rd=rd)

    edificaciones = pd.concat([df1, df2, df3]).sum().to_dict()
    edificaciones["topic"]    = "consumo_de_combustibles_fosiles"
    edificaciones["bloque"]   = "glp"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='glp', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='glp', tipo='residuos',      unidad='TWh')
    transporte    = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='glp', tipo='transporte',    unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='glp', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='glp', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="glp", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              carbon                                  #######
####################################################################################

@router.get('/energia_combustibles_fosiles/carbon')
def read_entradas_energia_combustibles_fosiles_carbon(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    # industria
    filter={"tipo": "carbon_mineral", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="carbon", 
        tipo="industria", 
        unidad="TWh")

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='carbon', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='carbon', tipo='residuos',      unidad='TWh')
    edificaciones = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='carbon', tipo='edificaciones', unidad='TWh')
    transporte    = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='carbon', tipo='transporte',    unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='carbon', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='carbon', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="carbon", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              queroseno                               #######
####################################################################################

@router.get('/energia_combustibles_fosiles/queroseno')
def read_entradas_energia_combustibles_fosiles_queroseno(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    # industria
    filter={"tipo": "queroseno", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="queroseno", 
        tipo="industria", 
        unidad="TWh")
    
    # edificaciones
    filter={"tipo": "queroseno", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)

    edificaciones = set_item(rd=rd, 
                       topic="consumo_de_combustibles_fosiles", 
                       bloque="queroseno", 
                       tipo="edificaciones", 
                       unidad="TWh")

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='queroseno', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='queroseno', tipo='residuos',      unidad='TWh')
    transporte    = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='queroseno', tipo='transporte',    unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='queroseno', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='queroseno', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="queroseno", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              coque                                   #######
####################################################################################

@router.get('/energia_combustibles_fosiles/coque')
def read_entradas_energia_combustibles_fosiles_coque(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

     # industria
    filter={"tipo": "coque", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="consumo_de_combustibles_fosiles", 
        bloque="coque", 
        tipo="industria", 
        unidad="TWh")

    electricidad  = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='coque', tipo='electricidad',  unidad='TWh')
    residuos      = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='coque', tipo='residuos',      unidad='TWh')
    edificaciones = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='coque', tipo='edificaciones', unidad='TWh')
    transporte    = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='coque', tipo='transporte',    unidad='TWh')
    agricultura   = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='coque', tipo='agricultura',   unidad='TWh')
    ganaderia     = set_zeros(topic_item='consumo_de_combustibles_fosiles', bloque='coque', tipo='ganaderia',     unidad='TWh')

    total = set_suma_total(items=[electricidad, industria, residuos, edificaciones, transporte, agricultura, ganaderia],
                   topic="consumo_de_combustibles_fosiles", 
                   bloque="coque", tipo="total", unidad="TWh")

    resultado = {"entradas_consumo_de_combustibles_fosiles": [
            electricidad,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
