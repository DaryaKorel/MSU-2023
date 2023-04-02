from tkinter import *
from tkinter import messagebox
from math import *
 
def my_action():
    frm = int(e1.get())
    to   = int(e2.get())
    col = str(e3.get())
    for i in range(frm, to):
        canvas.create_line(i, 20*sin(i)+250, i + 1, 20*sin(i)+250, fill=col, width=20)

master = Tk()
master.title('Рисуем синусоиду')
master.geometry('800x400')

l1 = Label(master, text='t0')
l1.grid(row=2, column=0, sticky='e')
l2 = Label(master, text='t1')
l2.grid(row=3, column=0, sticky='e')
l3 = Label(master, text = 'Выберите цвет синусоиды')
l3.grid(row=1, column=1, sticky='e')

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=1, column=2)

b1 = Button(master, text="Draw!", command = my_action)
b1.grid(row=4, column = 1)

canvas = Canvas(master, width=500, height=300, background='black')
canvas.grid(column=0, row=1)

master.mainloop()