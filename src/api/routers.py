from aiohttp.web import Application, get, post
from aiogram import Dispatcher


from src.api.endpoints import commands, debug


def register_bot_endpoints(dispatcher: Dispatcher) -> None:
    """
        Регистрация всех обработчиков событий Телеграм
    """
    dispatcher.register_message_handler(commands.cmd_start_handler, commands=["start"])


def register_web_endpoints(app: Application) -> None:
    """
        Регистрация обработчиков веб запросов
    """
    app.add_routes([
        get("/api/hello", debug.hello_world)
    ])