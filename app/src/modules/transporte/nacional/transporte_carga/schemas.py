from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano  = 'uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano'
    distancia_modo_ferreo                                                     = 'distancia_modo_ferreo'
    distancia_para_el_transporte_carretero_transporte_de_carga_interurbano    = 'distancia_para_el_transporte_carretero_transporte_de_carga_interurbano'
    uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano = 'uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano'
    uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano   = 'uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano'
    carga_sustituida_por_modo_transporte_de_carga_interurbano                 = 'carga_sustituida_por_modo_transporte_de_carga_interurbano'
    distribucion_por_tecnologia_transporte_de_carga_urbano                    = 'distribucion_por_tecnologia_transporte_de_carga_urbano'
    distribucion_por_tecnologia_transporte_de_carga_interurbano               = 'distribucion_por_tecnologia_transporte_de_carga_interurbano'


class TRANS_CAR_ST_uso_ener_trans_ferreo_transp_carga_interurbano(BaseModel):
    """Supuestos de Trayectoria uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano
    """

    topic       : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_ST_distancia_modo_ferreo(BaseModel):
    """Supuestos de Trayectoria distancia_modo_ferreo"""
    
    topic       : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_ST_dist_trans_carretero_transp_carga_interurbano(BaseModel):
    """Supuestos de Trayectoria distancia_para_el_transporte_carretero_transporte_de_carga_interurbano"""
    
    topic       : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_ST_uso_ener_trans_fluvial_transp_carga_interurbano(BaseModel):
    """Supuestos de Trayectoria uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano"""
    
    topic       : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_ST_uso_de_ener_trans_aereo_trans_carga_interurbano(BaseModel):
    """Supuestos de Trayectoria uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano"""
    
    topic       : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_ST_carga_sustituida_modo_trans_carga_interurbano(BaseModel):
    """Supuestos de Trayectoria carga_sustituida_por_modo_transporte_de_carga_interurbano"""
    
    topic       : str
    tipo        : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_ST_distr_tecnologia_transporte_carga_urbano(BaseModel):
    """Supuestos de Trayectoria distribucion_por_tecnologia_transporte_de_carga_urbano"""
    
    topic       : str
    tipo        : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_ST_dist_tecn_transporte_carga_interurbano(BaseModel):
    """Supuestos de Trayectoria distribucion_por_tecnologia_transporte_de_carga_interurbano"""
    
    topic       : str
    bloque      : str
    tipo        : str
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class SUPUESTOS_TRAYECTORIA(BaseModel):
    """Supuestos de trayectoria con todos los topics
    """
    
    uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano  : list[TRANS_CAR_ST_uso_ener_trans_ferreo_transp_carga_interurbano]
    distancia_modo_ferreo                                                     : list[TRANS_CAR_ST_distancia_modo_ferreo]
    distancia_para_el_transporte_carretero_transporte_de_carga_interurbano    : list[TRANS_CAR_ST_dist_trans_carretero_transp_carga_interurbano]
    uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano : list[TRANS_CAR_ST_uso_ener_trans_fluvial_transp_carga_interurbano]
    uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano   : list[TRANS_CAR_ST_uso_de_ener_trans_aereo_trans_carga_interurbano]
    carga_sustituida_por_modo_transporte_de_carga_interurbano                 : list[TRANS_CAR_ST_carga_sustituida_modo_trans_carga_interurbano]
    distribucion_por_tecnologia_transporte_de_carga_urbano                    : list[TRANS_CAR_ST_distr_tecnologia_transporte_carga_urbano]
    distribucion_por_tecnologia_transporte_de_carga_interurbano               : list[TRANS_CAR_ST_dist_tecn_transporte_carga_interurbano]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class TRANS_CAR_SF_factor_de_actividad_transporte_de_carga_urbano(BaseModel):
    """Supuestos Fijos factor_de_actividad_transporte_de_carga_urbano
    """

    topic       : str
    tipo        : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_SF_rendimiento_modo_carretero(BaseModel):
    """Supuestos Fijos rendimiento_modo_carretero
    """

    topic       : str
    bloque      : str
    tipo        : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_SF_distancia_tipica_por_modo(BaseModel):
    """Supuestos Fijos distancia_tipica_por_modo"""

    topic       : str
    tipo        : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_SF_vida_util(BaseModel):
    """Supuestos Fijos vida_util"""

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class TRANS_CAR_SF_numero_de_vehiculos_transporte_de_carga_urbano(BaseModel):
    """Supuestos Fijos numero_de_vehiculos_transporte_de_carga_urbano"""

    topic       : str
    tipo        : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class TRANS_CAR_SF_num_vehiculos_transporte_carga_interurbano(BaseModel):
    """Supuestos Fijos numero_de_vehiculos_transporte_de_carga_interurbano"""

    topic       : str
    tipo        : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """

    factor_de_actividad_transporte_de_carga_urbano      : list[TRANS_CAR_SF_factor_de_actividad_transporte_de_carga_urbano]
    rendimiento_modo_carretero                          : list[TRANS_CAR_SF_rendimiento_modo_carretero]
    distancia_tipica_por_modo                           : list[TRANS_CAR_SF_distancia_tipica_por_modo]
    vida_util                                           : list[TRANS_CAR_SF_vida_util]
    numero_de_vehiculos_transporte_de_carga_urbano      : list[TRANS_CAR_SF_numero_de_vehiculos_transporte_de_carga_urbano]
    numero_de_vehiculos_transporte_de_carga_interurbano : list[TRANS_CAR_SF_num_vehiculos_transporte_carga_interurbano]
    
    class ConfigDict:
        from_attributes = True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salidas = 'salidas'


class TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera(BaseModel):
    """Salidas - energia_requerida_transporte_de_carretera
    """

    topic       : str
    tipo        : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str
    medida_1    : float
    medida_2    : float


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salidas : list[TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class TRANS_CAR_emisiones_de_gases_efecto_invernadero(BaseModel):
    """Emisiones - emisiones_de_gases_efecto_invernadero
    """

    topic       : str
    tipo        : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str
    medida_1    : float
    medida_2    : float


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones : list[TRANS_CAR_emisiones_de_gases_efecto_invernadero]

    class ConfigDict:
        from_attributes = True
