from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("Дальше", callback_data='go')
    # btn1 = InlineKeyboardButton("", callback_data='')
    # btn1 = InlineKeyboardButton("", callback_data='')

    markup.add(btn1)
    return markup


def back_btn():
    back = InlineKeyboardButton("Назад", callback_data='back')

    return back


def make_sale():
    markup = InlineKeyboardMarkup()
    do = InlineKeyboardButton('Интересно!', callback_data='sale')

    markup.add(do)
    return markup