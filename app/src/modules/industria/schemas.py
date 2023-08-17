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
    reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica = 'reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica'
    eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras = 'eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras'
    eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion = 'eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion'
    eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras = 'eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras'
    sustitucion_de_sao_y_hfc = 'sustitucion_de_sao_y_hfc'
    procesos_productivos_sostenibles = 'procesos_productivos_sostenibles'


class INDU_ST_reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica(BaseModel):
    """Supuestos de Trayectoria reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica
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


class INDU_ST_eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras(BaseModel):
    """Supuestos de Trayectoria eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras
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


class INDU_ST_eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion(BaseModel):
    """Supuestos de Trayectoria eficiencia_energetica_%_crecimiento_de_autogeneracion_y_cogeneracion
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


class INDU_ST_eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras(BaseModel):
    """Supuestos de Trayectoria eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras
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


class INDU_ST_sustitucion_de_sao_y_hfc(BaseModel):
    """Supuestos de Trayectoria sustitucion_de_sao_y_hfc
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


class INDU_ST_procesos_productivos_sostenibles(BaseModel):
    """Supuestos de Trayectoria procesos_productivos_sostenibles
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
    
    reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica : list[INDU_ST_reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica]
    eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras       : list[INDU_ST_eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras]
    eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion      : list[INDU_ST_eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion]
    eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras         : list[INDU_ST_eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras]
    sustitucion_de_sao_y_hfc                                                : list[INDU_ST_sustitucion_de_sao_y_hfc]
    procesos_productivos_sostenibles                                        : list[INDU_ST_procesos_productivos_sostenibles]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class INDU_SF_produccion_anual_de_materiales(BaseModel):
    """Supuestos Fijos produccion_anual_de_materiales
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


class INDU_SF_produccion_de_acido_nitrico(BaseModel):
    """Supuestos Fijos produccion_de_acido_nitrico
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class INDU_SF_produccion_de_cemento(BaseModel):
    """Supuestos Fijos produccion_de_cemento
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class INDU_SF_produccion_anual_de_ladrillos(BaseModel):
    """Supuestos Fijos produccion_anual_de_ladrillos
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


class INDU_SF_indice_de_consumo(BaseModel):
    """Supuestos Fijos indice_de_consumo
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class INDU_SF_distribucion_segun_tipo_de_combustible_ladrilleras(BaseModel):
    """Supuestos Fijos distribucion_segun_tipo_de_combustible_ladrilleras
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class INDU_SF_uso_energetico_por_combustible(BaseModel):
    """Supuestos Fijos uso_energetico_por_combustible
    """

    topic       : str
    tipo        : str
    fuente      : str
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : str


class INDU_SF_factor_de_utilizacion_de_autogeneracion_y_cogeneracion(BaseModel):
    """Supuestos Fijos factor_de_utilizacion_de_autogeneracion_y_cogeneracion
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class INDU_SF_capacidad_instalada_de_autogeneracion(BaseModel):
    """Supuestos Fijos capacidad_instalada_de_autogeneracion
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class INDU_SF_excedentes_de_autogeneracion(BaseModel):
    """Supuestos Fijos excedentes_de_autogeneracion
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class INDU_SF_capacidad_instalada_de_cogeneracion(BaseModel):
    """Supuestos Fijos capacidad_instalada_de_cogeneracion
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class INDU_SF_excedentes_de_cogeneracion(BaseModel):
    """Supuestos Fijos excedentes_de_cogeneracion
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class INDU_SF_emision_de_sao(BaseModel):
    """Supuestos Fijos emision_de_sao
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
    
    produccion_anual_de_materiales                         : list[INDU_SF_produccion_anual_de_materiales]
    produccion_de_acido_nitrico                            : list[INDU_SF_produccion_de_acido_nitrico]
    produccion_de_cemento                                  : list[INDU_SF_produccion_de_cemento]
    produccion_anual_de_ladrillos                          : list[INDU_SF_produccion_anual_de_ladrillos]
    indice_de_consumo                                      : list[INDU_SF_indice_de_consumo]
    distribucion_segun_tipo_de_combustible_ladrilleras     : list[INDU_SF_distribucion_segun_tipo_de_combustible_ladrilleras]
    uso_energetico_por_combustible                         : list[INDU_SF_uso_energetico_por_combustible]
    factor_de_utilizacion_de_autogeneracion_y_cogeneracion : list[INDU_SF_factor_de_utilizacion_de_autogeneracion_y_cogeneracion]
    capacidad_instalada_de_autogeneracion                  : list[INDU_SF_capacidad_instalada_de_autogeneracion]
    excedentes_de_autogeneracion                           : list[INDU_SF_excedentes_de_autogeneracion]
    capacidad_instalada_de_cogeneracion                    : list[INDU_SF_capacidad_instalada_de_cogeneracion]
    excedentes_de_cogeneracion                             : list[INDU_SF_excedentes_de_cogeneracion]
    emision_de_sao                                         : list[INDU_SF_emision_de_sao]
    
    class ConfigDict:
        from_attributes = True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salida_energia_requerida_combustible = 'salida_energia_requerida_combustible'
    salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible = 'salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible'
    salida_balance_total_de_la_energia_requerida_combustible = 'salida_balance_total_de_la_energia_requerida_combustible'
    salida_energia_requerida_industria = 'salida_energia_requerida_industria'
    salida_energia_producida_por_autogeneracion_y_cogeneracion_industria = 'salida_energia_producida_por_autogeneracion_y_cogeneracion_industria'
    salida_balance_total_de_la_energia_requerida_industria = 'salida_balance_total_de_la_energia_requerida_industria'

