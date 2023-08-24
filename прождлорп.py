# import time
# my_lists=[time.sleep(x) for x in range (1,3)] #строгое вычисление
# print(my_lists)
#
# my_lists1=(time.sleep(x) for x in range(1,3)) #ленивое вычисление
# for elem in my_lists1:
#     print(elem)
# print(my_lists1)
# my_range=list(range(1,10)) #ленивая функция которая выводит [1,2,3,4,5,6,7,8,9]
# print(my_range)
#
# def  lazy_func():
#     for i in range(1,11):
#         print(f'До{i}')
#         yield i
#         print(f'После{i}')
#  for i in lazy_func():
#      print(i)
#
# my_lists1=list(lazy_func())
# print(my_lists1)
#
# def lazy_func2(items):
#     yield from items
# items=['яблоко',"апельсин","банан"]
# for i in lazy_func2(items):
#     print(i)

# with open('file,txt', 'w') as f:
#     f.write('Hello,world')
#     print(f.closed)
# print(f.closed)
#
import  contextlib
@contextlib.contextmanager
def str_reverse(my_str):
    print('Выводим в сонтекст менеджер:')
    yield my_str[::-1] #пишет задом наперед
    print('Выходим из контекста менеджера')
with str_reverse('Hello,world') as reverse_str:
    print(f'Выполняется код:{reverse_str}')
import contextlib
@contextlib.contextmanager
def exc_hanler(exc):
    try:
        yield True
    except exc:
        print('Произошло исключение')
with exc_hanler(IndexError):
    my_l=[1,2]
    print(my_l[3])

def func_with_args_and_kwargs(*args,**kwargs):
    print(f'Арги:{args}\n Кварги: {kwargs}')
func_with_args_and_kwargs(b=3,c=4,d=5,e=6)

#первый вариант
# def generator_1(n):
#     for i in range(n):
#         yield i ** 2
# # второй вариант
# def generator_2(n):
#     num_list = [i for i in range(n)]
#     return [x ** 2 for x in num_list]
# #тест
# import time
# def test(generator):
#     start_time = time.time()
#     result = list(generator(1000000))
#     end_time = time.time()
#     print(f'Time: {end_time - start_time:.5f} seconds')
#     print(f'Generated {len(result)} numbers')
#
# test(generator_1)
# test(generator_2)
# #homework
# import contextlib
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
#
# url = "http://www.cbr.ru/scripts/XML_daily.asp?"
#
# today = datetime.today()
# today = today.strftime("%d/%m/%Y")
#
# payload = {"date_req": today}
#
# response = requests.get(url, params=payload)
#
# xml = BeautifulSoup(response.content, 'lxml')
#
#
# currency = input('Введите код валюты: ')
# valute_name = xml.find('valute', {'id': currency}).charcode.text
# @contextlib.contextmanager
# def get_course(currency):
#     try:
#         yield xml.find("valute", {'id': currency}).value.text
#     except currency:
#         print('валюта не найдена')
# with get_course(currency) as currency:
#     print(f"(1 шт.) {valute_name} стоит(ят) {currency} руб.")
