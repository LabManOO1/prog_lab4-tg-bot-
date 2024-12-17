from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboard as kb
from API_func import *
from Inline_keyboard_bilder import create_inline_kb


router = Router()


class GameName(StatesGroup):
    game_name = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)


@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer('Вы нажали на кнопку информации')


@router.message(F.text == 'Топ 20 популярных игр')
async def cmd_info(message: Message):
    res = top_games()
    await message.answer('\n'.join(res))


@router.message(F.text == 'Информация о конкретной игре')
async def cmd_info(message: Message, state: FSMContext):
    await state.set_state(GameName.game_name)
    await message.answer('Введите название игры')


@router.message(GameName.game_name)
async def name_game(message: Message, state: FSMContext):
    await state.update_data(game_name=message.text)
    data = await state.get_data()
    if get_description_game(data['game_name']) == '':
        await message.answer('Игра не найдена!')
    else:
        await message.answer(get_description_game(data['game_name']))

    await state.clear()


@router.message(F.text == 'Жанр')
async def cmd_info(message: Message):
    inline_keyboard = create_inline_kb(2, *get_category_list())
    await message.answer('Выберете жанр:', reply_markup=inline_keyboard)


@router.callback_query(F.data == 'shooters')
async def shooters(callback: CallbackQuery):
    await callback.answer('Вы выбрали жанр "Шутеры"')
    await callback.message.answer('стрелялки')


@router.message(F.text == 'Платформа')
async def cmd_info(message: Message):
    inline_keyboard = create_inline_kb(1, *get_platforms_list())
    await message.answer('Выберете платформу:', reply_markup=inline_keyboard)