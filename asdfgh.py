from tkinter import *
window=Tk()
window.title('Неоригинальное предложение')
window.geometry('500x500+230+200')
count=0
def change():
    global count
    count +=1
    lab['text']=count


lab=Label(window, text='тут должен быть гениальный текс...',font='16',bg='gold',fg='red')
lab.place(x=165,y=100)
lab['text']='Поменяли текст)))'
lab['bg']='white'

btn=Button(text='Knock',bg='#555',fg='#ccc',font='18',command=change)
btn.place(x=200,y=200)


window.mainloop()