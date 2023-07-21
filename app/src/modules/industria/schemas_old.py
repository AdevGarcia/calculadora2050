from pydantic import BaseModel
from enum import Enum, IntEnum


class Trayectoria(IntEnum):
    """ Trayectorias
    """
    tr1 = 1
    tr2 = 2
    tr3 = 3
    tr4 = 4
    
    
class Unidades(str, Enum):
    """ Unidades
    """
    admiensional = ''
    porcentaje   = '%'
    t = 't'
    kg = 'kg'
    pj = 'Pj'
    twh = 'TWh'
    GgCO2_e = 'GgCO2_e'
    

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class Topic_ST(str, Enum):
    """ Topics Supuestos de Trayectoria
    """
    ef_energ_reduc_consumo                  = 'ef_energ_reduc_consumo'
    ef_crecim_autogener_cogener             = 'ef_crecim_autogener_cogener'
    ef_energ_reduc_consumo_ladrilleras      = 'ef_energ_reduc_consumo_ladrilleras'
    ef_crecim_autogener_cogener_ladrilleras = 'ef_crecim_autogener_cogener_ladrilleras'
    sustitucion_sao                         = 'sustitucion_sao'
    proc_productivos_sostenibles            = 'proc_productivos_sostenibles'


class Tipo(str, Enum):
    cemento            = 'cemento'
    hierro_no_ferrosos = 'hierro_no_ferrosos'
    papel              = 'papel'
    quimicos           = 'quimicos'
    alimentos_bebidas  = 'alimentos_bebidas'
    textil             = 'textil'
    otros_ptp          = 'otros_ptp'
    
    refrigeracion_aire_acondic  = 'refrigeracion_aire_acondic'
    agentes_espumantes          = 'agentes_espumantes'
    proteccion_contra_incendios = 'proteccion_contra_incendios'
    aerosoles                   = 'aerosoles'
    solventes                   = 'solventes'
    otros                       = 'otros'
    
    produccion_cemento         = 'produccion_cemento'
    produccion_cal             = 'produccion_cal'
    produccion_vidrio          = 'produccion_vidrio'
    produccion_amoniaco        = 'produccion_amoniaco'
    produccion_acido_nitrico   = 'produccion_acido_nitrico'
    produccion_hierro_acero    = 'produccion_hierro_acero'
    produccion_ferroaleaciones = 'produccion_ferroaleaciones'
    produccion_plomo           = 'produccion_plomo'
    produccion_pulpa_papel     = 'produccion_pulpa_papel'
    produccion_alimentacion    = 'produccion_alimentacion'
    
    aserrin     = 'aserrin'
    biomasa     = 'biomasa'
    cisco_cafe  = 'cisco_cafe'
    carbon      = 'carbon'
    gas_natural = 'gas_natural'
    
    hierro_acero = 'hierro_acero'
    ladrilleras  = 'ladrilleras'
    
    autogeneracion = 'autogeneracion'
    cogeneracion   = 'cogeneracion'
    
    carbon_mineral = 'carbon_mineral'
    diesel_oil     = 'diesel_oil'
    hidraulicos    = 'hidraulicos'
    fuel_oil       = 'fuel_oil'


### Eficiencia energética- % de reducción de consumo energético

class ST_EF_ENERG_REDUC_CONSUMO(BaseModel):
    """Supuestos de Trayectoria Eficiencia energética - % de reducción de consumo energético
    """
    
    topic       : Topic_ST = Topic_ST.ef_energ_reduc_consumo
    tipo        : Tipo
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : Unidades | None = Unidades.porcentaje


### Eficiencia energética- % crecimiento de autogeneración y cogeneración 

class ST_EF_CRECIM_AUTOGENER_COGENER(BaseModel):
    """Supuestos de Trayectoria Eficiencia energética - % crecimiento de autogeneración y cogeneración 
    """
    
    topic       : Topic_ST = Topic_ST.ef_crecim_autogener_cogener
    tipo        : Tipo
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : Unidades | None = Unidades.porcentaje


### Eficiencia energética- % de reducción de consumo energético (Ladrilleras)

