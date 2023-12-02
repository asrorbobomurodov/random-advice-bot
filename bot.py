from seetings import TOKEN
from bored.main import Bored
from time import sleep
import requests

def bot(chat_id: str, text: str):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.get(url, params=payload)

    return response.json()

def get_message():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(url)
    data = r.json()['result'][-1]
    return data

id = -1
while True:
    data = get_message()
    update_id = data['update_id']

    if id != update_id:

        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        
        menus = ['/start', '/charity', '/sport', '/education', 
                 '/recreational', '/social', '/diy', '/cooking', 
                 '/relaxation', '/busywork']

        if text == "/start":
            bot(chat_id, "Welcome to my bot")
        
        elif text == '/random':
            obj = Bored()
            retort = obj.get_activity()['activity']
            bot(chat_id, retort)

        elif text in menus:
            obj = Bored()
            answer = obj.get_activity_by_type(text[1:])['activity']

            dct = {
                '/charity': answer,
                '/sport': answer,
                '/education': answer,
                '/recreational': answer,
                '/social': answer,
                '/diy': answer,
                '/cooking': answer,
                '/relaxation': answer,
                '/busywork': answer,
            }
            
            reply = dct.get(text, "Error")
            bot(chat_id, reply)

        else:
            bot(chat_id, "Please, choose anyone menu")

        id = update_id
    
    sleep(1)