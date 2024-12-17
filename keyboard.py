from aiogram.filters.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from API_func import *

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Топ 20 популярных игр')],
                                     [KeyboardButton(text='Информация о конкретной игре')],
                                     [KeyboardButton(text="Жанр"), KeyboardButton(text='Платформа')]],
                           resize_keyboard=True, input_field_placeholder='Выберете что нужно вывести...')

