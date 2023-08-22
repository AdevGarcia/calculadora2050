from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Ganaderia

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class GANA_ST_pract_sost_suelos_ganaderos_crecimiento_estimado_sup(Base):
    """Supuestos de Trayectoria practicas_sostenibles_en_suelos_ganaderos_crecimiento_estimado_de_superficies
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


class GANA_ST_mejores_pract_pecuarias_cabezas_ganado(Base):
    """Supuestos de Trayectoria mejores_practicas_pecuarias_porcentaje_de_cabezas_de_ganado
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


class GANA_ST_produccion_de_estiercol_para_bioenergia(Base):
    """Supuestos de Trayectoria produccion_de_estiercol_para_bioenergia
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

class GANA_SF_uso_actual_tierra_sector_agropecuario_colombia(Base):
    """Supuestos Fijos uso_actual_de_la_tierra_sector_agropecuario_en_colombia
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class GANA_SF_hato_ganadero_colombiano(Base):
    """Supuestos Fijos hato_ganadero_colombiano
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


class GANA_SF_factor_de_emision_de_metano_ch4_por_genero(Base):
    """Supuestos Fijos factor_de_emision_de_metano_ch4_por_genero
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class GANA_SF_areas_ini_implem_pract_sostenibles_suelos_ganaderos(Base):
    """Supuestos Fijos areas_iniciales_de_implementacion_para_practicas_sostenibles_en_suelos_ganaderos
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class GANA_SF_fact_prod_estiercol_por_cabeza_ganado_y_emisiones(Base):
    """Supuestos Fijos factor_produccion_de_estiercol_por_cabeza_de_ganado_y_emisiones
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class GANA_SF_potencial_energetico_del_estiercol(Base):
    """Supuestos Fijos potencial_energetico_del_estiercol
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    value       = Column(name='value', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class GANA_SF_pot_reduc_emisiones_practicas_sost_suelos_ganaderos(Base):
    """Supuestos Fijos potencial_de_reduccion_de_emisiones_practicas_sostenibles_en_suelos_ganaderos
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


class GANA_SF_coef_remocion_carbono_dist_usos_suelo_ecorregion_anual(Base):
    """Supuestos Fijos coeficiente_de_remocion_de_carbono_para_los_distintos_usos_de_suelo_y_ecorregion_anual
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class GANA_SF_pot_reduccion_emisiones_mejores_practicas_pecuarias(Base):
    """Supuestos Fijos potencial_de_reduccion_de_emisiones_de_mejores_practicas_pecuarias
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


####################################################################################
#######                               Salidas                                #######
####################################################################################

class GANA_SALIDAS(Base):
    """produccion_de_estiercol_para_bioenergia"""

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

class GANA_EMISIONES(Base):
    """emisiones"""

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
