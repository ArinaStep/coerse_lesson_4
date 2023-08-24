import time
my_lists=[time.sleep(x) for x in range (1,3)] #строгое вычисление
print(my_lists)

my_lists1=(time.sleep(x) for x in range(1,3)) #ленивое вычисление
print(my_lists1)
