from random import randint
from tkinter import *


def press(x):
    if x == answer:
        clr = 'green'
    else:
        clr = 'red'
    lab.config(bg=clr)


def new_equ():
    global equ, answer, lab
    x = randint(-10, 10)
    y = randint(-10, 10)
    equ.set(f'{x} > {y}')
    answer = x > y
    lab.config(bg='light gray')


root = Tk()
root.title('Button')
f = 'Arial 24'
equ = StringVar()
answer = False
lab = Label(textvariable=equ, font=f, width=10)
lab.pack()
new_equ()
Button(text='Верно', font=f, command=lambda: press(True)).pack()
Button(text='Неверно', font=f, command=lambda: press(False)).pack()
Button(text='Новое неравенство', font=f, command=new_equ).pack()


root.mainloop()
