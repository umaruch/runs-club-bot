from fastapi import APIRouter
from aiogram import Bot, Dispatcher
from gtts import gTTS


from src.api.v1.endpoints.telegram import bot, dp
from src.schemes.forms import SigninForm


router = APIRouter()


@router.post("/signin")
async def signin_form_handler(form: SigninForm):
    print(form.user)
    print(form.new_username)
    Bot.set_current(bot)
    Dispatcher.set_current(dp)

    if form.user.username == form.new_username:
        await bot.send_message(form.user.id, f"О, да, ты помнишь свое имя. Да, тебя зовут {form.new_username}")
    else:
        await bot.send_message(form.user.id, f"Нет, тебя зовут {form.user.username} a не {form.new_username}")