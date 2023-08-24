#Словари
my_dict={'+79960167069':'Arina'}
my_dict['89308794530']='Mother'
#Списки и циклы
name='Pavel'
salary=100_000#нижнее подчёркивание для того, чтобы визуально было красивее
print(f'у {name} зарплата в месяц- {salary}')
print(f'у {name} зарплата в год- {salary*12}')

emlore={
'name':'Pavel',
'salary':100_000
}
print(f"у {emlore['name']} зарплата в месяц- {emlore.get('salary')}")#Вид ковычек имеет значение! внешние лучше ставить двойные ковычки, а внутренние одинарные
print(f"у {emlore['name']} зарплата в год- {emlore.get('salary')*12}")
emlore_list=[{
'name':'Pavel',
'salary':100_000
},{
'name':'Olga',
'salary':115_000
},{
'name':'Maria',
'salary':98_000
}
]

print(emlore_list[-1])
for i in emlore_list:
    print(i)

a='hello'
b=123#по этому типу данных нельзя пройтись
c=True#по этому типу данных нельзя пройтись
for emlore in emlore_list:
    print(f"у {emlore['name']} зарплата в месяц- {emlore.get('salary')}")
    print(f"у {emlore['name']} зарплата в год- {emlore.get('salary') * 12}")
    print('-'*50)

for emlore in emlore_list:
    if emlore['name']=='Olga':
        emlore_list.remove(emlore)
        print('уволить Ольгу!')
        break

emlore_list.append(
    {"name":'Oleg',
     'salary':150_000}
)

print(len(emlore_list))
#Магические методы. итерируемый объект, это тот в чьём классе есть метот __iter__
class Emloyee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.on_vacation=False
    def  get_info(self):
        return (f'{self.name} имеет зарплату - {self.salary}. Статус отпуска : {self.on_vacation}')

emloyee1=Emloyee('Ivan',80_000)
emloyee1.get_info()

emloyee_list=[
    Emloyee('Ivan',80_000),
    Emloyee('Ivan2',81_000),
    Emloyee('Ivan2',82_000)
]
emloyee_list[0].on_vacation=True
for empl in emloyee_list:
    print(empl.get_info())