import asyncio


async def flush_all():
    from loader import db
    print('Очистка базы...')

    await db.gino.drop_all()
    print('Готово')
    print('Создание таблиц...')
    await db.gino.create_all()
    print('Готово')


async def on_startup(dp):
    import middlewares
    from utils.db_api import database

    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify

    print('Подключение к базе данных...')
    await database.on_startup(dp)
    print('Подключение установлено')
    await flush_all()
    await on_startup_notify(dp)

if __name__ == '__main__':
    import filters
    filters.setup()

    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
