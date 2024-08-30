import asyncio, logging
from aiogram import Bot, Dispatcher, F
from config_reader import config
from handlers import cmd_handlers, text_handlers, callback_hadlers


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(cmd_handlers.router, text_handlers.router, callback_hadlers.router)

    #cmd_handlers.set_bot(bot)
    #text_handlers.set_bot(bot)
    callback_hadlers.set_bot(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())