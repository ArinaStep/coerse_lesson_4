import vk_api
from coerse import *
token='vk1.a.MeZU_BS33N7z7tUtalqlivIXnVmNJvGb_gkU7m_-DrFBnFTUP_rXONloxbyemG7dP5YJqOxRNkt15lPMXbKVpxFKIo3kIeWS4utL80tKmqf7X61njDuSdjtkcyIOeDQ83VMGBevW_9hNuXHmWloN_JlEg5psPW-1gc-aHoQiV9biBfQ_hPZXlmlkzLkzyih3WMKTDTmkAw-Wj8YmzYJNcg'

vk=vk_api.Vkapi(token=token)

vk._auth_token()
while True:
    messages=vk.method('messages.getConversations', {'count':20, 'filter':'unanswered'})
    print(messages)
    if messages['count']>=1:
        user_id=messages['items'][0]['last message']['from_id']
        text=messages['items'][0]['last message']['text']
        message_id = messages['items'][0]['last message']['id']
        if text.lower =='курс':
            vk.method('messages.send',{'peer_id':user_id, 'random_id':message_id, 'message':getCourse('R01235')})
        if text.lower=='диаметр планеты':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': getCourse('diameter')})
        if text.lower=='корабли':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': getCourse('fastest_ship')})
        else:
            vk.method('messages.send',{'peer_id':user_id, 'random_id':message_id, 'message':"неизвестная команда"})