class ST_EF_ENERG_REDUC_CONSUMO_LADRILLERAS(BaseModel):
    """Supuestos de Trayectoria Eficiencia energética - % de reducción de consumo energético (Ladrilleras)
    """
    
    topic       : Topic_ST = Topic_ST.ef_energ_reduc_consumo_ladrilleras
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : Unidades | None = Unidades.porcentaje


### Eficiencia energética- % de autogeneración y cogeneración y co-generación (Ladrilleras)

class ST_EF_CRECIM_AUTOGENER_COGENER_LADRILLERAS(BaseModel):
    """Supuestos de Trayectoria Eficiencia energética - % crecimiento de autogeneración y cogeneración (Ladrilleras)
    """
    
    topic       : Topic_ST = Topic_ST.ef_crecim_autogener_cogener_ladrilleras
    trayectoria : Trayectoria
    y2018       : float | None
    y2020       : float | None
    y2025       : float | None
    y2030       : float | None
    y2035       : float | None
    y2040       : float | None
    y2045       : float | None
    y2050       : float | None
    unidad      : Unidades | None = Unidades.porcentaje


### Sustitución de SAO

class ST_SUSTITUCION_SAO(BaseModel):
    """Supuestos de Trayectoria Sustitución de SAO
    """
    
    topic       : Topic_ST = Topic_ST.sustitucion_sao
    tipo        : Tipo
    trayectoria : Trayectoria
    valor       : float | None
    unidad      : Unidades | None = Unidades.porcentaje


### Procesos productivos sostenibles

class ST_PROC_PRODUCTIVOS_SOSTENIBLES(BaseModel):
    """Supuestos de Trayectoria Procesos productivos sostenibles
    """
    
    topic       : Topic_ST = Topic_ST.proc_productivos_sostenibles
    tipo        : Tipo
    trayectoria : Trayectoria
    valor       : float | None
    unidad      : Unidades | None = Unidades.porcentaje


class SUPUESTOS_TRAYECTORIA(BaseModel):
    """Supuestos de trayectoria con todos los topics
    """
    
    ef_energ_reduc_consumo                  : list[ST_EF_ENERG_REDUC_CONSUMO]
    ef_crecim_autogener_cogener             : list[ST_EF_CRECIM_AUTOGENER_COGENER]
    ef_energ_reduc_consumo_ladrilleras      : list[ST_EF_ENERG_REDUC_CONSUMO_LADRILLERAS]
    ef_crecim_autogener_cogener_ladrilleras : list[ST_EF_CRECIM_AUTOGENER_COGENER_LADRILLERAS]
    sustitucion_sao                         : list[ST_SUSTITUCION_SAO]
    proc_productivos_sostenibles            : list[ST_PROC_PRODUCTIVOS_SOSTENIBLES]

    class Config:
        orm_mode : True


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class Topic_SF(str, Enum):
    """ Topics Supuestos Fijos
    """
    prod_anual_materiales                = 'prod_anual_materiales'
    prod_anual_ladrillos                 = 'prod_anual_ladrillos'
    indice_consumo                       = 'indice_consumo'
    distrib_tipo_combustible_ladrilleras = 'distrib_tipo_combustible_ladrilleras'
    uso_energetico_combustible           = 'uso_energetico_combustible'
    factor_utilizacion_autogeneracion    = 'factor_utilizacion_autogeneracion'
    capacidad_instalada_autogeneracion   = 'capacidad_instalada_autogeneracion'
    excedentes_autogeneracion            = 'excedentes_autogeneracion'
    capacidad_instalada_cogeneracion     = 'capacidad_instalada_cogeneracion'
    excedentes_cogeneracion              = 'excedentes_cogeneracion'
    emision_sao                          = 'emision_sao'
    

