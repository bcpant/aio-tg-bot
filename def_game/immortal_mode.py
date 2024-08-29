import game_mods
import random
from config_reader import db_path, user_answers
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def play_immortal_mode(message: types.Message):
    get_word = game_mods.BotGames(db_path)
    user_answers[message.chat.id] = {
        'message_id': message.message_id,
        'true_answer': get_word.trueAnswer
    }
    
    options = [get_word.trueAnswer, get_word.wrongAnswer1, get_word.wrongAnswer2, get_word.wrongAnswer3]
    random.shuffle(options)


    inline_keyboard_components = []
    for option in options:
        callback_data = 'immortal_right' if option == get_word.trueAnswer else 'immortal_wrong'
        element = [InlineKeyboardButton(text=option, callback_data=callback_data)]
        inline_keyboard_components.append(element)

    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard_components)


    await message.answer(f'Загаданное слово: *{get_word.askedWord}*', reply_markup=inline_keyboard, parse_mode='Markdown')