from loader import dp
from aiogram.types import Message
from utils.misc.metrics import get_metrics

admins = [626041522, ]
banned_queries = []

@dp.message_handler(lambda u: u.from_user.id in admins,commands=['start'])
async def start_handler(msg: Message, state):
    data = get_metrics('postgres', 'userA', 'userA')
    for i in range(len(data)):
        await msg.answer(data[i])

@dp.message_handler(lambda u: u.from_user.id in admins,commands=['add'])
async def add_user(msg: Message, state):
    uid = int(msg.get_args())
    admins.append(uid)
    await msg.answer('Пользователь добавлен')

@dp.message_handler(lambda u: u.from_user.id in admins,commands=['q'])
async def add_user(msg: Message, state):
    q = msg.get_args()
    banned_queries.append(q)
    await msg.answer('Запрос добавлен')