# # Por combustible

class _INDU_SALIDAS_por_combustible_energia_requerida(BaseModel):
    """Salidas - por_combustible_energia_requerida
    """

    bloque      : str
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
    medida_4    : float

class INDU_SALIDAS_por_combustible_energia_requerida(BaseModel):
    """Salidas - por_combustible_energia_requerida
    """

    salida_energia_requerida_combustible : list[_INDU_SALIDAS_por_combustible_energia_requerida]

    class ConfigDict:
        from_attributes = True


class _INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion(BaseModel):
    """Salidas - por_combustible_energia_producida_por_autogeneracion_y_cogeneracion
    """

    bloque      : str
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
    medida_4    : float

class INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion(BaseModel):
    """Salidas - por_combustible_energia_producida_por_autogeneracion_y_cogeneracion
    """

    salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible : list[_INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion]

    class ConfigDict:
        from_attributes = True


class _INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida(BaseModel):
    """Salidas - por_combustible_balance_total_de_la_energia_requerida
    """

    bloque      : str
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
    medida_4    : float

class INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida(BaseModel):
    """Salidas - por_combustible_balance_total_de_la_energia_requerida
    """

    salida_balance_total_de_la_energia_requerida_combustible : list[_INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida]

    class ConfigDict:
        from_attributes = True


# # POR TIPO DE INDUSTRIA

class _INDU_SALIDAS_por_tipo_de_industria_energia_requerida(BaseModel):
    """Salidas - por_tipo_de_industria_energia_requerida
    """

    bloque      : str
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
    medida_4    : float

class INDU_SALIDAS_por_tipo_de_industria_energia_requerida(BaseModel):
    """Salidas - por_tipo_de_industria_energia_requerida
    """

    salida_energia_requerida_industria : list[_INDU_SALIDAS_por_tipo_de_industria_energia_requerida]

    class ConfigDict:
        from_attributes = True


class _INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion(BaseModel):
    """Salidas - por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion
    """

    bloque      : str
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
    medida_4    : float

class INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion(BaseModel):
    """Salidas - por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion
    """

    salida_energia_producida_por_autogeneracion_y_cogeneracion_industria : list[_INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion]

    class ConfigDict:
        from_attributes = True


class _INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida(BaseModel):
    """Salidas - por_tipo_de_industria_balance_total_de_la_energia_requerida
    """

    bloque      : str
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
    medida_4    : float

class INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida(BaseModel):
    """Salidas - por_tipo_de_industria_balance_total_de_la_energia_requerida
    """

    salida_balance_total_de_la_energia_requerida_industria : list[_INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida]

    class ConfigDict:
        from_attributes = True


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salida_energia_requerida_combustible                                   : list[_INDU_SALIDAS_por_combustible_energia_requerida]
    salida_energia_producida_por_autogeneracion_y_cogeneracion_combustible : list[_INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion]
    salida_balance_total_de_la_energia_requerida_combustible               : list[_INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida]
    salida_energia_requerida_industria                                     : list[_INDU_SALIDAS_por_tipo_de_industria_energia_requerida]
    salida_energia_producida_por_autogeneracion_y_cogeneracion_industria   : list[_INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion]
    salida_balance_total_de_la_energia_requerida_industria                 : list[_INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones_gases_efecto_invernadero         = 'emisiones_gases_efecto_invernadero'
    emisiones_por_el_consumo_de_bagazo_y_otros = 'emisiones_por_el_consumo_de_bagazo_y_otros'
    emisiones_sao                              = 'emisiones_sao'

class _INDU_emisiones_gases_efecto_invernadero(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
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
    medida_3    : float
    medida_4    : float

class INDU_emisiones_gases_efecto_invernadero(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones_gases_efecto_invernadero : list[_INDU_emisiones_gases_efecto_invernadero]

    class ConfigDict:
        from_attributes = True


class _INDU_emisiones_por_el_consumo_de_bagazo_y_otros(BaseModel):
    """Emisiones - emisiones_por_el_consumo_de_bagazo_y_otros
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
    medida_3    : float
    medida_4    : float


class INDU_emisiones_por_el_consumo_de_bagazo_y_otros(BaseModel):
    """Emisiones - emisiones_por_el_consumo_de_bagazo_y_otros
    """
    emisiones_por_el_consumo_de_bagazo_y_otros : list[_INDU_emisiones_por_el_consumo_de_bagazo_y_otros]

    class ConfigDict:
        from_attributes = True


class _INDU_emisiones_sao(BaseModel):
    """Emisiones - emisiones_sao
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
    medida_3    : float
    medida_4    : float


class INDU_emisiones_sao(BaseModel):
    """Emisiones - emisiones_sao
    """
    emisiones_sao : list[_INDU_emisiones_sao]

    class ConfigDict:
        from_attributes = True
    

class EMISIONES(BaseModel):
    """Emisiones
    """
    
    emisiones_gases_efecto_invernadero         : list[_INDU_emisiones_gases_efecto_invernadero]
    emisiones_por_el_consumo_de_bagazo_y_otros : list[_INDU_emisiones_por_el_consumo_de_bagazo_y_otros]
    emisiones_sao                              : list[_INDU_emisiones_sao]

    class ConfigDict:
        from_attributes = True