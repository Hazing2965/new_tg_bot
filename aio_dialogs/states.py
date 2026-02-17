from aiogram.fsm.state import StatesGroup, State


class state_user(StatesGroup):
    start = State()
    clic = State()
    

class state_admin(StatesGroup):
    start = State()

