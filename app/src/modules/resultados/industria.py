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
#######     Evolución de las emisiones del sector Industria                   #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_industria')
def resultados_evolucion_de_las_emisiones_del_sector_industria(
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

    ##########  1 cemento ############## Mt_CO2_e
    filter={"tipo": "cemento", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
        
    cemento = db_to_df(rd=rd).to_dict(orient='records')[0]
    cemento["topic"]    = "resultados"
    cemento["bloque"]   = "industria"
    cemento["tipo"]     = "cemento"
    cemento["unidad"]   = "Mt_CO2_e"
    
    ##########  2 hierro_y_no_ferrosos ############## Mt_CO2_e
    filter={"tipo": "hierro_y_no_ferrosos", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
        
    hierro_y_no_ferrosos = db_to_df(rd=rd).to_dict(orient='records')[0]
    hierro_y_no_ferrosos["topic"]    = "resultados"
    hierro_y_no_ferrosos["bloque"]   = "industria"
    hierro_y_no_ferrosos["tipo"]     = "hierro_y_no_ferrosos"
    hierro_y_no_ferrosos["unidad"]   = "Mt_CO2_e"

    ########## 3  papel ############## Mt_CO2_e
    filter={"tipo": "papel", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
        
    papel = db_to_df(rd=rd).to_dict(orient='records')[0]
    papel["topic"]    = "resultados"
    papel["bloque"]   = "industria"
    papel["tipo"]     = "papel"
    papel["unidad"]   = "Mt_CO2_e"

    ##########  4 quimicos  ############## Mt_CO2_e
    filter={"tipo": "quimicos", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
        
    quimicos = db_to_df(rd=rd).to_dict(orient='records')[0]
    quimicos["topic"]    = "resultados"
    quimicos["bloque"]   = "industria"
    quimicos["tipo"]     = "quimicos"
    quimicos["unidad"]   = "Mt_CO2_e"

    ##########  5 alimentos_y_bebidas  ############## Mt_CO2_e
    filter={"tipo": "alimentos_y_bebidas", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
    
    alimentos_y_bebidas = db_to_df(rd=rd).to_dict(orient='records')[0]
    alimentos_y_bebidas["topic"]    = "resultados"
    alimentos_y_bebidas["bloque"]   = "industria"
    alimentos_y_bebidas["tipo"]     = "alimentos_y_bebidas"
    alimentos_y_bebidas["unidad"]   = "Mt_CO2_e"


    ##########  6 textil  ############## Mt_CO2_e
    filter={"tipo": "textil", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
        
    textil = db_to_df(rd=rd).to_dict(orient='records')[0]
    textil["topic"]    = "resultados"
    textil["bloque"]   = "residuoes"
    textil["tipo"]     = "textil"
    textil["unidad"]   = "Mt_CO2_e"

    ##########  7 ladrilleras  ############## Mt_CO2_e
    filter={"tipo": "ladrilleras", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
        
    ladrilleras = db_to_df(rd=rd).to_dict(orient='records')[0]
    ladrilleras["topic"]    = "resultados"
    ladrilleras["bloque"]   = "industria"
    ladrilleras["tipo"]     = "ladrilleras"
    ladrilleras["unidad"]   = "Mt_CO2_e"


    ##########  8 otros  ############## Mt_CO2_e
    filter={"tipo": "otros", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_gases_efecto_invernadero,
        **filter)
        
    otros = db_to_df(rd=rd).to_dict(orient='records')[0]
    otros["topic"]    = "resultados"
    otros["bloque"]   = "industria"
    otros["tipo"]     = "otros"
    otros["unidad"]   = "Mt_CO2_e"


    ##########  9 emisiones_sao  ############## Mt_CO2_e
    filter={"tipo": "emisiones_sao", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='gases_efecto_invernadero',
        model=models.INDU_emisiones_sao,
        **filter)
        
    emisiones_sao = db_to_df(rd=rd).to_dict(orient='records')[0]
    emisiones_sao["topic"]    = "resultados"
    emisiones_sao["bloque"]   = "industria"
    emisiones_sao["tipo"]     = "emisiones_sao"
    emisiones_sao["unidad"]   = "Mt_CO2_e"
    

    resultado = {"resultados": [
        cemento,
        hierro_y_no_ferrosos,
        papel,
        quimicos, 
        alimentos_y_bebidas, 
        textil, 
        ladrilleras,
        otros,
        emisiones_sao
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######    Evolucion de la demanda energetica del sector industria           #######
#######                   por tipo de industria                              #######
####################################################################################
@router.get('/evolucion_demanda_energetica_por_tipo_industria')
def resultados_evolucion_demanda_energetica_por_tipo_industria(
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

    ##########  1 cemento ############## TWh
    filter={"tipo": "cemento", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
        
    cemento = db_to_df(rd=rd).to_dict(orient='records')[0]
    cemento["topic"]    = "resultados"
    cemento["bloque"]   = "industria"
    cemento["tipo"]     = "cemento"
    cemento["unidad"]   = "TWh"
    
    ##########  2 hierro_y_no_ferrosos ############## TWh
    filter={"tipo": "hierro_y_acero", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
        
    hierro_y_no_ferrosos = db_to_df(rd=rd).to_dict(orient='records')[0]
    hierro_y_no_ferrosos["topic"]    = "resultados"
    hierro_y_no_ferrosos["bloque"]   = "industria"
    hierro_y_no_ferrosos["tipo"]     = "hierro_y_no_ferrosos"
    hierro_y_no_ferrosos["unidad"]   = "TWh"

    ########## 3  papel ############## TWh
    filter={"tipo": "papel", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
        
    papel = db_to_df(rd=rd).to_dict(orient='records')[0]
    papel["topic"]    = "resultados"
    papel["bloque"]   = "industria"
    papel["tipo"]     = "papel"
    papel["unidad"]   = "TWh"

    ##########  4 quimicos  ############## TWh
    filter={"tipo": "quimicos", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
        
    quimicos = db_to_df(rd=rd).to_dict(orient='records')[0]
    quimicos["topic"]    = "resultados"
    quimicos["bloque"]   = "industria"
    quimicos["tipo"]     = "quimicos"
    quimicos["unidad"]   = "TWh"

    ##########  5 alimentos_y_bebidas  ############## TWh
    filter={"tipo": "alimentos_y_bebidas", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
    
    alimentos_y_bebidas = db_to_df(rd=rd).to_dict(orient='records')[0]
    alimentos_y_bebidas["topic"]    = "resultados"
    alimentos_y_bebidas["bloque"]   = "industria"
    alimentos_y_bebidas["tipo"]     = "alimentos_y_bebidas"
    alimentos_y_bebidas["unidad"]   = "TWh"


    ##########  6 textil  ############## TWh
    filter={"tipo": "textil", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
        
    textil = db_to_df(rd=rd).to_dict(orient='records')[0]
    textil["topic"]    = "resultados"
    textil["bloque"]   = "residuoes"
    textil["tipo"]     = "textil"
    textil["unidad"]   = "TWh"

    ##########  7 ladrilleras  ############## TWh
    filter={"tipo": "ladrilleras", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
        
    ladrilleras = db_to_df(rd=rd).to_dict(orient='records')[0]
    ladrilleras["topic"]    = "resultados"
    ladrilleras["bloque"]   = "industria"
    ladrilleras["tipo"]     = "ladrilleras"
    ladrilleras["unidad"]   = "TWh"


    ##########  8 otros  ############## TWh
    filter={"tipo": "otros", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia',
        model=models.INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida,
        **filter)
        
    otros = db_to_df(rd=rd).to_dict(orient='records')[0]
    otros["topic"]    = "resultados"
    otros["bloque"]   = "industria"
    otros["tipo"]     = "otros"
    otros["unidad"]   = "TWh"
    

    resultado = {"resultados": [
        cemento,
        hierro_y_no_ferrosos,
        papel,
        quimicos, 
        alimentos_y_bebidas, 
        textil, 
        ladrilleras,
        otros
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de la demanda energetica del sector Industria       #######
#######                   por combustibles                                   #######
####################################################################################
@router.get('/evolucion_demanda_energetica_por_combustibles')
def resultados_evolucion_demanda_energetica_por_combustibles(
    medida_ind_1: schemas.Trayectoria=1,
    medida_ind_2: schemas.Trayectoria=1,
    medida_ind_3: schemas.Trayectoria=1,
    medida_ind_4: schemas.Trayectoria=1,
    medida_agro_1: schemas.Trayectoria=1,
    medida_agro_2: schemas.Trayectoria=1,
    medida_agro_3: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   bagazo  ############## TWh
    filter={"bloque": "por_combustible", "tipo": "bagazo", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_energia_requerida,
        **filter)
    
    energia_requerida = db_to_df(rd=rd)

    filter={"bloque": "por_combustible", "tipo": "bagazo", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='energia_producida_por_autogeneracion_y_cogeneracion',
        model=models.INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion,
        **filter)
    
    energia_producida_por_autogeneracion_y_cogeneracion = db_to_df(rd=rd)

    filter={'medida_1': medida_agro_1, 'medida_2': medida_agro_2, 'medida_3': medida_agro_3}
    rd = downloader(db=db, topic='cultivos',
        model=models.AGRO_SALIDAS_cultivos,
        **filter)
    
    cultivos = db_to_df(rd=rd).sum()
    
    bagazo = energia_requerida - energia_producida_por_autogeneracion_y_cogeneracion - cultivos

    bagazo = bagazo.to_dict(orient='records')[0]
    bagazo["topic"]    = "resultados"
    bagazo["bloque"]   = "industria"
    bagazo["tipo"]     = "bagazo"
    bagazo["unidad"]   = "TWh"

    
    ##########   carbon_mineral  ############## TWh
    filter={"tipo": "carbon_mineral", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    carbon_mineral = db_to_df(rd=rd).to_dict(orient='records')[0]
    carbon_mineral["topic"]    = "resultados"
    carbon_mineral["bloque"]   = "industria"
    carbon_mineral["tipo"]     = "carbon_mineral"
    carbon_mineral["unidad"]   = "TWh"

    ##########   gas_natural  ############## TWh
    filter={"tipo": "gas_natural", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    gas_natural = db_to_df(rd=rd).to_dict(orient='records')[0]
    gas_natural["topic"]    = "resultados"
    gas_natural["bloque"]   = "industria"
    gas_natural["tipo"]     = "gas_natural"
    gas_natural["unidad"]   = "TWh"


    ##########   lena  ############## TWh
    filter={"tipo": "lena", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    lena = db_to_df(rd=rd).to_dict(orient='records')[0]
    lena["topic"]    = "resultados"
    lena["bloque"]   = "industria"
    lena["tipo"]     = "lena"
    lena["unidad"]   = "TWh"


    ##########   petroleo  ############## TWh
    filter={"tipo": "petroleo", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    petroleo = db_to_df(rd=rd).to_dict(orient='records')[0]
    petroleo["topic"]    = "resultados"
    petroleo["bloque"]   = "industria"
    petroleo["tipo"]     = "petroleo"
    petroleo["unidad"]   = "TWh"


    ##########   residuos  ############## TWh
    filter={"tipo": "residuos", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    residuos = db_to_df(rd=rd).to_dict(orient='records')[0]
    residuos["topic"]    = "resultados"
    residuos["bloque"]   = "industria"
    residuos["tipo"]     = "residuos"
    residuos["unidad"]   = "TWh"


    ##########   gasolina  ############## TWh
    filter={"tipo": "gasolina", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    gasolina = db_to_df(rd=rd).to_dict(orient='records')[0]
    gasolina["topic"]    = "resultados"
    gasolina["bloque"]   = "industria"
    gasolina["tipo"]     = "gasolina"
    gasolina["unidad"]   = "TWh"


    ##########   diesel  ############## TWh
    filter={"tipo": "diesel", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    diesel = db_to_df(rd=rd).to_dict(orient='records')[0]
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "industria"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "TWh"


    ##########   carbon_de_lena  ############## TWh
    filter={"tipo": "carbon_de_lena", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    carbon_de_lena = db_to_df(rd=rd).to_dict(orient='records')[0]
    carbon_de_lena["topic"]    = "resultados"
    carbon_de_lena["bloque"]   = "industria"
    carbon_de_lena["tipo"]     = "carbon_de_lena"
    carbon_de_lena["unidad"]   = "TWh"


    ##########   coque  ############## TWh
    filter={"tipo": "coque", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    coque = db_to_df(rd=rd).to_dict(orient='records')[0]
    coque["topic"]    = "resultados"
    coque["bloque"]   = "industria"
    coque["tipo"]     = "coque"
    coque["unidad"]   = "TWh"


    ##########   fuel_oil  ############## TWh
    filter={"tipo": "fuel_oil", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    fuel_oil = db_to_df(rd=rd).to_dict(orient='records')[0]
    fuel_oil["topic"]    = "resultados"
    fuel_oil["bloque"]   = "industria"
    fuel_oil["tipo"]     = "fuel_oil"
    fuel_oil["unidad"]   = "TWh"


    ##########   glp  ############## TWh
    filter={"tipo": "glp", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    glp = db_to_df(rd=rd).to_dict(orient='records')[0]
    glp["topic"]    = "resultados"
    glp["bloque"]   = "industria"
    glp["tipo"]     = "glp"
    glp["unidad"]   = "TWh"


    ##########   queroseno  ############## TWh
    filter={"tipo": "queroseno", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    queroseno = db_to_df(rd=rd).to_dict(orient='records')[0]
    queroseno["topic"]    = "resultados"
    queroseno["bloque"]   = "industria"
    queroseno["tipo"]     = "queroseno"
    queroseno["unidad"]   = "TWh"


    ##########   electricidad_sin  ############## TWh
    filter={"tipo": "electricidad_sin", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    electricidad_sin = db_to_df(rd=rd).to_dict(orient='records')[0]
    electricidad_sin["topic"]    = "resultados"
    electricidad_sin["bloque"]   = "industria"
    electricidad_sin["tipo"]     = "electricidad_sin"
    electricidad_sin["unidad"]   = "TWh"


    ##########   hidrogeno_verde  ############## TWh
    filter={"tipo": "hidrogeno_verde", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    hidrogeno_verde = db_to_df(rd=rd).to_dict(orient='records')[0]
    hidrogeno_verde["topic"]    = "resultados"
    hidrogeno_verde["bloque"]   = "industria"
    hidrogeno_verde["tipo"]     = "hidrogeno_verde"
    hidrogeno_verde["unidad"]   = "TWh"


    ##########   hidrogeno_azul  ############## TWh
    filter={"tipo": "hidrogeno_azul", 'medida_1': medida_ind_1, 'medida_2': medida_ind_2, 'medida_3': medida_ind_3, 'medida_4': medida_ind_4}
    rd = downloader(db=db, topic='balance_total_de_la_energia_requerida',
        model=models.INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida,
        **filter)
    
    hidrogeno_azul = db_to_df(rd=rd).to_dict(orient='records')[0]
    hidrogeno_azul["topic"]    = "resultados"
    hidrogeno_azul["bloque"]   = "industria"
    hidrogeno_azul["tipo"]     = "hidrogeno_azul"
    hidrogeno_azul["unidad"]   = "TWh"
    

    resultado = {"resultados": [
        bagazo,
        carbon_mineral,
        gas_natural,
        lena,
        petroleo,
        residuos,
        gasolina,
        diesel,
        carbon_de_lena,
        coque,
        fuel_oil,
        glp,
        queroseno,
        electricidad_sin,
        hidrogeno_verde,
        hidrogeno_azul
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
