from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    postgres_url: str
    mysql_url: str
    oracle_url: str
    mongo_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # <--- Allows extra env vars like MONGO_URI without crashing
    )

settings = Settings()