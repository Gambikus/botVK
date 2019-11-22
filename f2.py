import requests
import vk_api
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import pymorphy2
f = open('mats.txt', 'r', encoding='utf8')
mats = f.read().split()
print(mats)
morph = pymorphy2.MorphAnalyzer()
vk_session = vk_api.VkApi(token='22b50f62f62e145c1e59c7003be9dd2c05baa0cfe34f39a29c05afc91b64efd3c74fee13a685a416d617f')
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
            if 'васЬ' in a or 'веретен' in a:
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id=event.random_id,
                    message='Тебе лучше помолчать')
            if a == 'Сквернословь':
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id=event.obj["random_id"],
                    message='Не сквернословь, ❤')
            for i in a.lower().split():
                t = ' '
                for k in i:
                    if k.isalpha() and k != t[-1]:
                        t += k

                for g in morph.parse(t.strip()):
                    if g[2] in mats or i == 'бурдюг':
                        if event.obj["from_id"] == 198097059:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=event.obj["random_id"],
                                message='Фуу быдло....')
                        elif event.obj["from_id"] == 225633300:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=event.obj["random_id"],
                                message='Не сквернословь, Кирюша!!!❤')
                        else:
                            Name = vk.users.get(user_ids=event.obj["from_id"])[0]["first_name"]
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=event.obj["random_id"],
                                message='Не сквернословь, ' + Name + '❤')
                        fr = True
                        if schotch % 3 == 0:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=event.obj["random_id"],
                                message='Ищем девочку другу. Артём Биский, 16 лет. \n Б - божественный \n И - интересный \n С -сексуальный \n К - красивый \n И - идеальный \n Й - умный \n За подробностями сюда - https://vk.com/gambikus ')
                        schotch += 1
                        print(schotch)
                        break
                    if fr:
                        break
                if fr:
                    break

            print("Chat: ")
