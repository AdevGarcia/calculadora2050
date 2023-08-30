from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
import logging

from app.src.crud.base import loader, prune, downloader, downloader_batch
from . import models, schemas
from db import deps

from app.src.modules.user import models as models_user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URI_ST = '/supuestos_trayectoria'
URI_SF = '/supuestos_fijos'
URI_SALIDAS   = '/salidas'
URI_EMISIONES = '/emisiones'

SCHEMAS_ST  = schemas.SUPUESTOS_TRAYECTORIA
SCHEMAS_SF  = schemas.SUPUESTOS_FIJOS
SCHEMAS_SALIDAS    = schemas.SALIDAS
SCHEMAS_EMISIONES  = schemas.EMISIONES

DEBUG = False

router = APIRouter()


####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################
@router.post(URI_ST, response_model=SCHEMAS_ST, status_code=status.HTTP_201_CREATED)
def create_ST(
    data: SCHEMAS_ST, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'capacidad_de_generacion':
                loader(
                    db=db,
                    model=models.ELECT_Electricidad_ST_capacidad_de_generacion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
                    
            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get('/supuestos_trayectoria')
def read_ST_module(
    trayectoria: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'trayectoria' : trayectoria}

    rd = downloader(
        db=db, 
        model=models.ELECT_Electricidad_ST_capacidad_de_generacion,
        topic='capacidad_de_generacion',
        skip=skip, limit=limit,
        **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_ST, status_code=status.HTTP_200_OK)
def delete_ST(
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ELECT_Electricidad_ST_capacidad_de_generacion)

    return {'msg': 'Deleted successfully'}


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################
@router.post(URI_SF, response_model=SCHEMAS_SF, status_code=status.HTTP_201_CREATED)
def create_SF(
    data: SCHEMAS_SF, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'horas_de_operacion_ano':
                loader(
                    db=db, 
                    model=models.ELECT_Electricidad_SF_horas_de_operacion_ano, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'unidad']
                )
                    
            case 'factor_de_carga':
                loader(
                    db=db, 
                    model=models.ELECT_Electricidad_SF_factor_de_carga, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )

            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get(URI_SF, response_model=SCHEMAS_SF)
def read_SF(
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""
    
    d = {
        'horas_de_operacion_ano' : models.ELECT_Electricidad_SF_horas_de_operacion_ano,
        'factor_de_carga'        : models.ELECT_Electricidad_SF_factor_de_carga,
        }
    
    rd = downloader_batch(db=db, skip=skip, limit=limit, **d)
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SF, status_code=status.HTTP_200_OK)
def delete_SF(
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ELECT_Electricidad_SF_horas_de_operacion_ano)
    prune(db=db, model=models.ELECT_Electricidad_SF_factor_de_carga)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas_combustibles_fosiles',
        response_model=schemas.ELECT_Electricidad_SALIDAS_combustibles_fosiles, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_combustibels_fosiles(
    data: schemas.ELECT_Electricidad_SALIDAS_combustibles_fosiles, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles, 
        obj_in=jdata['salidas_combustibles_fosiles'], 
        filters=['topic', 'tipo', 'medida_1']
    )
    return jdata


@router.post(
        path='/salidas_energias_renovables_no_convencionales',
        response_model=schemas.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_energias_renovables_no_convencionales(
    data: schemas.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales, 
        obj_in=jdata['salidas_energias_renovables_no_convencionales'], 
        filters=['topic', 'tipo', 'medida_1']
    )
    return jdata


@router.post(
        path='/salidas_energia_demandada',
        response_model=schemas.ELECT_Electricidad_SALIDAS_energia_demandada, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_energia_demandada(
    data: schemas.ELECT_Electricidad_SALIDAS_energia_demandada, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.ELECT_Electricidad_SALIDAS_energia_demandada, 
        obj_in=jdata['salidas_energia_demandada'], 
        filters=['topic', 'tipo', 'medida_1']
    )
    return jdata


@router.post(
        path='/salidas_balance',
        response_model=schemas.ELECT_Electricidad_SALIDAS_balance, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_balance(
    data: schemas.ELECT_Electricidad_SALIDAS_balance, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.ELECT_Electricidad_SALIDAS_balance, 
        obj_in=jdata['salidas_balance'], 
        filters=['topic', 'tipo', 'medida_1']
    )
    return jdata


@router.get('/salidas/{module}')
def read_salidas_module(
    module: schemas.Salidas_name,
    medida_elect_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_elect_1}

    match module:
        case schemas.Salidas_name.salidas_combustibles_fosiles:
            rd = downloader(
                db=db, 
                model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles,
                topic='combustibels_fosiles',
                skip=skip, limit=limit,
                **filter
                )
        
        case schemas.Salidas_name.salidas_energias_renovables_no_convencionales:
            rd = downloader(
                db=db, 
                model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales,
                topic='energias_renovables_no_convencionales',
                skip=skip, limit=limit,
                **filter
                )
        
        case schemas.Salidas_name.salidas_energia_demandada:
            rd = downloader(
                db=db, 
                model=models.ELECT_Electricidad_SALIDAS_energia_demandada,
                topic='energia_demandada',
                skip=skip, limit=limit,
                **filter
                )
        
        case schemas.Salidas_name.salidas_balance:
            rd = downloader(
                db=db, 
                model=models.ELECT_Electricidad_SALIDAS_balance,
                topic='balance',
                skip=skip, limit=limit,
                **filter
                )

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SALIDAS, status_code=status.HTTP_200_OK)
def delete_Salidas(
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ELECT_Electricidad_SALIDAS_combustibles_fosiles)
    prune(db=db, model=models.ELECT_Electricidad_SALIDAS_ener_renov_no_convencionales)
    prune(db=db, model=models.ELECT_Electricidad_SALIDAS_energia_demandada)
    prune(db=db, model=models.ELECT_Electricidad_SALIDAS_balance)

    return {'msg': 'Deleted Salidas successfully'}

####################################################################################
#######                               Emisiones                              #######
####################################################################################

@router.post(
        path='/emisiones_combustibles_fosiles', 
        response_model=schemas.ELECT_Electricidad_EMISIONES_combustibles_fosiles, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones_combustibles_fosiles(
    data: schemas.ELECT_Electricidad_EMISIONES_combustibles_fosiles, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles, 
        obj_in=jdata['emisiones_combustibles_fosiles'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1']
    )

    return jdata


@router.post(
        path='/emisiones_energias_renovables_no_convencionales', 
        response_model=schemas.ELECT_Electricidad_EMISIONES_ener_renov_no_convencionales, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones_energias_renovables_no_convencionales(
    data: schemas.ELECT_Electricidad_EMISIONES_ener_renov_no_convencionales, 
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.ELECT_Electricidad_EMISIONES_ener_renov_no_convencionales, 
        obj_in=jdata['emisiones_energias_renovables_no_convencionales'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1']
    )

    return jdata


@router.get('/emisiones/{module}')
def read_emisiones_module(
    module: schemas.Emisiones_name,
    medida_elect_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_elect_1}

    match module:
        case schemas.Emisiones_name.emisiones_combustibles_fosiles:
            rd = downloader(
                db=db, 
                model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles,
                topic='emisiones_de_gases_de_efecto_invernadero_gei',
                skip=skip, limit=limit,
                **filter
                )
        
        case schemas.Emisiones_name.emisiones_energias_renovables_no_convencionales:
            rd = downloader(
                db=db, 
                model=models.ELECT_Electricidad_EMISIONES_ener_renov_no_convencionales,
                topic='emisiones_de_gases_de_efecto_invernadero_gei',
                skip=skip, limit=limit,
                **filter
                )

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_EMISIONES, status_code=status.HTTP_200_OK)
def delete_Emisiones(
    db: Session = Depends(deps.get_db),
    current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ELECT_Electricidad_EMISIONES_combustibles_fosiles)
    prune(db=db, model=models.ELECT_Electricidad_EMISIONES_ener_renov_no_convencionales)

    return {'msg': 'Deleted successfully'}