class Fuente_SF(str, Enum):
    
    bagazo           = 'bagazo'
    carbon_mineral   = 'carbon_mineral'
    gas_natural      = 'gas_natural'
    lena             = 'lena'
    petroleo         = 'petroleo'
    residuos         = 'residuos'
    gasolina         = 'gasolina'
    diesel_oil       = 'diesel_oil'
    carbon_lena      = 'carbon_lena'
    coque            = 'coque'
    fuel_oil         = 'fuel_oil'
    glp              = 'glp'
    queroseno        = 'queroseno'
    electricidad_SIN = 'electricidad_SIN'
    Hidrogeno_verde  = 'Hidrogeno_verde'
    hidrogeno_azul   = 'hidrogeno_azul'
    
    cemento = 'cemento'
    hierro_acero = 'hierro_acero'
    papel = 'papel'
    quimicos = 'quimicos'
    alimentos_bebidas = 'alimentos_bebidas'
    textil = 'textil'
    ladrilleras = 'ladrilleras'
    otros_ptp = 'otros_ptp'
    otros = 'otros'




### Producción  anual de materiales 

class SF_PROD_ANUAL_MATERIALES(BaseModel):
    """Supuestos Fijos Producción  anual de materiales 
    """
    
    topic  : Topic_SF = Topic_SF.prod_anual_materiales
    tipo   : Tipo
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades | None = Unidades.t


### Producción anual de ladrillos 

class SF_PROD_ANUAL_LADRILLOS(BaseModel):
    """Supuestos Fijos Producción anual de ladrillos 
    """
    
    topic  : Topic_SF = Topic_SF.prod_anual_ladrillos
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades | None = Unidades.t


### Indice de consumo

class SF_INDICE_CONSUMO(BaseModel):
    """Supuestos Fijos Producción anual de ladrillos 
    """
    
    topic  : Topic_SF = Topic_SF.indice_consumo
    valor  : float | None
    unidad : Unidades | None = Unidades.kg


### Distribución según tipo de combustible - Ladrilleras

class SF_DISTRIB_TIPO_COMBUSTIBLE_LADRILLERAS(BaseModel):
    """Supuestos Fijos Distribución según tipo de combustible - Ladrilleras
    """
    
    topic  : Topic_SF = Topic_SF.distrib_tipo_combustible_ladrilleras
    tipo   : Tipo
    valor  : float | None
    unidad : Unidades | None = Unidades.porcentaje


### Uso energético por combustible

class SF_USO_ENERGETICO_COMBUSTIBLE(BaseModel):
    """Supuestos Fijos Uso energético por combustible
    """
    
    topic  : Topic_SF = Topic_SF.uso_energetico_combustible
    tipo   : Tipo
    fuente : Fuente_SF
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades | None = Unidades.pj


### Factor de utilización de autogeneración y cogeneración

class SF_FACTOR_UTILIZACION_AUTOGENERACION(BaseModel):
    """Supuestos Fijos Factor de utilización de autogeneración y cogeneración
    """
    
    topic  : Topic_SF = Topic_SF.factor_utilizacion_autogeneracion
    tipo   : Tipo
    valor  : float | None
    unidad : Unidades | None = Unidades.admiensional


### Capacidad instalada de auto-generación 

class SF_CAPACIDAD_INSTALADA_AUTOGENERACION(BaseModel):
    """Supuestos Fijos Capacidad instalada de auto-generación 
    """
    
    topic  : Topic_SF = Topic_SF.capacidad_instalada_autogeneracion
    tipo   : Tipo
    fuente : Fuente_SF
    valor  : float | None
    unidad : Unidades | None = Unidades.twh


### Excedentes de autogeneración

class SF_EXCEDENTES_AUTOGENERACION(BaseModel):
    """Supuestos Fijos Excedentes de autogeneración
    """
    
    topic  : Topic_SF = Topic_SF.excedentes_autogeneracion
    tipo   : Tipo
    fuente : Fuente_SF
    valor  : float | None
    unidad : Unidades | None = Unidades.twh


### Capacidad instalada de cogeneración 

class SF_CAPACIDAD_INSTALADA_COGENERACION(BaseModel):
    """Supuestos Fijos Capacidad instalada de cogeneración 
    """
    
    topic  : Topic_SF = Topic_SF.capacidad_instalada_cogeneracion
    tipo   : Tipo
    fuente : Fuente_SF
    valor  : float | None
    unidad : Unidades | None = Unidades.twh


