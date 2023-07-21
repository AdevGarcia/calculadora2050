import logging

from app.src.db.init_db import init_db
from app.src.db.session import SessionLocal


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    # logger.info("Init SessionLocal")
    init()


if __name__ == "__main__":
    main()