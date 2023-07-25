from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Bosques

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class BOSQ_ST_escenarios_de_deforestacion(Base):
    """Supuestos de Trayectoria escenarios_de_deforestacion
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


class BOSQ_ST_desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales(Base):
    """Supuestos de Trayectoria desarrollo_y_consolidacion_de_la_cadena_productiva_de_las_plantaciones_forestales_con_fines_comerciales
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


####################################################################################
#######                          Supuestos Fijos                             #######
####################################################################################

class BOSQ_SF_area_anual_deforestada_puntual(Base):
    """Supuestos Fijos area_anual_deforestada_puntual
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


class BOSQ_SF_deforestacion_observada_no_acumulada(Base):
    """Supuestos Fijos deforestacion_observada_no_acumulada
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class BOSQ_SF_contenidos_de_carbono_por_zonas_naturales(Base):
    """Supuestos Fijos contenidos_de_carbono_por_zonas_naturales
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class BOSQ_SF_factor_de_conversion_de_biomasa_por_deforestacion(Base):
    """Supuestos Fijos factor_de_conversion_de_biomasa_por_deforestacion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class BOSQ_SF_area_para_la_reforestacion_comercial(Base):
    """Supuestos Fijos area_para_la_reforestacion_comercial
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


class BOSQ_SF_biomasa_aerea_subterranea_reforestacion_comercial(Base):
    """Supuestos Fijos biomasa_aerea_subterranea_reforestacion_comercial
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class BOSQ_SF_descuentos_aplicables_a_reforestacion_comercial(Base):
    """Supuestos Fijos descuentos_aplicables_a_reforestacion_comercial
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class BOSQ_SALIDAS(Base):
    """total_areas_reforestadas"""

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

class BOSQ_EMISIONES(Base):
    """total_emisiones"""

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

