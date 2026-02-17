from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from aio_dialogs.states import state_admin, state_user

router = Router()

@router.message(Command(commands=['start']))
async def process_start_command(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=state_user.start, mode=StartMode.RESET_STACK)

@router.message(Command(commands=['admin']))
async def process_admin_command(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=state_admin.start, mode=StartMode.RESET_STACK)

@router.message(Command(commands=['id']))
async def process_search_id_command(message: Message):
    await message.answer(f'Ваш ID: <code>{message.from_user.id}</code>')