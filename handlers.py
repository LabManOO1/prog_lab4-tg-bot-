from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboard as kb


router = Router()


class GameName(StatesGroup):
    game_name = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)


@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer('Вы нажали на кнопку информации')

@router.message(F.text == 'Все игры')
async def cmd_info(message: Message):
    await message.answer('')

@router.message(F.text == 'Конкретная игра')
async def cmd_info(message: Message, state: FSMContext):
    await state.set_state(GameName.game_name)
    await message.answer('Введите название игры')

@router.message(GameName.game_name)
async def name_game(message: Message, state: FSMContext):
    await state.update_data(game_name=message.text)
    data = await state.get_data()
    await message.answer(f'Вы ввели игру: {data["game_name"]}')
    await state.clear()

@router.message(F.text == 'Жанр')
async def cmd_info(message: Message):
    await message.answer('Выберете жанр', reply_markup=kb.genre)

@router.callback_query(F.data == 'shooters')
async def shooters(callback: CallbackQuery):
    await callback.answer('Вы выбрали жанр "Шутеры"')
    await callback.message.answer('стрелялки')




@router.message(F.text == 'Платформа')
async def cmd_info(message: Message):
    await message.answer('Выберете платформу', reply_markup=kb.platform)