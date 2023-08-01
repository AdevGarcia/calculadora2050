from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Edificaciones Residencial Iluminacion, Refrigeracion, Coccion y Otros

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    demanda_iluminacion                                       = 'demanda_iluminacion'
    porcentaje_tecnologia_para_iluminacion                    = 'porcentaje_tecnologia_para_iluminacion'
    demanda_total_por_refrigeracion                           = 'demanda_total_por_refrigeracion'
    porcentaje_de_neveras_mas_eficientes                      = 'porcentaje_de_neveras_mas_eficientes'
    demanda_coccion_con_gas_natural                           = 'demanda_coccion_con_gas_natural'
    porcentaje_de_estufas_con_eficiencia_mejorada             = 'porcentaje_de_estufas_con_eficiencia_mejorada'
    demanda_para_coccion_con_glp                              = 'demanda_para_coccion_con_glp'
    reduccion_total_de_la_demanda_de_energia_electrica        = 'reduccion_total_de_la_demanda_de_energia_electrica'
    potencia_instalada_para_autogeneracion_solar_fotovoltaica = 'potencia_instalada_para_autogeneracion_solar_fotovoltaica'


class EDIF_RES_ILU_REF_COC_OTR_ST_demanda_iluminacion(BaseModel):
    """Supuestos de Trayectoria demanda_iluminacion
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


class EDIF_RES_ILU_REF_COC_OTR_ST_porcentaje_tecnologia_para_iluminacion(BaseModel):
    """Supuestos de Trayectoria porcentaje_tecnologia_para_iluminacion
    """

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


class EDIF_RES_ILU_REF_COC_OTR_ST_demanda_total_por_refrigeracion(BaseModel):
    """Supuestos de Trayectoria demanda_total_por_refrigeracion
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


class EDIF_RES_ILU_REF_COC_OTR_ST_porcentaje_de_neveras_mas_eficientes(BaseModel):
    """Supuestos de Trayectoria porcentaje_de_neveras_mas_eficientes
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


class EDIF_RES_ILU_REF_COC_OTR_ST_demanda_coccion_con_gas_natural(BaseModel):
    """Supuestos de Trayectoria demanda_coccion_con_gas_natural
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


class EDIF_RES_ILU_REF_COC_OTR_ST_porcentaje_de_estufas_con_eficiencia_mejorada(BaseModel):
    """Supuestos de Trayectoria porcentaje_de_estufas_con_eficiencia_mejorada
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


class EDIF_RES_ILU_REF_COC_OTR_ST_demanda_para_coccion_con_glp(BaseModel):
    """Supuestos de Trayectoria demanda_para_coccion_con_glp
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