### Excedentes de cogeneración 

class SF_EXCEDENTES_COGENERACION(BaseModel):
    """Supuestos Fijos Excedentes de cogeneración 
    """
    
    topic  : Topic_SF = Topic_SF.excedentes_cogeneracion
    tipo   : Tipo
    fuente : Fuente_SF
    valor  : float | None
    unidad : Unidades | None = Unidades.twh


### Emisión de SAO 

class SF_EMISION_SAO(BaseModel):
    """Supuestos Fijos Emisión de SAO 
    """
    
    topic  : Topic_SF = Topic_SF.emision_sao
    tipo   : Tipo
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades | None = Unidades.GgCO2_e

class SUPUESTOS_FIJOS(BaseModel):
    """Supuestos fijos con todos los topics
    """
    
    prod_anual_materiales                : list[SF_PROD_ANUAL_MATERIALES]
    prod_anual_ladrillos                 : list[SF_PROD_ANUAL_LADRILLOS]
    indice_consumo                       : list[SF_INDICE_CONSUMO]
    distrib_tipo_combustible_ladrilleras : list[SF_DISTRIB_TIPO_COMBUSTIBLE_LADRILLERAS]
    uso_energetico_combustible           : list[SF_USO_ENERGETICO_COMBUSTIBLE]
    factor_utilizacion_autogeneracion    : list[SF_FACTOR_UTILIZACION_AUTOGENERACION]
    capacidad_instalada_autogeneracion   : list[SF_CAPACIDAD_INSTALADA_AUTOGENERACION]
    excedentes_autogeneracion            : list[SF_EXCEDENTES_AUTOGENERACION]
    capacidad_instalada_cogeneracion     : list[SF_CAPACIDAD_INSTALADA_COGENERACION]
    excedentes_cogeneracion              : list[SF_EXCEDENTES_COGENERACION]
    emision_sao                          : list[SF_EMISION_SAO]
    
    class Config:
        orm_mode : True


####################################################################################
#######                         Supuestos de Costos                          #######
####################################################################################


# class Topic_SC(str, Enum):
#     """ Topics Supuestos de Costos
#     """
#     incremental_reduccion       = 'incremental_reduccion'
#     indice_uso_energ_industria  = 'indice_uso_energ_industria'
#     capex_eficiencia_energetica = 'capex_eficiencia_energetica'
#     opex_eficiencia_energetica  = 'opex_eficiencia_energetica'


# class Costos(str, Enum):
#     alto  = 'alto'
#     medio = 'medio'
#     bajo  = 'bajo'


# class Unidades_SC(str, Enum):
#     MMCOP    = '$MMCOP'
#     porcentaje = '%'
    

# class Tipo_SC(str, Enum):
#     cemento           = 'cemento'
#     hierro_no_ferroso = 'hierro_no_ferroso'
#     papel             = 'papel'
#     quimicos          = 'quimicos'
#     alimentos_bebidas = 'alimentos_bebidas'
#     textil            = 'textil'
#     otros             = 'otros'
#     ladrilleras       = 'ladrilleras'
    

# ## Costo Incremental de la Reducción

# class SC_INCREMENTAL_REDUCCION(BaseModel):
#     """Supuestos de Costos - Costo Incremental de la Reducción
#     """
   
#     topic                      : Topic_SC = Topic_SC.incremental_reduccion
#     trayectoria : Trayectoria
#     tipo                       : Tipo_SC # cemento, hierro_no_ferroso, papel, quimicos, alimentos_bebidas, textil, otros, ladrilleras
#     costo                      : Costos
#     gasto_capex_neto           : float | None
#     gasto_opex_sin_combustible : float | None
#     unidad                     : Unidades_SC | None = Unidades_SC.MMCOP # $MMCOP


# ## Índice de Uso energético por Industria

# class SC_INDICE_USO_ENERG_INDUSTRIA(BaseModel):
#     """Supuestos de Costos - Índice de Uso energético por Industria
#     """
    
