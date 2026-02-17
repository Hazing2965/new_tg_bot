from dotenv import load_dotenv
from os import getenv
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()


# Конфигурируем логирование
handler = RotatingFileHandler(
    filename="bot.log",
    encoding="utf-8",
    maxBytes=1024*1024*5,  # 5 МБ
    backupCount=1
)
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s',
    handlers=[
        handler,
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Настройки Redis
REDIS_HOST = getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(getenv('REDIS_PORT', 6379))
REDIS_DB = int(getenv('REDIS_DB', 0))

# Настройки Telegram
BOT_TOKEN = getenv('BOT_TOKEN')

# Режим работы
TEST_MODE = True