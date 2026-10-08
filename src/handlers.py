from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from src.keyboards import reply_keyboard, inline_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Здравствуйте, {message.from_user.full_name}! Выберите язык программирования:",
        reply_markup=reply_keyboard
    )


@router.message(F.text == "Python")
async def python_button(message: Message):
    await message.answer(
        "Python — простой и популярный язык программирования. "
        "Используется в веб-разработке, анализе данных, AI и автоматизации."
    )


@router.message(F.text == "Java")
async def java_button(message: Message):
    await message.answer(
        "Java — популярный объектно-ориентированный язык программирования. "
        "Используется для создания приложений, веб-сервисов и Android-приложений."
    )


@router.message(F.text == "JavaScript")
async def javascript_button(message: Message):
    await message.answer(
        "JavaScript — язык программирования, который широко используется "
        "для создания интерактивных веб-сайтов и веб-приложений."
    )

@router.message(Command('docs'))
async def cmd_docs(message: Message):
    await message.answer(
        f"Выберите язык программирования для получения документации:",
        reply_markup=inline_keyboard
    )