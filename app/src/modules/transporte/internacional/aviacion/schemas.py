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
    uso_de_combustible_para_aviacion_internacional = 'uso_de_combustible_para_aviacion_internacional'


class TRANS_AVI_ST_uso_de_combustible_para_aviacion_internacional(BaseModel):
    """Supuestos de Trayectoria uso_de_combustible_para_aviacion_internacional
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
    
    uso_de_combustible_para_aviacion_internacional : list[TRANS_AVI_ST_uso_de_combustible_para_aviacion_internacional]
    
    class Config:
        orm_mode : True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class TRANS_AVI_SF_uso_de_combustible_para_aviacion_internacional(BaseModel):
    """Supuestos Fijos uso_de_combustible_para_aviacion_internacional
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class TRANS_AVI_SF_proporcion_de_combustible_utilizado_en_etapas_de_despegue_y_aterrizaje(BaseModel):
    """Supuestos Fijos proporcion_de_combustible_utilizado_en_etapas_de_despegue_y_aterrizaje
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
    
    uso_de_combustible_para_aviacion_internacional : list[TRANS_AVI_SF_uso_de_combustible_para_aviacion_internacional]
    proporcion_de_combustible_utilizado_en_etapas_de_despegue_y_aterrizaje : list[TRANS_AVI_SF_proporcion_de_combustible_utilizado_en_etapas_de_despegue_y_aterrizaje]
    
    class Config:
        orm_mode : True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salidas = 'salidas'


class TRANS_AVI_SALIDAS_energia_requerida(BaseModel):
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
    
    salidas : list[TRANS_AVI_SALIDAS_energia_requerida]

    class Config:
        orm_mode : True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class TRANS_AVI_emisiones_aviacion_y_navegacion_internacional(BaseModel):
    """Emisiones - emisiones_aviacion_y_navegacion_internacional
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
    emisiones : list[TRANS_AVI_emisiones_aviacion_y_navegacion_internacional]

    class Config:
        orm_mode : True