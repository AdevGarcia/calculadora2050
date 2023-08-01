from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Edificaciones Residencial Acondicionamiento Espacios Residenciales

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    demanda_para_acondicionamiento_de_espacios_diseno_y_eficiencia = 'demanda_para_acondicionamiento_de_espacios_diseno_y_eficiencia'
    demanda_para_acondicionamiento_de_espacios_solo_eficiencia  = 'demanda_para_acondicionamiento_de_espacios_solo_eficiencia'
    implementacion  = 'implementacion'
    equipos_para_el_acondicionamiento_de_espacios_de_alta_eficiencia = 'equipos_para_el_acondicionamiento_de_espacios_de_alta_eficiencia'


class EDIF_RES_ACOND_ST_demanda_para_acondicionamiento_de_espacios_diseno_y_eficiencia(BaseModel):
    """Supuestos de Trayectoria demanda_para_acondicionamiento_de_espacios_diseno_y_eficiencia
    """

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


class EDIF_RES_ACOND_ST_demanda_para_acondicionamiento_de_espacios_solo_eficiencia(BaseModel):
    """Supuestos de Trayectoria demanda_para_acondicionamiento_de_espacios_solo_eficiencia
    """

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


class EDIF_RES_ACOND_ST_implementacion(BaseModel):
    """Supuestos de Trayectoria implementacion
    """

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


class EDIF_RES_ACOND_ST_equipos_para_el_acondicionamiento_de_espacios_de_alta_eficiencia(BaseModel):
    """Supuestos de Trayectoria equipos_para_el_acondicionamiento_de_espacios_de_alta_eficiencia
    """

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
    
    demanda_para_acondicionamiento_de_espacios_diseno_y_eficiencia   : list[EDIF_RES_ACOND_ST_demanda_para_acondicionamiento_de_espacios_diseno_y_eficiencia]
    demanda_para_acondicionamiento_de_espacios_solo_eficiencia       : list[EDIF_RES_ACOND_ST_demanda_para_acondicionamiento_de_espacios_solo_eficiencia]
    implementacion                                                   : list[EDIF_RES_ACOND_ST_implementacion]
    equipos_para_el_acondicionamiento_de_espacios_de_alta_eficiencia : list[EDIF_RES_ACOND_ST_equipos_para_el_acondicionamiento_de_espacios_de_alta_eficiencia]

    class Config:
        orm_mode : True

####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class EDIF_RES_ACOND_SF_tenencia(BaseModel):
    """Supuestos Fijos tenencia
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


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """
    
    tenencia : list[EDIF_RES_ACOND_SF_tenencia]
    
    class Config:
        orm_mode : True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    energia_producida_y_requerida = 'energia_producida_y_requerida'


class EDIF_RES_ACOND_SALIDAS(BaseModel):
    """energia_producida_y_requerida"""

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


class SALIDAS(BaseModel):
    """Salidas"""
    
    salidas : list[EDIF_RES_ACOND_SALIDAS]

    class Config:
        orm_mode : True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class EDIF_RES_ACOND_EMISIONES(BaseModel):
    """emisiones_de_gases_efecto_invernadero"""

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


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones : list[EDIF_RES_ACOND_EMISIONES]

    class Config:
        orm_mode : True
    