from aiogram import Router, F
from aiogram.types import Message
from def_game.immortal_mode import play_immortal_mode
from def_game.three_lives_mode import play_three_lives_mode
from def_game.show_stats import stats
router = Router()


@router.message(F.text.lower() == "бесконечный режим")
async def play_immortal(message: Message):
    await play_immortal_mode(message)

@router.message(F.text.lower() == "три жизни")
async def answer_no(message: Message):
    await play_three_lives_mode(message)

@router.message(F.text.lower() == "статистика")
async def answer_no(message: Message):
    await stats(message)

