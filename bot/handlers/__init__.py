__all__ = ['register_user_handlers']

from aiogram import Router


from bot.handlers.inline_handlers import hello_querry


def register_user_handlers(router: Router) -> None:
    router.inline_query.register(hello_querry)
