from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
import logging

from app.src.crud.base import downloader

from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

from .util.util import db_to_df

from ..entradas.endpoint_ener_import_export import read_entradas_requerimientos_energeticos, read_entradas_excedentes_energeticos

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######     Evolución de las emisiones del sector Energia                    #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_energia')
def resultados_evolucion_de_las_emisiones_del_sector_energia(
    medida_ener_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  1 crudo ############## Mt_CO2_e
    filter={"bloque": "crudo", "tipo": "total_crudo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        skip=skip, limit=limit,
        **filter)
        
    crudo = db_to_df(rd=rd).to_dict(orient='records')[0]
    crudo["topic"]    = "resultados"
    crudo["bloque"]   = "energia"
    crudo["tipo"]     = "crudo"
    crudo["unidad"]   = "Mt_CO2_e"
    
    ##########  2 gas_natural ############## Mt_CO2_e
    filter={"bloque": "gas natural", "tipo": "total_gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        skip=skip, limit=limit,
        **filter)
        
    gas_natural = db_to_df(rd=rd).to_dict(orient='records')[0]
    gas_natural["topic"]    = "resultados"
    gas_natural["bloque"]   = "energia"
    gas_natural["tipo"]     = "gas_natural"
    gas_natural["unidad"]   = "Mt_CO2_e"

    ########## 3  carbon ############## Mt_CO2_e
    filter={"bloque": "carbon", "tipo": "total_carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ENER_CombFosil_EMISIONES_produccion,
        skip=skip, limit=limit,
        **filter)
        
    carbon = db_to_df(rd=rd).to_dict(orient='records')[0]
    carbon["topic"]    = "resultados"
    carbon["bloque"]   = "energia"
    carbon["tipo"]     = "carbon"
    carbon["unidad"]   = "Mt_CO2_e"
    

    resultado = {"resultados": [
        crudo,
        gas_natural,
        carbon
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######    Evolucion de la generacion energetica del sector energia          #######
#######            produccion de combustibles                                #######
####################################################################################
@router.get('/evolucion_generacion_energetica_del_sector_energia_por_combustibles')
def resultados_evolucion_generacion_energetica_del_sector_energia_por_combustibles(
    medida_ener_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  1 crudo ############## TWh
    filter={"tipo": "crudo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='combustibles_fosiles_producidos',
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        skip=skip, limit=limit,
        **filter)
        
    crudo = db_to_df(rd=rd).to_dict(orient='records')[0]
    crudo["topic"]    = "resultados"
    crudo["bloque"]   = "energia"
    crudo["tipo"]     = "crudo"
    crudo["unidad"]   = "TWh"
    
    ##########  2 gas_natural ############## TWh
    filter={"tipo": "gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='combustibles_fosiles_producidos',
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        skip=skip, limit=limit,
        **filter)
        
    gas_natural = db_to_df(rd=rd).to_dict(orient='records')[0]
    gas_natural["topic"]    = "resultados"
    gas_natural["bloque"]   = "energia"
    gas_natural["tipo"]     = "gas_natural"
    gas_natural["unidad"]   = "TWh"

    ########## 3  carbon ############## TWh
    filter={"tipo": "carbon", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='combustibles_fosiles_producidos',
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
        skip=skip, limit=limit,
        **filter)
        
    carbon = db_to_df(rd=rd).to_dict(orient='records')[0]
    carbon["topic"]    = "resultados"
    carbon["bloque"]   = "energia"
    carbon["tipo"]     = "carbon"
    carbon["unidad"]   = "TWh"

    resultado = {"resultados": [
        crudo,
        gas_natural,
        carbon
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución del consumo energetico                              #######
#######        consumo de combustibles fosiles                               #######
####################################################################################
@router.get('/evolucion_consumo_energetico_comb_fosiles')
def resultados_evolucion_consumo_energetico_comb_fosiles(
    medida_ener_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  gas_natural ############## TWh
    filter={"tipo": "gas_natural", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    gas_natural = db_to_df(rd=rd).to_dict(orient='records')[0]
    gas_natural["topic"]    = "resultados"
    gas_natural["bloque"]   = "energia"
    gas_natural["tipo"]     = "gas_natural"
    gas_natural["unidad"]   = "TWh"


    ##########  petroleo ############## TWh
    filter={"tipo": "petroleo", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    petroleo = db_to_df(rd=rd).to_dict(orient='records')[0]
    petroleo["topic"]    = "resultados"
    petroleo["bloque"]   = "energia"
    petroleo["tipo"]     = "petroleo"
    petroleo["unidad"]   = "TWh"


    ##########  diesel ############## TWh
    filter={"tipo": "diesel", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    diesel = db_to_df(rd=rd).to_dict(orient='records')[0]
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "energia"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "TWh"


    ##########  fuel_oil ############## TWh
    filter={"tipo": "fuel_oil", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    fuel_oil = db_to_df(rd=rd).to_dict(orient='records')[0]
    fuel_oil["topic"]    = "resultados"
    fuel_oil["bloque"]   = "energia"
    fuel_oil["tipo"]     = "fuel_oil"
    fuel_oil["unidad"]   = "TWh"


    ##########  glp ############## TWh
    filter={"tipo": "glp", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    glp = db_to_df(rd=rd).to_dict(orient='records')[0]
    glp["topic"]    = "resultados"
    glp["bloque"]   = "energia"
    glp["tipo"]     = "glp"
    glp["unidad"]   = "TWh"


    ##########  gasolina_para_motores ############## TWh
    filter={"tipo": "gasolina_para_motores", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    gasolina_para_motores = db_to_df(rd=rd).to_dict(orient='records')[0]
    gasolina_para_motores["topic"]    = "resultados"
    gasolina_para_motores["bloque"]   = "energia"
    gasolina_para_motores["tipo"]     = "gasolina_para_motores"
    gasolina_para_motores["unidad"]   = "TWh"


    ##########  queroseno ############## TWh
    filter={"tipo": "queroseno", 'medida_1': medida_ener_1}
    rd = downloader(db=db, topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
        model=models.ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector,
        skip=skip, limit=limit,
        **filter)
        
    queroseno = db_to_df(rd=rd).to_dict(orient='records')[0]
    queroseno["topic"]    = "resultados"
    queroseno["bloque"]   = "energia"
    queroseno["tipo"]     = "queroseno"
    queroseno["unidad"]   = "TWh"



    resultado = {"resultados": [
        gas_natural,
        petroleo,
        diesel,
        fuel_oil,
        glp,
        gasolina_para_motores,
        queroseno
    ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de los excedentes energetico                        #######
####################################################################################
@router.get('/evolucion_excedentes_energeticos')
def resultados_evolucion_excedentes_energeticos(
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
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    entrada = read_entradas_requerimientos_energeticos(
        medida_ener_1=medida_ener_1,
        medida_ind_1 =medida_ind_1,
        medida_ind_4 =medida_ind_4,
        medida_trans_car_1 =medida_trans_car_1,
        medida_trans_car_2 =medida_trans_car_2,
        medida_trans_pas_1 =medida_trans_pas_1,
        medida_trans_pas_2 =medida_trans_pas_2,
        medida_trans_nav_1 =medida_trans_nav_1,
        medida_edi_com_ute_1 =medida_edi_com_ute_1,
        medida_edi_res_irco_1 =medida_edi_res_irco_1,
        medida_edi_res_irco_2 =medida_edi_res_irco_2,
        medida_edi_res_irco_3 =medida_edi_res_irco_3,
        medida_edi_res_rural_1=medida_edi_res_rural_1,
        db=db,
        skip=skip, limit=limit
        )

    crudo = entrada['requerimientos_energeticos'][0]
    crudo["topic"]    = "resultados"
    crudo["bloque"]   = "energia"
    crudo["tipo"]     = "crudo"
    crudo["unidad"]   = "TWh"

    gas = entrada['requerimientos_energeticos'][1]
    gas["topic"]    = "resultados"
    gas["bloque"]   = "energia"
    gas["tipo"]     = "crudo"
    gas["unidad"]   = "TWh"

    carbon = entrada['requerimientos_energeticos'][2]
    carbon["topic"]    = "resultados"
    carbon["bloque"]   = "energia"
    carbon["tipo"]     = "carbon"
    carbon["unidad"]   = "TWh"

    resultado = {"resultados": [crudo, gas, carbon]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de los requerimientos energeticos                   #######
####################################################################################
@router.get('/evolucion_requerimientos_energeticos')
def resultados_evolucion_requerimientos_energeticos(
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
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   excedentes_energeticos  ############## TWh
    entrada = read_entradas_excedentes_energeticos(
        medida_ener_1=medida_ener_1,
        medida_ind_1 =medida_ind_1,
        medida_ind_4 =medida_ind_4,
        medida_trans_car_1 =medida_trans_car_1,
        medida_trans_car_2 =medida_trans_car_2,
        medida_trans_pas_1 =medida_trans_pas_1,
        medida_trans_pas_2 =medida_trans_pas_2,
        medida_trans_nav_1 =medida_trans_nav_1,
        medida_edi_com_ute_1 =medida_edi_com_ute_1,
        medida_edi_res_irco_1 =medida_edi_res_irco_1,
        medida_edi_res_irco_2 =medida_edi_res_irco_2,
        medida_edi_res_irco_3 =medida_edi_res_irco_3,
        medida_edi_res_rural_1=medida_edi_res_rural_1,
        db=db, skip=skip, limit=limit
    )

    crudo = entrada['excedentes_energeticos'][0]
    crudo["topic"]    = "resultados"
    crudo["bloque"]   = "energia"
    crudo["tipo"]     = "crudo"
    crudo["unidad"]   = "TWh"

    gas = entrada['excedentes_energeticos'][1]
    gas["topic"]    = "resultados"
    gas["bloque"]   = "energia"
    gas["tipo"]     = "crudo"
    gas["unidad"]   = "TWh"

    carbon = entrada['excedentes_energeticos'][2]
    carbon["topic"]    = "resultados"
    carbon["bloque"]   = "energia"
    carbon["tipo"]     = "carbon"
    carbon["unidad"]   = "TWh"

    resultado = {"resultados": [crudo, gas, carbon]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
