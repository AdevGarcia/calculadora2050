from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Ganaderia

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies = 'practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies'
    mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado = 'mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado'
    produccion_de_estiercol_para_bioenergia = 'produccion_de_estiercol_para_bioenergia'


class GANA_ST_pract_sost_suelos_ganaderos_crecimiento_estimado_sup(BaseModel):
    """Supuestos de Trayectoria practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies
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


class GANA_ST_mejores_pract_pecuarias_cabezas_ganado(BaseModel):
    """Supuestos de Trayectoria mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado
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


class GANA_ST_produccion_de_estiercol_para_bioenergia(BaseModel):
    """Supuestos de Trayectoria produccion_de_estiercol_para_bioenergia
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
    
    practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies : list[GANA_ST_pract_sost_suelos_ganaderos_crecimiento_estimado_sup]
    mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado                   : list[GANA_ST_mejores_pract_pecuarias_cabezas_ganado]
    produccion_de_estiercol_para_bioenergia                                       : list[GANA_ST_produccion_de_estiercol_para_bioenergia]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class GANA_SF_uso_actual_tierra_sector_agropecuario_colombia(BaseModel):
    """Supuestos Fijos uso_actual_de_la_tierra_sector_agropecuario_en_colombia
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class GANA_SF_hato_ganadero_colombiano(BaseModel):
    """Supuestos Fijos hato_ganadero_colombiano
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


class GANA_SF_factor_de_emision_de_metano_ch4_por_genero(BaseModel):
    """Supuestos Fijos factor_de_emision_de_metano_ch4_por_genero
    """

    topic       : str
    fuente      : str
    valor       : float | None
    unidad      : str


class GANA_SF_areas_ini_implem_pract_sostenibles_suelos_ganaderos(BaseModel):
    """Supuestos Fijos areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class GANA_SF_fact_prod_estiercol_por_cabeza_ganado_y_emisiones(BaseModel):
    """Supuestos Fijos factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones
    """

    topic       : str
    fuente      : str
    valor       : float | None
    unidad      : str


class GANA_SF_potencial_energetico_del_estiercol(BaseModel):
    """Supuestos Fijos potencial_energetico_del_estiercol
    """

    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str


class GANA_SF_pot_reduc_emisiones_practicas_sost_suelos_ganaderos(BaseModel):
    """Supuestos Fijos potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos
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


class GANA_SF_coef_remocion_carbono_dist_usos_suelo_ecorregion_anual(BaseModel):
    """Supuestos Fijos coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class GANA_SF_pot_reduccion_emisiones_mejores_practicas_pecuarias(BaseModel):
    """Supuestos Fijos potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias
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
    
    uso_actual_de_la_tierra_sector_agropecuario_en_colombia                                : list[GANA_SF_uso_actual_tierra_sector_agropecuario_colombia]
    hato_ganadero_colombiano                                                               : list[GANA_SF_hato_ganadero_colombiano]
    factor_de_emision_de_metano_ch4_por_genero                                             : list[GANA_SF_factor_de_emision_de_metano_ch4_por_genero]
    areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos       : list[GANA_SF_areas_ini_implem_pract_sostenibles_suelos_ganaderos]
    factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones                        : list[GANA_SF_fact_prod_estiercol_por_cabeza_ganado_y_emisiones]
    potencial_energetico_del_estiercol                                                     : list[GANA_SF_potencial_energetico_del_estiercol]
    potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos          : list[GANA_SF_pot_reduc_emisiones_practicas_sost_suelos_ganaderos]
    coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual : list[GANA_SF_coef_remocion_carbono_dist_usos_suelo_ecorregion_anual]
    potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias                     : list[GANA_SF_pot_reduccion_emisiones_mejores_practicas_pecuarias]
    
    class ConfigDict:
        from_attributes = True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salidas = 'salidas'

class GANA_SALIDAS(BaseModel):
    """produccion_de_estiercol_para_bioenergia"""

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


class SALIDAS(BaseModel):
    """salidas"""

    salidas : list[GANA_SALIDAS]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones_de_hato_ganadero = 'emisiones_de_hato_ganadero'
    practicas_sostenibles_en_suelos_ganaderos = 'practicas_sostenibles_en_suelos_ganaderos'
    mejores_practicas_pecuarias = 'mejores_practicas_pecuarias'
    manejo_de_estiercol = 'manejo_de_estiercol'


class GANA_EMISIONES(BaseModel):
    """emisiones"""

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


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones : list[GANA_EMISIONES]

    class ConfigDict:
        from_attributes = True
