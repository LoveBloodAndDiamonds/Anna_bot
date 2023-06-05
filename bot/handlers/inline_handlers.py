import hashlib

from aiogram import types
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle


async def hello_querry(querry: types.InlineQuery):
    print('----')
    text = querry.query or "echo"
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [
        InlineQueryResultArticle(
            id=result_id+"1",
            title='Сказать "привет"',
            input_message_content=InputTextMessageContent(
                message_text='Привет, я Аня!'
            )
        ),
        InlineQueryResultArticle(
            id=result_id+"2",
            title='Сказать "пока"',
            input_message_content=InputTextMessageContent(
                message_text='Пока, целую-обнимаю!'
            )
        ),
        InlineQueryResultArticle(
            id=result_id+"3",
            title='Сказать "Доброе утро"',
            input_message_content=InputTextMessageContent(
                message_text='Доброе утро, коллеги!!!!!!!'
            )
        )

    ]
    await querry.answer(articles, cache_time=0, is_personal=False)
    print('----')
