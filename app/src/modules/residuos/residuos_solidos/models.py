from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Residuos - Residuos Solidos

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class RES_SOL_ST_cantidad_de_residuos_generada_anual(Base):
    """Supuestos de Trayectoria cantidad_de_residuos_generada_anual
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    trayectoria = Column(name='trayectoria', type_=Integer)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float)
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_ST_tipo_de_gestion(Base):
    """Supuestos de Trayectoria tipo_de_gestion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    trayectoria = Column(name='trayectoria', type_=Integer)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float)
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)

      ############################################################### 
class RES_SOL_ST_cap_inst_sist_recup_aprov_biogas_rellenos_sanit(Base):
    """Supuestos de Trayectoria capacidad_instalada_para_los_sistemas_de_recuperacion_y_aprovechamiento_del_biogas_en_rellenos_sanitarios
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    trayectoria = Column(name='trayectoria', type_=Integer)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float)
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_ST_capacidad_instalada_sistemas_incineracion(Base):
    """Supuestos de Trayectoria capacidad_instalada_para_los_sistemas_de_incineracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    trayectoria = Column(name='trayectoria', type_=Integer)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float) 
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class RES_SOL_SF_rellenos_sanitarios_con_captacion_aprovechamiento(Base):
    """Supuestos Fijos rellenos_sanitarios_con_captacion_aprovechamiento
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float) 
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_SF_distribucion_de_los_residuos_por_zona_climatica(Base):
    """Supuestos Fijos distribucion_de_los_residuos_por_zona_climatica
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_SF_caracterizacion_por_tipo_de_residuos_generados(Base):
    """Supuestos Fijos caracterizacion_por_tipo_de_residuos_generados
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float) 
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_SF_generacion_de_metano_por_tipologia_de_residuo(Base):
    """Supuestos Fijos generacion_de_metano_por_tipologia_de_residuo
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_SF_generacion_energetica_mediante_incineracion(Base):
    """Supuestos Fijos datos_de_la_generacion_energetica_mediante_incineracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_SF_consumo_energetico_medio_por_tratamiento(Base):
    """Supuestos Fijos consumo_energetico_medio_por_tratamiento
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_SOL_SF_estimacion_emisiones_incineracion(Base):
    """Supuestos Fijos datos_para_la_estimacion_de_las_emisiones_de_incineracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    bloque      = Column(name='bloque', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class RES_SOL_SALIDAS_energia_consumida(Base):
    """Salidas - energia_consumida
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    bloque      = Column(name='bloque', type_=String)
    tipo        = Column(name='tipo', type_=String)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float)
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)
    medida_1    = Column(name='medida_1', type_=Integer)


class RES_SOL_SALIDAS_energia_producida(Base):
    """Salidas - energia_producida
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    bloque      = Column(name='bloque', type_=String)
    tipo        = Column(name='tipo', type_=String)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float)
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)
    medida_1    = Column(name='medida_1', type_=Integer)


####################################################################################
#######                             Emisiones                                #######
####################################################################################

# class RES_SOL_emisiones_de_gases_de_efecto_invernadero_residuos(Base):
#     """Emisiones - emisiones_de_gases_de_efecto_invernadero_residuos
#     """

#     id       = Column(Integer, primary_key=True, index=True)
#     topic    = Column(name='topic', type_=String)
#     bloque   = Column(name='bloque', type_=String)
#     grupo    = Column(name='grupo', type_=String)
#     tipo     = Column(name='tipo', type_=String)
#     y2018    = Column(name='2018', type_=Float)
#     y2020    = Column(name='2020', type_=Float)
#     y2025    = Column(name='2025', type_=Float)
#     y2030    = Column(name='2030', type_=Float)
#     y2035    = Column(name='2035', type_=Float)
#     y2040    = Column(name='2040', type_=Float)
#     y2045    = Column(name='2045', type_=Float)
#     y2050    = Column(name='2050', type_=Float)
#     unidad   = Column(name='unidad', type_=String)
#     medida_1 = Column(name='medida_1', type_=Integer)


# class RES_SOL_emisiones_de_gases_de_efecto_invernadero_energia(Base):
#     """Emisiones - emisiones_de_gases_de_efecto_invernadero_energia
#     """

#     id       = Column(Integer, primary_key=True, index=True)
#     topic    = Column(name='topic', type_=String)
#     bloque   = Column(name='bloque', type_=String)
#     grupo    = Column(name='grupo', type_=String)
#     tipo     = Column(name='tipo', type_=String)
#     y2018    = Column(name='2018', type_=Float)
#     y2020    = Column(name='2020', type_=Float)
#     y2025    = Column(name='2025', type_=Float)
#     y2030    = Column(name='2030', type_=Float)
#     y2035    = Column(name='2035', type_=Float)
#     y2040    = Column(name='2040', type_=Float)
#     y2045    = Column(name='2045', type_=Float)
#     y2050    = Column(name='2050', type_=Float)
#     unidad   = Column(name='unidad', type_=String)
#     medida_1 = Column(name='medida_1', type_=Integer)


class RES_SOL_emisiones(Base):
    """Emisiones - emisiones"""

    id       = Column(Integer, primary_key=True, index=True)
    topic    = Column(name='topic', type_=String)
    bloque   = Column(name='bloque', type_=String)
    grupo    = Column(name='grupo', type_=String)
    tipo     = Column(name='tipo', type_=String)
    y2018    = Column(name='2018', type_=Float)
    y2020    = Column(name='2020', type_=Float)
    y2025    = Column(name='2025', type_=Float)
    y2030    = Column(name='2030', type_=Float)
    y2035    = Column(name='2035', type_=Float)
    y2040    = Column(name='2040', type_=Float)
    y2045    = Column(name='2045', type_=Float)
    y2050    = Column(name='2050', type_=Float)
    unidad   = Column(name='unidad', type_=String)
    medida_1 = Column(name='medida_1', type_=Integer)
