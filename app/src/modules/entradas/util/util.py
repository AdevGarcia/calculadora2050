import pandas as pd
from fastapi.encoders import jsonable_encoder

from app.src.crud.base import downloader

from .constants import YEARS



def db_to_df(rd: dict, debug: bool=False)-> pd.DataFrame:
    """convert db request to pandas Dataframe"""

    d = jsonable_encoder(rd)
    if debug:
        print('### db_to_df\n', d)
    return pd.DataFrame(d[list(d.keys())[0]])[YEARS]


def db_to_dict(rd: dict)-> dict:
    """convert db request to dict"""

    return db_to_df(rd=rd).to_dict(orient='records')[0]


def set_item(rd: dict, topic: str=None, bloque: str=None, tipo: str=None, unidad:str=None)-> dict:
    """set item dict"""

    d = db_to_dict(rd=rd)
    if topic != None:
        d["topic"]    = topic

    if bloque != None:
        d["bloque"]   = bloque

    if tipo != None:
        d["tipo"]     = tipo

    if unidad != None:
        d["unidad"]   = unidad
    return d


def set_suma_total(items: list, topic: str, tipo: str, unidad:str, bloque: str=None)->dict:
    """ set total amount"""
    total = pd.DataFrame(items)[YEARS].sum().to_dict()

    total["topic"]    = topic
    if bloque != None:
        total["bloque"]   = bloque
    total["tipo"]     = tipo
    total["unidad"]   = unidad

    return total


def set_zeros(topic_item: str, tipo: str, unidad:str, bloque: str=None)-> dict:
        """set zeros item dict"""

        d= {
            'y2018'  : 0.0, 
            'y2020'  : 0.0, 
            'y2025'  : 0.0, 
            'y2030'  : 0.0, 
            'y2035'  : 0.0, 
            'y2040'  : 0.0, 
            'y2045'  : 0.0, 
            'y2050'  : 0.0,
            'topic'  : topic_item,
            'tipo'   : tipo, 
            'unidad' : unidad
        }

        if bloque != None:
            d["bloque"]   = bloque
        
        return d


def get_total(d: dict)-> pd.DataFrame:
    """get total item"""

    df = pd.DataFrame(d[list(d.keys())[0]])
    return df[df.tipo == 'total'][YEARS]


def get_item(db, model, filter, topic: str, topic_item: str=None, bloque: str=None, tipo: str=None, unidad: str=None)-> dict:
    """get item from a query to ddbb"""

    rd = downloader(db=db, topic=topic, model=model, **filter)
    return set_item(rd=rd, topic=topic_item, tipo=tipo, unidad=unidad, bloque=bloque)
    


def not_negative(x):
    if x < 0:
        return 0
    else:
        return x

def abs_negative(x):
    if x < 0:
        return abs(x)
    else:
        return 0