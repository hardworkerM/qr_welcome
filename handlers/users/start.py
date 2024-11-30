import time

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot

from message_texts import texts as t
from help_functions.sql import user as u
from keyboards.inline.mane_kb import main_menu, make_sale
from aiogram.types import CallbackQuery
import datetime
import random
from aiogram.types import InputFile
import os
from pathlib import Path
from help_functions.make_mokap import add_qr_to_shirt_centered
# from make_user_mokap import add_qr_to_shirt_centered
import hashlib
import base64


async def send_info(what_happened, alias, id=None):
    date = datetime.datetime.now()
    text = f'👨‍💻\n@{alias} or id:{id}\n📲\n{what_happened}\n🕐\n{date}'
    await bot.send_message(565843474, text)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # await message.answer(f"Привет, {message.from_user.full_name}!")
    user_id = message.from_user.id

    await send_info('start bot', message.chat.username, message.chat.id)
    # if not u.check_user(user_id):
    #     u_name = message.from_user.full_name
    #     await message.answer(t.hello_text)
    #     u.main_info_fill((user_id, u_name))

    gif_path = 'src/file.gif'

    gif_path=os.path.join(os.path.dirname(__file__), 'src/file.gif')
    file_id = 'CgACAgIAAxkDAAOaZzf4dxX56s9vjjBdz7RyJ7nnJDgAAvdUAAIiL8FJVTrn8UNBS482BA'

    try:
        await bot.send_animation(chat_id=message.chat.id, animation=file_id)
    except Exception:
        await bot.send_animation(chat_id=message.chat.id, animation=InputFile(gif_path))

    await message.answer(t.menu_text, reply_markup=main_menu())


@dp.callback_query_handler(text='go')
async def explain1(call: CallbackQuery):
    # await call.message.answer('Объясняю как это работает')
    await send_info('press button go', call.message.chat.username, call.message.chat.id)

    image_path = os.path.join(os.path.dirname(__file__), 'src/1step.jpg')
    caption = t.explain_text1
    with open(image_path, 'rb') as file:
        a1 = await bot.send_photo(chat_id=call.message.chat.id, photo=file, caption=caption)
    # print(a1)
    time.sleep(10)

    image_path = os.path.join(os.path.dirname(__file__), 'src/2step.jpg')
    caption = t.explain_text2
    file_id1 = 'AgACAgIAAxkDAAO0ZzgIEDg0zxwcfeonEUq_rB7splsAApnhMRsiL8FJ91n1rCjGi_MBAAMCAANzAAM2BA'
    file_id2 = 'AgACAgIAAxkDAAO1ZzgIFaMP-74kYLrd8zST0wXgYZoAAprhMRsiL8FJQRSLwQ6p1VUBAAMCAAN5AAM2BA'
    with open(image_path, 'rb') as file:
        a2=await bot.send_photo(chat_id=call.message.chat.id, photo=file, caption=caption)
    time.sleep(10)

    image_path = os.path.join(os.path.dirname(__file__), 'src/text_example.png')
    caption = t.explain_text3
    with open(image_path, 'rb') as file:
        a2 = await bot.send_photo(chat_id=call.message.chat.id, photo=file, caption=caption)
    time.sleep(10)

    # user_id = call.message.chat.id
    # add_qr_to_shirt_centered(user_id=user_id)
    # print('РАБТАЮ С ПОЕБИКОЙ')
    # image_path = os.path.join(os.path.dirname(__file__), f'src\\mokap_done{user_id}.png')
    # with open(image_path, 'rb') as file:
    #     a2=await bot.send_photo(chat_id=call.message.chat.id, photo=file, caption=caption)
    # print(a2)
    await call.message.answer(t.end)


@dp.callback_query_handler(text='sale')
async def end_user(call: CallbackQuery):
    await call.message.answer('Большое спасибо за интерес к проекту!\n'
                              'Мы будем делиться нашими новостями в телеграмм канале https://t.me/quar_news\n'
                              'Буду рад вашим комментариям')

    # sale_vals = [5, 10, 15, 20]
    # sale_weights = [60, 20, 10, 5]
    #
    # sale = random.choices(sale_vals, cum_weights=sale_weights, k=1)
    # sale = str(sale[0])
    # a = ['5️⃣', '1️⃣', '2️⃣0️⃣', '1️⃣0️⃣', '1️⃣5️⃣']
    # await send_info('press button SALE!!', call.message.chat.username, call.message.chat.id)
    #
    # await call.message.answer(t.end_text+sale)
