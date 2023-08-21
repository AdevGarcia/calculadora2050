from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Edificaciones Comerciales Usos Termicos y Equipamiento

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    reduccion_por_eficiencia_en_la_iluminacion = 'reduccion_por_eficiencia_en_la_iluminacion'
    reduccion_por_eficiencia_en_refrigeracion  = 'reduccion_por_eficiencia_en_refrigeracion'
    reduccion_por_eficiencia_en_usos_termicos  = 'reduccion_por_eficiencia_en_usos_termicos'


class EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_iluminacion(BaseModel):
    """Supuestos de Trayectoria reduccion_por_eficiencia_en_la_iluminacion
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


class EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_refrigeracion(BaseModel):
    """Supuestos de Trayectoria reduccion_por_eficiencia_en_refrigeracion
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


class EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_usos_termicos(BaseModel):
    """Supuestos de Trayectoria reduccion_por_eficiencia_en_usos_termicos
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
    
    reduccion_por_eficiencia_en_la_iluminacion : list[EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_iluminacion]
    reduccion_por_eficiencia_en_refrigeracion  : list[EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_refrigeracion]
    reduccion_por_eficiencia_en_usos_termicos  : list[EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_usos_termicos]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class EDIF_COM_USOS_TERM_EQUIP_SF_consumo_total_de_energia_por_uso(BaseModel):
    """Supuestos Fijos consumo_total_de_energia_por_uso
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


class EDIF_COM_USOS_TERM_EQUIP_SF_participacion_usos_en_equipamiento(BaseModel):
    """Supuestos Fijos participacion_usos_en_equipamiento
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


class EDIF_COM_USOS_TERM_EQUIP_SF_part_energeticos_usos_termicos(BaseModel):
    """Supuestos Fijos participacion_de_los_energeticos_en_los_usos_termicos
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


class EDIF_COM_USOS_TERM_EQUIP_SF_participacion_energ_equipamiento(BaseModel):
    """Supuestos Fijos participacion_de_los_energeticos_en_equipamiento
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


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """
    
    consumo_total_de_energia_por_uso                      : list[EDIF_COM_USOS_TERM_EQUIP_SF_consumo_total_de_energia_por_uso]
    participacion_usos_en_equipamiento                    : list[EDIF_COM_USOS_TERM_EQUIP_SF_participacion_usos_en_equipamiento]
    participacion_de_los_energeticos_en_los_usos_termicos : list[EDIF_COM_USOS_TERM_EQUIP_SF_part_energeticos_usos_termicos]
    participacion_de_los_energeticos_en_equipamiento      : list[EDIF_COM_USOS_TERM_EQUIP_SF_participacion_energ_equipamiento]
    
    class ConfigDict:
        from_attributes = True


####################################################################################
#######                               Salidas                                #######
####################################################################################

class Salidas_name(str, Enum):
    energia_producida_y_requerida = 'energia_producida_y_requerida'


class EDIF_COM_USOS_TERM_EQUIP_SALIDAS(BaseModel):
    """energia_producida_y_requerida"""

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
    """Salidas"""
    
    salidas : list[EDIF_COM_USOS_TERM_EQUIP_SALIDAS]

    class ConfigDict:
        from_attributes = True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones = 'emisiones'


class EDIF_COM_USOS_TERM_EQUIP_EMISIONES(BaseModel):
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


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones : list[EDIF_COM_USOS_TERM_EQUIP_EMISIONES]

    class ConfigDict:
        from_attributes = True
