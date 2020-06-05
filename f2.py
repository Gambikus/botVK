import requests
import vk_api
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import pymorphy2
f = open('mats.txt', 'r', encoding='utf8')
mats = f.read().split()
print(mats)
morph = pymorphy2.MorphAnalyzer()
vk_session = vk_api.VkApi(token='token')
longpoll = VkBotLongPoll(vk_session, group_id=187735439, wait=25)
vk = vk_session.get_api()

schotch = 0

for event in longpoll.listen():
    print(event.type)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_user:
            pass
            # vk.messages.send(user_id=event.user_id, message='Привет.',random_id = int(time.time()))
        if event.from_chat:
           # if event.obj['from_id'] == 345833617:
               # vk.method("messages.removeChatUser",
                         # {"chat_id": event.chat_id, "user_id": 345833617, "random_id": event.random_id})*/
            print(event.chat_id)
            fr = False
            a = event.obj['text']
            for i in a.lower().split():
                t = ' '
                for k in i:
                    if k.isalpha() and k != t[-1]:
                        t += k

                for g in morph.parse(t.strip()):
                    if g[2] in mats:
                        Name = vk.users.get(user_ids=event.obj["from_id"])[0]["first_name"]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=event.obj["random_id"],
                            message='Не сквернословь, ' + Name + '❤')
                        fr = True
                        break
                    if fr:
                        break
                if fr:
                    break

            print("Chat: ")
