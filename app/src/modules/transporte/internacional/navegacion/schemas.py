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
    uso_de_combustible_para_navegacion_nacional = 'uso_de_combustible_para_navegacion_nacional'


class TRANS_NAV_ST_uso_de_combustible_para_navegacion_nacional(BaseModel):
    """Supuestos de Trayectoria uso_de_combustible_para_navegacion_nacional
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
    
    uso_de_combustible_para_navegacion_nacional : list[TRANS_NAV_ST_uso_de_combustible_para_navegacion_nacional]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                               Salidas                                #######
####################################################################################

class Salidas_name(str, Enum):
    salidas = 'salidas'


class TRANS_NAV_SALIDAS_energia_requerida(BaseModel):
    """Salidas - energia_requerida
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


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salidas : list[TRANS_NAV_SALIDAS_energia_requerida]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class TRANS_NAV_emisiones(BaseModel):
    """Emisiones - emisiones
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


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones : list[TRANS_NAV_emisiones]

    class ConfigDict:
        from_attributes = True
