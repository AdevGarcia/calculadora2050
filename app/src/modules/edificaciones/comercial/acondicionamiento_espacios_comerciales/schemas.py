from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Edificaciones Comerciales Acondicionamiento de espacios comerciales

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    demanda_total_energia_para_acondicionamiento_de_espacios_diseno_y_eficiencia = 'demanda_total_energia_para_acondicionamiento_de_espacios_diseno_y_eficiencia'
    demanda_total_energia_para_acondicionamiento_de_espacios_eficiencia          = 'demanda_total_energia_para_acondicionamiento_de_espacios_eficiencia'


class EDIF_COM_ACOND_ST_demanda_total_energia_para_acondicionamiento_de_espacios_diseno_y_eficiencia(BaseModel):
    """Supuestos de Trayectoria demanda_total_energia_para_acondicionamiento_de_espacios_diseno_y_eficiencia
    """

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


class EDIF_COM_ACOND_ST_demanda_total_energia_para_acondicionamiento_de_espacios_eficiencia(BaseModel):
    """Supuestos de Trayectoria demanda_total_energia_para_acondicionamiento_de_espacios_eficiencia
    """

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


class SUPUESTOS_TRAYECTORIA(BaseModel):
    """Supuestos de trayectoria con todos los topics
    """
    
    demanda_total_energia_para_acondicionamiento_de_espacios_diseno_y_eficiencia : list[EDIF_COM_ACOND_ST_demanda_total_energia_para_acondicionamiento_de_espacios_diseno_y_eficiencia]
    demanda_total_energia_para_acondicionamiento_de_espacios_eficiencia          : list[EDIF_COM_ACOND_ST_demanda_total_energia_para_acondicionamiento_de_espacios_eficiencia]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################



# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    energia_producida_y_requerida = 'energia_producida_y_requerida'

class EDIF_COM_ACOND_SALIDAS(BaseModel):
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
    
    salidas : list[EDIF_COM_ACOND_SALIDAS]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class EDIF_COM_ACOND_EMISIONES(BaseModel):
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
    emisiones : list[EDIF_COM_ACOND_EMISIONES]

    class ConfigDict:
        from_attributes = True
