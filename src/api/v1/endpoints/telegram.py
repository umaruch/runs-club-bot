from fastapi import APIRouter
from aiogram import Bot, Dispatcher, types


from src.core.settings import settings


router = APIRouter()
bot = Bot(token=settings.bot_token)
dp = Dispatcher(bot)


@router.post("")
async def on_post(body: dict, a: int = 5) -> None:
    telegram_update = types.Update(**body)
    Bot.set_current(bot)
    bot.a = a
    Dispatcher.set_current(dp)
    await dp.process_update(telegram_update)


@dp.message_handler(commands=["start"])
async def on_start(message: types.Message) -> None:
    print(bot.a)
    await message.answer("Теперь жми кнопку:", 
        reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Тык", web_app=types.WebAppInfo(url=f"https://3c3f-185-233-82-134.ngrok.io/signin")))
    )
