import random
from tkinter import *
window = Tk()
window.title("Задание 2")
window.geometry('800x500')
s=""
rand = random.randint(0,256)
s += str(rand)
s += '.'
rand = random.randint(0,256)
s += str(rand)
s += '.'
rand = random.randint(0,256)
s += str(rand)
s += '.'
rand = random.randint(0,256)
s += str(rand)
c = str(random.randint(0,1))
def clk():
    global otvet
    l=''
    otvet = format(txt.get())
    mas = s.split('.')
    mas1 = []
    proverka = 0
    m = 0
    for i in range(len(mas)):
        mas1.append('')
        m = int(mas[i])
        while m > 0:
            m, a = divmod(m, 2)
            l = str(a)
            mas1[i] = l + str(mas1[i])
            mas1[i] = mas1[i].count(c)
        proverka += mas1[i]
    proverka = str(proverka)
    if proverka == otvet:
        lbl = Label(window, text=" Верно!  ")
        lbl.grid(column=0, row=4)
    else:
        lbl = Label(window, text="Неверно(")  
        lbl.grid(column=0, row=4)
        lbl = Label(window, text=proverka)
        lbl.grid(column=0, row=5)
        
lbl = Label(window, text="Подсчитайте количество") 
lbl.grid(column=0, row=0) 
lbl = Label(window, text=c)  
lbl.grid(column=1, row=0) 
lbl = Label(window, text="в двоичной записи маски подсети:")  
lbl.grid(column=2, row=0)
lbl = Label(window, text=s)  
lbl.grid(column=3, row=0) 
txt = Entry(window,width=30)  
txt.grid(column=0, row=1) 
btn = Button(window, text="Ввести", command=clk)  
btn.grid(column=1, row=1)

window.mainloop()
