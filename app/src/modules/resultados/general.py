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
#######     Evolución de las emisiones a nivel nacional                      #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_nivel_nacional')
def resultados_evolucion_de_las_emisiones_nivel_nacional(
    medida_ener_1: schemas.Trayectoria=1,
    medida_elect_1: schemas.Trayectoria=1,
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    medida_edi_res_aer_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    medida_edi_com_aec_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_avi_1: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    medida_gana_1: schemas.Trayectoria=1,
    medida_gana_2: schemas.Trayectoria=1,
    medida_gana_3: schemas.Trayectoria=1,
    medida_bosq_1: schemas.Trayectoria=1,
    medida_bosq_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## Mt_CO2_e
    filter={"bloque": "total", "tipo": "total_mt_co2_e", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        skip=skip, limit=limit,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "Mt_CO2_e"
    
    ##########  electricidad ############## Mt_CO2_e
    filter={"bloque": "emisiones_totales_electricidad", "tipo": "emisiones_totales_electricidad", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_ener_renov_no_convencionales,
        skip=skip, limit=limit,
        **filter)
        
    electricidad = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "Mt_CO2_e"


    ##########  industria ############## Mt_CO2_e
    filter={"tipo": "total_emisiones_industria", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='total_emisiones_industria',
        model=models.INDU_emisiones_sao,
        skip=skip, limit=limit,
        **filter)
    
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "Mt_CO2_e"


    ##########  residuos ############## Mt_CO2_e
    # res_sol
    filter={"bloque": "total", "grupo": "total", "tipo": "total_co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_residuos',
        model=models.RES_SOL_emisiones,
        skip=skip, limit=limit,
        **filter)
        
    res_sol = db_to_df(rd=rd)

    # res_agu
    filter={"bloque": "total_emisiones_gei_aguas_residuales", "tipo": "total_emisiones_gei_aguas_residuales", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_aguas_residuales',
        model=models.RES_AGU_emisiones,
        skip=skip, limit=limit,
        **filter)
    
    res_agu = db_to_df(rd=rd)

    residuos = pd.concat([res_sol, res_agu]).sum().to_dict()
    residuos["topic"]    = "resultados"
    residuos["bloque"]   = "general"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "Mt_CO2_e"


    ##########  edificaciones ############## Mt_CO2_e
    # edi_res_urb_aer
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_res_aer_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_RES_ACOND_EMISIONES,
        skip=skip, limit=limit,
        **filter)
        
    edi_res_urb_aer = db_to_df(rd=rd)

    # edi_res_urb_irco
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_RES_ILU_REF_COC_OTR_EMISIONES,
        skip=skip, limit=limit,
        **filter)
    
    edi_res_urb_irco = db_to_df(rd=rd)

    # edi_res_urb_rural
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_RES_RURAL_EMISIONES,
        skip=skip, limit=limit,
        **filter)
    
    edi_res_urb_rural = db_to_df(rd=rd)

    # edi_com_aec
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_com_aec_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_COM_ACOND_EMISIONES,
        skip=skip, limit=limit,
        **filter)
    
    edi_com_aec = db_to_df(rd=rd)

    # edi_com_ute
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_COM_USOS_TERM_EQUIP_EMISIONES,
        skip=skip, limit=limit,
        **filter)
    
    edi_com_ute = db_to_df(rd=rd)

    edificaciones = pd.concat([
        edi_res_urb_aer, 
        edi_res_urb_irco, 
        edi_res_urb_rural, 
        edi_com_aec, 
        edi_com_ute
        ]).sum().to_dict()
    
    edificaciones["topic"]    = "resultados"
    edificaciones["bloque"]   = "general"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "Mt_CO2_e"


    ##########  transporte ############## Mt_CO2_e
    # trans_pas
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.TRANS_PAS_emisiones_de_gases_efecto_invernadero,
        skip=skip, limit=limit,
        **filter)
        
    trans_pas = db_to_df(rd=rd)

    # trans_car
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.TRANS_CAR_emisiones_de_gases_efecto_invernadero,
        skip=skip, limit=limit,
        **filter)
    
    trans_car = db_to_df(rd=rd)

    # trans_avi
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_avi_1}
    rd = downloader(db=db, topic='aviacion_y_navegacion_internacional',
        model=models.TRANS_AVI_emisiones_aviacion_y_navegacion_internacional,
        skip=skip, limit=limit,
        **filter)
    
    trans_avi = db_to_df(rd=rd)

    # trans_nav
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='emisiones',
        model=models.TRANS_NAV_emisiones,
        skip=skip, limit=limit,
        **filter)
    
    trans_nav = db_to_df(rd=rd)

    transporte = pd.concat([
        trans_pas, 
        trans_car, 
        trans_avi, 
        trans_nav
        ]).sum().to_dict()
    
    transporte["topic"]    = "resultados"
    transporte["bloque"]   = "general"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "Mt_CO2_e"


    ##########  agricultura ############## Mt_CO2_e
    filter={"bloque": "total_agricultura", "tipo": "total_agricultura", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='total_agricultura',
        model=models.AGRO_EMISIONES,
        skip=skip, limit=limit,
        **filter)
        
    agricultura = db_to_df(rd=rd).to_dict(orient='records')[0]
    agricultura["topic"]    = "resultados"
    agricultura["bloque"]   = "general"
    agricultura["tipo"]     = "agricultura"
    agricultura["unidad"]   = "Mt_CO2_e"


    ##########  ganaderia ############## Mt_CO2_e
    filter={"tipo": "total", 'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='total',
        model=models.GANA_EMISIONES,
        skip=skip, limit=limit,
        **filter)
        
    ganaderia = db_to_df(rd=rd).to_dict(orient='records')[0]
    ganaderia["topic"]    = "resultados"
    ganaderia["bloque"]   = "general"
    ganaderia["tipo"]     = "ganaderia"
    ganaderia["unidad"]   = "Mt_CO2_e"


    ##########  bosques ############## Mt_CO2_e
    filter={"tipo": "total_de_emisiones", 'medida_1': medida_bosq_1, 'medida_2': medida_bosq_2}
    rd = downloader(db=db, topic='total_emisiones',
        model=models.BOSQ_EMISIONES,
        skip=skip, limit=limit,
        **filter)
        
    bosques = db_to_df(rd=rd).to_dict(orient='records')[0]
    bosques["topic"]    = "resultados"
    bosques["bloque"]   = "general"
    bosques["tipo"]     = "bosques"
    bosques["unidad"]   = "Mt_CO2_e"
    

    resultado = {"resultados": [
        energia,
        electricidad,
        industria,
        residuos,
        edificaciones,
        transporte,
        agricultura,
        ganaderia,
        bosques
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######    Evolucion de la generacion energetica nacional                    #######
####################################################################################
@router.get('/evolucion_generacion_energetica_nacional')
def resultados_evolucion_generacion_energetica_nacional(
    medida_ener_1: schemas.Trayectoria=1,
    medida_elect_1: schemas.Trayectoria=1,
    medida_ind_1: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
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

    ##########  energia ############## TWh
    filter={"tipo": "total_combustibles_fosiles", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='combustibles_fosiles_producidos',
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        skip=skip, limit=limit,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "TWh"
    
    ##########  electricidad ############## TWh
    filter={"tipo": "total_combustibles_fosiles", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        skip=skip, limit=limit,
        **filter)
    
    df1 = db_to_df(rd=rd)
    
    filter={"tipo": "total_renovables", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        skip=skip, limit=limit,
        **filter)
    
    df2 = db_to_df(rd=rd)
        
    electricidad = pd.concat([df1, df2]).sum().to_dict()
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    ##########  industria ############## TWh
    filter={"bloque": "por_combustible", "tipo": "total", 'medida_1': medida_ind_1}
    rd = downloader(db=db, topic='energia_producida_por_autogeneracion_y_cogeneracion',
        model=models.INDU_SALIDAS_por_comb_ener_prod_autogeneracion_cogeneracion,
        skip=skip, limit=limit,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh
    filter={"bloque": "energia_producida", "tipo": "total_producido", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)
    
    filter={"tipo": "total_generacion", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)
        
    residuos = pd.concat([df1, df2]).sum().to_dict()
    residuos["topic"]    = "resultados"
    residuos["bloque"]   = "general"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "TWh"


    ##########  edificaciones ############## TWh
    filter={"bloque": "generacion", "tipo": "solar_fotovoltaica", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)
        
    edificaciones = db_to_df(rd=rd).to_dict(orient='records')[0]
    edificaciones["topic"]    = "resultados"
    edificaciones["bloque"]   = "general"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"


    ##########  transporte ############## TWh
    transporte = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "transporte",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  agricultura ############## TWh
    filter={"bloque": "total_cultivos", "tipo": "total_cultivos", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='cultivos',
        model=models.AGRO_SALIDAS_cultivos,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)
    
    filter={"tipo": "total", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='biocombustibles',
        model=models.AGRO_SALIDAS_biocombustibles,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)
        
    agricultura = pd.concat([df1, df2]).sum().to_dict()
    agricultura["topic"]    = "resultados"
    agricultura["bloque"]   = "general"
    agricultura["tipo"]     = "agricultura"
    agricultura["unidad"]   = "TWh"


    ##########  ganaderia ############## TWh
    filter={"tipo": "total", 'medida_1': medida_gana_1, 'medida_2': medida_gana_2, 'medida_3': medida_gana_3}
    rd = downloader(db=db, topic='produccion_de_estiercol_para_bioenergia',
        model=models.GANA_SALIDAS,
        skip=skip, limit=limit,
        **filter)
        
    ganaderia = db_to_df(rd=rd).to_dict(orient='records')[0]
    ganaderia["topic"]    = "resultados"
    ganaderia["bloque"]   = "general"
    ganaderia["tipo"]     = "ganaderia"
    ganaderia["unidad"]   = "TWh"


    ##########  bosques ############## TWh
    bosques = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "bosques",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }
    

    resultado = {"resultados": [
        energia,
        electricidad,
        industria,
        residuos,
        edificaciones,
        transporte,
        agricultura,
        ganaderia,
        bosques
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de la demanda energetica nacional                   #######
####################################################################################
@router.get('/evolucion_demanda_energetica_nacional')
def resultados_evolucion_demanda_energetica_nacional(
    medida_ener_1: schemas.Trayectoria=1,
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    medida_edi_res_aer_1: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1 : schemas.Trayectoria=1,
    medida_edi_com_aec_1 : schemas.Trayectoria=1,
    medida_edi_com_ute_1 : schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1 : schemas.Trayectoria=1,
    medida_trans_car_2 : schemas.Trayectoria=1,
    medida_trans_avi_1 : schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## TWh
    filter={"tipo": "total_combustibles_fosiles", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "TWh"
    
    ##########  electricidad ############## TWh
    electricidad = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "electricidad",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }

    ##########  industria ############## TWh
    filter={"bloque": "por_combustible", "tipo": "total_combustibles_fosiles", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh
    # res_sol
    filter={"bloque": "energia_consumida", "tipo": "celda_de_contingencia", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    filter={"bloque": "energia_consumida", "tipo": "incineracion", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    filter={"bloque": "energia_consumida", "tipo": "relleno_sanitario_controlados", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)
    df3 = db_to_df(rd=rd)

    filter={"bloque": "energia_consumida", "tipo": "reciclado", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)
    df4 = db_to_df(rd=rd)

    filter={"bloque": "energia_producida", "tipo": "tratamiento_mecanico_biologico_tmbcompostaje", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_SOL_SALIDAS_energia_producida,
        skip=skip, limit=limit,
        **filter)
    df5 = db_to_df(rd=rd)

    # res_agu
    
    filter={"tipo": "total_consumo", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.RES_AGU_SALIDAS_energia_consumida,
        skip=skip, limit=limit,
        **filter)
    df6 = db_to_df(rd=rd)
        
    residuos = pd.concat([df1, df2, df3, df4, df5, df6]).sum().to_dict()
    residuos["topic"]    = "resultados"
    residuos["bloque"]   = "general"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "TWh"


    ##########  edificaciones ############## TWh
    # edi_res_urb_aer 466
    filter={"tipo": "acondicionamiento_de_espacios", 'medida_1': medida_edi_res_aer_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ACOND_SALIDAS,
        skip=skip, limit=limit,
        **filter)
        
    edi_res_urb_aer = db_to_df(rd=rd)

    # edi_res_urb_irco 703
    filter={"bloque": "demanda", "tipo": "iluminacion_y_otros_usos", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    edi_res_urb_irco = db_to_df(rd=rd)

    # edi_res_urb_rural 62
    filter={"tipo": "demanda_edificaciones_rurales", 'medida_1': medida_edi_res_rural_1} 
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    edi_res_urb_rural = db_to_df(rd=rd)

    # edi_com_aec 159
    filter={"tipo": "acondicionamiento_de_espacios", 'medida_1': medida_edi_com_aec_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_ACOND_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    edi_com_aec = db_to_df(rd=rd)

    # edi_com_ute 258
    filter={"tipo": "usos_termicos_y_equipamiento", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    edi_com_ute = db_to_df(rd=rd)

    _edificaciones = pd.concat([
        edi_res_urb_aer, 
        edi_res_urb_irco, 
        edi_res_urb_rural, 
        edi_com_aec, 
        edi_com_ute
        ]).sum()
    
    edificaciones = _edificaciones.to_dict()
    edificaciones["topic"]    = "resultados"
    edificaciones["bloque"]   = "general"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"


    ##########  transporte ############## TWh
    # trans_pas 1165
    filter={"tipo": "total", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
        
    trans_pas = db_to_df(rd=rd)

    # trans_car 519
    filter={"tipo": "total", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2} 
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    
    trans_car = db_to_df(rd=rd)

    # trans_avi 59
    filter={"tipo": "aviacion_internacional", 'medida_1': medida_trans_avi_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_AVI_SALIDAS_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    
    trans_avi = db_to_df(rd=rd)

    # trans_nav 41
    filter={"tipo": "diesel", 'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_NAV_SALIDAS_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    
    trans_nav = db_to_df(rd=rd)

    _transporte = pd.concat([
        trans_pas, 
        trans_car, 
        trans_avi, 
        trans_nav
        ]).sum()
    
    transporte = _transporte.to_dict()
    transporte["topic"]    = "resultados"
    transporte["bloque"]   = "general"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "TWh"


    ##########  agricultura ############## TWh
    agricultura = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "agricultura",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  ganaderia ############## TWh
    ganaderia = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "ganaderia",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  bosques ############## TWh
    bosques = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "bosques",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }
    

    resultado = {"resultados": [
        energia,
        electricidad,
        industria,
        residuos,
        edificaciones,
        transporte,
        agricultura,
        ganaderia,
        bosques
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Consumo de combustibles por sector                            #######
####################################################################################
@router.get('/consumo_combustibles_por_sector')
def resultados_consumo_combustibles_por_sector(
    medida_ener_1: schemas.Trayectoria=1,
    medida_elect_1: schemas.Trayectoria=1,
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1 : schemas.Trayectoria=1,
    medida_edi_com_ute_1 : schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1 : schemas.Trayectoria=1,
    medida_trans_car_2 : schemas.Trayectoria=1,
    medida_trans_avi_1 : schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## TWh
    filter={"tipo": "total_combustibles_fosiles", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "TWh"
    
    ##########  electricidad ############## TWh
    filter={"tipo": "total_combustibles_fosiles", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        skip=skip, limit=limit,
        **filter)
        
    electricidad = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    ##########  industria ############## TWh
    filter={"bloque": "por_combustible", "tipo": "total_combustibles_fosiles", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh
    residuos = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "residuos",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  edificaciones ############## TWh
    # edi_res_urb_irco 705
    filter={"bloque": "demanda", "tipo": "gas_natural", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df1 = db_to_df(rd=rd)

    # edi_res_urb_irco 706
    filter={"bloque": "demanda", "tipo": "glp", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df2 = db_to_df(rd=rd)

    # edi_res_urb_rural 64
    filter={"tipo": "hidrocarburos_gaseosos_glp", 'medida_1': medida_edi_res_rural_1} 
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df3 = db_to_df(rd=rd)

    # edi_res_urb_rural 65
    filter={"tipo": "biomasa_seca_y_residuos_lena", 'medida_1': medida_edi_res_rural_1} 
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df4 = db_to_df(rd=rd)

    # edi_com_ute 261
    filter={"tipo": "hidrocarburos", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df5 = db_to_df(rd=rd)

    edificaciones = pd.concat([
        df1, 
        df2, 
        df3, 
        df4, 
        df5
        ]).sum().to_dict()
    
    edificaciones["topic"]    = "resultados"
    edificaciones["bloque"]   = "general"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"


    ##########  transporte ############## TWh
    # trans_pas 1165
    filter={"tipo": "total", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
        
    trans_pas_combustibles = db_to_df(rd=rd)

    filter={"tipo": "electrico", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
        
    trans_pas_electrico = db_to_df(rd=rd)

    trans_pas = trans_pas_combustibles - trans_pas_electrico

    # trans_car 519
    filter={"tipo": "total", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2} 
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    
    trans_car_combustibles = db_to_df(rd=rd)

    filter={"tipo": "electricidad", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2} 
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    
    trans_car_electricidad = db_to_df(rd=rd)

    trans_car = trans_car_combustibles - trans_car_electricidad

    # trans_avi 60
    filter={"tipo": "queroseno", 'medida_1': medida_trans_avi_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_AVI_SALIDAS_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    
    trans_avi = db_to_df(rd=rd)

    # trans_nav 41
    filter={"tipo": "diesel", 'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_NAV_SALIDAS_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    
    trans_nav = db_to_df(rd=rd)

    transporte = pd.concat([
        trans_pas, 
        trans_car, 
        trans_avi, 
        trans_nav
        ]).sum().to_dict()
    
    transporte["topic"]    = "resultados"
    transporte["bloque"]   = "general"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "TWh"


    ##########  agricultura ############## TWh
    agricultura = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "agricultura",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  ganaderia ############## TWh
    ganaderia = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "ganaderia",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  bosques ############## TWh
    bosques = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "bosques",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }
    

    resultado = {"resultados": [
        energia,
        electricidad,
        industria,
        residuos,
        edificaciones,
        transporte,
        agricultura,
        ganaderia,
        bosques
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Consumo por tipo de combustible                               #######
####################################################################################
@router.get('/consumo_por_tipo_de_combustible')
def resultados_consumo_por_tipo_de_combustible(
    medida_ener_1: schemas.Trayectoria=1,
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1: schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_avi_1: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  gasolina ############## TWh
    # trans_pas 1158
    filter={"tipo": "gasolina", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)
    
    # trans_car 511
    filter={"tipo": "gasolina", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    # ind 660
    filter={"tipo": "gasolina", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df3 = db_to_df(rd=rd)
        
    gasolina = pd.concat([df1, df2, df3]).sum().to_dict()
    gasolina["topic"]    = "resultados"
    gasolina["bloque"]   = "general"
    gasolina["tipo"]     = "gasolina"
    gasolina["unidad"]   = "TWh"
    
    ##########  diesel ############## TWh
    # edi_com_ute 265
    filter={"tipo": "diesel", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)
    
    # trans_pas 1159
    filter={"tipo": "diesel", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    # trans_car 512
    filter={"tipo": "diesel", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    df3 = db_to_df(rd=rd)

    # trans_nav 41
    filter={"tipo": "diesel", 'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_NAV_SALIDAS_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df4 = db_to_df(rd=rd)

    # ind 661
    filter={"tipo": "diesel", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df5 = db_to_df(rd=rd)
        
    diesel = pd.concat([df1, df2, df3, df4, df5]).sum().to_dict()
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "general"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "TWh"

    ##########  gas_gnc ############## TWh
    # trans_car 513
    filter={"tipo": "gas_gnc", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
        
    gas_gnc = db_to_df(rd=rd).to_dict(orient='records')[0]
    gas_gnc["topic"]    = "resultados"
    gas_gnc["bloque"]   = "general"
    gas_gnc["tipo"]     = "gas_gnc"
    gas_gnc["unidad"]   = "TWh"

    ##########  gas_gnl ############## TWh
    # ener 265
    filter={"tipo": "gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    # edi_res_irco 705
    filter={"tipo": "gas_natural", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    # edi_com_ute 261
    filter={"tipo": "gas_natural", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df3 = db_to_df(rd=rd)

    # trans_pas 1161
    filter={"tipo": "gas_natural", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
    df4 = db_to_df(rd=rd)

    # trans_car 514
    filter={"tipo": "gas_gnl", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    df5 = db_to_df(rd=rd)

    # ind 656
    filter={"tipo": "gas_natural", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df6 = db_to_df(rd=rd)
    
    gas_gnl = pd.concat([df1, df2, df3, df4, df5, df6]).sum().to_dict()
    gas_gnl["topic"]    = "resultados"
    gas_gnl["bloque"]   = "general"
    gas_gnl["tipo"]     = "gas_gnl"
    gas_gnl["unidad"]   = "TWh"


    ##########  glp ############## TWh
    # edi_res_irco 706
    filter={"tipo": "glp", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    # edi_res_rural 64
    filter={"tipo": "hidrocarburos_gaseosos_glp", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    # edi_com_ute 263
    filter={"tipo": "glp", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df3 = db_to_df(rd=rd)

    # trans_pas 1162
    filter={"tipo": "glp", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
    df4 = db_to_df(rd=rd)

    # trans_car 515
    filter={"tipo": "glp", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    df5 = db_to_df(rd=rd)

    # ind 665
    filter={"tipo": "glp", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df6 = db_to_df(rd=rd)
    
    glp = pd.concat([df1, df2, df3, df4, df5, df6]).sum().to_dict()
    glp["topic"]    = "resultados"
    glp["bloque"]   = "general"
    glp["tipo"]     = "glp"
    glp["unidad"]   = "TWh"

    ##########  fuel_oil ############## TWh
    # edi_com_ute 266
    filter={"tipo": "fuel_oil", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    # ind 664
    filter={"tipo": "fuel_oil", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)
    
    fuel_oil = pd.concat([df1, df2]).sum().to_dict()
    fuel_oil["topic"]    = "resultados"
    fuel_oil["bloque"]   = "general"
    fuel_oil["tipo"]     = "fuel_oil"
    fuel_oil["unidad"]   = "TWh"

    ##########  crudo ############## TWh
    # edi_com_ute 262
    filter={"tipo": "petroleo", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    # ind 658
    filter={"tipo": "petroleo", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    crudo = pd.concat([df1, df2]).sum().to_dict()
    crudo["topic"]    = "resultados"
    crudo["bloque"]   = "general"
    crudo["tipo"]     = "crudo"
    crudo["unidad"]   = "TWh"


    ##########  hidrogeno ############## TWh
    # trans_pas 1164
    # filter={"tipo": "vehiculo_de_hidrogeno", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    # rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
    #     model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
    #     skip=skip, limit=limit,
    #     **filter)
    # df1 = db_to_df(rd=rd)

    # trans_car 517
    filter={"tipo": "hidrogeno", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    # ind 669
    filter={"tipo": "hidrogeno_verde", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df3 = db_to_df(rd=rd)

    hidrogeno = pd.concat([df2, df3]).sum().to_dict()
    hidrogeno["topic"]    = "resultados"
    hidrogeno["bloque"]   = "general"
    hidrogeno["tipo"]     = "hidrogeno"
    hidrogeno["unidad"]   = "TWh"


    ##########  queroseno ############## TWh
    # edi_com_ute 264
    filter={"tipo": "queroseno", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    # trans_pas 1163
    filter={"tipo": "queroseno_jet", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)

    # trans_car 518
    filter={"tipo": "queroseno", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    df3 = db_to_df(rd=rd)

    # trans_avi 60
    filter={"tipo": "queroseno", 'medida_1': medida_trans_avi_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_AVI_SALIDAS_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df4 = db_to_df(rd=rd)

    # ind 666
    filter={"tipo": "queroseno", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df5 = db_to_df(rd=rd)

    queroseno = pd.concat([df1, df2, df3, df4, df5]).sum().to_dict()
    queroseno["topic"]    = "resultados"
    queroseno["bloque"]   = "general"
    queroseno["tipo"]     = "queroseno"
    queroseno["unidad"]   = "TWh"


    ##########  lena ############## TWh
    # edi_res_rural 65
    filter={"tipo": "biomasa_seca_y_residuos_lena", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)

    # ind 657
    filter={"tipo": "lena", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)
    
    lena = pd.concat([df1, df2]).sum().to_dict()
    lena["topic"]    = "resultados"
    lena["bloque"]   = "general"
    lena["tipo"]     = "lena"
    lena["unidad"]   = "TWh"


    ##########  bagazo ############## TWh
    # ind 610
    filter={"tipo": "bagazo", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    df1 = db_to_df(rd=rd)
    
    # ind 632
    filter={"tipo": "bagazo", 'medida_1': medida_ind_1}
    rd = downloader(db=db, topic='energia_producida_por_autogeneracion_y_cogeneracion',
        model=models.INDU_SALIDAS_por_comb_ener_prod_autogeneracion_cogeneracion,
        skip=skip, limit=limit,
        **filter)
    df2 = db_to_df(rd=rd)
    
    # agro 282
    filter={"bloque": "total_cultivos", "tipo": "total_cultivos", 'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='cultivos',
        model=models.AGRO_SALIDAS_cultivos,
        skip=skip, limit=limit,
        **filter)
    
    df3 = db_to_df(rd=rd)

    df = df1 - df2 - df3
    
    bagazo = df.to_dict(orient='records')[0]
    bagazo["topic"]    = "resultados"
    bagazo["bloque"]   = "general"
    bagazo["tipo"]     = "bagazo"
    bagazo["unidad"]   = "TWh"


    ##########  carbon_mineral ############## TWh
    # ind 655
    filter={"tipo": "carbon_mineral", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)

    carbon_mineral = db_to_df(rd=rd).to_dict(orient='records')[0]
    carbon_mineral["topic"]    = "resultados"
    carbon_mineral["bloque"]   = "general"
    carbon_mineral["tipo"]     = "carbon_mineral"
    carbon_mineral["unidad"]   = "TWh"


    ##########  carbon_lena ############## TWh
    # ind 652
    filter={"tipo": "carbon_de_lena", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    
    carbon_lena = db_to_df(rd=rd).to_dict(orient='records')[0]
    carbon_lena["topic"]    = "resultados"
    carbon_lena["bloque"]   = "general"
    carbon_lena["tipo"]     = "carbon_lena"
    carbon_lena["unidad"]   = "TWh"


    ##########  coque ############## TWh
    # ind 663
    filter={"tipo": "coque", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
    
    coque = db_to_df(rd=rd).to_dict(orient='records')[0]
    coque["topic"]    = "resultados"
    coque["bloque"]   = "general"
    coque["tipo"]     = "coque"
    coque["unidad"]   = "TWh"
    

    resultado = {"resultados": [
        gasolina,
        diesel,
        gas_gnc,
        gas_gnl,
        glp,
        fuel_oil,
        crudo,
        hidrogeno,
        queroseno,
        lena,
        bagazo,
        carbon_mineral,
        carbon_lena,
        coque
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Consumo de electricidad por sector                            #######
####################################################################################
@router.get('/consumo_electricidad_por_sector')
def resultados_consumo_electricidad_por_sector(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_edi_res_aer_1 : schemas.Trayectoria=1,
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    medida_edi_res_rural_1 : schemas.Trayectoria=1,
    medida_edi_com_aec_1: schemas.Trayectoria=1,
    medida_edi_com_ute_1 : schemas.Trayectoria=1,
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1 : schemas.Trayectoria=1,
    medida_trans_car_2 : schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## TWh
    energia = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "energia",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }
    
    ##########  electricidad ############## TWh
    electricidad = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "electricidad",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }

    ##########  industria ############## TWh
    filter={"bloque": "por_combustible", "tipo": "total_electricidad", 'medida_1': medida_ind_1, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_energia_requerida,
        skip=skip, limit=limit,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh
    residuos = {
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "topic": "resultados",
            "bloque": "general",
            "tipo": "residuos",
            "unidad": "TWh"
        }


    ##########  edificaciones ############## TWh
    # edi_res_urb_rural 63
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_res_rural_1} 
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df1 = db_to_df(rd=rd)

    # edi_com_aec 160
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_com_aec_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_ACOND_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df2 = db_to_df(rd=rd)

    # edi_com_ute 259
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df3 = db_to_df(rd=rd)

    # edi_res_aer 467 #############################
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_res_aer_1} 
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ACOND_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df4 = db_to_df(rd=rd)

    # edi_res_irco 704
    filter={"bloque": "demanda","tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        skip=skip, limit=limit,
        **filter)
    
    df5 = db_to_df(rd=rd)

    _edificaciones = pd.concat([df1, df2, df3, df4, df5]).sum()
    
    edificaciones = _edificaciones.to_dict()
    edificaciones["topic"]    = "resultados"
    edificaciones["bloque"]   = "general"
    edificaciones["tipo"]     = "edificaciones"
    edificaciones["unidad"]   = "TWh"


    ##########  transporte ############## TWh
    # trans_pas 1160
    filter={"tipo": "electrico", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        skip=skip, limit=limit,
        **filter)
        
    trans_pas = db_to_df(rd=rd)

    # trans_car 516
    filter={"tipo": "electricidad", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2} 
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        skip=skip, limit=limit,
        **filter)
    
    trans_car = db_to_df(rd=rd)

    _transporte = pd.concat([trans_pas, trans_car]).sum()
    
    transporte = _transporte.to_dict()
    transporte["topic"]    = "resultados"
    transporte["bloque"]   = "general"
    transporte["tipo"]     = "transporte"
    transporte["unidad"]   = "TWh"


    ##########  agricultura ############## TWh
    agricultura = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "agricultura",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  ganaderia ############## TWh
    ganaderia = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "ganaderia",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }


    ##########  bosques ############## TWh
    bosques = {
            "topic": "resultados",
            "bloque": "general",
            "tipo": "bosques",
            "y2018": 0.0,
            "y2020": 0.0,
            "y2025": 0.0,
            "y2030": 0.0,
            "y2035": 0.0,
            "y2040": 0.0,
            "y2045": 0.0,
            "y2050": 0.0,
            "unidad": "TWh"
        }
    

    resultado = {"resultados": [
        energia,
        electricidad,
        industria,
        residuos,
        edificaciones,
        transporte,
        agricultura,
        ganaderia,
        bosques
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


# ####################################################################################
# #######                         Flujos de energia                            #######
# ####################################################################################
@router.get('/flujos_energia')
def resultados_evolucion_excedentes_energeticos(
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""


    resultado = {"resultados": 'TODO'}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
