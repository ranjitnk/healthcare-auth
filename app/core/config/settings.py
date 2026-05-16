from pydantic import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "HealthAuthAI"
    ENVIRONMENT: str = "DEV"

    class Config:
        env_file = ".env"

settings = Settings()