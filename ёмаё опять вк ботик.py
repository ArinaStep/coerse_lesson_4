import random
from coerse import *
from wiki import *
import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
def main():
    TOKEN='vk1.a.MeZU_BS33N7z7tUtalqlivIXnVmNJvGb_gkU7m_-DrFBnFTUP_rXONloxbyemG7dP5YJqOxRNkt15lPMXbKVpxFKIo3kIeWS4utL80tKmqf7X61njDuSdjtkcyIOeDQ83VMGBevW_9hNuXHmWloN_JlEg5psPW-1gc-aHoQiV9biBfQ_hPZXlmlkzLkzyih3WMKTDTmkAw-Wj8YmzYJNcg'

    vk_session=vk_api.VkApi(token=TOKEN)
    vk=vk_session.get_api()
    longpoll=VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            user_id=event.user_id
            random_id=random.randint(1,100000000)

            if msg=='курс':
                responce='{0} рублей за 1 доллар \n \'' \
                         '{1} рублей за 1 евро\n'\
                         '{2} рублей за 1 фунт'
                responce=responce.format(getCourse('R01235'),getCourse('R01239'),getCourse('R01035'))
                vk.messages.send(user_id=event.user_id, random_id=random_id,message=responce)
            elif msg[0:2]== '-в':
                article =msg[2:]
                responce=get_wiki_article(article)
            else:
                responce='Неизвестная команда'
            vk.messages.send(user_id=event.user_id, random_id=random_id, message=responce[0:4096])#4096-максимальное допустимое кол-во символо в сообщении ВК
main()