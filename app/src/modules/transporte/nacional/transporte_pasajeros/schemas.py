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
    transporte_urbano_distribucion_modal = 'transporte_urbano_distribucion_modal'
    transporte_urbano_distancia_promedio_por_viaje_por_modo = 'transporte_urbano_distancia_promedio_por_viaje_por_modo'
    transporte_urbano_distribucion_por_tecnologia = 'transporte_urbano_distribucion_por_tecnologia'


class TRANS_PAS_ST_transporte_urbano_distribucion_modal(BaseModel):
    """Supuestos de Trayectoria transporte_urbano_distribucion_modal
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


class TRANS_PAS_ST_transp_urbano_dist_promedio_viaje_modo(BaseModel):
    """Supuestos de Trayectoria transporte_urbano_distancia_promedio_por_viaje_por_modo"""
    
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


class TRANS_PAS_ST_transporte_urbano_distribucion_por_tecnologia(BaseModel):
    """Supuestos de Trayectoria transporte_urbano_distribucion_por_tecnologia"""
    
    topic       : str
    bloque      : str
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
    
    transporte_urbano_distribucion_modal : list[TRANS_PAS_ST_transporte_urbano_distribucion_modal]
    transporte_urbano_distancia_promedio_por_viaje_por_modo : list[TRANS_PAS_ST_transp_urbano_dist_promedio_viaje_modo]
    transporte_urbano_distribucion_por_tecnologia : list[TRANS_PAS_ST_transporte_urbano_distribucion_por_tecnologia]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class TRANS_PAS_SF_n_viajes_por_habitante_por_dia(BaseModel):
    """Supuestos Fijos n_viajes_por_habitante_por_dia
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


class TRANS_PAS_SF_uso_de_combustibles_fosiles_en_vehiculos_hibridos(BaseModel):
    """Supuestos Fijos uso_de_combustibles_fosiles_en_vehiculos_hibridos
    """
    topic       : str
    tipo        : str
    value       : float | None
    unidad      : str
    

class TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_nuevos(BaseModel):
    """Supuestos Fijos rendimiento_modo_tecnologia_transporte_urbano_vehiculos_nuevos"""

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


class TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_existentes(BaseModel):
    """Supuestos Fijos rendimiento_modo_tecnologia_transporte_urbano_vehiculos_existentes"""

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


class TRANS_PAS_SF_rendimiento_modo_tecnologia_transporte_urbano(BaseModel):
    """Supuestos Fijos rendimiento_modo_tecnologia_transporte_urbano"""

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


class TRANS_PAS_SF_rend_modo_tec_transp_urbano_electrico(BaseModel):
    """Supuestos Fijos rendimiento_modo_tecnologia_transporte_urbano_electrico"""

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


class TRANS_PAS_SF_gas_natural_vehicular(BaseModel):
    """Supuestos Fijos gas_natural_vehicular
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


class TRANS_PAS_SF_porcentaje_de_vehiculos_nuevos_transporte_urbano(BaseModel):
    """Supuestos Fijos porcentaje_de_vehiculos_nuevos_transporte_urbano
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


class TRANS_PAS_SF_km_tot_modo_carretero_transp_interurbano(BaseModel):
    """Supuestos Fijos kilometros_totales_modo_carretero_transporte_interurbano"""

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


class TRANS_PAS_SF_demanda_ener_otros_modos_transp_interurbano(BaseModel):
    """Supuestos Fijos demanda_de_energia_otros_modos_transporte_interurbano"""

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


class TRANS_PAS_SF_demanda_electrica_modo_ferreo(BaseModel):
    """Supuestos Fijos porcentaje_de_demanda_electrica_para_el_modo_ferreo"""

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


class TRANS_PAS_SF_distr_modo_carretero_trans_interurbano(BaseModel):
    """Supuestos Fijos distribucion_por_modo_carretero_transporte_interurbano"""

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


class TRANS_PAS_SF_rend_modo_tec_trans_interurbano_vehic_existentes(BaseModel):
    """Supuestos Fijos rendimiento_modo_tecnologia_transporte_interurbano_vehiculos_existentes
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


class TRANS_PAS_SF_vehiculos_nuevos_transp_interurbano(BaseModel):
    """Supuestos Fijos porcentaje_de_vehiculos_nuevos_transporte_interurbano
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


class TRANS_PAS_SF_dist_tip_viajada_por_modo_transp_urbano(BaseModel):
    """Supuestos Fijos distancia_tipica_viajada_por_modo_transporte_urbano"""

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


