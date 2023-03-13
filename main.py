from telethon import TelegramClient, errors, events, utils
from chat import ChatBot

API_ID = 20951724
API_HASH = "1784c4f55ea7c0008c8c09695b4d8242"
chatbot = ChatBot()

client = TelegramClient("AAAAAAAAAAAAAAAAAAAA", API_ID, API_HASH)
@client.on(events.NewMessage())
async def handler_new_message(event: events.newmessage.NewMessage.Event):
    try:
        reply = chatbot.parcer(event.message.message.lower())
        await client.send_message(event.chat, reply)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    client.start(bot_token="6152978052:AAH0QznLvEmEwtM0kg8oLjmTJCSpUUFUUh0")
    client.run_until_disconnected()