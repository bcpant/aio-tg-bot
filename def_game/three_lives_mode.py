import game_mods
import random
from config_reader import db_path, user_answers
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def play_three_lives_mode(message: types.Message, lives=3, guessed_words=0):
    current_asked_word = game_mods.BotGames(db_path)
    user_answers[message.chat.id] = {
      'message_id': message.message_id,
      'true_answer': current_asked_word.trueAnswer,
      'lives': lives,
      'guessed_words': guessed_words
    }

    options = [current_asked_word.trueAnswer, current_asked_word.wrongAnswer1, 
               current_asked_word.wrongAnswer2, current_asked_word.wrongAnswer3]
    random.shuffle(options)

    inline_keyboard_components = []

    for option in options:
        callback_data = 'three_lives_right' if option == current_asked_word.trueAnswer else 'three_lives_wrong'
        element = [InlineKeyboardButton(text=option, callback_data=callback_data)]
        inline_keyboard_components.append(element)

    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard_components)
    await message.answer(f'Загаданное слово: *{current_asked_word.askedWord}*', reply_markup=inline_keyboard, parse_mode='Markdown')