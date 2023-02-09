from aiogram.types import *

keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

buttons = []
buttons.append(KeyboardButton(text="/help"))
buttons.append(KeyboardButton(text="/now"))
buttons.append(KeyboardButton(text="/tomorrow"))
buttons.append(KeyboardButton(text="/week"))

for button in buttons:
    keyboard.add(button)