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

    keys = data.__dict__.keys()
    jdata = jsonable_encoder(data)
    
    for key in keys:
        match key:
            case 'demanda_iluminacion':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_iluminacion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'porcentaje_tecnologia_para_iluminacion':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_tecnologia_iluminacion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo', 'trayectoria']
                )
            
            case 'demanda_total_por_refrigeracion':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_total_por_refrigeracion, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'porcentaje_de_neveras_mas_eficientes':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_neveras_mas_eficientes, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'demanda_coccion_con_gas_natural':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_coccion_con_gas_natural, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'porcentaje_de_estufas_con_eficiencia_mejorada':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_estufas_eficiencia_mejorada, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )
            
            case 'demanda_para_coccion_con_glp':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_para_coccion_con_glp, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'reduccion_total_de_la_demanda_de_energia_electrica':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_reduccion_demanda_electrica, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo', 'trayectoria']
                )
            
            case 'potencia_instalada_para_autogeneracion_solar_fotovoltaica':
                loader(
                    db=db,
                    model=models.EDIF_RES_ILU_REF_COC_OTR_ST_pot_inst_autogeneracion_fotovolt, 
                    obj_in=jdata[key], 
                    filters=['topic', 'trayectoria']
                )

            case _:
                logger.error(f'[ERROR] {key} is invalid')

    return jdata


@router.get('/supuestos_trayectoria/{module}')
def read_ST_module(
    module: schemas.ST_name,
    trayectoria: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'trayectoria' : trayectoria}

    match module:        
        case schemas.ST_name.demanda_iluminacion:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_iluminacion,
                topic='demanda_iluminacion',
                **filter
                )
        
        case schemas.ST_name.porcentaje_tecnologia_para_iluminacion:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_tecnologia_iluminacion,
                topic='porcentaje_tecnologia_para_iluminacion',
                **filter
                )
        
        case schemas.ST_name.demanda_total_por_refrigeracion:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_total_por_refrigeracion,
                topic='demanda_total_por_refrigeracion',
                **filter
                )
        
        case schemas.ST_name.porcentaje_de_neveras_mas_eficientes:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_neveras_mas_eficientes,
                topic='porcentaje_de_neveras_mas_eficientes',
                **filter
                )
        
        case schemas.ST_name.demanda_coccion_con_gas_natural:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_coccion_con_gas_natural,
                topic='demanda_coccion_con_gas_natural',
                **filter
                )
        
        case schemas.ST_name.porcentaje_de_estufas_con_eficiencia_mejorada:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_estufas_eficiencia_mejorada,
                topic='porcentaje_de_estufas_con_eficiencia_mejorada',
                **filter
                )
        
        case schemas.ST_name.demanda_para_coccion_con_glp:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_para_coccion_con_glp,
                topic='demanda_para_coccion_con_glp',
                **filter
                )
        
        case schemas.ST_name.reduccion_total_de_la_demanda_de_energia_electrica:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_reduccion_demanda_electrica,
                topic='reduccion_total_de_la_demanda_de_energia_electrica',
                **filter
                )
        
        case schemas.ST_name.potencia_instalada_para_autogeneracion_solar_fotovoltaica:
            rd = downloader(
                db=db, 
                model=models.EDIF_RES_ILU_REF_COC_OTR_ST_pot_inst_autogeneracion_fotovolt,
                topic='potencia_instalada_para_autogeneracion_solar_fotovoltaica',
                **filter
                )

        case _:
            logger.error(f'[ERROR] {module} is invalid')
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_ST, status_code=status.HTTP_200_OK)
def delete_ST(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_iluminacion)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_tecnologia_iluminacion)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_total_por_refrigeracion)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_neveras_mas_eficientes)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_coccion_con_gas_natural)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_estufas_eficiencia_mejorada)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_demanda_para_coccion_con_glp)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_reduccion_demanda_electrica)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_ST_pot_inst_autogeneracion_fotovolt)


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
            case 'demanda_energia_electrica_por_uso':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_energia_electrica_por_uso, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                
            case 'demanda_gas_natural_por_uso':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_gas_natural_por_uso, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                
            case 'demanda_glp_por_uso':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_glp_por_uso, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                
            case 'tenencia_por_uso_energia_electrica':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_energia_electrica, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                
            case 'tenencia_por_uso_gas_natural':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_gas_natural, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                
            case 'tenencia_por_uso_glp':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_glp, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                
            case 'numero_de_bombillos_por_hogar':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_numero_de_bombillos_por_hogar, 
                    obj_in=jdata[key], 
                    filters=['topic', 'bloque', 'tipo']
                )
                
            case 'porcentaje_de_tenencia_refrigeradores':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_refrigeradores, 
                    obj_in=jdata[key], 
                    filters=['topic', 'tipo']
                )
                
            case 'horas_utiles_de_operacion_de_la_autogeneracion_solar_fotovoltaica':
                loader(
                    db=db, 
                    model=models.EDIF_RES_ILU_REF_COC_OTR_SF_hr_ope_autogeneracion_fotovoltaica, 
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
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""
    
    d = {
        'demanda_energia_electrica_por_uso'     : models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_energia_electrica_por_uso,
        'demanda_gas_natural_por_uso'           : models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_gas_natural_por_uso,
        'demanda_glp_por_uso'                   : models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_glp_por_uso,
        'tenencia_por_uso_energia_electrica'    : models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_energia_electrica,
        'tenencia_por_uso_gas_natural'          : models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_gas_natural,
        'tenencia_por_uso_glp'                  : models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_glp,
        'numero_de_bombillos_por_hogar'         : models.EDIF_RES_ILU_REF_COC_OTR_SF_numero_de_bombillos_por_hogar,
        'porcentaje_de_tenencia_refrigeradores' : models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_refrigeradores,
        'horas_utiles_de_operacion_de_la_autogeneracion_solar_fotovoltaica' : models.EDIF_RES_ILU_REF_COC_OTR_SF_hr_ope_autogeneracion_fotovoltaica
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

    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_energia_electrica_por_uso)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_gas_natural_por_uso)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_demanda_glp_por_uso)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_energia_electrica)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_gas_natural)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_glp)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_numero_de_bombillos_por_hogar)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_refrigeradores)
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SF_hr_ope_autogeneracion_fotovoltaica)

    return {'msg': 'Deleted SF successfully'}

