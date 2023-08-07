from pydantic import BaseModel
from enum import IntEnum, Enum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4

# Energia - Combustibles fosiles

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ST_name(str, Enum):
    eficiencia_energetica_en_la_refinacion_de_crudo  = 'eficiencia_energetica_en_la_refinacion_de_crudo'
    

class ENER_CombFosil_ST_eficiencia_energetica_en_la_refinacion_de_crudo(BaseModel):
    """Supuestos de Trayectoria eficiencia_energetica_en_la_refinacion_de_crudo"""

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
    
    eficiencia_energetica_en_la_refinacion_de_crudo  : list[ENER_CombFosil_ST_eficiencia_energetica_en_la_refinacion_de_crudo]
    
    class Config:
        orm_mode : True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class ENER_CombFosil_SF_produccion_de_hidrocarburos(BaseModel):
    """Supuestos Fijos produccion_de_hidrocarburos
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


class ENER_CombFosil_SF_produccion_de_carbon(BaseModel):
    """Supuestos Fijos produccion_de_carbon
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


class ENER_CombFosil_SF_factores_de_emision_carbon(BaseModel):
    """Supuestos Fijos factores_de_emision_carbon
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class ENER_CombFosil_SF_no_de_pozos(BaseModel):
    """Supuestos Fijos no_de_pozos
    """

    topic       : str
    tipo        : str
    fuente      : str
    valor       : float | None
    unidad      : str


class ENER_CombFosil_SF_datos_de_la_produccion_de_crudo_en_el_ano_base(BaseModel):
    """Supuestos Fijos datos_de_la_produccion_de_crudo_en_el_ano_BaseModel
    """

    topic       : str
    tipo        : str
    valor       : float | None
    total_crudo : float | None
    unidad      : str


class ENER_CombFosil_SF_datos_de_la_produccion_de_gas_natural_en_el_ano_base(BaseModel):
    """Supuestos Fijos datos_de_la_produccion_de_gas_natural_en_el_ano_BaseModel
    """

    topic       : str
    tipo        : str
    valor       : float | None
    total_crudo : float | None
    unidad      : str


class ENER_CombFosil_SF_consumo_de_energeticos(BaseModel):
    """Supuestos Fijos consumo_de_energeticos
    """

    topic       : str
    tipo        : str
    valor       : float | None
    unidad      : str


class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """

    produccion_de_hidrocarburos                               : list[ENER_CombFosil_SF_produccion_de_hidrocarburos]
    produccion_de_carbon                                      : list[ENER_CombFosil_SF_produccion_de_carbon]
    factores_de_emision_carbon                                : list[ENER_CombFosil_SF_factores_de_emision_carbon]
    no_de_pozos                                               : list[ENER_CombFosil_SF_no_de_pozos]
    datos_de_la_produccion_de_crudo_en_el_ano_base            : list[ENER_CombFosil_SF_datos_de_la_produccion_de_crudo_en_el_ano_base]
    datos_de_la_produccion_de_gas_natural_en_el_ano_base      : list[ENER_CombFosil_SF_datos_de_la_produccion_de_gas_natural_en_el_ano_base]
    consumo_de_energeticos                                    : list[ENER_CombFosil_SF_consumo_de_energeticos]

    class Config:
        orm_mode : True


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class Salidas_name(str, Enum):
    salidas_combustibles_fosiles_producidos                      = 'salidas_combustibles_fosiles_producidos'
    salidas_consumo_de_combustibles_fosiles_por_el_propio_sector = 'salidas_consumo_de_combustibles_fosiles_por_el_propio_sector'
    salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos  = 'salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos'


class _ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos(BaseModel):
    """salidas_combustibles_fosiles_producidos"""

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


class _ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector(BaseModel):
    """salidas_consumo_de_combustibles_fosiles_por_el_propio_sector"""

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


class _ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos(BaseModel):
    """salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos"""

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


class ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos(BaseModel):
    """salidas_combustibles_fosiles_producidos"""

    salidas_combustibles_fosiles_producidos : list[_ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos]

    class Config:
        orm_mode : True


class ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector(BaseModel):
    """salidas_consumo_de_combustibles_fosiles_por_el_propio_sector"""

    salidas_consumo_de_combustibles_fosiles_por_el_propio_sector : list[_ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector]

    class Config:
        orm_mode : True


class ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos(BaseModel):
    """salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos"""

    salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos  : list[_ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos]

    class Config:
        orm_mode : True


class SALIDAS(BaseModel):
    """Salidas
    """
    
    salidas_combustibles_fosiles_producidos                      : list[_ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos]
    salidas_consumo_de_combustibles_fosiles_por_el_propio_sector : list[_ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_el_propio_sector]
    salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos  : list[_ENER_CombFosil_SALIDAS_consumo_de_combustibles_fosiles_por_sectores_ajenos]

    class Config:
        orm_mode : True


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class Emisiones_name(str, Enum):
    emisiones_produccion = 'emisiones_produccion'
    emisiones_consumo    = 'emisiones_consumo'


class _ENER_CombFosil_EMISIONES_produccion(BaseModel):
    """emisiones_produccion"""

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


class _ENER_CombFosil_EMISIONES_consumo(BaseModel):
    """emisiones_consumo"""

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


class ENER_CombFosil_EMISIONES_produccion(BaseModel):
    """emisiones_produccion"""

    emisiones_produccion : list[_ENER_CombFosil_EMISIONES_produccion]

    class Config:
        orm_mode : True


class ENER_CombFosil_EMISIONES_consumo(BaseModel):
    """emisiones_consumo"""

    emisiones_consumo    : list[_ENER_CombFosil_EMISIONES_consumo]

    class Config:
        orm_mode : True


class EMISIONES(BaseModel):
    """Emisiones - emisiones_gases_efecto_invernadero
    """
    emisiones_produccion : list[_ENER_CombFosil_EMISIONES_produccion]
    emisiones_consumo    : list[_ENER_CombFosil_EMISIONES_consumo]

    class Config:
        orm_mode : True
