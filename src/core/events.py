from typing import Callable


from src.api.v1.endpoints.telegram import bot


def set_on_startup() -> Callable:
    async def on_startup() -> None:
        await bot.set_webhook("https://3c3f-185-233-82-134.ngrok.io/bot")

    return on_startup


def set_on_shutdown() -> Callable:
    async def on_shutdown() -> None:
        await bot.delete_webhook()

    return on_shutdown