import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")  # Must be public HTTPS URL

if not BOT_TOKEN:
    raise RuntimeError("Set BOT_TOKEN in environment.")
if not WEBAPP_URL or not WEBAPP_URL.startswith("https://"):
    raise RuntimeError("Set WEBAPP_URL to the deployed Mini App HTTPS address.")

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(
                text="Открыть экскурсию",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]],
        resize_keyboard=True
    )
    await message.answer(
        "<b>SERBIA DISCOVERED</b>\n"
        "Тестовая аудиоэкскурсия по историческому центру Белграда.\n\n"
        "Нажмите кнопку ниже, чтобы открыть маршрут. "
        "Для работы GPS разрешите доступ к геопозиции.",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())