from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Edificaciones Residencial Rural

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    demanda_de_glp  = 'demanda_de_glp'
    demanda_de_lena = 'demanda_de_lena'
    

class EDIF_RES_RURAL_ST_demanda_de_glp(BaseModel):
    """Supuestos de Trayectoria demanda_de_glp
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


class EDIF_RES_RURAL_ST_demanda_de_lena(BaseModel):
    """Supuestos de Trayectoria demanda_de_lena
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


class SUPUESTOS_TRAYECTORIA(BaseModel):
    """Supuestos de trayectoria con todos los topics
    """
    
    demanda_de_glp  : list[EDIF_RES_RURAL_ST_demanda_de_glp]
    demanda_de_lena : list[EDIF_RES_RURAL_ST_demanda_de_lena]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class EDIF_RES_RURAL_SF_demanda_de_energia_electrica(BaseModel):
    """Supuestos Fijos demanda_de_energia_electrica"""

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
    
    demanda_de_energia_electrica     : list[EDIF_RES_RURAL_SF_demanda_de_energia_electrica]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                               Salidas                                #######
####################################################################################

class Salidas_name(str, Enum):
    energia_producida_y_requerida = 'energia_producida_y_requerida'


class EDIF_RES_RURAL_SALIDAS(BaseModel):
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
    
    salidas : list[EDIF_RES_RURAL_SALIDAS]

    class ConfigDict:
        from_attributes = True

####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class EDIF_RES_RURAL_EMISIONES(BaseModel):
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
    emisiones : list[EDIF_RES_RURAL_EMISIONES]

    class ConfigDict:
        from_attributes = True
    