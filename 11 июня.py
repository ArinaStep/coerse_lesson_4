# Магический метод __add__
class Item:
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight
    def __add__(self, other):
        if isinstance(other,Item): #эта функция проверяет принадлежность объекта к классу
            return self.price + other.price
        elif isinstance(other,int):
            return self.price+other
    def __sub__(self, other):
        new_price = self.price - other.price
        new_weight = self.weight - other.weight
        return Item(new_price, new_weight)

    def __mul__(self, other):
        new_price = self.price * other
        new_weight = self.weight * other
        return Item(new_price, new_weight)

    def __truediv__(self, other):
        new_price = self.price / other
        new_weight = self.weight / other
        return Item(new_price, new_weight)
item1=Item('Видеокарта',15_000,0.8)
item2=Item('Процессор',12_000,0.3)
total_price=item1+1000
print(total_price)
from random import randint
from tkinter import *
window=Tk()
window.geometry('600x600')
class Fire:
    image=PhotoImage(file='fire.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other,Earth):
            return Clay
class Water:
    image=PhotoImage(file='water.png').subsample(4,4)#уменьшает картинку
    def __add__(self, other):
        if isinstance(other,Wind):
            return Aroma
class Wind:
    image=PhotoImage(file='wind.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other,Water):
            return Aroma
    def __add1__(self, other):
        if isinstance(other,Earth):
            return Dust
class Earth:
    image=PhotoImage(file='ground.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other,Fire):
            return Clay
    def __add2__(self, other):
        if isinstance(other,Wind):
            return Dust
class Clay:
    image=PhotoImage(file='pottery.png')
class Aroma:
    image=PhotoImage(file='aroma.png')
class Dust:
    image=PhotoImage(file='dust.png')

canvas=Canvas(window,width=600,height=600)
canvas.pack()
elements=[Earth(),Fire(),Water(),Wind()]
for elem in elements:
    canvas.create_image(randint(50,550),randint(50,550),image=elem.image)

def move(event):
    image_id=canvas.find_overlapping(event.x,event.y,event.x+10,event.y+10)
    # print(event.x,event.y)
    if len(image_id)==2:
        elem_id_1,elem_id_2=image_id[0],image_id[1]
        element_1=elements[elem_id_1-1]
        element_2=elements[elem_id_2-1]
        new_element=element_1+element_2
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x,event.y,image=new_element.image)
                elements.append(new_element)
                
    canvas.coords(image_id, event.x, event.y)

window.bind('<B1-Motion>', move)

window.mainloop()
