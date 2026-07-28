from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_url: str
    mysql_url: str
    oracle_url: str
    mongo_url: str

    class Config:
        env_file = ".env"

settings = Settings()