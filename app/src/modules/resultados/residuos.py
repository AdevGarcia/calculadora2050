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

from .util.util import db_to_df

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######     Evolución de las emisiones del sector Residuos                   #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_residuos')
def resultados_evolucion_de_las_emisiones_del_sector_residuos(
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  1 relleno_sanitario_controlados_sin_captacion  RES_SOL ############## Mt_CO2_e
    filter={"bloque": "relleno_sanitario_controlados", "grupo": "sin_captacion", "tipo": "co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_residuos',
        model=models.RES_SOL_emisiones,
        **filter)
        
    relleno_sanitario_controlados_sin_captacion = db_to_df(rd=rd).to_dict(orient='records')[0]
    relleno_sanitario_controlados_sin_captacion["topic"]    = "resultados"
    relleno_sanitario_controlados_sin_captacion["bloque"]   = "residuos"
    relleno_sanitario_controlados_sin_captacion["tipo"]     = "relleno_sanitario_controlados_sin_captacion"
    relleno_sanitario_controlados_sin_captacion["unidad"]   = "Mt_CO2_e"
    
    ##########  2 relleno_sanitario_controlados_quema_antorcha  RES_SOL ############## Mt_CO2_e
    filter={"bloque": "relleno_sanitario_controlados", "grupo": "quema_en_antorcha", "tipo": "co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_residuos',
        model=models.RES_SOL_emisiones,
        **filter)
        
    relleno_sanitario_controlados_quema_antorcha = db_to_df(rd=rd).sum().to_dict()
    relleno_sanitario_controlados_quema_antorcha["topic"]    = "resultados"
    relleno_sanitario_controlados_quema_antorcha["bloque"]   = "residuos"
    relleno_sanitario_controlados_quema_antorcha["tipo"]     = "relleno_sanitario_controlados_quema_antorcha"
    relleno_sanitario_controlados_quema_antorcha["unidad"]   = "Mt_CO2_e"

    ########## 3  celda_de_contingencia  RES_SOL ############## Mt_CO2_e
    filter={"bloque": "relleno_sanitario_controlados", "grupo": "celda_de_contingencia", "tipo": "co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_residuos',
        model=models.RES_SOL_emisiones,
        **filter)
        
    celda_de_contingencia = db_to_df(rd=rd).sum().to_dict()
    celda_de_contingencia["topic"]    = "resultados"
    celda_de_contingencia["bloque"]   = "residuos"
    celda_de_contingencia["tipo"]     = "celda_de_contingencia"
    celda_de_contingencia["unidad"]   = "Mt_CO2_e"

    ##########  4 tratamiento_mecanico_biologico_compostaje RES_SOL  ############## Mt_CO2_e
    filter={"bloque": "planta_de_tratamiento", "grupo": "tratamiento_mecanico_biologico_tmbcompostaje", "tipo": "co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_residuos',
        model=models.RES_SOL_emisiones,
        **filter)
        
    tratamiento_mecanico_biologico_compostaje = db_to_df(rd=rd).to_dict(orient='records')[0]
    tratamiento_mecanico_biologico_compostaje["topic"]    = "resultados"
    tratamiento_mecanico_biologico_compostaje["bloque"]   = "residuos"
    tratamiento_mecanico_biologico_compostaje["tipo"]     = "tratamiento_mecanico_biologico_compostaje"
    tratamiento_mecanico_biologico_compostaje["unidad"]   = "Mt_CO2_e"

    ##########  5 aguas_residuales_domesticas RES_AGU  ############## Mt_CO2_e
    filter={"bloque": "aguas_residuales_domesticas", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_aguas_residuales',
        model=models.RES_AGU_emisiones,
        **filter)
    
    df = db_to_df(rd=rd)

    PCG_CO2 = 1
    PCG_CH4 = 28
    PCG_N2O = 265

    df.iloc[0] = df.iloc[0] * PCG_CO2
    df.iloc[1] = df.iloc[1] * PCG_CH4
    df.iloc[2] = df.iloc[2] * PCG_N2O
        
    aguas_residuales_domesticas = df.sum().to_dict()
    aguas_residuales_domesticas["topic"]    = "resultados"
    aguas_residuales_domesticas["bloque"]   = "residuos"
    aguas_residuales_domesticas["tipo"]     = "aguas_residuales_domesticas"
    aguas_residuales_domesticas["unidad"]   = "Mt_CO2_e"


    ##########  6 aguas_residuales_industriales RES_AGU  ############## Mt_CO2_e
    filter={"bloque": "aguas_residuales_industriales", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_aguas_residuales',
        model=models.RES_AGU_emisiones,
        **filter)
    
    df = db_to_df(rd=rd)

    PCG_CO2 = 1
    PCG_CH4 = 28
    PCG_N2O = 265

    df.iloc[0] = df.iloc[0] * PCG_CO2
    df.iloc[1] = df.iloc[1] * PCG_CH4
    df.iloc[2] = df.iloc[2] * PCG_N2O
        
    aguas_residuales_industriales = df.sum().to_dict()
    aguas_residuales_industriales["topic"]    = "resultados"
    aguas_residuales_industriales["bloque"]   = "residuoes"
    aguas_residuales_industriales["tipo"]     = "aguas_residuales_industriales"
    aguas_residuales_industriales["unidad"]   = "Mt_CO2_e"
    

    resultado = {"resultados": [
        relleno_sanitario_controlados_sin_captacion, 
        relleno_sanitario_controlados_quema_antorcha, 
        celda_de_contingencia, 
        tratamiento_mecanico_biologico_compostaje,
        aguas_residuales_domesticas,
        aguas_residuales_industriales
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######                               Residuos                               #######
####################################################################################
@router.get('/residuos')
def resultados_residuos(
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   reduccion_y_mejora_de_la_gestion_de_residuos_solidos RES_SOL  ############## TWh
    # 331
    filter={"bloque": "energia_consumida", "tipo": "celda_de_contingencia", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        **filter)
    df1 = db_to_df(rd=rd)

    # 334
    filter={"bloque": "energia_consumida", "tipo": "combustibles_derivados_de_residuos_cdm", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        **filter)
    df2 = db_to_df(rd=rd)

    # 335
    filter={"bloque": "energia_consumida", "tipo": "incineracion", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        **filter)
    df3 = db_to_df(rd=rd)

    # 336
    filter={"bloque": "energia_consumida", "tipo": "reciclado", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        **filter)
    df4 = db_to_df(rd=rd)

    # 333
    filter={"bloque": "energia_consumida", "tipo": "tratamiento_mecanico_biologico_tmbcompostaje", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        **filter)
    df5 = db_to_df(rd=rd)

    # 330
    filter={"bloque": "energia_consumida", "tipo": "relleno_sanitario_controlados", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        **filter)
    df6 = db_to_df(rd=rd)


    reduccion_y_mejora_de_la_gestion_de_residuos_solidos = pd.concat([df1, df2, df3, df4, df5, df6]).sum().to_dict()
    reduccion_y_mejora_de_la_gestion_de_residuos_solidos["topic"]    = "resultados"
    reduccion_y_mejora_de_la_gestion_de_residuos_solidos["bloque"]   = "residuos"
    reduccion_y_mejora_de_la_gestion_de_residuos_solidos["tipo"]     = "reduccion_y_mejora_de_la_gestion_de_residuos_solidos"
    reduccion_y_mejora_de_la_gestion_de_residuos_solidos["unidad"]   = "TWh"

    
    ##########   aprovechamiento_del_biogas_de_las_aguas_residuales  RES_AGU ############## TWh
    filter={"tipo": "total_consumo", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_consumida,
        **filter)

    aprovechamiento_del_biogas_de_las_aguas_residuales = db_to_df(rd=rd).to_dict(orient='records')[0]
    aprovechamiento_del_biogas_de_las_aguas_residuales["topic"]    = "resultados"
    aprovechamiento_del_biogas_de_las_aguas_residuales["bloque"]   = "residuos"
    aprovechamiento_del_biogas_de_las_aguas_residuales["tipo"]     = "aprovechamiento_del_biogas_de_las_aguas_residuales"
    aprovechamiento_del_biogas_de_las_aguas_residuales["unidad"]   = "TWh"
    
    
    resultado = {"resultados": [
        reduccion_y_mejora_de_la_gestion_de_residuos_solidos, 
        aprovechamiento_del_biogas_de_las_aguas_residuales
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de la generacion energetica del sector residuos     #######
####################################################################################
@router.get('/evolucion_generacion_energetica_sector_residuos')
def resultados_evolucion_generacion_energetica_sector_residuos(
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   reduccion_y_mejora_de_gestion_de_residuos_solidos RES_SOL  ############## TWh
    filter={"bloque": "energia_producida", "tipo": "total_producido", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_producida,
        **filter)

    reduccion_y_mejora_de_gestion_de_residuos_solidos = db_to_df(rd=rd).to_dict(orient='records')[0]
    reduccion_y_mejora_de_gestion_de_residuos_solidos["topic"]    = "resultados"
    reduccion_y_mejora_de_gestion_de_residuos_solidos["bloque"]   = "residuos"
    reduccion_y_mejora_de_gestion_de_residuos_solidos["tipo"]     = "reduccion_y_mejora_de_gestion_de_residuos_solidos"
    reduccion_y_mejora_de_gestion_de_residuos_solidos["unidad"]   = "TWh"
    
    
    ##########   aprovechamiento_biogás_de_aguas_residuales RES_AGU  ############## TWh
    filter={"tipo": "total_generacion", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_producida,
        **filter)
    
    aprovechamiento_biogás_de_aguas_residuales = db_to_df(rd=rd).to_dict(orient='records')[0]
    aprovechamiento_biogás_de_aguas_residuales["topic"]    = "resultados"
    aprovechamiento_biogás_de_aguas_residuales["bloque"]   = "residuos"
    aprovechamiento_biogás_de_aguas_residuales["tipo"]     = "aprovechamiento_biogás_de_aguas_residuales"
    aprovechamiento_biogás_de_aguas_residuales["unidad"]   = "TWh"
    

    resultado = {"resultados": [
        reduccion_y_mejora_de_gestion_de_residuos_solidos, 
        aprovechamiento_biogás_de_aguas_residuales
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
