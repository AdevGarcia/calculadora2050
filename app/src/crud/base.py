from typing import Dict, Generic, List, Optional, Type, TypeVar
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
import logging

from app.src.db.base_class import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ModelType  = TypeVar("ModelType",  bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class CRUD(Generic[ModelType, SchemaType]):
    def __init__(self, db: Session, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.db = db
        self.model = model

    # GET
    # def get_id(self, id: Any) -> Optional[ModelType]:
    #     return self.db.query(self.model).filter(self.model.id == id).first()

    def get(self, **kwargs) -> Optional[ModelType]:
        """generic get
        Ej.: crud.get(topic='areas_forestales_protegidas', trayectoria=2)
        """
        filters = []
        for key, value in kwargs.items():
            filters.append(getattr(self.model, key) == value)
        return self.db.query(self.model).filter(*filters).first()

    def get_multi(self, skip: int = 0, limit: int = 100, **kwargs) -> List[ModelType]:
        filters = []
        for key, value in kwargs.items():
            filters.append(getattr(self.model, key) == value)
        return self.db.query(self.model).filter(*filters).offset(skip).limit(limit).all()

    # CREATE
    def _create(self, *, obj_in: SchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def create(self, obj_in: SchemaType, **kwargs) -> ModelType:
        _db = self.get(**kwargs)
        if _db:
            raise HTTPException(status_code=400, detail="Data already registered")
        db_obj = self._create(obj_in=obj_in)
        return db_obj

    def create_batch(self, obj_in: list[SchemaType], filters: list[str | float]) -> ModelType:
        """create_batch
        TODO: check https://docs.pydantic.dev/usage/models/
        En el proceso de crear, estoy haciendo dos jsonable_encoder()
        """

        for item in obj_in:

            lfilter = [getattr(self.model, filter) == item[filter]
                       for filter in filters]
            # get
            _db = self.db.query(self.model).filter(*lfilter).first()
            if _db:
                raise HTTPException(status_code=400, detail="Data already registered")
            db_obj = self._create(obj_in=self.model(**item))
        return db_obj

    # REMOVE
    def remove(self, **kwargs) -> ModelType:
        obj = self.get(**kwargs)
        self.db.delete(obj)
        self.db.commit()
        return obj

    def remove_multi(self, **kwargs) -> ModelType:
        obj = self.get_multi(**kwargs)
        self.db.delete(obj)
        self.db.commit()
        return obj

    def removeAll(self) -> ModelType:
        obj = self.db.query(self.model).delete()
        self.db.commit()
        return obj


def loader(db: Session, model: Type[ModelType], obj_in: SchemaType, filters: list[str]) -> ModelType:
    """aux function to loader data
    TODO: cambiar filters por *filters o **filters, para no tener que meter una lista vacia
    """
    crud = CRUD(db=db, model=model)
    db_obj = crud.create_batch(obj_in, filters)
    return db_obj

def downloader(db: Session, model: Type[ModelType], topic: str, skip: int = 0, limit: int = 100, **kwargs) -> Dict:
    """aux function to download data
    """
    d={}
    crud = CRUD(db=db, model=model)
    d[topic] = crud.get_multi(topic=topic, skip=skip, limit=limit, **kwargs)
    return d

def downloader_batch(db: Session, skip: int = 0, limit: int = 100, **kwargs) -> Dict:
    """aux function to download data in batch
    """
    d = {}
    for key, value in kwargs.items():
        data = downloader(db=db, model=value, topic=key, skip=skip, limit=limit)
        d.update(data)
    return d


def prune(db: Session, model: Type[ModelType]) -> ModelType:
    """aux function to download data
    """
    crud = CRUD(db=db, model=model)
    return crud.removeAll()
