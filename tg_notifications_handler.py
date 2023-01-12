from telethon import events
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat
from background import keep_alive


api_id = <YOUR_API_ID> #check my.telegram.org to get api id and hash
api_hash = <YOUR_API_HASH>
client = TelegramClient('session', api_id, api_hash)
phone = <YOUR_PHONE_NUMBER_WITH_COUNTRY_CODE>
password = <PASSWORD_THAT_TG_SENDS_TO_YOU> #for the first run paste 11111 here;
                                           #in the first run you'll have to enter your password manually in terminal
                                           #after that, you can paste it here and everything will be done automatically in next runs
receiver = InputPeerChat(<WANTED_CHAT_ID>) #chat id of a receiver, it is easy to google how to get it
#IMPORTANT NOTE
#if the receiver is not a group chat, but, for example, another user, you might want to change InputPeerChat->InputPeerUser or whatever you need


white_list = ["word1", "word2", "etc"] #lists for wanted and unwanted words/phrases, that is to say, strs
black_list = ["word11", "word22", "etc!"]
def filter_words(event): #simple filtration
    for wanted_word in white_list:
        if wanted_word in event.raw_text:
            for unwanted_word in black_list:
                if unwanted_word in event.raw_text:
                    return False
            return True
    return False

#activates when new message that passes the filter comes in a specified chat
@client.on(events.NewMessage(incoming=True, chats=<CHAT_ID_TO_GET_MESSAGED>, func=filter_words))
async def notifications_handler(event):
    message = event.raw_text #gets text of the message
    await client.send_message(receiver, message, parse_mode='html') #sends message to the receiver


keep_alive() #runs flask server, needed to keep script running 24/7 on some vps
client.start(phone=phone, password=password) #starting client
client.run_until_disconnected() #running it forever
