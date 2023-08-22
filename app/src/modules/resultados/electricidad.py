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

from ..entradas.endpoint_elect_import_export import read_entradas_requerimientos_energeticos, read_entradas_excedentes_energeticos

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False

router = APIRouter()


####################################################################################
#######     Evolución de las emisiones del sector Electricidad               #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_electricidad')
def resultados_evolucion_de_las_emisiones_del_sector_electricidad(
    medida_elect_1: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    medida_res_agu_1: schemas.Trayectoria=1,
    medida_res_agu_2: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  1 termoelectrica_gas_natural ############## Mt_CO2_e
    filter={"tipo": "termoelectrica_gas_natural", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
        
    termoelectrica_gas_natural = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_gas_natural["topic"]    = "resultados"
    termoelectrica_gas_natural["bloque"]   = "electricidad"
    termoelectrica_gas_natural["tipo"]     = "termoelectrica_gas_natural"
    termoelectrica_gas_natural["unidad"]   = "Mt_CO2_e"
    
    ##########  2 termoelectrica_carbon ############## Mt_CO2_e
    filter={"tipo": "termoelectrica_carbon", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
        
    termoelectrica_carbon = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_carbon["topic"]    = "resultados"
    termoelectrica_carbon["bloque"]   = "electricidad"
    termoelectrica_carbon["tipo"]     = "termoelectrica_carbon"
    termoelectrica_carbon["unidad"]   = "Mt_CO2_e"

    ########## 3  diesel ############## Mt_CO2_e
    filter={"tipo": "diesel", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
        
    diesel = db_to_df(rd=rd).to_dict(orient='records')[0]
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "electricidad"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "Mt_CO2_e"

    ##########  4 fuel_oil  ############## Mt_CO2_e
    filter={"tipo": "fuel_oil", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
        
    fuel_oil = db_to_df(rd=rd).to_dict(orient='records')[0]
    fuel_oil["topic"]    = "resultados"
    fuel_oil["bloque"]   = "electricidad"
    fuel_oil["tipo"]     = "fuel_oil"
    fuel_oil["unidad"]   = "Mt_CO2_e"

    ##########  5 petroleo  ############## Mt_CO2_e
    filter={"tipo": "petroleo", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
    
    petroleo = db_to_df(rd=rd).to_dict(orient='records')[0]
    petroleo["topic"]    = "resultados"
    petroleo["bloque"]   = "electricidad"
    petroleo["tipo"]     = "petroleo"
    petroleo["unidad"]   = "Mt_CO2_e"


    ##########  6 glp  ############## Mt_CO2_e
    filter={"tipo": "gas_lp", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
        
    glp = db_to_df(rd=rd).to_dict(orient='records')[0]
    glp["topic"]    = "resultados"
    glp["bloque"]   = "residuoes"
    glp["tipo"]     = "glp"
    glp["unidad"]   = "Mt_CO2_e"

    ##########  7 termoelectrica_gas_natural_ccus  ############## Mt_CO2_e
    filter={"tipo": "termoelectrica_gas_natural_ccus", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
        
    termoelectrica_gas_natural_ccus = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_gas_natural_ccus["topic"]    = "resultados"
    termoelectrica_gas_natural_ccus["bloque"]   = "electricidad"
    termoelectrica_gas_natural_ccus["tipo"]     = "termoelectrica_gas_natural_ccus"
    termoelectrica_gas_natural_ccus["unidad"]   = "Mt_CO2_e"


    ##########  8 termoelectrica_carbon_ccus  ############## Mt_CO2_e
    filter={"tipo": "termoelectrica_carbon_ccus", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_gei',
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
        **filter)
        
    termoelectrica_carbon_ccus = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_carbon_ccus["topic"]    = "resultados"
    termoelectrica_carbon_ccus["bloque"]   = "electricidad"
    termoelectrica_carbon_ccus["tipo"]     = "termoelectrica_carbon_ccus"
    termoelectrica_carbon_ccus["unidad"]   = "Mt_CO2_e"


    ##########  9 autogeneracion_residuos  ############## Mt_CO2_e
    # RES_AGU [245]
    filter={"bloque": "total_emisiones_gei_energia", "tipo": "total_emisiones_gei_energia", 'medida_1': medida_res_agu_1, 'medida_2': medida_res_agu_2}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_energia',
        model=models.RES_AGU_emisiones,
        **filter)
    res_agu = db_to_df(rd=rd)

    # RES_SOL [400]
    filter={"bloque": "total", "grupo": "total", "tipo": "total_co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_energia',
        model=models.RES_SOL_emisiones,
        **filter)
    res_sol = db_to_df(rd=rd)
    
    autogeneracion_residuos = res_agu + res_sol
        
    autogeneracion_residuos = autogeneracion_residuos.to_dict(orient='records')[0]
    autogeneracion_residuos["topic"]    = "resultados"
    autogeneracion_residuos["bloque"]   = "electricidad"
    autogeneracion_residuos["tipo"]     = "autogeneracion_residuos"
    autogeneracion_residuos["unidad"]   = "Mt_CO2_e"
    

    resultado = {"resultados": [
        termoelectrica_gas_natural,
        termoelectrica_carbon,
        diesel,
        fuel_oil, 
        petroleo, 
        glp, 
        termoelectrica_gas_natural_ccus,
        termoelectrica_carbon_ccus,
        autogeneracion_residuos
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######    Evolucion de la generacion electrica del sector electricidad      #######
####################################################################################
@router.get('/evolucion_generacion_electrica_del_sector_electricidad')
def resultados_evolucion_generacion_electrica_del_sector_electricidad(
    medida_elect_1: schemas.Trayectoria=1,
    medida_res_sol_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########  1 termoelectrica_gas_natural ############## TWh
    filter={"tipo": "termoelectrica_gas_natural", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
        
    termoelectrica_gas_natural = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_gas_natural["topic"]    = "resultados"
    termoelectrica_gas_natural["bloque"]   = "electricidad"
    termoelectrica_gas_natural["tipo"]     = "termoelectrica_gas_natural"
    termoelectrica_gas_natural["unidad"]   = "TWh"
    
    ##########  2 termoelectrica_carbon ############## TWh
    filter={"tipo": "termoelectrica_carbon", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
        
    termoelectrica_carbon = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_carbon["topic"]    = "resultados"
    termoelectrica_carbon["bloque"]   = "electricidad"
    termoelectrica_carbon["tipo"]     = "termoelectrica_carbon"
    termoelectrica_carbon["unidad"]   = "TWh"

    ########## 3  diesel ############## TWh
    filter={"tipo": "diesel", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
        
    diesel = db_to_df(rd=rd).to_dict(orient='records')[0]
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "electricidad"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "TWh"

    ##########  4 fuel_oil  ############## TWh
    filter={"tipo": "fuel_oil", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
        
    fuel_oil = db_to_df(rd=rd).to_dict(orient='records')[0]
    fuel_oil["topic"]    = "resultados"
    fuel_oil["bloque"]   = "electricidad"
    fuel_oil["tipo"]     = "fuel_oil"
    fuel_oil["unidad"]   = "TWh"

    ##########  5 petroleo  ############## TWh
    filter={"tipo": "petroleo", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
    
    petroleo = db_to_df(rd=rd).to_dict(orient='records')[0]
    petroleo["topic"]    = "resultados"
    petroleo["bloque"]   = "electricidad"
    petroleo["tipo"]     = "petroleo"
    petroleo["unidad"]   = "TWh"


    ##########  6 glp  ############## TWh
    filter={"tipo": "gas_lp", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
        
    glp = db_to_df(rd=rd).to_dict(orient='records')[0]
    glp["topic"]    = "resultados"
    glp["bloque"]   = "residuoes"
    glp["tipo"]     = "glp"
    glp["unidad"]   = "TWh"

    ##########  7 termoelectrica_gas_natural_ccus  ############## TWh
    filter={"tipo": "termoelectrica_gas_natural_ccus", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
        
    termoelectrica_gas_natural_ccus = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_gas_natural_ccus["topic"]    = "resultados"
    termoelectrica_gas_natural_ccus["bloque"]   = "electricidad"
    termoelectrica_gas_natural_ccus["tipo"]     = "termoelectrica_gas_natural_ccus"
    termoelectrica_gas_natural_ccus["unidad"]   = "TWh"


    ##########  8 termoelectrica_carbon_ccus  ############## TWh
    filter={"tipo": "termoelectrica_carbon_ccus", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='combustibels_fosiles',
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
        **filter)
        
    termoelectrica_carbon_ccus = db_to_df(rd=rd).to_dict(orient='records')[0]
    termoelectrica_carbon_ccus["topic"]    = "resultados"
    termoelectrica_carbon_ccus["bloque"]   = "electricidad"
    termoelectrica_carbon_ccus["tipo"]     = "termoelectrica_carbon_ccus"
    termoelectrica_carbon_ccus["unidad"]   = "TWh"

    ##########  9 autogeneracion_residuos  ############## TWh
    # RES_SOL [400]
    filter={"bloque": "total", "grupo": "total", "tipo": "total_co2_e", 'medida_1': medida_res_sol_1}
    rd = downloader(db=db, topic='emisiones_de_gases_de_efecto_invernadero_energia',
        model=models.RES_SOL_emisiones,
        **filter)
        
    autogeneracion_residuos = db_to_df(rd=rd).to_dict(orient='records')[0]
    autogeneracion_residuos["topic"]    = "resultados"
    autogeneracion_residuos["bloque"]   = "electricidad"
    autogeneracion_residuos["tipo"]     = "autogeneracion_residuos"
    autogeneracion_residuos["unidad"]   = "TWh"

    ##########  10 grandes_centrales_hidroelectricas  ############## TWh
    filter={"tipo": "grandes_centrales_hidroelectricas", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    grandes_centrales_hidroelectricas = db_to_df(rd=rd).to_dict(orient='records')[0]
    grandes_centrales_hidroelectricas["topic"]    = "resultados"
    grandes_centrales_hidroelectricas["bloque"]   = "electricidad"
    grandes_centrales_hidroelectricas["tipo"]     = "grandes_centrales_hidroelectricas"
    grandes_centrales_hidroelectricas["unidad"]   = "TWh"

    ##########  11 pequenas_centrales_hidroelectricas  ############## TWh
    filter={"tipo": "pequenas_centrales_hidroelectricas", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    pequenas_centrales_hidroelectricas = db_to_df(rd=rd).to_dict(orient='records')[0]
    pequenas_centrales_hidroelectricas["topic"]    = "resultados"
    pequenas_centrales_hidroelectricas["bloque"]   = "electricidad"
    pequenas_centrales_hidroelectricas["tipo"]     = "pequenas_centrales_hidroelectricas"
    pequenas_centrales_hidroelectricas["unidad"]   = "TWh"

    ##########  12 solar_termica  ############## TWh
    filter={"tipo": "solar_distribuida_terciario", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    solar_termica = db_to_df(rd=rd).to_dict(orient='records')[0]
    solar_termica["topic"]    = "resultados"
    solar_termica["bloque"]   = "electricidad"
    solar_termica["tipo"]     = "solar_termica"
    solar_termica["unidad"]   = "TWh"

    ##########  13 solar_fotovoltaica  ############## TWh
    filter={"tipo": "solar_fotovoltaica", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    solar_fotovoltaica = db_to_df(rd=rd).to_dict(orient='records')[0]
    solar_fotovoltaica["topic"]    = "resultados"
    solar_fotovoltaica["bloque"]   = "electricidad"
    solar_fotovoltaica["tipo"]     = "solar_fotovoltaica"
    solar_fotovoltaica["unidad"]   = "TWh"

    ##########  14 eolica_costa_adentro_parque_jepirachi  ############## TWh
    filter={"tipo": "eolica_costa_adentro_parque_jepirachi", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    eolica_costa_adentro_parque_jepirachi = db_to_df(rd=rd).to_dict(orient='records')[0]
    eolica_costa_adentro_parque_jepirachi["topic"]    = "resultados"
    eolica_costa_adentro_parque_jepirachi["bloque"]   = "electricidad"
    eolica_costa_adentro_parque_jepirachi["tipo"]     = "eolica_costa_adentro_parque_jepirachi"
    eolica_costa_adentro_parque_jepirachi["unidad"]   = "TWh"

    ##########  15 eolica_costa_adentro_resto_pais  ############## TWh
    filter={"tipo": "eolica_costa_adentro_resto_del_pais", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    eolica_costa_adentro_resto_pais = db_to_df(rd=rd).to_dict(orient='records')[0]
    eolica_costa_adentro_resto_pais["topic"]    = "resultados"
    eolica_costa_adentro_resto_pais["bloque"]   = "electricidad"
    eolica_costa_adentro_resto_pais["tipo"]     = "eolica_costa_adentro_resto_pais"
    eolica_costa_adentro_resto_pais["unidad"]   = "TWh"

    ##########  16 eolica_costa_afuera  ############## TWh
    filter={"tipo": "eolica_costa_afuera", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    eolica_costa_afuera = db_to_df(rd=rd).to_dict(orient='records')[0]
    eolica_costa_afuera["topic"]    = "resultados"
    eolica_costa_afuera["bloque"]   = "electricidad"
    eolica_costa_afuera["tipo"]     = "eolica_costa_afuera"
    eolica_costa_afuera["unidad"]   = "TWh"

    ##########  17 hidrogeno_verde  ############## TWh
    filter={"tipo": "hidrogeno_verde", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    hidrogeno_verde = db_to_df(rd=rd).to_dict(orient='records')[0]
    hidrogeno_verde["topic"]    = "resultados"
    hidrogeno_verde["bloque"]   = "electricidad"
    hidrogeno_verde["tipo"]     = "hidrogeno_verde"
    hidrogeno_verde["unidad"]   = "TWh"

    ##########  18 biomasa  ############## TWh
    filter={"tipo": "biomasa", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    biomasa = db_to_df(rd=rd).to_dict(orient='records')[0]
    biomasa["topic"]    = "resultados"
    biomasa["bloque"]   = "electricidad"
    biomasa["tipo"]     = "biomasa"
    biomasa["unidad"]   = "TWh"

    ##########  19 bagazo  ############## TWh
    filter={"tipo": "bagazo", 'medida_1': medida_elect_1}
    rd = downloader(db=db, topic='energias_renovables_no_convencionales',
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
        **filter)
        
    bagazo = db_to_df(rd=rd).to_dict(orient='records')[0]
    bagazo["topic"]    = "resultados"
    bagazo["bloque"]   = "electricidad"
    bagazo["tipo"]     = "bagazo"
    bagazo["unidad"]   = "TWh"
    

    resultado = {"resultados": [
        termoelectrica_gas_natural,
        termoelectrica_carbon,
        diesel,
        fuel_oil,
        petroleo,
        glp,
        termoelectrica_gas_natural_ccus, 
        termoelectrica_carbon_ccus, 
        autogeneracion_residuos, 
        grandes_centrales_hidroelectricas,
        pequenas_centrales_hidroelectricas,
        solar_termica,
        solar_fotovoltaica,
        eolica_costa_adentro_parque_jepirachi,
        eolica_costa_adentro_resto_pais,
        eolica_costa_afuera,
        hidrogeno_verde,
        biomasa,
        bagazo
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de los requerimientos energeticos                   #######
####################################################################################
@router.get('/evolucion_requerimientos_energeticos')
def resultados_evolucion_requerimientos_energeticos(
    medida_elect_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    entrada = read_entradas_requerimientos_energeticos(medida_elect_1=medida_elect_1, db=db)
    requerimientos_energeticos = entrada['requerimientos_energeticos'][0]
    requerimientos_energeticos["topic"]    = "resultados"
    requerimientos_energeticos["bloque"]   = "electricidad"
    requerimientos_energeticos["tipo"]     = "requerimientos_energeticos"
    requerimientos_energeticos["unidad"]   = "TWh"

    resultado = {"resultados": [requerimientos_energeticos]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de los excedentes energeticos                       #######
####################################################################################
@router.get('/evolucion_excedentes_energeticos')
def resultados_evolucion_excedentes_energeticos(
    medida_elect_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   excedentes_energeticos  ############## TWh
    entrada = read_entradas_excedentes_energeticos(medida_elect_1=medida_elect_1, db=db)

    excedentes_energeticos = entrada['excedentes_energeticos'][0]
    excedentes_energeticos["topic"]    = "resultados"
    excedentes_energeticos["bloque"]   = "electricidad"
    excedentes_energeticos["tipo"]     = "excedentes_energeticos"
    excedentes_energeticos["unidad"]   = "TWh"


    resultado = {"resultados": [excedentes_energeticos]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
