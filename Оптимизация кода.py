
def simple(*args):
    print(args)
simple(1)
simple(1,2,3)

def simple_1(**kwargs):
    print(kwargs)
    print(kwargs.get('str'))
simple_1(one=1,two=2,str='String')

def simple_2(*args,x,**kwargs):
    print(f'x:{x}')
    print(f'Args:{args}')
    print(f'Kwargs:{kwargs}')
simple_2(1,2,3,x=10,one='1')


print([i for i in range(5)])

temp=[element for element in range(10) if element%2 ==0]
print(temp)

m_temp={'temp':1}
m_dict={i:i for i in range(10)}
print(m_dict)

list_word=['a','aa','aaa','aaaa','aaaaa']
m_dict1={element:len(element) for element in list_word}
print(m_dict1)

temp_3=('str',2,3,4,True)

temp_4=([1,],[2,3],3,4,True)
print(temp_4)
print(temp_4[0][0])
temp_4[0][0]=10
print(temp_4)

numbers1 = []
numbers2 = []

for i in range(10):
    number = int(input("Введите число: "))
    if number % 2 == 0:
        numbers1.append(number)
    else:
        numbers2.append(number)

print("Четные числа:", numbers1)
print("Нечетные числа:", numbers2)
a = (5, 3, 2, 1, 4)
b = tuple(sorted(a, key=tuple))

print('Первый кортеж:', a)
print('Отсортированный кортеж:', b)