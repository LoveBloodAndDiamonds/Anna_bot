from aiogram import types


async def start_command(message: types.Message) -> None:
    """/start command"""
    await message.answer(text='Привет!')