class EDIF_RES_ILU_REF_COC_OTR_ST_reduccion_total_de_la_demanda_de_energia_electrica(BaseModel):
    """Supuestos de Trayectoria reduccion_total_de_la_demanda_de_energia_electrica
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


class EDIF_RES_ILU_REF_COC_OTR_ST_potencia_instalada_para_autogeneracion_solar_fotovoltaica(BaseModel):
    """Supuestos de Trayectoria potencia_instalada_para_autogeneracion_solar_fotovoltaica
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
    
    demanda_iluminacion                                       : list[EDIF_RES_ILU_REF_COC_OTR_ST_demanda_iluminacion]
    porcentaje_tecnologia_para_iluminacion                    : list[EDIF_RES_ILU_REF_COC_OTR_ST_porcentaje_tecnologia_para_iluminacion]
    demanda_total_por_refrigeracion                           : list[EDIF_RES_ILU_REF_COC_OTR_ST_demanda_total_por_refrigeracion]
    porcentaje_de_neveras_mas_eficientes                      : list[EDIF_RES_ILU_REF_COC_OTR_ST_porcentaje_de_neveras_mas_eficientes]
    demanda_coccion_con_gas_natural                           : list[EDIF_RES_ILU_REF_COC_OTR_ST_demanda_coccion_con_gas_natural]
    porcentaje_de_estufas_con_eficiencia_mejorada             : list[EDIF_RES_ILU_REF_COC_OTR_ST_porcentaje_de_estufas_con_eficiencia_mejorada]
    demanda_para_coccion_con_glp                              : list[EDIF_RES_ILU_REF_COC_OTR_ST_demanda_para_coccion_con_glp]
    reduccion_total_de_la_demanda_de_energia_electrica        : list[EDIF_RES_ILU_REF_COC_OTR_ST_reduccion_total_de_la_demanda_de_energia_electrica]
    potencia_instalada_para_autogeneracion_solar_fotovoltaica : list[EDIF_RES_ILU_REF_COC_OTR_ST_potencia_instalada_para_autogeneracion_solar_fotovoltaica]

    class Config:
        orm_mode : True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class EDIF_RES_ILU_REF_COC_OTR_SF_demanda_energia_electrica_por_uso(BaseModel):
    """Supuestos Fijos demanda_energia_electrica_por_uso"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_demanda_gas_natural_por_uso(BaseModel):
    """Supuestos Fijos demanda_gas_natural_por_uso"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_demanda_glp_por_uso(BaseModel):
    """Supuestos Fijos demanda_glp_por_uso"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_energia_electrica(BaseModel):
    """Supuestos Fijos tenencia_por_uso_energia_electrica"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_gas_natural(BaseModel):
    """Supuestos Fijos tenencia_por_uso_gas_natural"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_glp(BaseModel):
    """Supuestos Fijos tenencia_por_uso_glp"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_numero_de_bombillos_por_hogar(BaseModel):
    """Supuestos Fijos numero_de_bombillos_por_hogar"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_porcentaje_de_tenencia_refrigeradores(BaseModel):
    """Supuestos Fijos porcentaje_de_tenencia_refrigeradores"""

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


class EDIF_RES_ILU_REF_COC_OTR_SF_horas_utiles_de_operacion_de_la_autogeneracion_solar_fotovoltaica(BaseModel):
    """Supuestos Fijos horas_utiles_de_operacion_de_la_autogeneracion_solar_fotovoltaica"""

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
    
    demanda_energia_electrica_por_uso     : list[EDIF_RES_ILU_REF_COC_OTR_SF_demanda_energia_electrica_por_uso]
    demanda_gas_natural_por_uso           : list[EDIF_RES_ILU_REF_COC_OTR_SF_demanda_gas_natural_por_uso]
    demanda_glp_por_uso                   : list[EDIF_RES_ILU_REF_COC_OTR_SF_demanda_glp_por_uso]
    tenencia_por_uso_energia_electrica    : list[EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_energia_electrica]
    tenencia_por_uso_gas_natural          : list[EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_gas_natural]
    tenencia_por_uso_glp                  : list[EDIF_RES_ILU_REF_COC_OTR_SF_tenencia_por_uso_glp]
    numero_de_bombillos_por_hogar         : list[EDIF_RES_ILU_REF_COC_OTR_SF_numero_de_bombillos_por_hogar]
    porcentaje_de_tenencia_refrigeradores : list[EDIF_RES_ILU_REF_COC_OTR_SF_porcentaje_de_tenencia_refrigeradores]
    horas_utiles_de_operacion_de_la_autogeneracion_solar_fotovoltaica : list[EDIF_RES_ILU_REF_COC_OTR_SF_horas_utiles_de_operacion_de_la_autogeneracion_solar_fotovoltaica]
    
    class Config:
        orm_mode : True

# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    energia_producida_y_requerida = 'energia_producida_y_requerida'


class EDIF_RES_ILU_REF_COC_OTR_SALIDAS(BaseModel):
    """energia_producida_y_requerida"""

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


class SALIDAS(BaseModel):
    """Salidas"""
    
    salidas : list[EDIF_RES_ILU_REF_COC_OTR_SALIDAS]

    class Config:
        orm_mode : True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class EDIF_RES_ILU_REF_COC_OTR_EMISIONES(BaseModel):
    """emisiones_de_gases_efecto_invernadero"""

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
    emisiones : list[EDIF_RES_ILU_REF_COC_OTR_EMISIONES]

    class Config:
        orm_mode : True
    