#     topic  : Topic_SC = Topic_SC.indice_uso_energ_industria
#     trayectoria : Trayectoria
#     tipo   : Tipo_SC # cemento, hierro_no_ferroso, papel, quimicos, alimentos_bebidas, textil, otros, ladrilleras
#     y2018  : float | None
#     y2020  : float | None
#     y2025  : float | None
#     y2030  : float | None
#     y2035  : float | None
#     y2040  : float | None
#     y2045  : float | None
#     y2050  : float | None
#     unidad : Unidades_SC | None = Unidades_SC.porcentaje # %


# ## Costos de Capital Eficiencia energética (reducción de consumo energético)

# class SC_EFICIENCIA_ENERGETICA_CAPEX(BaseModel):
#     """Supuestos de Costos - Costos de Capital Eficiencia energética (reducción de consumo energético)
#     """
  
#     topic  : Topic_SC = Topic_SC.capex_eficiencia_energetica
#     trayectoria : Trayectoria
#     tipo   : Tipo_SC # cemento, hierro_no_ferroso, papel, quimicos, alimentos_bebidas, textil, otros, ladrilleras
#     costo  : Costos
#     y2018  : float | None
#     y2020  : float | None
#     y2025  : float | None
#     y2030  : float | None
#     y2035  : float | None
#     y2040  : float | None
#     y2045  : float | None
#     y2050  : float | None
#     unidad : Unidades_SC | None = Unidades_SC.MMCOP # $MMCOP

# ## Costos de O&M Eficiencia Energética (reducción de consumo energético) 

# class SC_EFICIENCIA_ENERGETICA_OPEX(BaseModel):
#     """Supuestos de Costos - Costos de O&M Eficiencia Energética (reducción de consumo energético) 
#     """
    
#     topic  : Topic_SC = Topic_SC.opex_eficiencia_energetica
#     trayectoria : Trayectoria
#     tipo   : Tipo_SC # cemento, hierro_no_ferroso, papel, quimicos, alimentos_bebidas, textil, otros, ladrilleras
#     costo  : Costos
#     y2018  : float | None
#     y2020  : float | None
#     y2025  : float | None
#     y2030  : float | None
#     y2035  : float | None
#     y2040  : float | None
#     y2045  : float | None
#     y2050  : float | None
#     unidad : Unidades_SC | None = Unidades_SC.MMCOP # $MMCOP
    
    
# class SUPUESTOS_COSTO(BaseModel):
#     """Supuestos fijos con todos los topics
#     """
    
#     incremental_reduccion       : list[SC_INCREMENTAL_REDUCCION]
#     indice_uso_energ_industria  : list[SC_INDICE_USO_ENERG_INDUSTRIA]
#     capex_eficiencia_energetica : list[SC_EFICIENCIA_ENERGETICA_CAPEX]
#     opex_eficiencia_energetica  : list[SC_EFICIENCIA_ENERGETICA_OPEX]
    
#     class Config:
#         orm_mode : True


####################################################################################
#######                               Salidas                                #######
####################################################################################

    
class Topic_SALIDAS(str, Enum):
    """ Topics Salidas
    """
    por_combustible_energia_requerida = 'por_combustible_energia_requerida'
    por_combustible_energia_producida_autogeneracion_cogeneracion = 'por_combustible_energia_producida_autogeneracion_cogeneracion'
    por_combustible_balance_total_energia_requerida = 'por_combustible_balance_total_energia_requerida'
    por_tipo_industria_energia_requerida = 'por_tipo_industria_energia_requerida'
    por_tipo_industria_energia_producida_autogeneracion_cogeneracion = 'por_tipo_industria_energia_producida_autogeneracion_cogeneracion'
    por_tipo_industria_balance_total_energia_requerida = 'por_tipo_industria_balance_total_energia_requerida'


class Unidades_SALIDAS(str, Enum):
    TWh = 'TWh'