class TRANS_PAS_SF_dist_tip_viajada_modo_transp_interurbano(BaseModel):
    """Supuestos Fijos distancia_tipica_viajada_por_modo_transporte_interurbano"""

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


class TRANS_PAS_SF_total_viajes_anuales(BaseModel):
    """Supuestos Fijos total_viajes_anuales"""

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


class TRANS_PAS_SF_vida_util(BaseModel):
    """Supuestos Fijos vida_util"""

    topic       : str
    bloque      : str
    tipo        : str
    value       : float | None
    unidad      : str


class TRANS_PAS_SF_numero_de_vehiculos_transporte_urbano(BaseModel):
    """Supuestos Fijos numero_de_vehiculos_transporte_urbano
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


class TRANS_PAS_SF_numero_de_vehiculos_transporte_interurbano(BaseModel):
    """Supuestos Fijos numero_de_vehiculos_transporte_interurbano
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
    """Supuestos fijos con todos los topics"""
    
    n_viajes_por_habitante_por_dia                                          : list[TRANS_PAS_SF_n_viajes_por_habitante_por_dia]
    uso_de_combustibles_fosiles_en_vehiculos_hibridos                       : list[TRANS_PAS_SF_uso_de_combustibles_fosiles_en_vehiculos_hibridos]
    rendimiento_modo_tecnologia_transporte_urbano_vehiculos_nuevos          : list[TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_nuevos]
    rendimiento_modo_tecnologia_transporte_urbano_vehiculos_existentes      : list[TRANS_PAS_SF_rend_modo_tec_trans_urbano_vehiculos_existentes]
    rendimiento_modo_tecnologia_transporte_urbano                           : list[TRANS_PAS_SF_rendimiento_modo_tecnologia_transporte_urbano]
    rendimiento_modo_tecnologia_transporte_urbano_electrico                 : list[TRANS_PAS_SF_rend_modo_tec_transp_urbano_electrico]
    gas_natural_vehicular                                                   : list[TRANS_PAS_SF_gas_natural_vehicular]
    porcentaje_de_vehiculos_nuevos_transporte_urbano                        : list[TRANS_PAS_SF_porcentaje_de_vehiculos_nuevos_transporte_urbano]
    kilometros_totales_modo_carretero_transporte_interurbano                : list[TRANS_PAS_SF_km_tot_modo_carretero_transp_interurbano]
    demanda_de_energia_otros_modos_transporte_interurbano                   : list[TRANS_PAS_SF_demanda_ener_otros_modos_transp_interurbano]
    porcentaje_de_demanda_electrica_para_el_modo_ferreo                     : list[TRANS_PAS_SF_demanda_electrica_modo_ferreo]
    distribucion_por_modo_carretero_transporte_interurbano                  : list[TRANS_PAS_SF_distr_modo_carretero_trans_interurbano]
    rendimiento_modo_tecnologia_transporte_interurbano_vehiculos_existentes : list[TRANS_PAS_SF_rend_modo_tec_trans_interurbano_vehic_existentes]
    porcentaje_de_vehiculos_nuevos_transporte_interurbano                   : list[TRANS_PAS_SF_vehiculos_nuevos_transp_interurbano]
    distancia_tipica_viajada_por_modo_transporte_urbano                     : list[TRANS_PAS_SF_dist_tip_viajada_por_modo_transp_urbano]
    distancia_tipica_viajada_por_modo_transporte_interurbano                : list[TRANS_PAS_SF_dist_tip_viajada_modo_transp_interurbano]
    total_viajes_anuales                                                    : list[TRANS_PAS_SF_total_viajes_anuales]
    vida_util                                                               : list[TRANS_PAS_SF_vida_util]
    numero_de_vehiculos_transporte_urbano                                   : list[TRANS_PAS_SF_numero_de_vehiculos_transporte_urbano]
    numero_de_vehiculos_transporte_interurbano                              : list[TRANS_PAS_SF_numero_de_vehiculos_transporte_interurbano]

    
    class ConfigDict:
        from_attributes = True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salidas = 'salidas'


class TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros(BaseModel):
    """Salidas - energia_requerida_transporte_pasajeros
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
    medida_1 : float
    medida_2 : float


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salidas : list[TRANS_PAS_SALIDAS_energia_requerida_transporte_pasajeros]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class TRANS_PAS_emisiones_de_gases_efecto_invernadero(BaseModel):
    """Emisiones - emisiones_de_gases_efecto_invernadero
    """

    topic       : str
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
    medida_1 : float
    medida_2 : float


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones : list[TRANS_PAS_emisiones_de_gases_efecto_invernadero]

    class ConfigDict:
        from_attributes = True