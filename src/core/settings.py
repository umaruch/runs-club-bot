from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # Настройки веб сервера
    secret_key: str = Field(..., env="SECRET_KEY")

    # Настройки Telegram
    bot_token: str = Field(..., env="TELEGRAM_TOKEN")

    # Настройки PostgreSQL

    # Настройки Redis?

    class Config:
        env_file = ".env"


settings = Settings()