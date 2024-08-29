from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message
import db_users, kb
from config_reader import db_path

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def welcome(message: Message):
    if message.chat.type == 'private':
        user = db_users.Db(db_path)
        if not user.user_exists(message.from_user.id):
            user.add_user(message.from_user.id, message.chat.id)
        user.close()
        keyboard = types.ReplyKeyboardMarkup(
            keyboard = kb.menu_keyboard,
            resize_keyboard=True
        )
        await message.answer('Добро пожаловать ' + message.from_user.full_name + '!',
                        reply_markup=keyboard)
        