from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Residuos - Aguas Residuales

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    cantidad_de_aguas_residuales_domesticas   = 'cantidad_de_aguas_residuales_domesticas'
    cantidad_de_aguas_residuales_industriales = 'cantidad_de_aguas_residuales_industriales'
    estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas  = 'estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas'
    estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas = 'estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas'


class RES_AGU_ST_cantidad_de_aguas_residuales_domesticas(BaseModel):
    """Supuestos de Trayectoria cantidad_de_aguas_residuales_domesticas
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


class RES_AGU_ST_cantidad_de_aguas_residuales_industriales(BaseModel):
    """Supuestos de Trayectoria cantidad_de_aguas_residuales_industriales
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


class RES_AGU_ST_estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas(BaseModel):
    """Supuestos de Trayectoria estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas
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


class RES_AGU_ST_estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas(BaseModel):
    """Supuestos de Trayectoria estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas
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
    
    cantidad_de_aguas_residuales_domesticas          : list[RES_AGU_ST_cantidad_de_aguas_residuales_domesticas]
    cantidad_de_aguas_residuales_industriales        : list[RES_AGU_ST_cantidad_de_aguas_residuales_industriales]
    estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas  : list[RES_AGU_ST_estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas]
    estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas : list[RES_AGU_ST_estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas]
    
    class Config:
        orm_mode : True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_tratada(BaseModel):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_domestica_tratada
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_no_tratada(BaseModel):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_domestica_no_tratada
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_tratada(BaseModel):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_industrial_tratada
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_no_tratada(BaseModel):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_industrial_no_tratada
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_AGU_SF_generacion_de_ch4_por_kg_dbo_tratado(BaseModel):
    """Supuestos Fijos generacion_de_ch4_por_kg_dbo_tratado
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_AGU_SF_generacion_de_ch4_por_kg_dbo_no_tratado(BaseModel):
    """Supuestos Fijos generacion_de_ch4_por_kg_dbo_no_tratado
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_AGU_SF_datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento(BaseModel):
    """Supuestos Fijos datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_AGU_SF_consumo_energetico_medio_por_tratamiento(BaseModel):
    """Supuestos Fijos consumo_energetico_medio_por_tratamiento
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """
    
    dbo_por_m3_de_agua_residual_domestica_tratada                      : list[RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_tratada]
    dbo_por_m3_de_agua_residual_domestica_no_tratada                   : list[RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_no_tratada]
    dbo_por_m3_de_agua_residual_industrial_tratada                     : list[RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_tratada]
    dbo_por_m3_de_agua_residual_industrial_no_tratada                  : list[RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_no_tratada]
    generacion_de_ch4_por_kg_dbo_tratado                               : list[RES_AGU_SF_generacion_de_ch4_por_kg_dbo_tratado]
    generacion_de_ch4_por_kg_dbo_no_tratado                            : list[RES_AGU_SF_generacion_de_ch4_por_kg_dbo_no_tratado]
    datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento : list[RES_AGU_SF_datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento]
    consumo_energetico_medio_por_tratamiento                           : list[RES_AGU_SF_consumo_energetico_medio_por_tratamiento]
    
    class Config:
        orm_mode : True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salida_energia_consumida = 'salida_energia_consumida'
    salida_energia_producida = 'salida_energia_producida'


class _RES_AGU_SALIDAS_energia_consumida(BaseModel):
    """Salidas - energia_consumida
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


class RES_AGU_SALIDAS_energia_consumida(BaseModel):
    """energia_consumida"""

    salida_energia_consumida : list[_RES_AGU_SALIDAS_energia_consumida]

    class Config:
        orm_mode : True


class _RES_AGU_SALIDAS_energia_producida(BaseModel):
    """Salidas - energia_producida
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


class RES_AGU_SALIDAS_energia_producida(BaseModel):
    """energia_producida"""

    salida_energia_producida : list[_RES_AGU_SALIDAS_energia_producida]

    class Config:
        orm_mode : True


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salida_energia_consumida : list[_RES_AGU_SALIDAS_energia_consumida]
    salida_energia_producida : list[_RES_AGU_SALIDAS_energia_producida]

    class Config:
        orm_mode : True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones_de_gases_de_efecto_invernadero_aguas_residuales = 'emisiones_de_gases_de_efecto_invernadero_aguas_residuales'
    emisiones_de_gases_de_efecto_invernadero_energia = 'emisiones_de_gases_de_efecto_invernadero_energia'


class Emisiones_bloque(str, Enum):
    aguas_residuales_domesticas = 'aguas_residuales_domesticas'
    aguas_residuales_industriales = 'aguas_residuales_industriales'


class Emisiones_emisiones(str, Enum):
    emisiones = 'emisiones'


class RES_AGU_emisiones_de_gases_de_efecto_invernadero_aguas_residuales(BaseModel):
    """Emisiones - emisiones_de_gases_de_efecto_invernadero_aguas_residuales
    """

    topic    : str
    bloque   : str
    tipo     : str
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


class RES_AGU_emisiones_de_gases_de_efecto_invernadero_energia(BaseModel):
    """Emisiones - emisiones_de_gases_de_efecto_invernadero_energia
    """

    topic    : str
    bloque   : str
    tipo     : str
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


class RES_AGU_emisiones(BaseModel):
    """Emisiones - emisiones"""

    topic    : str
    bloque   : str
    tipo     : str
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
    # emisiones_de_gases_de_efecto_invernadero_aguas_residuales : list[RES_AGU_emisiones_de_gases_de_efecto_invernadero_aguas_residuales]
    # emisiones_de_gases_de_efecto_invernadero_energia : list[RES_AGU_emisiones_de_gases_de_efecto_invernadero_energia]
    emisiones : list[RES_AGU_emisiones]

    class Config:
        orm_mode : True