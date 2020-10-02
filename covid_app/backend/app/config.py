import os
from pydantic import BaseSettings


if os.getenv('ENV_NAME') == 'local_docker':
    celery_host = 'rabbit'
    mongo_host = 'mongodb'
else:
    celery_host = 'localhost'
    mongo_host = 'localhost'


class Settings(BaseSettings):
    celery_host: str = celery_host
    mongo_host: str = mongo_host


settings = Settings()
