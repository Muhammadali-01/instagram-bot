import logging

from aiogram import Bot, Dispatcher, executor, types
from test import video_yuklab_ber
API_TOKEN = 'YOUR API TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom\n Bu instagram bot")



@dp.message_handler()
async def echo(message: types.Message):
    mes_text = message.text
    video_link = video_yuklab_ber(mes_text)
    await message.answer("Video yuklanmoqda")
    await message.answer_video(video_link, caption="video ma'lumot")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
