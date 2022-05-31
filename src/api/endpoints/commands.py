from aiogram import types
from aiogram.dispatcher.webhook import SendMessage

async def cmd_start_handler(message: types.Message) -> None:
    await message.answer( 
        "Учетная запись не найдена, пожалуйста заполните форму регистрации:",
        reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Регистрация", 
        web_app=types.WebAppInfo(url="https://64ae-176-213-234-29.eu.ngrok.io/api/hello")))
    )