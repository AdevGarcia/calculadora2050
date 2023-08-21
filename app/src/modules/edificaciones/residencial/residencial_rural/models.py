from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Edificaciones Residencial Rural

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class EDIF_RES_RURAL_ST_demanda_de_glp(Base):
    """Supuestos de Trayectoria demanda_de_glp
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


class EDIF_RES_RURAL_ST_demanda_de_lena(Base):
    """Supuestos de Trayectoria demanda_de_lena
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

class EDIF_RES_RURAL_SF_demanda_de_energia_electrica(Base):
    """Supuestos Fijos demanda_de_energia_electrica"""

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


####################################################################################
#######                               Salidas                                #######
####################################################################################

class EDIF_RES_RURAL_SALIDAS(Base):
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

class EDIF_RES_RURAL_EMISIONES(Base):
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

