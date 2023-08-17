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

    ##########  1 diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_res_acond_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_RES_ACOND_EMISIONES,
        **filter)
        
    diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios = db_to_df(rd=rd).to_dict(orient='records')[0]
    diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios["topic"]    = "resultados"
    diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios["bloque"]   = "edificaciones"
    diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios["tipo"]     = "diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios"
    diseno_y_eficiencia_energetica_para_el_acondicionamiento_de_espacios["unidad"]   = "Mt_CO2_e"
    
    
    ##########  2 eficiencia_energetica_y_equipos_eficientes_en_viviendas   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_RES_ILU_REF_COC_OTR_EMISIONES,
        **filter)
        
    eficiencia_energetica_y_equipos_eficientes_en_viviendas = db_to_df(rd=rd).to_dict(orient='records')[0]
    eficiencia_energetica_y_equipos_eficientes_en_viviendas["topic"]    = "resultados"
    eficiencia_energetica_y_equipos_eficientes_en_viviendas["bloque"]   = "edificaciones"
    eficiencia_energetica_y_equipos_eficientes_en_viviendas["tipo"]     = "eficiencia_energetica_y_equipos_eficientes_en_viviendas"
    eficiencia_energetica_y_equipos_eficientes_en_viviendas["unidad"]   = "Mt_CO2_e"
    

    ########## 3  eficiencia_energetica_para_viviendas_rurales   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_RES_RURAL_EMISIONES,
        **filter)
        
    eficiencia_energetica_para_viviendas_rurales = db_to_df(rd=rd).to_dict(orient='records')[0]
    eficiencia_energetica_para_viviendas_rurales["topic"]    = "resultados"
    eficiencia_energetica_para_viviendas_rurales["bloque"]   = "edificaciones"
    eficiencia_energetica_para_viviendas_rurales["tipo"]     = "eficiencia_energetica_para_viviendas_rurales"
    eficiencia_energetica_para_viviendas_rurales["unidad"]   = "Mt_CO2_e"
    

    ##########  4 acondicionamiento_de_espacios_comerciales_y_de_servicio   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_com_acond_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_COM_ACOND_EMISIONES,
        **filter)
        
    acondicionamiento_de_espacios_comerciales_y_de_servicio = db_to_df(rd=rd).to_dict(orient='records')[0]
    acondicionamiento_de_espacios_comerciales_y_de_servicio["topic"]    = "resultados"
    acondicionamiento_de_espacios_comerciales_y_de_servicio["bloque"]   = "edificaciones"
    acondicionamiento_de_espacios_comerciales_y_de_servicio["tipo"]     = "acondicionamiento_de_espacios_comerciales_y_de_servicio"
    acondicionamiento_de_espacios_comerciales_y_de_servicio["unidad"]   = "Mt_CO2_e"

    ##########  5 usos_termicos_y_equipamiento_comercial_y_de_servicio   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.EDIF_COM_USOS_TERM_EQUIP_EMISIONES,
        **filter)
        
    usos_termicos_y_equipamiento_comercial_y_de_servicio = db_to_df(rd=rd).to_dict(orient='records')[0]
    usos_termicos_y_equipamiento_comercial_y_de_servicio["topic"]    = "resultados"
    usos_termicos_y_equipamiento_comercial_y_de_servicio["bloque"]   = "edificaciones"
    usos_termicos_y_equipamiento_comercial_y_de_servicio["tipo"]     = "usos_termicos_y_equipamiento_comercial_y_de_servicio"
    usos_termicos_y_equipamiento_comercial_y_de_servicio["unidad"]   = "Mt_CO2_e"
    

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
    # edi_res_urb_aer
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_res_acond_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ACOND_SALIDAS,
        **filter)
    edi_res_urb_aer = db_to_df(rd=rd)

    # edi_res_urb_irco
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        **filter)
    edi_res_urb_irco = db_to_df(rd=rd)

    # edi_res_rural
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        **filter)
    edi_res_rural = db_to_df(rd=rd)

    # edi_com_aec
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_com_acond_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_ACOND_SALIDAS,
        **filter)
    edi_com_aec = db_to_df(rd=rd)

    # edi_com_ute
    filter={"tipo": "electricidad_entregado_al_usuario_final", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    edi_com_ute = db_to_df(rd=rd)


    electricidad = pd.concat([edi_res_urb_aer, edi_res_urb_irco, edi_res_rural, edi_com_aec, edi_com_ute]).sum().to_dict()
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "edificaciones"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    
    ##########   gas_natural   ############## TWh

    # edi_res_urb_irco
    filter={"tipo": "gas_natural", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        **filter)
    edi_res_urb_irco = db_to_df(rd=rd)

    # edi_com_ute
    filter={"tipo": "gas_natural", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    edi_com_ute = db_to_df(rd=rd)

    gas_natural = pd.concat([edi_res_urb_irco, edi_com_ute]).sum().to_dict()
    gas_natural["topic"]    = "resultados"
    gas_natural["bloque"]   = "edificaciones"
    gas_natural["tipo"]     = "gas_natural"
    gas_natural["unidad"]   = "TWh"
    
    
    ##########   glp   ############## TWh

    # edi_com_ute
    filter={"tipo": "glp", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    edi_com_ute = db_to_df(rd=rd)

    # edi_res_urb_irco
    filter={"tipo": "glp", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        **filter)
    edi_res_urb_irco = db_to_df(rd=rd)

    # edi_res_rural
    filter={"tipo": "hidrocarburos_gaseosos_glp", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        **filter)
    edi_res_rural = db_to_df(rd=rd)

    glp = pd.concat([edi_res_urb_irco, edi_com_ute, edi_res_rural]).sum().to_dict()
    glp["topic"]    = "resultados"
    glp["bloque"]   = "edificaciones"
    glp["tipo"]     = "glp"
    glp["unidad"]   = "TWh"


    ##########   petroleo   ############## TWh
    filter={"tipo": "petroleo", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    
    petroleo = db_to_df(rd=rd).to_dict(orient='records')[0]
    petroleo["topic"]    = "resultados"
    petroleo["bloque"]   = "edificaciones"
    petroleo["tipo"]     = "petroleo"
    petroleo["unidad"]   = "TWh"


    ##########   queroseno   ############## TWh
    filter={"tipo": "queroseno", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    
    queroseno = db_to_df(rd=rd).to_dict(orient='records')[0]
    queroseno["topic"]    = "resultados"
    queroseno["bloque"]   = "edificaciones"
    queroseno["tipo"]     = "queroseno"
    queroseno["unidad"]   = "TWh"

    
    ##########   diesel   ############## TWh
    filter={"tipo": "diesel", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    
    diesel = db_to_df(rd=rd).to_dict(orient='records')[0]
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "edificaciones"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "TWh"

    
    ##########   fuel_oil   ############## TWh
    filter={"tipo": "fuel_oil", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    
    fuel_oil = db_to_df(rd=rd).to_dict(orient='records')[0]
    fuel_oil["topic"]    = "resultados"
    fuel_oil["bloque"]   = "edificaciones"
    fuel_oil["tipo"]     = "fuel_oil"
    fuel_oil["unidad"]   = "TWh"


    ##########   biomansa_seca_y_residuos   ############## TWh
    filter={"tipo": "biomasa_seca_y_residuos_lena", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        **filter)
    
    biomansa_seca_y_residuos = db_to_df(rd=rd).to_dict(orient='records')[0]
    biomansa_seca_y_residuos["topic"]    = "resultados"
    biomansa_seca_y_residuos["bloque"]   = "edificaciones"
    biomansa_seca_y_residuos["tipo"]     = "biomansa_seca_y_residuos"
    biomansa_seca_y_residuos["unidad"]   = "TWh"


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
    # edi_res_urb_aer
    filter={"tipo": "acondicionamiento_de_espacios", 'medida_1': medida_edi_res_acond_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ACOND_SALIDAS,
        **filter)
    edi_res_urb_aer = db_to_df(rd=rd)

    # edi_res_urb_irco
    filter={"tipo": "iluminacion_y_otros_usos", 'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        **filter)
    edi_res_urb_irco = db_to_df(rd=rd)

    edificaciones_residenciales_urbanas = pd.concat([edi_res_urb_aer, edi_res_urb_irco]).sum().to_dict()
    edificaciones_residenciales_urbanas["topic"]    = "resultados"
    edificaciones_residenciales_urbanas["bloque"]   = "edificaciones"
    edificaciones_residenciales_urbanas["tipo"]     = "edificaciones_residenciales_urbanas"
    edificaciones_residenciales_urbanas["unidad"]   = "TWh"
    
    ##########   edificaciones_residenciales_rurales   ############## TWh
    # edi_res_rural
    filter={"tipo": "demanda_edificaciones_rurales", 'medida_1': medida_edi_res_rural_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_RES_RURAL_SALIDAS,
        **filter)
    edificaciones_residenciales_rurales = db_to_df(rd=rd).to_dict(orient='records')[0]
    edificaciones_residenciales_rurales["topic"]    = "resultados"
    edificaciones_residenciales_rurales["bloque"]   = "edificaciones"
    edificaciones_residenciales_rurales["tipo"]     = "edificaciones_residenciales_rurales"
    edificaciones_residenciales_rurales["unidad"]   = "TWh"
    
    ##########   edificaciones_comerciales_y_de_servicio   ############## TWh
    # edi_com_aec
    filter={"tipo": "acondicionamiento_de_espacios", 'medida_1': medida_edi_com_acond_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_ACOND_SALIDAS,
        **filter)
    edi_com_aec = db_to_df(rd=rd)

    # edi_com_ute
    filter={"tipo": "usos_termicos_y_equipamiento", 'medida_1': medida_edi_com_ute_1}
    rd = downloader(db=db, topic='energia_producida_y_requerida',
        model=models.EDIF_COM_USOS_TERM_EQUIP_SALIDAS,
        **filter)
    edi_com_ute = db_to_df(rd=rd)

    edificaciones_comerciales_y_de_servicio = pd.concat([edi_com_aec, edi_com_ute]).sum().to_dict()
    edificaciones_comerciales_y_de_servicio["topic"]    = "resultados"
    edificaciones_comerciales_y_de_servicio["bloque"]   = "edificaciones"
    edificaciones_comerciales_y_de_servicio["tipo"]     = "edificaciones_comerciales_y_de_servicio"
    edificaciones_comerciales_y_de_servicio["unidad"]   = "TWh"
    
    
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
    medida_edi_res_irco_1: schemas.Trayectoria=1,
    medida_edi_res_irco_2: schemas.Trayectoria=1,
    medida_edi_res_irco_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""    
    
    filter={'medida_1': medida_edi_res_irco_1, 'medida_2': medida_edi_res_irco_2, 'medida_3': medida_edi_res_irco_3}
    rd = downloader(db=db, topic='generacion_solar_fotovoltaica',
        model=models.EDIF_RES_ILU_REF_COC_OTR_Metodologia_generacion_solar_fotovoltaica,
        **filter)

    edificaciones_residenciales_urbanas = db_to_df(rd=rd).to_dict(orient='records')[0]
    edificaciones_residenciales_urbanas["topic"]    = "resultados"
    edificaciones_residenciales_urbanas["bloque"]   = "edificaciones"
    edificaciones_residenciales_urbanas["tipo"]     = "edificaciones_residenciales_urbanas"
    edificaciones_residenciales_urbanas["unidad"]   = "TWh"
    

    resultado = {"resultados": [edificaciones_residenciales_urbanas]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
