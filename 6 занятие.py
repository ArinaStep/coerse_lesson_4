#API-программный интерфейс для управления или взаимодействия с чем-либо
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url='http://www.cbr.ru/scripts/XML_daily.asp?'
today=datetime.today()
today=today.strftime('%d/%m/%Y')
payload={'date_req':today}
response=requests.get(url,params=payload)

xml=BeautifulSoup(response.content, features='xml')

def get_course(id):
    course=xml.find('Valute',{'ID':id}).Value.text
    return course

print(get_course("R01060"), 'рублей за 10 армянских драм')
print(get_course("R01100"), 'рублей за 1 болгарский лев')
print(get_course("R01200"), 'рублей за 10 гонконгских долларов')
print(get_course("R01240"), 'рублей за 10 египетских фунтов')
print(get_course("R01375"), 'рублей за 10 китайских юаней')
print(get_course("R01670"), 'рублей за 10 таджикских сомони')

valute_from = "EUR"
valute_to = "USD"
amount = int(input("Введите сумму, которая будет конвертирована: "))


def course(valute_from, valute_to, amount):
    rates = {
        "RUR": 1.0,
        "USD": 63.0,
        "EUR": 75.0
    }

    if valute_from == "RUR":
        return amount / rates[valute_to]
    else:
        return amount / rates[valute_from] * rates[valute_to]


print("Конвертированная сумма:", course(valute_from, valute_to, amount))
