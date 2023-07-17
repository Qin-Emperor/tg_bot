from aiogram import *
from aiogram.types import *
from random import randint

helping_text = """
Список команд
/start - начинает работу
/help - список команд
/media - социальние сети авторов
/work - простая функция
"""

token = '6384893174:AAELwm6z69J391zi20CRY3L0hDJFYmRjWEc'
bot = Bot(token)
dp = Dispatcher(bot)

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton(text='/help'))
main_kb.add(KeyboardButton(text='/media'))
main_kb.add(KeyboardButton(text='/work'))

in_kb = InlineKeyboardMarkup(row_width=3)
in_kb.add(InlineKeyboardButton(text='random', callback_data='gen'))

help_kb = InlineKeyboardMarkup(row_width=3)
help_kb.add(InlineKeyboardButton(text='Telegram', url='t.me/His_Majesty_Qin'))

async def start(_):
    print('Bot works')

@dp.message_handler(commands=['start'])
async def st(message: types.Message):
    await bot.send_message(message.chat.id, text=f'Привет, {message.from_user.first_name}.', reply_markup=main_kb)

@dp.message_handler(commands=['help'])
async def hp(message: types.Message):
    await bot.send_message(message.chat.id, text=helping_text)

@dp.message_handler(commands=['work'])
async def work(message: types.Message):
    await bot.send_message(message.chat.id, text='Выберите что будем делать: ', reply_markup=in_kb)

@dp.callback_query_handler(lambda c: c.data == 'gen')
async def mes(callback: types.CallbackQuery):
    await callback.message.answer(text=randint(1, 100))

@dp.message_handler(commands=['media'])
async def work(message: types.Message):
    await bot.send_message(message.chat.id, text='Социальные сети: ', reply_markup=help_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start)
