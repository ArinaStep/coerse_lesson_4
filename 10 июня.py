#геттеры и сеттеры
# class People:
#     def __init__(self,name,year)-> None:
#         self.__name=name
#         self.__year=year
#     #геттерю метод для получения аттрибутов
#     @property
#     def get_name(self):
#         return self.__name
#     def get_year(self):
#         return self.__year
#     # сеттер метод для установления аттрибута
#     @property
#     def set_name(self,name):
#         if len(name)<2 or len(name)>147:
#             raise Exception('Неккоректное значение')
#         self.__name=name
#     def set_year(self,year):
#         if len(year)<1900 or len(year)>2023:
#             raise Exception('Неккоректное значение')
#         self.__year=year
# people1=People('Pavel',2000)
# people1.set_name('Oleg')
# people1.set_year('2010')
#
# print(people1.get_name())
# print(people1.get_year())

class People:
    def __init__(self,name,year)-> None:
        self.__name=name
        self.__year=year
    #геттер. метод для получения аттрибутов
    @property
    def get_name(self):
        return self.__name
    @property
    def get_year(self):
        return self.__year
    # сеттер метод для установления аттрибута
    @name.setter
    def name(self,name):
        if len(name)<2 or len(name)>147:
            raise Exception('Неккоректное значение')
        self.__name=name
    @year.setter
    def year(self,year):
        if year<1900 or year>2023:
            raise Exception('Неккоректное значение')
        self.__year=year
    @name.deleter
    def name(self):
        del self.__name

    @year.deleter
    def name(self):
        del self.__year


people1=People('pavel',2000)
print(people1.name)
del people1.name
del people1.year
class MyList(list):
    def delete_last_item(self):
        self.pop()
x=MyList(1,2,3,4,5,6)
x.delete_last_item()
print(x)