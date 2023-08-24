# элементы функционального программирования
from pprint import pprint
if __name__=='__main__':
    goods=[
    {
        'name':'Iphone 14',
        'brand':'Apple',
        'price':1200
    },
    {
        'name':'Samsung Galaxy A53',
        'brand':'Samsung',
        'price':500
    },
        {
        'name':'Realne C25s',
        'brand':'Realne',
        'price':400
     }
     ]
    # def item_price(item):
    #     return item['price'] # item.get('price')
    # print(sorted(goods,key=item_price))

    # pprint(sorted(goods,key=lambda item:item['price']))
    # apple_list=list(filter(lambda item:item['brand']=='Apple',goods))
    # print(apple_list)

    # numbers=['1','2','3','4','5','6']
    # numbers=list(map(int,numbers)) #это значит что каждый элемент станет int
    # print(numbers)
    names=['Даниил',"Павел","Анастасия","Екатерина"]
    surnames=['Петров',"Иванов","Сидорова","Данилова"]
    patronymic=['Александрович',"Никитич","Евгеньевна","Ивановна"]
    # full_names=list(map(lambda name,surname:f'{name} {surname}',names,surnames))#соединяет последовательно элементы списков
    # print(full_names)
    #функция enumerate
    # index_good=[]
    # for i,item in enumerate(goods):
    #     index_good.append({i:item})
    # pprint(index_good)
    for surname,names,patronymic in zip(surnames,names,patronymic):#объединяет элементы списка
        print(surname,names,patronymic)

    #__name__
print(__name__)
