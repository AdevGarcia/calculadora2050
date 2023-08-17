from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Bosques

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    escenarios_de_deforestacion = 'escenarios_de_deforestacion'
    desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales = 'desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales'


class BOSQ_ST_escenarios_de_deforestacion(BaseModel):
    """Supuestos de Trayectoria escenarios_de_deforestacion
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


class BOSQ_ST_desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales(BaseModel):
    """Supuestos de Trayectoria desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales
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
    
    escenarios_de_deforestacion          : list[BOSQ_ST_escenarios_de_deforestacion]
    desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales : list[BOSQ_ST_desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class BOSQ_SF_area_anual_deforestada_puntual(BaseModel):
    """Supuestos Fijos area_anual_deforestada_puntual
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


class BOSQ_SF_deforestacion_observada_no_acumulada(BaseModel):
    """Supuestos Fijos deforestacion_observada_no_acumulada
    """

    topic       : str
    fuente      : str
    valor       : float | None
    unidad      : str


class BOSQ_SF_contenidos_de_carbono_por_zonas_naturales(BaseModel):
    """Supuestos Fijos contenidos_de_carbono_por_zonas_naturales
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class BOSQ_SF_factor_de_conversion_de_biomasa_por_deforestacion(BaseModel):
    """Supuestos Fijos factor_de_conversion_de_biomasa_por_deforestacion
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class BOSQ_SF_area_para_la_reforestacion_comercial(BaseModel):
    """Supuestos Fijos area_para_la_reforestacion_comercial
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


class BOSQ_SF_biomasa_aerea_subterranea_reforestacion_comercial(BaseModel):
    """Supuestos Fijos biomasa_aerea_subterranea_reforestacion_comercial
    """

    topic       : str
    fuente      : str
    valor       : float | None
    unidad      : str


class BOSQ_SF_descuentos_aplicables_a_reforestacion_comercial(BaseModel):
    """Supuestos Fijos descuentos_aplicables_a_reforestacion_comercial
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """
    
    area_anual_deforestada_puntual                    : list[BOSQ_SF_area_anual_deforestada_puntual]
    deforestacion_observada_no_acumulada              : list[BOSQ_SF_deforestacion_observada_no_acumulada]
    contenidos_de_carbono_por_zonas_naturales         : list[BOSQ_SF_contenidos_de_carbono_por_zonas_naturales]
    factor_de_conversion_de_biomasa_por_deforestacion : list[BOSQ_SF_factor_de_conversion_de_biomasa_por_deforestacion]
    area_para_la_reforestacion_comercial              : list[BOSQ_SF_area_para_la_reforestacion_comercial]
    biomasa_aerea_subterranea_reforestacion_comercial : list[BOSQ_SF_biomasa_aerea_subterranea_reforestacion_comercial]
    descuentos_aplicables_a_reforestacion_comercial   : list[BOSQ_SF_descuentos_aplicables_a_reforestacion_comercial]
    
    class ConfigDict:
        from_attributes = True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    total_areas_reforestadas = 'total_areas_reforestadas'


class BOSQ_SALIDAS(BaseModel):
    """total_areas_reforestadas"""

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
    """Salidas"""
    
    salidas : list[BOSQ_SALIDAS]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class BOSQ_EMISIONES(BaseModel):
    """total_emisiones"""

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
    emisiones : list[BOSQ_EMISIONES]

    class ConfigDict:
        from_attributes = True
