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
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db,
        model=models.ENER_CombFosil_ST_eficiencia_energetica_en_la_refinacion_de_crudo, 
        obj_in=jdata['eficiencia_energetica_en_la_refinacion_de_crudo'], 
        filters=['topic', 'trayectoria']
    )

    return jdata


@router.get('/supuestos_trayectoria')
def read_ST_module(
    trayectoria: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'trayectoria' : trayectoria}

    rd = downloader(
        db=db, 
        model=models.ENER_CombFosil_ST_eficiencia_energetica_en_la_refinacion_de_crudo,
        topic='eficiencia_energetica_en_la_refinacion_de_crudo',
        **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_ST, status_code=status.HTTP_200_OK)
def delete_ST(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ENER_CombFosil_ST_eficiencia_energetica_en_la_refinacion_de_crudo)

    return {'msg': 'Deleted successfully'}


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################
@router.post(URI_SF, response_model=SCHEMAS_SF, status_code=status.HTTP_201_CREATED)
def create_SF(
    data: SCHEMAS_SF, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'produccion_de_hidrocarburos':
                loader(
                    db=db, 
                    model=models.ENER_CombFosil_SF_produccion_de_hidrocarburos, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                    
            case 'produccion_de_carbon':
                loader(
                    db=db, 
                    model=models.ENER_CombFosil_SF_produccion_de_carbon, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                
            case 'factores_de_emision_carbon':
                loader(
                    db=db, 
                    model=models.ENER_CombFosil_SF_factores_de_emision_carbon, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'unidad']
                )
                
            case 'no_de_pozos':
                loader(
                    db=db, 
                    model=models.ENER_CombFosil_SF_no_de_pozos, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'fuente', 'unidad']
                )
            
            case 'datos_de_la_produccion_de_crudo_en_el_ano_base':
                loader(
                    db=db, 
                    model=models.ENER_CombFosil_SF_datos_de_la_produccion_de_crudo_en_el_ano_base, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'total_crudo', 'unidad']
                )
            
            case 'datos_de_la_produccion_de_gas_natural_en_el_ano_base':
                loader(
                    db=db, 
                    model=models.ENER_CombFosil_SF_datos_de_la_produccion_de_gas_natural_en_el_ano_base, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'total_crudo', 'unidad']
                )
                
            case 'consumo_de_energeticos':
                loader(
                    db=db, 
                    model=models.ENER_CombFosil_SF_consumo_de_energeticos, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'unidad']
                )
            
            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get(URI_SF, response_model=SCHEMAS_SF)
