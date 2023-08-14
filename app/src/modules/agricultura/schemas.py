from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Agricultura

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    mejores_practicas_agricolas_superficie_de_implementacion = 'mejores_practicas_agricolas_superficie_de_implementacion'
    tierra_dedicada_para_biocombustibles_superficie_de_implementacion = 'tierra_dedicada_para_biocombustibles_superficie_de_implementacion'


class AGRO_ST_mejores_practicas_agricolas_superficie_de_implementacion(BaseModel):
    """Supuestos de Trayectoria mejores_practicas_agricolas_superficie_de_implementacion
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


class AGRO_ST_tierra_dedicada_para_biocombustibles_superficie_de_implementacion(BaseModel):
    """Supuestos de Trayectoria tierra_dedicada_para_biocombustibles_superficie_de_implementacion
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
    
    mejores_practicas_agricolas_superficie_de_implementacion          : list[AGRO_ST_mejores_practicas_agricolas_superficie_de_implementacion]
    tierra_dedicada_para_biocombustibles_superficie_de_implementacion : list[AGRO_ST_tierra_dedicada_para_biocombustibles_superficie_de_implementacion]
    
    class Config:
        orm_mode : True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class AGRO_SF_factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo(BaseModel):
    """Supuestos Fijos factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class AGRO_SF_produccion_biocombustibles(BaseModel):
    """Supuestos Fijos produccion_biocombustibles
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class AGRO_SF_porcentaje_del_cultivo_usado_para_biocombustibles(BaseModel):
    """Supuestos Fijos porcentaje_del_cultivo_usado_para_biocombustibles
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class AGRO_SF_factor_de_emision_de_cultivo_usado_para_biocombustibles(BaseModel):
    """Supuestos Fijos factor_de_emision_de_cultivo_usado_para_biocombustibles
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class AGRO_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia(BaseModel):
    """Supuestos Fijos uso_actual_de_la_tierra_sector_agropecuario_en_colombia
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class AGRO_SF_tasas_de_crecimiento_del_pib_sectorial_de_agricultura(BaseModel):
    """Supuestos Fijos tasas_de_crecimiento_del_pib_sectorial_de_agricultura
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


class AGRO_SF_areas_de_implementacion_de_mejores_practicas_agricolas(BaseModel):
    """Supuestos Fijos areas_de_implementacion_de_mejores_practicas_agricolas
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


class AGRO_SF_factor_de_produccion_biomasa_por_cultivo(BaseModel):
    """Supuestos Fijos factor_de_produccion_biomasa_por_cultivo
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class AGRO_SF_potencial_energetico_por_unidad_de_biomasa(BaseModel):
    """Supuestos Fijos potencial_energetico_por_unidad_de_biomasa
    """

    topic            : str
    bloque           : str
    tipo             : str
    factor           : float | None
    unidad_factor    : str
    potencial        : float | None
    unidad_potencial : str


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """
    
    factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo : list[AGRO_SF_factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo]
    produccion_biocombustibles                                           : list[AGRO_SF_produccion_biocombustibles]
    porcentaje_del_cultivo_usado_para_biocombustibles                    : list[AGRO_SF_porcentaje_del_cultivo_usado_para_biocombustibles]
    factor_de_emision_de_cultivo_usado_para_biocombustibles              : list[AGRO_SF_factor_de_emision_de_cultivo_usado_para_biocombustibles]
    uso_actual_de_la_tierra_sector_agropecuario_en_colombia              : list[AGRO_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia]
    tasas_de_crecimiento_del_pib_sectorial_de_agricultura                : list[AGRO_SF_tasas_de_crecimiento_del_pib_sectorial_de_agricultura]
    areas_de_implementacion_de_mejores_practicas_agricolas               : list[AGRO_SF_areas_de_implementacion_de_mejores_practicas_agricolas]
    factor_de_produccion_biomasa_por_cultivo                             : list[AGRO_SF_factor_de_produccion_biomasa_por_cultivo]
    potencial_energetico_por_unidad_de_biomasa                           : list[AGRO_SF_potencial_energetico_por_unidad_de_biomasa]
    
    class Config:
        orm_mode : True


####################################################################################
#######                           Metodologia                                #######
####################################################################################

class Metodologia_name(str, Enum):
    metodologia= 'metodologia'


class AGRO_Metodologia_tierra_dedicada_para_biocombustibles(BaseModel):
    """Metodologia_tierra_dedicada_para_biocombustibles"""

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
    medida_3    : float 


class METODOLOGIA(BaseModel):
    """Metodologia con todos los topics
    """
    
    metodologia : list[AGRO_Metodologia_tierra_dedicada_para_biocombustibles]
    
    class Config:
        orm_mode : True


####################################################################################
#######                               Salidas                                #######
####################################################################################

class Salidas_name(str, Enum):
    salida_cultivos         = 'salida_cultivos'
    salida_biocombustibles  = 'salida_biocombustibles'
    

class _AGRO_SALIDAS_cultivos(BaseModel):
    """salida_cultivos"""

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
    medida_2    : float
    medida_3    : float


class AGRO_SALIDAS_cultivos(BaseModel):
    """salida_cultivos"""

    salida_cultivos : list[_AGRO_SALIDAS_cultivos]

    class Config:
        orm_mode : True


class _AGRO_SALIDAS_biocombustibles(BaseModel):
    """Salidas_biocombustibles"""

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
    medida_3    : float


class AGRO_SALIDAS_biocombustibles(BaseModel):
    """Salidas_biocombustibles"""

    salida_biocombustibles : list[_AGRO_SALIDAS_biocombustibles]

    class Config:
        orm_mode : True


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salida_cultivos         : list[_AGRO_SALIDAS_cultivos]
    salida_biocombustibles  : list[_AGRO_SALIDAS_biocombustibles]

    class Config:
        orm_mode : True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    # emisiones = 'emisiones'
    emisiones_cultivo_biocombustibles = 'emisiones_cultivo_biocombustibles',
    implementacion_de_mejores_practicas_agricolas = 'implementacion_de_mejores_practicas_agricolas',
    emisiones_a_industria = 'emisiones_a_industria'


class AGRO_EMISIONES(BaseModel):
    """Emisiones"""

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
    medida_2    : float
    medida_3    : float


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones : list[AGRO_EMISIONES]

    class Config:
        orm_mode : True

