
from sqlalchemy.orm import Session

from app.src.db import base  # noqa: F401

from app.src.core.config import settings
from app.src.crud.crud_user import user as crud_user
from app.src.modules.user import schemas

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line 
    # Base.metadata.create_all(bind=engine)
    
    user = crud_user.get_by_email(db, email=settings.ADMIN)
    if not user:
        logger.info("NOT USER")
        user_in = schemas.UserCreateUpdate(
            email=settings.ADMIN,
            password=settings.ADMIN_PASSWORD,
            is_superuser=True,
        )
        user = crud_user.create(db, obj_in=user_in)  # noqa: F841
