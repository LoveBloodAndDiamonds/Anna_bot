__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters import CommandStart

from bot.commands.start import start_command


bot_commands = (
    ("help", "Помощь и справка"),
    ("contacts", "Показать контакты"),
    ("show_menu", "Показать меню")
)


def register_user_commands(router: Router) -> None:
    """Register commands"""
    router.message.register(start_command, CommandStart())
