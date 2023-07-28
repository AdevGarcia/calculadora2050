from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Transporte - Carga

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class TRANS_CAR_ST_uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano(Base):
    """Supuestos de Trayectoria uso_de_energia_para_el_transporte_ferreo_transporte_de_carga_interurbano
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


class TRANS_CAR_ST_distancia_modo_ferreo(Base):
    """Supuestos de Trayectoria distancia_modo_ferreo"""
    
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


class TRANS_CAR_ST_distancia_para_el_transporte_carretero_transporte_de_carga_interurbano(Base):
    """Supuestos de Trayectoria distancia_para_el_transporte_carretero_transporte_de_carga_interurbano"""
    
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


class TRANS_CAR_ST_uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano(Base):
    """Supuestos de Trayectoria uso_de_energia_para_el_transporte_fluvial_transporte_de_carga_interurbano"""
    
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


class TRANS_CAR_ST_uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano(Base):
    """Supuestos de Trayectoria uso_de_energia_para_el_transporte_aereo_transporte_de_carga_interurbano"""
    
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


class TRANS_CAR_ST_carga_sustituida_por_modo_transporte_de_carga_interurbano(Base):
    """Supuestos de Trayectoria carga_sustituida_por_modo_transporte_de_carga_interurbano"""
    
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


class TRANS_CAR_ST_distribucion_por_tecnologia_transporte_de_carga_urbano(Base):
    """Supuestos de Trayectoria distribucion_por_tecnologia_transporte_de_carga_urbano"""
    
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


class TRANS_CAR_ST_distribucion_por_tecnologia_transporte_de_carga_interurbano(Base):
    """Supuestos de Trayectoria distribucion_por_tecnologia_transporte_de_carga_interurbano"""
    
    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    bloque      = Column(name='bloque', type_=String)
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


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class TRANS_CAR_SF_factor_de_actividad_transporte_de_carga_urbano(Base):
    """Supuestos Fijos factor_de_actividad_transporte_de_carga_urbano
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


class TRANS_CAR_SF_rendimiento_modo_carretero(Base):
    """Supuestos Fijos rendimiento_modo_carretero
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


class TRANS_CAR_SF_distancia_tipica_por_modo(Base):
    """Supuestos Fijos distancia_tipica_por_modo"""

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


class TRANS_CAR_SF_vida_util(Base):
    """Supuestos Fijos vida_util"""

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class TRANS_CAR_SF_numero_de_vehiculos_transporte_de_carga_urbano(Base):
    """Supuestos Fijos numero_de_vehiculos_transporte_de_carga_urbano"""

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


class TRANS_CAR_SF_numero_de_vehiculos_transporte_de_carga_interurbano(Base):
    """Supuestos Fijos numero_de_vehiculos_transporte_de_carga_interurbano"""

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




# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class TRANS_CAR_SALIDAS_energia_requerida_transporte_de_carretera(Base):
    """Salidas - energia_requerida_transporte_de_carretera
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

class TRANS_CAR_emisiones_de_gases_efecto_invernadero(Base):
    """Emisiones - emisiones_de_gases_efecto_invernadero
    """

    id       = Column(Integer, primary_key=True, index=True)
    topic    = Column(name='topic', type_=String)
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
    medida_2    = Column(name='medida_2', type_=Integer)
