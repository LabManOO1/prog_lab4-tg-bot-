from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Топ 20 популярных игр')], [KeyboardButton(text='Конкретная игра')],
                                     [KeyboardButton(text="Жанр"), KeyboardButton(text='Платформа')]],
                           resize_keyboard=True, input_field_placeholder='Выберете что нужно вывести...')

genre = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Шутеры', callback_data='shooters')],
                                              [InlineKeyboardButton(text='Стратегии', callback_data='strategies')]])


platform = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='PC', callback_data='PC')],
                                              [InlineKeyboardButton(text='Браузер', callback_data='Web Browser')]])
