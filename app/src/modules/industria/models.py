from sqlalchemy import Column, Integer, Float, String

from app.src.db.base_class import Base

# Industria

####################################################################################
#######                      Supuestos de Trayectoria                        #######
####################################################################################

class INDU_ST_reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica(Base):
    """Supuestos de Trayectoria reduccion_de_consumo_energetico_por_aumento_en_la_eficiencia_energetica
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


class INDU_ST_eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras(Base):
    """Supuestos de Trayectoria eficiencia_energetica_reduccion_de_consumo_energetico_ladrilleras
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


class INDU_ST_eficiencia_energetica_crecimiento_de_autogeneracion_y_cogeneracion(Base):
    """Supuestos de Trayectoria eficiencia_energetica_%_crecimiento_de_autogeneracion_y_cogeneracion
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


class INDU_ST_eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras(Base):
    """Supuestos de Trayectoria eficiencia_energetica_autogeneracion_y_cogeneracion_ladrilleras
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


class INDU_ST_sustitucion_de_sao_y_hfc(Base):
    """Supuestos de Trayectoria sustitucion_de_sao_y_hfc
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


class INDU_ST_procesos_productivos_sostenibles(Base):
    """Supuestos de Trayectoria procesos_productivos_sostenibles
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

class INDU_SF_produccion_anual_de_materiales(Base):
    """Supuestos Fijos produccion_anual_de_materiales
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


class INDU_SF_produccion_de_acido_nitrico(Base):
    """Supuestos Fijos produccion_de_acido_nitrico
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_produccion_de_cemento(Base):
    """Supuestos Fijos produccion_de_cemento
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_produccion_anual_de_ladrillos(Base):
    """Supuestos Fijos produccion_anual_de_ladrillos
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


class INDU_SF_indice_de_consumo(Base):
    """Supuestos Fijos indice_de_consumo
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_distribucion_segun_tipo_de_combustible_ladrilleras(Base):
    """Supuestos Fijos distribucion_segun_tipo_de_combustible_ladrilleras
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_uso_energetico_por_combustible(Base):
    """Supuestos Fijos uso_energetico_por_combustible
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    y2018       = Column(name='2018', type_=Float)
    y2020       = Column(name='2020', type_=Float)
    y2025       = Column(name='2025', type_=Float)
    y2030       = Column(name='2030', type_=Float)
    y2035       = Column(name='2035', type_=Float)
    y2040       = Column(name='2040', type_=Float)
    y2045       = Column(name='2045', type_=Float)
    y2050       = Column(name='2050', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_factor_de_utilizacion_de_autogeneracion_y_cogeneracion(Base):
    """Supuestos Fijos factor_de_utilizacion_de_autogeneracion_y_cogeneracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_capacidad_instalada_de_autogeneracion(Base):
    """Supuestos Fijos capacidad_instalada_de_autogeneracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_excedentes_de_autogeneracion(Base):
    """Supuestos Fijos excedentes_de_autogeneracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_capacidad_instalada_de_cogeneracion(Base):
    """Supuestos Fijos capacidad_instalada_de_cogeneracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_excedentes_de_cogeneracion(Base):
    """Supuestos Fijos excedentes_de_cogeneracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    topic       = Column(name='topic', type_=String)
    tipo        = Column(name='tipo', type_=String)
    fuente      = Column(name='fuente', type_=String)
    valor       = Column(name='valor', type_=Float)
    unidad      = Column(name='unidad', type_=String)


class INDU_SF_emision_de_sao(Base):
    """Supuestos Fijos emision_de_sao
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


# ####################################################################################
# #######                               Salidas                                #######
# ####################################################################################

# # Por combustible

class INDU_SALIDAS_por_combustible_energia_requerida(Base):
    """Salidas - por_combustible_energia_requerida
    """

    id          = Column(Integer, primary_key=True, index=True)
    bloque      = Column(name='bloque', type_=String)
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
    medida_4    = Column(name='medida_4', type_=Integer)


class INDU_SALIDAS_por_combustible_energia_producida_por_autogeneracion_y_cogeneracion(Base):
    """Salidas - por_combustible_energia_producida_por_autogeneracion_y_cogeneracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    bloque      = Column(name='bloque', type_=String)
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
    medida_4    = Column(name='medida_4', type_=Integer)


class INDU_SALIDAS_por_combustible_balance_total_de_la_energia_requerida(Base):
    """Salidas - por_combustible_balance_total_de_la_energia_requerida
    """

    id          = Column(Integer, primary_key=True, index=True)
    bloque      = Column(name='bloque', type_=String)
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
    medida_4    = Column(name='medida_4', type_=Integer)


# # POR TIPO DE INDUSTRIA

class INDU_SALIDAS_por_tipo_de_industria_energia_requerida(Base):
    """Salidas - por_tipo_de_industria_energia_requerida
    """

    id          = Column(Integer, primary_key=True, index=True)
    bloque      = Column(name='bloque', type_=String)
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
    medida_4    = Column(name='medida_4', type_=Integer)


class INDU_SALIDAS_por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion(Base):
    """Salidas - por_tipo_de_industria_energia_producida_por_autogeneracion_y_cogeneracion
    """

    id          = Column(Integer, primary_key=True, index=True)
    bloque      = Column(name='bloque', type_=String)
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
    medida_4    = Column(name='medida_4', type_=Integer)


class INDU_SALIDAS_por_tipo_de_industria_balance_total_de_la_energia_requerida(Base):
    """Salidas - por_tipo_de_industria_balance_total_de_la_energia_requerida
    """

    id          = Column(Integer, primary_key=True, index=True)
    bloque      = Column(name='bloque', type_=String)
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
    medida_4    = Column(name='medida_4', type_=Integer)


####################################################################################
#######                             Emisiones                                #######
####################################################################################

class INDU_emisiones_gases_efecto_invernadero(Base):
    """Emisiones - emisiones_gases_efecto_invernadero
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
    medida_2 = Column(name='medida_2', type_=Integer)
    medida_3 = Column(name='medida_3', type_=Integer)
    medida_4 = Column(name='medida_4', type_=Integer)


class INDU_emisiones_por_el_consumo_de_bagazo_y_otros(Base):
    """Emisiones - emisiones_por_el_consumo_de_bagazo_y_otros
    """

    id     = Column(Integer, primary_key=True, index=True)
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
    medida_2 = Column(name='medida_2', type_=Integer)
    medida_3 = Column(name='medida_3', type_=Integer)
    medida_4 = Column(name='medida_4', type_=Integer)


class INDU_emisiones_sao(Base):
    """Emisiones - emisiones_sao
    """

    id     = Column(Integer, primary_key=True, index=True)
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
    medida_2 = Column(name='medida_2', type_=Integer)
    medida_3 = Column(name='medida_3', type_=Integer)
    medida_4 = Column(name='medida_4', type_=Integer)