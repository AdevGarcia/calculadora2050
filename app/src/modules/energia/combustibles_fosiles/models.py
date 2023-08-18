from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Energia - Combustibles fosiles

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class ENER_CombFosil_ST_eficiencia_energetica_refinacion_de_crudo(Base):
    """Supuestos de Trayectoria Eficiencia energética en la refinación de crudo"""

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

class ENER_CombFosil_SF_produccion_de_hidrocarburos(Base):
    """Supuestos Fijos produccion_de_hidrocarburos
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


class ENER_CombFosil_SF_produccion_de_carbon(Base):
    """Supuestos Fijos produccion_de_carbon
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


class ENER_CombFosil_SF_factores_de_emision_carbon(Base):
    """Supuestos Fijos factores_de_emision_carbon
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class ENER_CombFosil_SF_no_de_pozos(Base):
    """Supuestos Fijos no_de_pozos
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class ENER_CombFosil_SF_datos_produccion_crudo_ano_base(Base):
    """Supuestos Fijos datos_de_la_produccion_de_crudo_en_el_ano_base
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    total_crudo = Column(name='total_crudo', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class ENER_CombFosil_SF_datos_produccion_gas_natural_ano_base(Base):
    """Supuestos Fijos datos_de_la_produccion_de_gas_natural_en_el_ano_base
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    total_crudo = Column(name='total_crudo', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class ENER_CombFosil_SF_consumo_de_energeticos(Base):
    """Supuestos Fijos consumo_de_energeticos
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

class ENER_CombFosil_SALIDAS_combustibles_fosiles_producidos(Base):
    """salidas_combustibles_fosiles_producidos"""

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

      ############################################################### 
class ENER_CombFosil_SALIDAS_consumo_comb_fosiles_propio_sector(Base):
    """salidas_consumo_de_combustibles_fosiles_por_el_propio_sector"""

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

      ############################################################### 
class ENER_CombFosil_SALIDAS_consumo_comb_fosiles_sectores_ajenos(Base):
    """salidas_consumo_de_combustibles_fosiles_por_sectores_ajenos"""

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

class ENER_CombFosil_EMISIONES_produccion(Base):
    """emisiones_produccion"""

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


class ENER_CombFosil_EMISIONES_consumo(Base):
    """emisiones_consumo"""

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