def read_SF(
    db: Session = Depends(deps.get_db), 
    skip: int = 0, 
    limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""
    
    d = {
        'produccion_de_hidrocarburos'                          : models.ENER_CombFosil_SF_produccion_de_hidrocarburos,
        'produccion_de_carbon'                                 : models.ENER_CombFosil_SF_produccion_de_carbon,
        'factores_de_emision_carbon'                           : models.ENER_CombFosil_SF_factores_de_emision_carbon,
        'no_de_pozos'                                          : models.ENER_CombFosil_SF_no_de_pozos,
        'datos_de_la_produccion_de_crudo_en_el_ano_base'       : models.ENER_CombFosil_SF_datos_de_la_produccion_de_crudo_en_el_ano_base,
        'datos_de_la_produccion_de_gas_natural_en_el_ano_base' : models.ENER_CombFosil_SF_datos_de_la_produccion_de_gas_natural_en_el_ano_base,
        'consumo_de_energeticos'                               : models.ENER_CombFosil_SF_consumo_de_energeticos
        }
    
    rd = downloader_batch(db=db, **d)
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SF, status_code=status.HTTP_200_OK)
def delete_SF(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ENER_CombFosil_SF_produccion_de_hidrocarburos)
    prune(db=db, model=models.ENER_CombFosil_SF_produccion_de_carbon)
    prune(db=db, model=models.ENER_CombFosil_SF_factores_de_emision_carbon)
    prune(db=db, model=models.ENER_CombFosil_SF_no_de_pozos)
    prune(db=db, model=models.ENER_CombFosil_SF_datos_de_la_produccion_de_crudo_en_el_ano_base)
    prune(db=db, model=models.ENER_CombFosil_SF_datos_de_la_produccion_de_gas_natural_en_el_ano_base)
    prune(db=db, model=models.ENER_CombFosil_SF_consumo_de_energeticos)

    return {'msg': 'Deleted SF successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas_combustibles_fosiles_producidos', 
        response_model=schemas.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_combustibles_fosiles_producidos(
    data: schemas.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos, 
        obj_in=jdata['salidas_combustibles_fosiles_producidos'], 
        filters=['topic', 'tipo', 'medida_1']
    )

    return jdata


@router.post(
        path='/salidas_consumo_de_combustibles_fosiles_por_el_propio_sector', 
        response_model=schemas.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_consumo_de_combustibles_fosiles_por_el_propio_sector(
    data: schemas.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    
    loader(
        db=db, 
        model=models.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector, 
        obj_in=jdata['salidas_consumo_de_combustibles_fosiles_por_el_propio_sector'], 
        filters=['topic', 'tipo', 'medida_1']
    )

    return jdata


@router.post(
        path='/salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos', 
        response_model=schemas.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos, 
        status_code=status.HTTP_201_CREATED)
def create_salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos(
    data: schemas.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    
    loader(
        db=db, 
        model=models.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos, 
        obj_in=jdata['salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos'], 
        filters=['topic', 'tipo', 'medida_1']
    )

    return jdata


@router.get('/salidas/{module}')
def read_salidas_module(
    module: schemas.Salidas_name,
    medida_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_1}

    match module:
        case schemas.Salidas_name.salidas_combustibles_fosiles_producidos:
            rd = downloader(
                db=db, 
                model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos,
                topic='combustibles_fosiles_producidos',
                **filter
                )
        
        case schemas.Salidas_name.salidas_consumo_de_combustibles_fosiles_por_el_propio_sector:
            rd = downloader(
                db=db, 
                model=models.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector,
                topic='consumo_de_combustibles_fosiles_por_el_propio_sector',
                **filter
                )
        
        case schemas.Salidas_name.salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos:
            rd = downloader(
                db=db, 
                model=models.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos,
                topic='consumo_de_combustibles_fosiles_por_sectores_ajenos',
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
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos)
    prune(db=db, model=models.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector)
    prune(db=db, model=models.ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos)

    return {'msg': 'Deleted Salidas successfully'}

####################################################################################
#######                               Emisiones                              #######
####################################################################################

@router.post(
        path='/emisiones_produccion', 
        response_model=schemas.ENER_CombFosil_EMISIONES_produccion, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones_produccion(
    data: schemas.ENER_CombFosil_EMISIONES_produccion, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    
    loader(
        db=db, 
        model=models.ENER_CombFosil_EMISIONES_produccion, 
        obj_in=jdata['emisiones_produccion'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1']
    )

    return jdata


@router.post(
        path='/emisiones_consumo', 
        response_model=schemas.ENER_CombFosil_EMISIONES_consumo, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones_consumo(
    data: schemas.ENER_CombFosil_EMISIONES_consumo, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    
    loader(
        db=db, 
        model=models.ENER_CombFosil_EMISIONES_consumo, 
        obj_in=jdata['emisiones_consumo'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1']
    )

    return jdata


@router.get('/emisiones/{module}')
def read_emisiones_module(
    module: schemas.Emisiones_name,
    medida_1: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_1}

    match module:
        case schemas.Emisiones_name.emisiones_produccion:
            rd = downloader(
                db=db, 
                model=models.ENER_CombFosil_EMISIONES_produccion,
                topic='emisiones_de_gases_de_efecto_invernadero_gei',
                **filter
                )
        
        case schemas.Emisiones_name.emisiones_consumo:
            rd = downloader(
                db=db, 
                model=models.ENER_CombFosil_EMISIONES_consumo,
                topic='emisiones_de_gases_de_efecto_invernadero_gei',
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
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.ENER_CombFosil_EMISIONES_produccion)
    prune(db=db, model=models.ENER_CombFosil_EMISIONES_consumo)

    return {'msg': 'Deleted successfully'}
