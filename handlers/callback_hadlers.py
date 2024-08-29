from aiogram import Router, types, F
import db_users
from config_reader import db_path, user_answers
from def_game.immortal_mode import play_immortal_mode
from def_game.three_lives_mode import play_three_lives_mode
from def_game.reply_text import reply_message_default, game_over_msg, game_over_msg_rec

router = Router()
bot = None

def set_bot(instance):
    global bot
    bot = instance

async def kb_clean(chat_id, message_id):
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)

@router.callback_query(F.data == "immortal_right")
async def right_answer(callback: types.CallbackQuery):
    await kb_clean(callback.message.chat.id,callback.message.message_id)

    db_for_stats = db_users.Db(db_path)
    db_for_stats.add_true_survansw(user_id=callback.from_user.id)
    db_for_stats.close()

    await callback.message.answer('Правильно!')
    await play_immortal_mode(callback.message)
    await callback.answer()

@router.callback_query(F.data == "immortal_wrong")
async def wrong_answer(callback: types.CallbackQuery):
    await kb_clean(callback.message.chat.id,callback.message.message_id)

    user_data = user_answers.get(callback.message.chat.id, {})
    correct_answer = user_data.get('true_answer')
    db_for_stats = db_users.Db(db_path)
    db_for_stats.add_wrong_surwansw(user_id=callback.from_user.id)
    db_for_stats.close()

    await callback.message.answer(f'Вы ошиблись, верный перевод: *{correct_answer}* \n', parse_mode='Markdown')
    await play_immortal_mode(callback.message)
    await callback.answer()

@router.callback_query(F.data == "three_lives_right")
async def right_answer(callback: types.CallbackQuery):
    await kb_clean(callback.message.chat.id,callback.message.message_id)

    user_data = user_answers.get(callback.message.chat.id, {})
    lives = user_data.get('lives', None)
    guessed_words = user_data.get('guessed_words', 0)
    guessed_words += 1

    await callback.message.answer('Правильно!')
    await play_three_lives_mode(callback.message, lives=lives, guessed_words=guessed_words)
    await callback.answer()    

@router.callback_query(F.data == "three_lives_wrong")
async def wrong_answer(callback: types.CallbackQuery):
    await kb_clean(callback.message.chat.id,callback.message.message_id)

    user_data = user_answers.get(callback.message.chat.id, {})
    lives = user_data.get('lives', None)
    guessed_words = user_data.get('guessed_words', 0)
    correct_answer = user_data.get('true_answer')

    lives -= 1

    if lives <= 0:
        db_for_stats = db_users.Db(db_path)
        print(f'callback.message.from_user.id: {callback.message.from_user.id}\n{guessed_words}')
        if db_for_stats.livesModeRecord(callback.message.chat.id, guessed_words):
            db_for_stats.close()
            await callback.message.answer(game_over_msg_rec(guessed_words=guessed_words))
            await callback.answer() 
        else:
            db_for_stats.close()         
            await callback.message.answer(game_over_msg(guessed_words=guessed_words))
            await callback.answer() 
    else:
        await callback.message.answer(reply_message_default(correct_answer=correct_answer,lives=lives))
        await play_three_lives_mode(callback.message, lives=lives, guessed_words=guessed_words)
        await callback.answer()    

@router.callback_query(F.data == "refresh_stats")
async def refresh_stats(callback: types.CallbackQuery):
    await kb_clean(callback.message.chat.id,callback.message.message_id)
    db = db_users.Db(db_path)
    db.refresh_the_stats(user_id=callback.message.chat.id)
    db.close()
    await callback.message.answer('Статистика обнулена.')
    

