import os
import secrets
from dotenv import load_dotenv
from typing import List, Union

from pydantic import AnyHttpUrl, EmailStr, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    load_dotenv()
    PROJECT_NAME: str                      = os.getenv('PROJECT_NAME')
    API_ENV: str                           = os.getenv('API_ENV')
    DEBUG: str                             = os.getenv('DEBUG')
    API_V1_STR: str                        = os.getenv('API_V1_STR')
    SECRET_KEY: str                        = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int       = 60 * 24 * 8 # = 8 days
    SERVER_HOST: AnyHttpUrl                = os.getenv('SERVER_HOST')
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.getenv('BACKEND_CORS_ORIGINS')

    ADMIN: EmailStr                 = os.getenv('ADMIN')
    ADMIN_PASSWORD: str             = os.getenv('ADMIN_PASSWORD')
    USERS_OPEN_REGISTRATION: bool   = os.getenv('USERS_OPEN_REGISTRATION')

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    
    if API_ENV == 'production':

        POSTGRES_SERVER: str   = os.getenv('POSTGRES_SERVER', 'db')
        POSTGRES_PORT: str     = os.getenv('POSTGRES_PORT', '5432')
        POSTGRES_USER: str     = os.getenv('POSTGRES_USER', 'postgres')
        POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'password')
        POSTGRES_DB: str       = os.getenv('POSTGRES_DB', 'api')
        SQLALCHEMY_DATABASE_URI : str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    
    class Config:
        case_sensitive = True


settings = Settings()
