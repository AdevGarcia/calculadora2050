from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Agricultura

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class AGRO_ST_mejores_practicas_agricolas_superficie_de_implementacion(Base):
    """Supuestos de Trayectoria mejores_practicas_agricolas_superficie_de_implementacion
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


class AGRO_ST_tierra_dedicada_para_biocombustibles_superficie_de_implementacion(Base):
    """Supuestos de Trayectoria tierra_dedicada_para_biocombustibles_superficie_de_implementacion
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

class AGRO_SF_factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo(Base):
    """Supuestos Fijos factor_de_produccion_de_biocombustibles_por_ha_segun_tipo_de_cultivo
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class AGRO_SF_produccion_biocombustibles(Base):
    """Supuestos Fijos produccion_biocombustibles
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class AGRO_SF_porcentaje_del_cultivo_usado_para_biocombustibles(Base):
    """Supuestos Fijos porcentaje_del_cultivo_usado_para_biocombustibles
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class AGRO_SF_factor_de_emision_de_cultivo_usado_para_biocombustibles(Base):
    """Supuestos Fijos factor_de_emision_de_cultivo_usado_para_biocombustibles
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class AGRO_SF_uso_actual_de_la_tierra_sector_agropecuario_en_colombia(Base):
    """Supuestos Fijos uso_actual_de_la_tierra_sector_agropecuario_en_colombia
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class AGRO_SF_tasas_de_crecimiento_del_pib_sectorial_de_agricultura(Base):
    """Supuestos Fijos tasas_de_crecimiento_del_pib_sectorial_de_agricultura
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


class AGRO_SF_areas_de_implementacion_de_mejores_practicas_agricolas(Base):
    """Supuestos Fijos areas_de_implementacion_de_mejores_practicas_agricolas
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


class AGRO_SF_factor_de_produccion_biomasa_por_cultivo(Base):
    """Supuestos Fijos factor_de_produccion_biomasa_por_cultivo
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class AGRO_SF_potencial_energetico_por_unidad_de_biomasa(Base):
    """Supuestos Fijos potencial_energetico_por_unidad_de_biomasa
    """

    id               = Column(Integer, primary_key=True, index=True)
    topic            = Column(name='topic', type_=String)
    bloque           = Column(name='bloque', type_=String)
    tipo             = Column(name='tipo', type_=String)
    factor           = Column(name='factor', type_=Float)
    unidad_factor    = Column(name='unidad_factor', type_=String)
    potencial        = Column(name='potencial', type_=Float)
    unidad_potencial = Column(name='unidad_potencial', type_=String)


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class AGRO_SALIDAS_cultivos(Base):
    """salida_cultivos"""

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
    medida_2    = Column(name='medida_2', type_=Integer)
    medida_3    = Column(name='medida_3', type_=Integer)


class AGRO_SALIDAS_biocombustibles(Base):
    """Salidas_biocombustibles"""

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
    medida_3    = Column(name='medida_3', type_=Integer)


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class AGRO_EMISIONES(Base):
    """Emisiones"""

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
    medida_2    = Column(name='medida_2', type_=Integer)
    medida_3    = Column(name='medida_3', type_=Integer)

