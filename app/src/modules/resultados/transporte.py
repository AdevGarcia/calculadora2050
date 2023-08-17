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
#######     Evolución de las emisiones del sector Transporte                 #######
####################################################################################

@router.get('/evolucion_de_las_emisiones_del_sector_transporte')
def resultados_evolucion_de_las_emisiones_del_sector_transporte(
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_avi_1: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   transporte_de_pasajeros   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.TRANS_PAS_emisiones_de_gases_efecto_invernadero,
        **filter)
        
    transporte_de_pasajeros = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_de_pasajeros["topic"]    = "resultados"
    transporte_de_pasajeros["bloque"]   = "transporte"
    transporte_de_pasajeros["tipo"]     = "transporte_de_pasajeros"
    transporte_de_pasajeros["unidad"]   = "Mt_CO2_e"
    
    ##########   transporte_de_carga   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='emisiones_de_gases_efecto_invernadero',
        model=models.TRANS_CAR_emisiones_de_gases_efecto_invernadero,
        **filter)
        
    transporte_de_carga = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_de_carga["topic"]    = "resultados"
    transporte_de_carga["bloque"]   = "transporte"
    transporte_de_carga["tipo"]     = "transporte_de_carga"
    transporte_de_carga["unidad"]   = "Mt_CO2_e"

    ##########   transporte_internacional_aviacion   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_avi_1}
    rd = downloader(db=db, topic='aviacion_y_navegacion_internacional',
        model=models.TRANS_AVI_emisiones_aviacion_y_navegacion_internacional,
        **filter)
        
    transporte_internacional_aviacion = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_internacional_aviacion["topic"]    = "resultados"
    transporte_internacional_aviacion["bloque"]   = "transporte"
    transporte_internacional_aviacion["tipo"]     = "transporte_internacional_aviacion"
    transporte_internacional_aviacion["unidad"]   = "Mt_CO2_e"

    ##########   transporte_internacional_navegacion   ############## Mt_CO2_e
    filter={"tipo": "total_co2_e", 'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='emisiones',
        model=models.TRANS_NAV_emisiones,
        **filter)
        
    transporte_internacional_navegacion = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_internacional_navegacion["topic"]    = "resultados"
    transporte_internacional_navegacion["bloque"]   = "transporte"
    transporte_internacional_navegacion["tipo"]     = "transporte_internacional_navegacion"
    transporte_internacional_navegacion["unidad"]   = "Mt_CO2_e"
    

    resultado = {"resultados": [
        transporte_de_pasajeros, 
        transporte_de_carga, 
        transporte_internacional_aviacion, 
        transporte_internacional_navegacion
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de la demanda energetica del sector transporte      #######
#######                      por modo transporte                             #######
####################################################################################
@router.get('/evolucion_demanda_energetica_por_modo_transporte')
def resultados_evolucion_demanda_energetica_por_modo_transporte(
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_avi_1: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   transporte_de_pasajeros   ############## TWh
    filter={"tipo": "total", 'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)
        
    transporte_de_pasajeros = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_de_pasajeros["topic"]    = "resultados"
    transporte_de_pasajeros["bloque"]   = "transporte"
    transporte_de_pasajeros["tipo"]     = "transporte_de_pasajeros"
    transporte_de_pasajeros["unidad"]   = "TWh"
    
    ##########   transporte_de_carga   ############## TWh
    filter={"tipo": "total", 'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
        
    transporte_de_carga = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_de_carga["topic"]    = "resultados"
    transporte_de_carga["bloque"]   = "transporte"
    transporte_de_carga["tipo"]     = "transporte_de_carga"
    transporte_de_carga["unidad"]   = "TWh"
    
    ##########   transporte_internacional_aviacion   ############## TWh
    filter={"tipo": "aviacion_internacional",'medida_1': medida_trans_avi_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_AVI_SALIDAS_energia_requerida,
        **filter)
        
    transporte_internacional_aviacion = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_internacional_aviacion["topic"]    = "resultados"
    transporte_internacional_aviacion["bloque"]   = "transporte"
    transporte_internacional_aviacion["tipo"]     = "transporte_internacional_aviacion"
    transporte_internacional_aviacion["unidad"]   = "TWh"

    ##########   transporte_internacional_navegacion   ############## TWh
    filter={"tipo": "diesel",'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_NAV_SALIDAS_energia_requerida,
        **filter)
        
    transporte_internacional_navegacion = db_to_df(rd=rd).to_dict(orient='records')[0]
    transporte_internacional_navegacion["topic"]    = "resultados"
    transporte_internacional_navegacion["bloque"]   = "transporte"
    transporte_internacional_navegacion["tipo"]     = "transporte_internacional_navegacion"
    transporte_internacional_navegacion["unidad"]   = "TWh"
    

    resultado = {"resultados": [
        transporte_de_pasajeros, 
        transporte_de_carga, 
        transporte_internacional_aviacion, 
        transporte_internacional_navegacion
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)


####################################################################################
#######        Evolución de la demanda energetica del sector transporte      #######
#######                      por combustible                                 #######
####################################################################################
@router.get('/evolucion_demanda_energetica_por_combustible')
def resultados_evolucion_demanda_energetica_por_combustible(
    medida_trans_pas_1: schemas.Trayectoria=1,
    medida_trans_pas_2: schemas.Trayectoria=1,
    medida_trans_car_1: schemas.Trayectoria=1,
    medida_trans_car_2: schemas.Trayectoria=1,
    medida_trans_avi_1: schemas.Trayectoria=1,
    medida_trans_nav_1: schemas.Trayectoria=1,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ"""

    ##########   gasolina   ############## TWh
    filter={"tipo": "gasolina",'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)
    
    df1 = db_to_df(rd=rd)

    filter={"tipo": "gasolina",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
    
    df2 = db_to_df(rd=rd)
        
    gasolina = pd.concat([df1, df2]).sum().to_dict()
    gasolina["topic"]    = "resultados"
    gasolina["bloque"]   = "transporte"
    gasolina["tipo"]     = "gasolina"
    gasolina["unidad"]   = "TWh"
    
    ##########   diesel   ############## TWh
    filter={"tipo": "diesel",'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)
    
    df1 = db_to_df(rd=rd)

    filter={"tipo": "diesel",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
    
    df2 = db_to_df(rd=rd)

    filter={"tipo": "diesel",'medida_1': medida_trans_nav_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_NAV_SALIDAS_energia_requerida,
        **filter)
    
    df3 = db_to_df(rd=rd)
        
    diesel = pd.concat([df1, df2, df3]).sum().to_dict()
    diesel["topic"]    = "resultados"
    diesel["bloque"]   = "transporte"
    diesel["tipo"]     = "diesel"
    diesel["unidad"]   = "TWh"

    ##########   electrico   ############## TWh
    filter={"tipo": "electricidad",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
        
    electrico = db_to_df(rd=rd).to_dict(orient='records')[0]
    electrico["topic"]    = "resultados"
    electrico["bloque"]   = "transporte"
    electrico["tipo"]     = "electrico"
    electrico["unidad"]   = "TWh"

    ##########   gas_natural   ############## TWh
    filter={"tipo": "gas_natural",'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)
    
    df1 = db_to_df(rd=rd)

    filter={"tipo": "gas_gnc",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
    
    df2 = db_to_df(rd=rd)

    filter={"tipo": "gas_gnl",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
    
    df3 = db_to_df(rd=rd)
        
    gas_natural = pd.concat([df1, df2, df3]).sum().to_dict()
    gas_natural["topic"]    = "resultados"
    gas_natural["bloque"]   = "transporte"
    gas_natural["tipo"]     = "gas_natural"
    gas_natural["unidad"]   = "TWh"

    ##########   glp   ############## TWh
    filter={"tipo": "glp",'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)
    
    df1 = db_to_df(rd=rd)

    filter={"tipo": "glp",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
    
    df2 = db_to_df(rd=rd)
        
    glp = pd.concat([df1, df2]).sum().to_dict()
    glp["topic"]    = "resultados"
    glp["bloque"]   = "transporte"
    glp["tipo"]     = "glp"
    glp["unidad"]   = "TWh"

    ##########   queroseno_jet   ############## TWh
    filter={"tipo": "queroseno_jet",'medida_1': medida_trans_pas_1, 'medida_2': medida_trans_pas_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_pasajeros',
        model=models.TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros,
        **filter)
    
    df1 = db_to_df(rd=rd)

    filter={"tipo": "queroseno",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
    
    df2 = db_to_df(rd=rd)

    filter={"tipo": "queroseno",'medida_1': medida_trans_avi_1}
    rd = downloader(db=db, topic='energia_requerida',
        model=models.TRANS_AVI_SALIDAS_energia_requerida,
        **filter)
    
    df3 = db_to_df(rd=rd)
        
    queroseno_jet = pd.concat([df1, df2, df3]).sum().to_dict()
    queroseno_jet["topic"]    = "resultados"
    queroseno_jet["bloque"]   = "transporte"
    queroseno_jet["tipo"]     = "queroseno_jet"
    queroseno_jet["unidad"]   = "TWh"

    ##########   vehiculo_hidrogeno   ############## TWh
    filter={"tipo": "hidrogeno",'medida_1': medida_trans_car_1, 'medida_2': medida_trans_car_2}
    rd = downloader(db=db, topic='energia_requerida_transporte_de_carretera',
        model=models.TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera,
        **filter)
        
    vehiculo_hidrogeno = db_to_df(rd=rd).to_dict(orient='records')[0]
    vehiculo_hidrogeno["topic"]    = "resultados"
    vehiculo_hidrogeno["bloque"]   = "transporte"
    vehiculo_hidrogeno["tipo"]     = "vehiculo_hidrogeno"
    vehiculo_hidrogeno["unidad"]   = "TWh"
    

    resultado = {"resultados": [
        gasolina, 
        diesel, 
        electrico, 
        gas_natural,
        glp,
        queroseno_jet,
        vehiculo_hidrogeno
        ]}

    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(resultado)}')

    return jsonable_encoder(resultado)
 