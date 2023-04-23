import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message


bot = Bot(token='6023656375:AAE7d_7qn782FQPZkTXx_154cmQKA2DzyNA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    # Приветственное сообщение
    await bot.send_message(message.chat.id, "Чтобы получить номера, используй /num")


@dp.message_handler(commands=['num'])
async def num_command_handler(message: types.Message):
    await message.answer('Введите количество игроков (от 7 до 10):')


@dp.message_handler(lambda message: message.text.isdigit() and int(message.text) in range(7, 11))
async def process_num(message: types.Message):
    num_players = int(message.text)
    player_numbers = random.sample(range(1, num_players + 1), num_players)

    # Создаем словарь с заменами номеров игроков
    replacements = {i: player_numbers[(i + 2) % num_players] for i in range(1, num_players + 1)}

    # Формируем ответное сообщение со списком замен
    response_message = 'Замена номеров для игроков:\n'
    for i, new_number in replacements.items():
        response_message += f'{i} => {new_number}\n'

    await message.answer(response_message)


if __name__ == '__main__':
    executor.start_polling(dp)
