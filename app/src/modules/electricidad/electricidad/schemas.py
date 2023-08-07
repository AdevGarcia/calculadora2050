from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Electricidad - Electricidad

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    capacidad_de_generacion  = 'capacidad_de_generacion'
    

class ELECT_Electricidad_ST_capacidad_de_generacion(BaseModel):
    """Supuestos de Trayectoria capacidad_de_generacion"""

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
    
    capacidad_de_generacion  : list[ELECT_Electricidad_ST_capacidad_de_generacion]
    
    class Config:
        orm_mode : True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class ELECT_Electricidad_SF_horas_de_operacion_ano(BaseModel):
    """Supuestos Fijos horas_de_operacion_ano
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class ELECT_Electricidad_SF_factor_de_carga(BaseModel):
    """Supuestos Fijos factor_de_carga
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

    horas_de_operacion_ano : list[ELECT_Electricidad_SF_horas_de_operacion_ano]
    factor_de_carga        : list[ELECT_Electricidad_SF_factor_de_carga]
    
    class Config:
        orm_mode : True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salidas_combustibles_fosiles                  = 'salidas_combustibles_fosiles'
    salidas_energias_renovables_no_convencionales = 'salidas_energias_renovables_no_convencionales'
    salidas_energia_demandada                     = 'salidas_energia_demandada'
    salidas_balance                               = 'salidas_balance'

class _ELECT_Electricidad_SALIDAS_combustibles_fosiles(BaseModel):
    """salidas_combustibels_fosiles"""

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


class _ELECT_Electricidad_SALIDAS_energias_renovables_no_convencionales(BaseModel):
    """salidas_energias_renovables_no_convencionales"""

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


class _ELECT_Electricidad_SALIDAS_energia_demandada(BaseModel):
    """salidas_energia_demandada"""

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


class _ELECT_Electricidad_SALIDAS_balance(BaseModel):
    """salidas_balance"""

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


class ELECT_Electricidad_SALIDAS_combustibles_fosiles(BaseModel):
    """salidas_combustibels_fosiles"""

    salidas_combustibles_fosiles : list[_ELECT_Electricidad_SALIDAS_combustibles_fosiles]

    class Config:
        orm_mode : True


class ELECT_Electricidad_SALIDAS_energias_renovables_no_convencionales(BaseModel):
    """salidas_energias_renovables_no_convencionales"""

    salidas_energias_renovables_no_convencionales : list[_ELECT_Electricidad_SALIDAS_energias_renovables_no_convencionales]

    class Config:
        orm_mode : True


class ELECT_Electricidad_SALIDAS_energia_demandada(BaseModel):
    """salidas_energia_demandada"""

    salidas_energia_demandada : list[_ELECT_Electricidad_SALIDAS_energia_demandada]

    class Config:
        orm_mode : True


class ELECT_Electricidad_SALIDAS_balance(BaseModel):
    """salidas_balance"""

    salidas_balance : list[_ELECT_Electricidad_SALIDAS_balance]

    class Config:
        orm_mode : True
  


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salidas_combustibels_fosiles                  : list[ELECT_Electricidad_SALIDAS_combustibles_fosiles]
    salidas_energias_renovables_no_convencionales : list[ELECT_Electricidad_SALIDAS_energias_renovables_no_convencionales]
    salidas_energia_demandada                     : list[ELECT_Electricidad_SALIDAS_energia_demandada]
    salidas_balance                               : list[ELECT_Electricidad_SALIDAS_balance]

    class Config:
        orm_mode : True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones_combustibles_fosiles                  = 'emisiones_combustibles_fosiles'
    emisiones_energias_renovables_no_convencionales = 'emisiones_energias_renovables_no_convencionales'


class _ELECT_Electricidad_EMISIONES_combustibles_fosiles(BaseModel):
    """emisiones_combustibles_fosiles"""

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
    medida_1    : float


class _ELECT_Electricidad_EMISIONES_energias_renovables_no_convencionales(BaseModel):
    """emisiones_energias_renovables_no_convencionales"""

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
    medida_1    : float


class ELECT_Electricidad_EMISIONES_combustibles_fosiles(BaseModel):
    """emisiones_combustibles_fosiles"""

    emisiones_combustibles_fosiles : list[_ELECT_Electricidad_EMISIONES_combustibles_fosiles]

    class Config:
        orm_mode : True


class ELECT_Electricidad_EMISIONES_energias_renovables_no_convencionales(BaseModel):
    """emisiones_energias_renovables_no_convencionales"""

    emisiones_energias_renovables_no_convencionales : list[_ELECT_Electricidad_EMISIONES_energias_renovables_no_convencionales]

    class Config:
        orm_mode : True


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones_combustibles_fosiles                  : list[ELECT_Electricidad_EMISIONES_combustibles_fosiles]
    emisiones_energias_renovables_no_convencionales : list[ELECT_Electricidad_EMISIONES_energias_renovables_no_convencionales]

    class Config:
        orm_mode : True
