from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Residuos - Residuos Solidos

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    cantidad_de_residuos_generada_anual = 'cantidad_de_residuos_generada_anual'
    tipo_de_gestion                     = 'tipo_de_gestion'
    capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios  = 'capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios'
    capacidad_instalada_para_los_sistemas_de_incineracion = 'capacidad_instalada_para_los_sistemas_de_incineracion'


class RES_SOL_ST_cantidad_de_residuos_generada_anual(BaseModel):
    """Supuestos de Trayectoria cantidad_de_residuos_generada_anual
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


class RES_SOL_ST_tipo_de_gestion(BaseModel):
    """Supuestos de Trayectoria tipo_de_gestion
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


class RES_SOL_ST_cap_inst_sist_recup_aprov_biogas_rellenos_sanit(BaseModel):
    """Supuestos de Trayectoria capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios
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


class RES_SOL_ST_capacidad_instalada_sistemas_incineracion(BaseModel):
    """Supuestos de Trayectoria capacidad_instalada_para_los_sistemas_de_incineracion
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
    
    cantidad_de_residuos_generada_anual : list[RES_SOL_ST_cantidad_de_residuos_generada_anual]
    tipo_de_gestion                     : list[RES_SOL_ST_tipo_de_gestion]
    capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios : list[RES_SOL_ST_cap_inst_sist_recup_aprov_biogas_rellenos_sanit]
    capacidad_instalada_para_los_sistemas_de_incineracion : list[RES_SOL_ST_capacidad_instalada_sistemas_incineracion]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class RES_SOL_SF_rellenos_sanitarios_con_captacion_aprovechamiento(BaseModel):
    """Supuestos Fijos rellenos_sanitarios_con_captacion_aprovechamiento
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


class RES_SOL_SF_distribucion_de_los_residuos_por_zona_climatica(BaseModel):
    """Supuestos Fijos distribucion_de_los_residuos_por_zona_climatica
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_SOL_SF_caracterizacion_por_tipo_de_residuos_generados(BaseModel):
    """Supuestos Fijos caracterizacion_por_tipo_de_residuos_generados
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


class RES_SOL_SF_generacion_de_metano_por_tipologia_de_residuo(BaseModel):
    """Supuestos Fijos generacion_de_metano_por_tipologia_de_residuo
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_SOL_SF_generacion_energetica_mediante_incineracion(BaseModel):
    """Supuestos Fijos datos_de_la_generacion_energetica_mediante_incineracion
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_SOL_SF_consumo_energetico_medio_por_tratamiento(BaseModel):
    """Supuestos Fijos consumo_energetico_medio_por_tratamiento
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class RES_SOL_SF_estimacion_emisiones_incineracion(BaseModel):
    """Supuestos Fijos datos_para_la_estimacion_de_las_emisiones_de_incineracion
    """

    topic       : str
    bloque      : str
    tipo        : str
    value       : float | None
    unidad      : str


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """
    
    rellenos_sanitarios_con_captacion_aprovechamiento         : list[RES_SOL_SF_rellenos_sanitarios_con_captacion_aprovechamiento]
    distribucion_de_los_residuos_por_zona_climatica           : list[RES_SOL_SF_distribucion_de_los_residuos_por_zona_climatica]
    caracterizacion_por_tipo_de_residuos_generados            : list[RES_SOL_SF_caracterizacion_por_tipo_de_residuos_generados]
    generacion_de_metano_por_tipologia_de_residuo             : list[RES_SOL_SF_generacion_de_metano_por_tipologia_de_residuo]
    datos_de_la_generacion_energetica_mediante_incineracion   : list[RES_SOL_SF_generacion_energetica_mediante_incineracion]
    consumo_energetico_medio_por_tratamiento                  : list[RES_SOL_SF_consumo_energetico_medio_por_tratamiento]
    datos_para_la_estimacion_de_las_emisiones_de_incineracion : list[RES_SOL_SF_estimacion_emisiones_incineracion]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                               Salidas                                #######
####################################################################################

class Salidas_name(str, Enum):
    salida_energia_consumida = 'salida_energia_consumida'
    salida_energia_producida = 'salida_energia_producida'

class _RES_SOL_SALIDAS_energia_consumida(BaseModel):
    """Salidas - energia_consumida
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
    medida_1    : float


class RES_SOL_SALIDAS_energia_consumida(BaseModel):
    """energia_consumida"""

    salida_energia_consumida : list[_RES_SOL_SALIDAS_energia_consumida]

    class ConfigDict:
        from_attributes = True


class _RES_SOL_SALIDAS_energia_producida(BaseModel):
    """Salidas - energia_producida
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
    medida_1    : float


class RES_SOL_SALIDAS_energia_producida(BaseModel):
    """energia_producida"""

    salida_energia_producida : list[_RES_SOL_SALIDAS_energia_producida]

    class ConfigDict:
        from_attributes = True


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salida_energia_consumida : list[_RES_SOL_SALIDAS_energia_consumida]
    salida_energia_producida : list[_RES_SOL_SALIDAS_energia_producida]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones_de_gases_de_efecto_invernadero_residuos = 'emisiones_de_gases_de_efecto_invernadero_residuos'
    emisiones_de_gases_de_efecto_invernadero_energia  = 'emisiones_de_gases_de_efecto_invernadero_energia'


class Emisiones_emisiones(str, Enum):
    emisiones = 'emisiones'


class RES_SOL_emisiones(BaseModel):
    """Emisiones - emisiones"""

    topic       : str
    bloque      : str
    grupo       : str
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

    emisiones : list[RES_SOL_emisiones]

    class ConfigDict:
        from_attributes = True
