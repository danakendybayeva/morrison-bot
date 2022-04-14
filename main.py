import schedule
# import telegram_send
# import telegram
from aiogram import Bot, Dispatcher, executor, types

my_token = '5132531303:AAGMEB1L3hLqZzuGszu3dtZEpNLOJo56b1s'
my_chat = '-1001591101663'

bot = Bot(token = my_token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply("What's up")

# bot = telegram.Bot(token=my_token)

# bot.send_message(chat_id=my_chat, text='@danusya_k  Heeeeello')

# def greeting():
#     telegram_send.send(messages=['Test'])
#     # print("Day One")

# def main():
#     # greeting()
#     # schedule.every(5).seconds.do(greeting)
#     # schedule.every().thursday.at('11:43').do(greeting)
#     # schedule.every().day.at("12:31").do(greeting)
#     schedule.every(30).seconds.do(greeting)

#     while True:
#         schedule.run_pending()

if __name__ == '__main__':
    executor.start_polling(dp)
    # main()