class Tipo_Salidas_Combustible(str, Enum):
    bagazo           = 'bagazo'
    carbon_mineral   = 'carbon_mineral'
    gas_natural      = 'gas_natural'
    lena             = 'lena'
    petroleo         = 'petroleo'
    residuos         = 'residuos'
    gasolina         = 'gasolina'
    diesel           = 'diesel'
    carbon_lena      = 'carbon_lena'
    coque            = 'coque'
    fuel_oil         = 'fuel_oil'
    glp              = 'glp'
    queroseno        = 'queroseno'
    electricidad_sin = 'electricidad_sin'
    hidraulico       = 'hidraulico'
    hidrogeno_verde  = 'hidrogeno_verde'
    hidrogeno_azul   = 'hidrogeno_azul'
    
    total_electricidad         = 'total_electricidad'
    total_combustibles_fosiles = 'total_combustibles_fosiles'
    total_otros_combustibles   = 'total_otros_combustibles'
    total                      = 'total'
    total_inyectado_red        = 'total_inyectado_red'


class Tipo_Salidas_Industria(str, Enum):
    cemento           = 'cemento'
    hierro_acero      = 'hierro_acero'
    papel             = 'papel'
    quimicos          = 'quimicos'
    alimentos_bebidas = 'alimentos_bebidas'
    textil            = 'textil'
    ladrilleras       = 'ladrilleras'
    otros             = 'otros'


class SALIDAS_TIPO_COMBUSTIBLE_ENERGIA_REQUERIDA(BaseModel):
    """Salidas - Por combustible, Energia requerida
    """
    
    topic  : Topic_SALIDAS = Topic_SALIDAS.por_combustible_energia_requerida
    trayectoria : Trayectoria
    tipo   : Tipo_Salidas_Combustible
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_SALIDAS | None = Unidades_SALIDAS.TWh


class SALIDAS_TIPO_COMBUSTIBLE_PRODUCT_AUTOGEN_COGEN(BaseModel):
    """Salidas - Por combustible, Energía producida por autogeneración y cogeneración
    """
    
    topic  : Topic_SALIDAS = Topic_SALIDAS.por_combustible_energia_producida_autogeneracion_cogeneracion
    trayectoria : Trayectoria
    tipo   : Tipo_Salidas_Combustible
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_SALIDAS | None = Unidades_SALIDAS.TWh


class SALIDAS_TIPO_COMBUSTIBLE_BALANCE_TOTAL_ENERG_REQUERIDA(BaseModel):
    """Salidas - Por combustible, Balance total de la energía requerida
    """
   
    topic  : Topic_SALIDAS = Topic_SALIDAS.por_combustible_balance_total_energia_requerida
    trayectoria : Trayectoria
    tipo   : Tipo_Salidas_Combustible
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_SALIDAS | None = Unidades_SALIDAS.TWh


class SALIDAS_TIPO_INDUSTRIA_ENERGIA_REQUERIDA(BaseModel):
    """Salidas - Por tipo de industria, Energia requerida
    """
   
    topic  : Topic_SALIDAS = Topic_SALIDAS.por_tipo_industria_energia_requerida
    trayectoria : Trayectoria
    tipo   : Tipo_Salidas_Industria
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_SALIDAS | None = Unidades_SALIDAS.TWh


class SALIDAS_TIPO_INDUSTRIA_PRODUCT_AUTOGEN_COGEN(BaseModel):
    """Salidas - Por tipo de industria, Energía producida por autogeneración y cogeneración
    """
 
    topic  : Topic_SALIDAS = Topic_SALIDAS.por_tipo_industria_energia_producida_autogeneracion_cogeneracion
    trayectoria : Trayectoria
    tipo   : Tipo_Salidas_Industria
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_SALIDAS | None = Unidades_SALIDAS.TWh


class SALIDAS_TIPO_INDUSTRIA_BALANCE_TOTAL_ENERG_REQUERIDA(BaseModel):
    """Salidas - Por combustible, Balance total de la energía requerida
    """

    topic  : Topic_SALIDAS = Topic_SALIDAS.por_tipo_industria_balance_total_energia_requerida
    trayectoria : Trayectoria
    tipo   : Tipo_Salidas_Industria
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_SALIDAS | None = Unidades_SALIDAS.TWh
    