####################################################################################
#######                           Metodologia                                #######
####################################################################################

@router.post(
        path='/metodologia', 
        response_model=schemas.METODOLOGIA, 
        status_code=status.HTTP_201_CREATED)
def create_metodologia_generacion_solar_fotovoltaica(
    data: schemas.METODOLOGIA, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.EDIF_RES_ILU_REF_COC_OTR_Metod_generacion_solar_fotovoltaica, 
        obj_in=jdata['metodologia'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2', 'medida_3']
    )
    return jdata


@router.get('/metodologia')
def read_metodologia(
    medida_edi_res_irco_1: schemas.Trayectoria,
    medida_edi_res_irco_2: schemas.Trayectoria,
    medida_edi_res_irco_3: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_edi_res_irco_1, 'medida_2' : medida_edi_res_irco_2, 'medida_3' : medida_edi_res_irco_3}

    rd = downloader(
            db=db, 
            model=models.EDIF_RES_ILU_REF_COC_OTR_Metod_generacion_solar_fotovoltaica,
            topic='generacion_solar_fotovoltaica',
            **filter
            )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete('/metodologia', status_code=status.HTTP_200_OK)
def delete_Metodologia(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_Metod_generacion_solar_fotovoltaica)

    return {'msg': 'Deleted Metodologia successfully'}


####################################################################################
#######                               Salidas                                #######
####################################################################################

@router.post(
        path='/salidas', 
        response_model=schemas.SALIDAS, 
        status_code=status.HTTP_201_CREATED)
def create_salidas(
    data: schemas.SALIDAS, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS, 
        obj_in=jdata['salidas'], 
        filters=['topic', 'bloque', 'tipo', 'medida_1', 'medida_2', 'medida_3']
    )
    return jdata


@router.get('/salidas')
def read_salidas_module(
    medida_edi_res_irco_1: schemas.Trayectoria,
    medida_edi_res_irco_2: schemas.Trayectoria,
    medida_edi_res_irco_3: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_edi_res_irco_1, 'medida_2' : medida_edi_res_irco_2, 'medida_3' : medida_edi_res_irco_3}

    rd = downloader(
        db=db, 
        model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS,
        topic='energia_producida_y_requerida',
        **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_SALIDAS, status_code=status.HTTP_200_OK)
def delete_Salidas(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_SALIDAS)

    return {'msg': 'Deleted Salidas successfully'}

####################################################################################
#######                               Emisiones                              #######
####################################################################################

@router.post(
        path='/emisiones', 
        response_model=schemas.EMISIONES, 
        status_code=status.HTTP_201_CREATED)
def create_emisiones(
    data: schemas.EMISIONES, 
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """CREATE"""

    jdata = jsonable_encoder(data)
    loader(
        db=db, 
        model=models.EDIF_RES_ILU_REF_COC_OTR_EMISIONES, 
        obj_in=jdata['emisiones'], 
        filters=['topic', 'tipo', 'medida_1', 'medida_2', 'medida_3']
    )
    return jdata


@router.get('/emisiones')
def read_Emisiones_module(
    medida_edi_res_irco_1: schemas.Trayectoria,
    medida_edi_res_irco_2: schemas.Trayectoria,
    medida_edi_res_irco_3: schemas.Trayectoria,
    db: Session = Depends(deps.get_db), 
    # skip: int = 0, 
    # limit: int = 100,
    # current_user: models_user.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """READ ALL"""

    filter = {'medida_1' : medida_edi_res_irco_1, 'medida_2' : medida_edi_res_irco_2, 'medida_3' : medida_edi_res_irco_3}

    rd = downloader(
            db=db, 
            model=models.EDIF_RES_ILU_REF_COC_OTR_EMISIONES,
            topic='emisiones_de_gases_efecto_invernadero',
            **filter
        )
    
    if DEBUG:
        logger.info(f'Read Data: {jsonable_encoder(rd)}')

    return jsonable_encoder(rd)


@router.delete(URI_EMISIONES, status_code=status.HTTP_200_OK)
def delete_Emisiones(
    db: Session = Depends(deps.get_db),
    # current_user: models_user.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    """DELETE ALL"""
    
    prune(db=db, model=models.EDIF_RES_ILU_REF_COC_OTR_EMISIONES)

    return {'msg': 'Deleted successfully'}
