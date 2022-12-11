from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher import FSMContext
import requests
import json

bot = Bot(token="") #Тут токен
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
async def anti_flood(*args, **kwargs):
    pass

headers = {
    'authority': 'xu.su',
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://xu.su',
    'referer': 'https://xu.su/',
    'sec-ch-ua': '"Opera";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition Yx 05)',
}

@dp.message_handler(commands="start")
@dp.throttled(anti_flood,rate=5)
async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Добро пожаловать в бота ЧатБот Ержан\nПросто напиши мне, пообщаемся)\n(Основано на запросах куда то далекооооо далеко)")
    
@dp.message_handler(content_types=["text"])
@dp.throttled(anti_flood,rate=1)
async def get_text(message):
    chat_id = message.chat.id
    msg = await bot.send_message(chat_id, "Думаю...\n\nРазработчик @CTOHKC")
    try:
        json_data = {
        'uid': None,
        'bot': 'main',
        'text': message.text,
        }
        
        response = requests.post('https://xu.su/api/send', headers=headers, json=json_data)
        result = json.loads(response.text)
        
        await msg.edit_text(f"{result['text']}")
    except Exception as er:
        await msg.edit_text(f"Сервер прислал ошибку.\nОшибка: {er}")
    
while True:
    try:
        if __name__ == "__main__":
            executor.start_polling(dp, skip_updates=True)
            break
    except:
        print("Ошибка.\nОжидаем перезапуск 20 сек...")
        time.sleep(20)