from aiohttp.web import Application
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.webhook import get_new_configured_app


from src.core.settings import settings
from src.core.events import on_startup, on_shutdown
from src.api.routers import register_bot_endpoints, register_web_endpoints


def build_application() -> Application:
    """
        Создание базового экземпляра приложения
    """
    bot = Bot(settings.bot_token)
    dispatcher = Dispatcher(bot)
    app = get_new_configured_app(dispatcher, settings.bot_webhook_path)
    app["bot"] = bot

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    register_web_endpoints(app)
    register_bot_endpoints(dispatcher)

    return app