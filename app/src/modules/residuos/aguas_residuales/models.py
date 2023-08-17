from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Residuos - Aguas Residuales

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class RES_AGU_ST_cantidad_de_aguas_residuales_domesticas(Base):
    """Supuestos de Trayectoria cantidad_de_aguas_residuales_domesticas
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


class RES_AGU_ST_cantidad_de_aguas_residuales_industriales(Base):
    """Supuestos de Trayectoria cantidad_de_aguas_residuales_industriales
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


class RES_AGU_ST_estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas(Base):
    """Supuestos de Trayectoria estaciones_de_tratamiento_de_aguas_residuales_municipales_con_extraccion_de_biogas
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


class RES_AGU_ST_estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas(Base):
    """Supuestos de Trayectoria estaciones_de_tratamiento_de_aguas_residuales_industriales_con_extraccion_de_biogas
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

class RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_tratada(Base):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_domestica_tratada
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_AGU_SF_dbo_por_m3_de_agua_residual_domestica_no_tratada(Base):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_domestica_no_tratada
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_tratada(Base):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_industrial_tratada
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_AGU_SF_dbo_por_m3_de_agua_residual_industrial_no_tratada(Base):
    """Supuestos Fijos dbo_por_m3_de_agua_residual_industrial_no_tratada
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_AGU_SF_generacion_de_ch4_por_kg_dbo_tratado(Base):
    """Supuestos Fijos generacion_de_ch4_por_kg_dbo_tratado
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_AGU_SF_generacion_de_ch4_por_kg_dbo_no_tratado(Base):
    """Supuestos Fijos generacion_de_ch4_por_kg_dbo_no_tratado
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_AGU_SF_datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento(Base):
    """Supuestos Fijos datos_de_la_generacion_energetica_de_las_estaciones_de_tratamiento
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class RES_AGU_SF_consumo_energetico_medio_por_tratamiento(Base):
    """Supuestos Fijos consumo_energetico_medio_por_tratamiento
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class RES_AGU_SALIDAS_energia_consumida(Base):
    """Salidas - energia_consumida
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
    medida_1    = Column(name='medida_1', type_=Integer)
    medida_2    = Column(name='medida_2', type_=Integer)


class RES_AGU_SALIDAS_energia_producida(Base):
    """Salidas - energia_producida
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
    medida_1    = Column(name='medida_1', type_=Integer)
    medida_2    = Column(name='medida_2', type_=Integer)


####################################################################################
#######                             Emisiones                                #######
####################################################################################

# class RES_AGU_emisiones_de_gases_de_efecto_invernadero_aguas_residuales(Base):
#     """Emisiones - emisiones_de_gases_de_efecto_invernadero_aguas_residuales
#     """

#     id       = Column(Integer, primary_key=True, index=True)
#     topic    = Column(name='topic', type_=String)
#     bloque   = Column(name='bloque', type_=String)
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
#     medida_2 = Column(name='medida_2', type_=Integer)


# class RES_AGU_emisiones_de_gases_de_efecto_invernadero_energia(Base):
#     """Emisiones - emisiones_de_gases_de_efecto_invernadero_energia
#     """

#     id       = Column(Integer, primary_key=True, index=True)
#     topic    = Column(name='topic', type_=String)
#     bloque   = Column(name='bloque', type_=String)
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
#     medida_2 = Column(name='medida_2', type_=Integer)


class RES_AGU_emisiones(Base):
    """Emisiones - emisiones"""

    id       = Column(Integer, primary_key=True, index=True)
    topic    = Column(name='topic', type_=String)
    bloque   = Column(name='bloque', type_=String)
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
    medida_2 = Column(name='medida_2', type_=Integer)
