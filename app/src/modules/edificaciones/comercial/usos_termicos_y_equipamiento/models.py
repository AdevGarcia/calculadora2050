from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Edificaciones Comerciales Usos Termicos y Equipamiento

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_iluminacion(Base):
    """Supuestos de Trayectoria reduccion_por_eficiencia_en_la_iluminacion
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


class EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_refrigeracion(Base):
    """Supuestos de Trayectoria reduccion_por_eficiencia_en_refrigeracion
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


class EDIF_COM_USOS_TERM_EQUIP_ST_reduccion_eficiencia_usos_termicos(Base):
    """Supuestos de Trayectoria reduccion_por_eficiencia_en_usos_termicos
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

class EDIF_COM_USOS_TERM_EQUIP_SF_consumo_total_de_energia_por_uso(Base):
    """Supuestos Fijos consumo_total_de_energia_por_uso
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


class EDIF_COM_USOS_TERM_EQUIP_SF_participacion_usos_en_equipamiento(Base):
    """Supuestos Fijos participacion_usos_en_equipamiento
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


class EDIF_COM_USOS_TERM_EQUIP_SF_part_energeticos_usos_termicos(Base):
    """Supuestos Fijos participacion_de_los_energeticos_en_los_usos_termicos
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


class EDIF_COM_USOS_TERM_EQUIP_SF_participacion_energ_equipamiento(Base):
    """Supuestos Fijos participacion_de_los_energeticos_en_equipamiento
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


####################################################################################
#######                               Salidas                                #######
####################################################################################

class EDIF_COM_USOS_TERM_EQUIP_SALIDAS(Base):
    """energia_producida_y_requerida"""

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


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class EDIF_COM_USOS_TERM_EQUIP_EMISIONES(Base):
    """emisiones_de_gases_efecto_invernadero"""

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
