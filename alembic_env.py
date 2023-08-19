from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# ---------------- added Angel ------------------------------#
import os, sys
from dotenv import load_dotenv

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(APP_DIR)
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

print(f'\n########  alembic_env.py  ######## \nAlembic env:')
print(f'BASE_DIR          : {BASE_DIR}')
print(f'API_ENV           : {os.getenv("API_ENV")}')
print(f'POSTGRES_SERVER   : {os.getenv("POSTGRES_SERVER")}')
print(f'POSTGRES_USER     : {os.getenv("POSTGRES_USER")}')
print(f'POSTGRES_PASSWORD : {os.getenv("POSTGRES_PASSWORD")}')
print(f'POSTGRES_DB       : {os.getenv("POSTGRES_DB")}')

_user     = os.getenv("POSTGRES_USER", "postgres")
_password = os.getenv("POSTGRES_PASSWORD", "")
_server   = os.getenv("POSTGRES_SERVER", "db")
_port     = os.getenv("POSTGRES_PORT", "5432")
_db       = os.getenv("POSTGRES_DB", "app")
print(f"postgresql://{_user}:{_password}@{_server}:{_port}/{_db}")
print()
#------------------------------------------------------------#

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# ---------------- added Angel ------------------------------#
# this will overwrite the ini-file sqlalchemy.url path
# with the path given in the config of the main code
# config.set_main_option("sqlalchemy.url", os.environ["DATABASE_URL"])

#------------------------------------------------------------#

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# ---------------- added Angel ------------------------------#
# import models

# here target_metadata was equal to None
from app.src.db.base import Base  # noqa
target_metadata = Base.metadata
#------------------------------------------------------------#

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_url(ddbb: str= 'sqlite'):
    
    if ddbb == 'postgresql':
        user     = os.getenv("POSTGRES_USER", "postgres")
        password = os.getenv("POSTGRES_PASSWORD", "")
        server   = os.getenv("POSTGRES_SERVER", "db")
        port   = os.getenv("POSTGRES_PORT", "5432")
        db       = os.getenv("POSTGRES_DB", "app")
        return f"postgresql://{user}:{password}@{server}:{port}/{db}"
    
    elif ddbb == 'sqlite':
        return "sqlite:///./app.sqlite"
    else:
        return ''

if os.getenv("API_ENV") == 'development':
    ddbb = 'sqlite'

if os.getenv("API_ENV") == 'production':
    ddbb = 'postgresql'

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # url = config.get_main_option("sqlalchemy.url")
    url = get_url(ddbb)
    print(f'\n ############## \n Run Migrations Offline:')
    print(f'\n API_ENV: {os.getenv("API_ENV")} - {ddbb}')
    print(f'\n PostgreSQL: {url}')
    
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url(ddbb)
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