class SALIDAS(BaseModel):
    """Salidas
    """
    
    por_combustible_energia_requerida : list[SALIDAS_TIPO_COMBUSTIBLE_ENERGIA_REQUERIDA]
    por_combustible_energia_producida_autogeneracion_cogeneracion : list[SALIDAS_TIPO_COMBUSTIBLE_PRODUCT_AUTOGEN_COGEN]
    por_combustible_balance_total_energia_requerida : list[SALIDAS_TIPO_COMBUSTIBLE_BALANCE_TOTAL_ENERG_REQUERIDA]
    por_tipo_industria_energia_requerida : list[SALIDAS_TIPO_INDUSTRIA_ENERGIA_REQUERIDA]
    por_tipo_industria_energia_producida_autogeneracion_cogeneracion : list[SALIDAS_TIPO_INDUSTRIA_PRODUCT_AUTOGEN_COGEN]
    por_tipo_industria_balance_total_energia_requerida : list[SALIDAS_TIPO_INDUSTRIA_BALANCE_TOTAL_ENERG_REQUERIDA]
    
    class Config:
        orm_mode : True


####################################################################################
#######                               Emisiones                              #######
####################################################################################

class Topic_EMISIONES(str, Enum):
    emisiones_gei_por_industria        = 'emisiones_gei_por_industria'
    emisiones_por_consumo_bagazo_otros = 'emisiones_por_consumo_bagazo_otros'


class Unidades_EMISIONES(str, Enum):
    Mt_CO2e = 'Mt_CO2e'


class Tipo_EMISIONES(str, Enum):
    cemento           = 'cemento'
    hierro_acero      = 'hierro_acero'
    papel             = 'papel'
    quimicos          = 'quimicos'
    alimentos_bebidas = 'alimentos_bebidas'
    textil            = 'textil'
    ladrilleras       = 'ladrilleras'
    otros             = 'otros'
    
    emisiones_sao = 'emisiones_sao'

    emisiones_provenientes_agricultura = 'emisiones_provenientes_agricultura'
    

class EMISIONES_GASES_EFECTO_INVERNADERO(BaseModel):
    """Salidas - Emisiones de efecto invernadero
    """
    
    topic  : Topic_EMISIONES = Topic_EMISIONES.emisiones_gei_por_industria
    trayectoria : Trayectoria
    tipo   : Tipo_EMISIONES
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_EMISIONES | None = Unidades_EMISIONES.Mt_CO2e


class EMISIONES_CONSUMO_BAGAZO_OTROS(BaseModel):
    """Salidas - Emisiones de efecto invernadero
    """

    topic  : Topic_EMISIONES = Topic_EMISIONES.emisiones_por_consumo_bagazo_otros
    trayectoria : Trayectoria
    tipo   : Tipo_EMISIONES
    y2018  : float | None
    y2020  : float | None
    y2025  : float | None
    y2030  : float | None
    y2035  : float | None
    y2040  : float | None
    y2045  : float | None
    y2050  : float | None
    unidad : Unidades_EMISIONES | None = Unidades_EMISIONES.Mt_CO2e
    
class EMISIONES(BaseModel):
    """Emisiones
    """
    
    emisiones_gei_por_industria        : list[EMISIONES_GASES_EFECTO_INVERNADERO]
    emisiones_por_consumo_bagazo_otros : list[EMISIONES_CONSUMO_BAGAZO_OTROS]
    
    class Config:
        orm_mode : True


####################################################################################
#######                               Costos                                 #######
####################################################################################


# class COSTOS(BaseModel):
#     """Costos
#     """
    
#     class Config:
#         orm_mode : True





####################################################################################
#######                               Global                                 #######
####################################################################################

class INDUSTRIA(BaseModel):
    """Schema global
    """
    supuestos_trayectoria : SUPUESTOS_TRAYECTORIA | None
    supuestos_fijos       : SUPUESTOS_FIJOS | None
    # supuestos_costos      : SUPUESTOS_COSTO | None
    salidas               : SALIDAS | None
    emisiones             : EMISIONES | None
    # costos                : COSTOS | None
    
    class Config:
        orm_mode : True

