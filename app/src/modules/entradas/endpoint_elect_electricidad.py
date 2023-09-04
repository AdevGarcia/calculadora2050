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

from .util.util import db_to_df, get_item, set_zeros, set_suma_total, not_negative

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######                     Energía inyectada a red                          #######
####################################################################################

@router.get('/energia_inyectada_a_red')
def read_entradas_energia_inyectada_a_red(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    medida_res_irco_1: schemas.Trayectoria=1,
    medida_res_irco_2: schemas.Trayectoria=1,
    medida_res_irco_3: schemas.Trayectoria=1,
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    medida_gana_1: schemas.Trayectoria=1,
    medida_gana_2: schemas.Trayectoria=1,
    medida_gana_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   industria   ##############
    filter={"tipo": "total_inyectado_a_red", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="entradas",
        bloque="energia_inyectada_a_red",
        tipo='industria',
        unidad="TWh")
        
    ##########   residuos   ##############
    ### residuos solidos
    filter={"tipo": "total_consumido", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    filter={"tipo": "total_producido", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    df = pd.concat([df1, df2])
    balance_total_residuos_solidos = abs(df.iloc[0] - df.iloc[1])

    ### aguas residuales
    filter={"tipo": "total_consumo", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    filter={"tipo": "total_generacion", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    df = pd.concat([df1, df2])
    balance_total_aguas_residuales = df.iloc[0] - df.iloc[1]

    suma = balance_total_residuos_solidos + balance_total_aguas_residuales

    residuos = suma.to_dict()
    residuos["topic"]    = "entradas"
    residuos["bloque"]   = "energia_inyectada_a_red"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "TWh"

    ##########   edificaciones   ##############    
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_res_irco_1, 'medida_2': medida_res_irco_2, 'medida_3': medida_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    filter={"tipo": "solar_fotovoltaica", 'medida_1': medida_res_irco_1, 'medida_2': medida_res_irco_2, 'medida_3': medida_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    df = pd.concat([df1, df2])
    resta = df.iloc[0] - df.iloc[1]

    edificaciones = resta.apply(not_negative).to_dict()
    edificaciones["topic"]    = "entradas"
    edificaciones["bloque"]   = "energia_inyectada_a_red"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"

    ##########   agricultura   ##############
    filter={'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='cultivos',
        model=models.AGRO_SALIDAS_cultivos,
        skip=skip, limit=limit,
        **filter)
    
    agricultura = db_to_df(rd=rd).sum().to_dict()
    agricultura["topic"]    = "entradas"
    agricultura["bloque"]   = "energia_inyectada_a_red"
    agricultura["tipo"]     = "agricultura"
    agricultura["unidad"]   = "TWh"
    
    ##########   ganaderia   ##############
    filter={"tipo": "total", 'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    ganaderia = get_item(db=db, 
        model=models.GANA_SALIDAS,
        topic='produccion_de_estiercol_para_bioenergia',
        filter=filter,
        topic_item='entradas',
        bloque="energia_inyectada_a_red",
        tipo='ganaderia',
        unidad='TWh')
    
    ##############################
    combustibles_fosiles = set_zeros(topic_item='entradas', bloque='energia_inyectada_a_red', tipo='combustibles_fosiles', unidad='TWh')
    transporte           = set_zeros(topic_item='entradas', bloque='energia_inyectada_a_red', tipo='transporte',           unidad='TWh')
    bosques              = set_zeros(topic_item='entradas', bloque='energia_inyectada_a_red', tipo='bosques',              unidad='TWh')

    total = set_suma_total(items=[combustibles_fosiles, industria, residuos, edificaciones, transporte, agricultura, ganaderia, bosques],
                   topic="entradas", 
                   bloque="energia_inyectada_a_red", tipo="total", unidad="TWh")

    resultado = {"entradas": [
            combustibles_fosiles,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            bosques,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                              Demanda                                 #######
####################################################################################

@router.get('/demanda')
def read_entradas_demanda(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    medida_res_acond_1: schemas.Trayectoria=1,
    medida_res_irco_1: schemas.Trayectoria=1,
    medida_res_irco_2: schemas.Trayectoria=1,
    medida_res_irco_3: schemas.Trayectoria=1,
    medida_res_rural_1: schemas.Trayectoria=1,
    medida_com_acond_1: schemas.Trayectoria=1,
    medida_com_ute_1: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   industria   ##############
    filter={"tipo": "total_electricidad", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    
    industria = get_item(db=db, 
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        topic='balance_total_de_la_energia_requerida',
        filter=filter,
        topic_item="entradas",
        bloque="demanda",
        tipo='industria',
        unidad="TWh")
        
    ##########   residuos   ##############
    ### residuos solidos
    filter={"tipo": "total_consumido", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    filter={"tipo": "total_producido", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    df = pd.concat([df1, df2])
    balance_total_residuos_solidos = df.iloc[0] - df.iloc[1]

    balance_total_residuos_solidos = balance_total_residuos_solidos.apply(not_negative)

    ### aguas residuales
    filter={"tipo": "total_consumo", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    filter={"tipo": "total_generacion", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    df = pd.concat([df1, df2])
    balance_total_aguas_residuales = df.iloc[0] - df.iloc[1]

    balance_total_aguas_residuales = balance_total_aguas_residuales.apply(not_negative)

    suma = balance_total_residuos_solidos + balance_total_aguas_residuales

    residuos = suma.to_dict()
    residuos["topic"]    = "entradas"
    residuos["bloque"]   = "demanda"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "TWh"

    ##########   edificaciones   ##############    
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_res_acond_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ACOND_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    ###
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_res_irco_1, 'medida_2': medida_res_irco_2, 'medida_3': medida_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    ###
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    df3 = db_to_df(rd=rd)

    ###
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_com_acond_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_ACOND_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    df4 = db_to_df(rd=rd)

    ###
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)

    df5 = db_to_df(rd=rd)

    edificaciones = pd.concat([df1, df2, df3, df4, df5]).sum().to_dict()
    edificaciones["topic"]    = "entradas"
    edificaciones["bloque"]   = "demanda"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"

    ##########   transporte   ##############
    filter={'tipo': 'electrico', 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    filter={'tipo': 'electricidad', 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)
    
    transporte = pd.concat([df1, df2]).sum().to_dict()
    transporte["topic"]    = "entradas"
    transporte["bloque"]   = "demanda"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "TWh"
    
    ##############################
    combustibles_fosiles = set_zeros(topic_item='entradas', bloque='demanda', tipo='combustibles_fosiles', unidad='TWh')
    agricultura          = set_zeros(topic_item='entradas', bloque='demanda', tipo='agricultura',          unidad='TWh')
    ganaderia            = set_zeros(topic_item='entradas', bloque='demanda', tipo='ganaderia',            unidad='TWh')
    bosques              = set_zeros(topic_item='entradas', bloque='demanda', tipo='bosques',              unidad='TWh')

    total = set_suma_total(items=[combustibles_fosiles, industria, residuos, edificaciones, transporte, agricultura, ganaderia, bosques],
                   topic="entradas", bloque="demanda", tipo="total", unidad="TWh")

    resultado = {"entradas": [
            combustibles_fosiles,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            bosques,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######            Emisiones derivadas de la autogeneración                  #######
####################################################################################

@router.get('/emisiones_derivadas_de_la_autogeneracion')
def read_entradas_emisiones_derivadas_de_la_autogeneracion(
    medida_res_sol_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""
    
    ##########   residuos   ##############
    ### residuos solidos
    filter={"grupo": "aprovechamiento_energetico_del_biogas", "tipo": "co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_energia',
        model=models.RES_SOL_emisiones,
        skip=skip, limit=limit,
        **filter)

    df1 = db_to_df(rd=rd)

    filter={"grupo": "incineracion", "tipo": "co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_energia',
        model=models.RES_SOL_emisiones,
        skip=skip, limit=limit,
        **filter)

    df2 = db_to_df(rd=rd)

    residuos = pd.concat([df1, df2]).sum().to_dict()
    residuos["topic"]    = "entradas"
    residuos["bloque"]   = "emisiones_derivadas_de_la_autogeneracion"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "TWh"

    ##############################
    combustibles_fosiles = set_zeros(topic_item='entradas', bloque='emisiones_derivadas_de_la_autogeneracion', tipo='combustibles_fosiles', unidad='TWh')
    industria            = set_zeros(topic_item='entradas', bloque='emisiones_derivadas_de_la_autogeneracion', tipo='industria',            unidad='TWh')
    edificaciones        = set_zeros(topic_item='entradas', bloque='emisiones_derivadas_de_la_autogeneracion', tipo='edificaciones',        unidad='TWh')
    transporte           = set_zeros(topic_item='entradas', bloque='emisiones_derivadas_de_la_autogeneracion', tipo='transporte',           unidad='TWh')
    agricultura          = set_zeros(topic_item='entradas', bloque='emisiones_derivadas_de_la_autogeneracion', tipo='agricultura',          unidad='TWh')
    ganaderia            = set_zeros(topic_item='entradas', bloque='emisiones_derivadas_de_la_autogeneracion', tipo='ganaderia',            unidad='TWh')
    bosques              = set_zeros(topic_item='entradas', bloque='emisiones_derivadas_de_la_autogeneracion', tipo='bosques',              unidad='TWh')

    total = set_suma_total(items=[combustibles_fosiles, industria, residuos, edificaciones, transporte, agricultura, ganaderia, bosques],
                   topic="entradas", 
                   bloque="emisiones_derivadas_de_la_autogeneracion", tipo="total", unidad="TWh")

    resultado = {"entradas": [
            combustibles_fosiles,
            industria,
            residuos,
            edificaciones,
            transporte,
            agricultura,
            ganaderia,
            bosques,
            total
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
