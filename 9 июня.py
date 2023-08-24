#класс как контекст менеджер
#with enter внутри кода блока
# exit-это выход
# import time
# class RunningCodeJudge:
#     def __init__(self):
#         self.start=None
#     def __enter__(self):
#         self.start=time.time()
#         return self
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         # print(exc_type)
#         # print(exc_val)
#         # print(exc_tb)
#         t=time.time()-self.start
#         print(f'Время работы кода : {t} секунд')
#         if exc_type is TypeError:
#             return True
# with RunningCodeJudge() as t1:
#     my_list=[x for x in range(1,10_000_000)]
#     my_list-='s'
#итератор и итерируемый объект
# my_list=[1,2,3,4,5]
# list_iteration=iter(my_list)
# print(next(list_iteration))
# print(next(list_iteration))
# print(next(list_iteration))
# print(next(list_iteration))
#
#
# for i in list_iteration:
#     print(i)
# import random
# class RandomIter:
#     def __init__(self,limit):
#         self.limit=limit
#         self.__reload=limit #это для того чтобы выводилось 2 раза(сняли ограничения)
#     def __iter__(self):
#         self.limit=self.__reload #это для того чтобы выводилось 2 раза(сняли ограничения)
#         return self
#     def __next__(self):
#         if self.limit==0:
#             raise StopIteration
#         self.limit-=1
#         return random.randint(0,101)
# rand_iter=RandomIter(10)
# # print(iter(rand_iter))
# # print(next(rand_iter))
# for rand_int in rand_iter:
#     print(rand_int)
# for rand_int1 in rand_iter:
#     print(rand_int1)

class CardDeck:
    def __init__(self):
        self.suits=['пик',"бубен","червей","крестей"]
        self.ranks=[*range(2,11), 'J',"Q",'K','A']
        self.length=52
        self.index=0
    def __next__(self):
        if self.index>= self.length:
            raise StopIteration
        else:
            suit= self.suits[self.index//len(self.ranks)]
            rank=self.ranks[self.index%len(self.ranks)]
            self.index+=1
            return f'{rank}{suit}'
    def __iter__(self):
        return self
deck=CardDeck()
while True:
    print(next(deck))
