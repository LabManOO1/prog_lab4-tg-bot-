from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboard as kb
from API_func import *
from Inline_keyboard_bilder import create_inline_kb


router = Router()


class GameName(StatesGroup):  # Класс для состояния при вводе пользователем названия игры
    game_name = State()


@router.message(CommandStart())  # команда /start
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)


@router.message(F.text == 'Топ 20 популярных игр')  # Обработка кнопки для вывода 20-ти самых популярных игр
async def cmd_info(message: Message):
    res = top_games()
    await message.answer('\n'.join(res))


@router.message(F.text == 'Информация о конкретной игре')  # Обработка кнопки для вывода информации об игре
async def cmd_info(message: Message, state: FSMContext):
    await state.set_state(GameName.game_name)
    await message.answer('Введите название игры')


@router.message(GameName.game_name)  # Обработка ввода пользователем названия игры
async def name_game(message: Message, state: FSMContext):
    await state.update_data(game_name=message.text)
    data = await state.get_data()
    if get_description_game(data['game_name']) == '':
        await message.answer('Игра не найдена!')
    else:
        await message.answer(get_description_game(data['game_name']))

    await state.clear()


@router.message(F.text == 'Жанр')  # Выбор жанра
async def cmd_info(message: Message):
    inline_keyboard = create_inline_kb(2, *get_category_list())
    await message.answer('Выберете жанр:', reply_markup=inline_keyboard)


@router.message(F.text == 'Платформа')  # Выбор платформы
async def platform(message: Message):
    inline_keyboard = create_inline_kb(1, *get_platforms_list())
    await message.answer('Выберете платформу:', reply_markup=inline_keyboard)


@router.callback_query(F.data.in_(get_platforms_list()))  # Вывод игр выбранной платформы
async def click_platform(callback: CallbackQuery):
    res = get_games_by_platforms(callback.data)
    await callback.message.answer('\n'.join(res))


@router.callback_query()  # Вывод игр выбранного жанра
async def click_categories(callback: CallbackQuery):
    res = get_games_by_category(callback.data)
    await callback.message.answer('\n'.join(res))
