from aiohttp.web import Application


from src.core.settings import settings


async def on_startup(app: Application) -> None: 
    await app["bot"].set_webhook(settings.bot_webhook_url)



async def on_shutdown(app: Application) -> None:
    await app["bot"].delete_webhook()
