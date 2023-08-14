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

from .util.util import db_to_df, db_to_dict, get_item, set_zeros, set_suma_total, not_negative, YEARS

from .energia import resultados_evolucion_de_las_emisiones_del_sector_energia

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
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## Mt_CO2_e
    produccion = resultados_evolucion_de_las_emisiones_del_sector_energia(medida_ener_1=medida_ener_1,db=db)
    
    df_produccion = pd.DataFrame(produccion['resultados'])[YEARS]

    filter={"tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        **filter)
    df1 = db_to_df(rd=rd)

    filter={"tipo": "total_petroleo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        **filter)
    df2 = db_to_df(rd=rd)

    filter={"tipo": "total_diesel", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        **filter)
    df3 = db_to_df(rd=rd)

    filter={"tipo": "total_fuel_oil", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        **filter)
    df4 = db_to_df(rd=rd)

    filter={"tipo": "total_glp", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        **filter)
    df5 = db_to_df(rd=rd)

    filter={"tipo": "total_gasolina", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        **filter)
    df6 = db_to_df(rd=rd)

    filter={"tipo": "total_queroseno", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_consumo,
        **filter)
    df7 = db_to_df(rd=rd)

    df_consumo = pd.concat([df1, df2, df3, df4, df5, df6, df7]).sum()

    energia = df_produccion + df_consumo
    
    energia = energia.sum().to_dict()
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "Mt_CO2_e"

    print('\n energia \n', energia)
    
    ##########  electricidad ############## Mt_CO2_e
    filter={"bloque": "gas natural", "tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    electricidad = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "Mt_CO2_e"

    ##########  industria ############## Mt_CO2_e
    filter={"bloque": "carbon", "tipo": "total_carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "Mt_CO2_e"

    ##########  residuos ############## Mt_CO2_e


    ##########  edificaciones ############## Mt_CO2_e


    ##########  transporte ############## Mt_CO2_e


    ##########  agricultura ############## Mt_CO2_e


    ##########  ganaderia ############## Mt_CO2_e


    ##########  bosques ############## Mt_CO2_e
    

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
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## TWh
    filter={"bloque": "crudo", "tipo": "total_crudo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "TWh"
    
    ##########  electricidad ############## TWh
    filter={"bloque": "gas natural", "tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    electricidad = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    ##########  industria ############## TWh
    filter={"bloque": "carbon", "tipo": "total_carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh


    ##########  edificaciones ############## TWh


    ##########  transporte ############## TWh


    ##########  agricultura ############## TWh


    ##########  ganaderia ############## TWh


    ##########  bosques ############## TWh
    

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
    # medida_elect_1: schemas.Trayectoria=1,
    medida_ener_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## TWh
    filter={"bloque": "crudo", "tipo": "total_crudo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "TWh"
    
    ##########  electricidad ############## TWh
    filter={"bloque": "gas natural", "tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    electricidad = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    ##########  industria ############## TWh
    filter={"bloque": "carbon", "tipo": "total_carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh


    ##########  edificaciones ############## TWh


    ##########  transporte ############## TWh


    ##########  agricultura ############## TWh


    ##########  ganaderia ############## TWh


    ##########  bosques ############## TWh
    

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
    # medida_elect_1: schemas.Trayectoria=1,
    medida_ener_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## TWh
    filter={"bloque": "crudo", "tipo": "total_crudo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "TWh"
    
    ##########  electricidad ############## TWh
    filter={"bloque": "gas natural", "tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    electricidad = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    ##########  industria ############## TWh
    filter={"bloque": "carbon", "tipo": "total_carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh


    ##########  edificaciones ############## TWh


    ##########  transporte ############## TWh


    ##########  agricultura ############## TWh


    ##########  ganaderia ############## TWh


    ##########  bosques ############## TWh
    

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
    # medida_elect_1: schemas.Trayectoria=1,
    medida_ener_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  gasolina ############## TWh
    filter={"bloque": "crudo", "tipo": "total_crudo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    gasolina = db_to_df(rd=rd).to_dict(orient='records')[0]
    gasolina["topic"]    = "resultados"
    gasolina["bloque"]   = "general"
    gasolina["tipo"]     = "gasolina"
    gasolina["unidad"]   = "TWh"
    
    ##########  diesel ############## TWh
    filter={"bloque": "gas natural", "tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    diesel = db_to_df(rd=rd).to_dict(orient='records')[0]
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "general"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "TWh"

    ##########  gas_gnc ############## TWh
    filter={"bloque": "carbon", "tipo": "total_carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    gas_gnc = db_to_df(rd=rd).to_dict(orient='records')[0]
    gas_gnc["topic"]    = "resultados"
    gas_gnc["bloque"]   = "general"
    gas_gnc["tipo"]     = "gas_gnc"
    gas_gnc["unidad"]   = "TWh"

    ##########  gas_gnl ############## TWh


    ##########  glp ############## TWh


    ##########  fuel_oil ############## TWh


    ##########  crudo ############## TWh


    ##########  hidrogeno ############## TWh


    ##########  queroseno ############## TWh


    ##########  lena ############## TWh


    ##########  bagazo ############## TWh


    ##########  carbon_mineral ############## TWh


    ##########  carbon_lena ############## TWh


    ##########  coque ############## TWh
    

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
    # medida_elect_1: schemas.Trayectoria=1,
    medida_ener_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  energia ############## TWh
    filter={"bloque": "crudo", "tipo": "total_crudo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    energia = db_to_df(rd=rd).to_dict(orient='records')[0]
    energia["topic"]    = "resultados"
    energia["bloque"]   = "general"
    energia["tipo"]     = "energia"
    energia["unidad"]   = "TWh"
    
    ##########  electricidad ############## TWh
    filter={"bloque": "gas natural", "tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    electricidad = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad["topic"]    = "resultados"
    electricidad["bloque"]   = "general"
    electricidad["tipo"]     = "electricidad"
    electricidad["unidad"]   = "TWh"

    ##########  industria ############## TWh
    filter={"bloque": "carbon", "tipo": "total_carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        **filter)
        
    industria = db_to_df(rd=rd).to_dict(orient='records')[0]
    industria["topic"]    = "resultados"
    industria["bloque"]   = "general"
    industria["tipo"]     = "industria"
    industria["unidad"]   = "TWh"

    ##########  residuos ############## TWh


    ##########  edificaciones ############## TWh


    ##########  transporte ############## TWh


    ##########  agricultura ############## TWh


    ##########  ganaderia ############## TWh


    ##########  bosques ############## TWh
    

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
# #######        Evolución de los excedentes energetico                        #######
# ####################################################################################
# @router.get('/evolucion_excedentes_energeticos')
# def resultados_evolucion_excedentes_energeticos(
#     medida_ener_1: schemas.Trayectoria=1,
#     medida_ind_1: schemas.Trayectoria=1,
#     medida_ind_2: schemas.Trayectoria=1,
#     medida_ind_3: schemas.Trayectoria=1,
#     medida_ind_4: schemas.Trayectoria=1,
#     medida_trans_car_1: schemas.Trayectoria=1,
#     medida_trans_car_2: schemas.Trayectoria=1,
#     medida_trans_pas_1: schemas.Trayectoria=1,
#     medida_trans_pas_2: schemas.Trayectoria=1,
#     medida_trans_nav_1: schemas.Trayectoria=1,
#     medida_edi_com_ute_1: schemas.Trayectoria=1,
#     medida_edi_res_irco_1: schemas.Trayectoria=1,
#     medida_edi_res_irco_2: schemas.Trayectoria=1,
#     medida_edi_res_irco_3: schemas.Trayectoria=1,
#     medida_edi_res_rural_1: schemas.Trayectoria=1,
#     db: Session = Depends(deps.get_db), 
#     # skip: int = 0, 
#     # limit: int = 100,
#     # current_user: models_user.User = Depends(deps.get_current_active_user)
#     ) -> Any:
#     """READ"""

#     entrada = read_entradas_requerimientos_energeticos(
#         medida_ener_1=medida_ener_1,
#         medida_ind_1 =medida_ind_1,
#         medida_ind_2 =medida_ind_2,
#         medida_ind_3 =medida_ind_3,
#         medida_ind_4 =medida_ind_4,
#         medida_trans_car_1 =medida_trans_car_1,
#         medida_trans_car_2 =medida_trans_car_2,
#         medida_trans_pas_1 =medida_trans_pas_1,
#         medida_trans_pas_2 =medida_trans_pas_2,
#         medida_trans_nav_1 =medida_trans_nav_1,
#         medida_edi_com_ute_1 =medida_edi_com_ute_1,
#         medida_edi_res_irco_1 =medida_edi_res_irco_1,
#         medida_edi_res_irco_2 =medida_edi_res_irco_2,
#         medida_edi_res_irco_3 =medida_edi_res_irco_3,
#         medida_edi_res_rural_1=medida_edi_res_rural_1,
#         db=db
#         )

#     crudo = entrada['requerimientos_energeticos'][0]
#     crudo["topic"]    = "resultados"
#     crudo["bloque"]   = "general"
#     crudo["tipo"]     = "crudo"
#     crudo["unidad"]   = "TWh"

#     gas = entrada['requerimientos_energeticos'][1]
#     gas["topic"]    = "resultados"
#     gas["bloque"]   = "general"
#     gas["tipo"]     = "crudo"
#     gas["unidad"]   = "TWh"

#     carbon = entrada['requerimientos_energeticos'][2]
#     carbon["topic"]    = "resultados"
#     carbon["bloque"]   = "general"
#     carbon["tipo"]     = "carbon"
#     carbon["unidad"]   = "TWh"

#     resultado = {"resultados": [crudo, gas, carbon]}

#     if DEBUG:
#         logger.info(f'Read Data: {jsonable_encoder(resultado)}')

#     return jsonable_encoder(resultado)


# ####################################################################################
# #######        Evolución de los requerimientos energeticos                   #######
# ####################################################################################
# @router.get('/evolucion_requerimientos_energeticos')
# def resultados_eevolucion_requerimientos_energeticos(
#     medida_ener_1: schemas.Trayectoria=1,
#     medida_ind_1: schemas.Trayectoria=1,
#     medida_ind_2: schemas.Trayectoria=1,
#     medida_ind_3: schemas.Trayectoria=1,
#     medida_ind_4: schemas.Trayectoria=1,
#     medida_trans_car_1: schemas.Trayectoria=1,
#     medida_trans_car_2: schemas.Trayectoria=1,
#     medida_trans_pas_1: schemas.Trayectoria=1,
#     medida_trans_pas_2: schemas.Trayectoria=1,
#     medida_trans_nav_1: schemas.Trayectoria=1,
#     medida_edi_com_ute_1: schemas.Trayectoria=1,
#     medida_edi_res_irco_1: schemas.Trayectoria=1,
#     medida_edi_res_irco_2: schemas.Trayectoria=1,
#     medida_edi_res_irco_3: schemas.Trayectoria=1,
#     medida_edi_res_rural_1: schemas.Trayectoria=1,
#     db: Session = Depends(deps.get_db), 
#     # skip: int = 0, 
#     # limit: int = 100,
#     # current_user: models_user.User = Depends(deps.get_current_active_user)
#     ) -> Any:
#     """READ"""

#     ##########   excedentes_energeticos  ############## TWh
#     entrada = read_entradas_excedentes_energeticos(
#         medida_ener_1=medida_ener_1,
#         medida_ind_1 =medida_ind_1,
#         medida_ind_2 =medida_ind_2,
#         medida_ind_3 =medida_ind_3,
#         medida_ind_4 =medida_ind_4,
#         medida_trans_car_1 =medida_trans_car_1,
#         medida_trans_car_2 =medida_trans_car_2,
#         medida_trans_pas_1 =medida_trans_pas_1,
#         medida_trans_pas_2 =medida_trans_pas_2,
#         medida_trans_nav_1 =medida_trans_nav_1,
#         medida_edi_com_ute_1 =medida_edi_com_ute_1,
#         medida_edi_res_irco_1 =medida_edi_res_irco_1,
#         medida_edi_res_irco_2 =medida_edi_res_irco_2,
#         medida_edi_res_irco_3 =medida_edi_res_irco_3,
#         medida_edi_res_rural_1=medida_edi_res_rural_1,
#         db=db
#     )

#     crudo = entrada['excedentes_energeticos'][0]
#     crudo["topic"]    = "resultados"
#     crudo["bloque"]   = "general"
#     crudo["tipo"]     = "crudo"
#     crudo["unidad"]   = "TWh"

#     gas = entrada['excedentes_energeticos'][1]
#     gas["topic"]    = "resultados"
#     gas["bloque"]   = "general"
#     gas["tipo"]     = "crudo"
#     gas["unidad"]   = "TWh"

#     carbon = entrada['excedentes_energeticos'][2]
#     carbon["topic"]    = "resultados"
#     carbon["bloque"]   = "general"
#     carbon["tipo"]     = "carbon"
#     carbon["unidad"]   = "TWh"

#     resultado = {"resultados": [crudo, gas, carbon]}

#     if DEBUG:
#         logger.info(f'Read Data: {jsonable_encoder(resultado)}')

#     return jsonable_encoder(resultado)
