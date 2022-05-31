from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # Настройки веб сервера
    secret_key: str = Field(..., env="SECRET_KEY")
    

    # Настройки Telegram
    bot_token: str = Field(..., env="TELEGRAM_TOKEN")
    bot_webhook_url: str = "https://64ae-176-213-234-29.eu.ngrok.io/webhook" # Полный url https://пример/webhook
    bot_webhook_path: str = "/webhook"

    # Настройки PostgreSQL

    # Настройки Redis?

    class Config:
        env_file = ".env"


settings = Settings()