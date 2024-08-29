import db_users
from config_reader import db_path
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from def_game.reply_text import stats_msg

async def stats(message: types.Message):
    db = db_users.Db(db_path)

    right_answers, wrong_answers, surv_record = (
        db.get_true_srvc(message.from_user.id), 
        db.get_wrong_srvc(message.from_user.id), 
        db.get_lives_mode(message.from_user.id))
    total_count = right_answers + wrong_answers

    db.close()

    if total_count != 0:
        non_round_right_proc = (right_answers/(right_answers+wrong_answers)) * 100
        right_proc = round(non_round_right_proc, 2)
    else: right_proc = 0

    inline_keyboard_components = []
    element = [InlineKeyboardButton(text='Обнулить статистику', callback_data='refresh_stats')]
    inline_keyboard_components.append(element)
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard_components)

    await message.answer(stats_msg(total_count, right_answers, wrong_answers, right_proc, surv_record),
                         reply_markup=inline_keyboard, parse_mode='Markdown')


