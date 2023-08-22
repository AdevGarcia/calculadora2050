from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Transporte - Navegacion

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class TRANS_NAV_ST_uso_de_combustible_para_navegacion_nacional(Base):
    """Supuestos de Trayectoria uso_de_combustible_para_navegacion_nacional
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
#######                               Salidas                                #######
####################################################################################

class TRANS_NAV_SALIDAS_energia_requerida(Base):
    """Salidas - energia_requerida
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


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class TRANS_NAV_emisiones(Base):
    """Emisiones - emisiones
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
