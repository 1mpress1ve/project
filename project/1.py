import random
from tkinter import *
window=Tk()
window.title("Задание 1")
window.geometry('800x500')
j = random.randint(1,3)

k1 = 0
k2 = 0
k3 = 0
k4 = 0

def click():
    global otvet
    res= format(txt.get())
    otvet = res
    k5 = ''

    if k1 == 1:
        k5 += '1'
    if k2 == 1:
        k5 += '2'
    if k3 == 1:
        k5 += '3'
    if k4 == 1:
        k5 += '4'


    

    h=''

    for i in range(0, len(otvet)):
        if otvet[i].isdigit():
            h += otvet[i]

    h1 = ''


    k = h.count('1')
    if k >= 1:
        h1 +='1'

    k = h.count('2')
    if k >= 1:
        h1 +='2'

    k = h.count('3')
    if k >= 1:
        h1 +='3'

    k = h.count('4')
    if k >= 1:
        h1 +='4'

    proverka = 0

    for i in range(0, len(h1)):   
        if (h1[i]=='1' and k1==1):
            proverka +=1
        if (h1[i]=='2' and k2==1):
            proverka +=1
        if (h1[i]=='3' and k3==1):
            proverka +=1
        if (h1[i]=='4' and k4==1):
            proverka +=1
    
    k = 0
    k = k1+k2+k3+k4
    if proverka == k:
        lbl = Label(window, text=" Верно!!! ")  
        lbl.grid(column=3, row=4)
    else:
        lbl = Label(window, text="Неверно(")  
        lbl.grid(column=3, row=4)
        lbl = Label(window, text="Ваш ответ: ")  
        lbl.grid(column=3, row=5)
        lbl = Label(window, text=h1)  
        lbl.grid(column=4, row=5)
        lbl = Label(window, text="Правильный ответ: ")  
        lbl.grid(column=3, row=6)
        lbl = Label(window, text=k5)  
        lbl.grid(column=4, row=6)
   

        
if j == 1:
    adr1=""
    rand = random.randint(0,256)
    adr1 += str(rand)
    adr1 += '.'
    rand = random.randint(0,256)
    adr1 += str(rand)
    adr1 += '.'
    rand = random.randint(0,256)
    adr1 += str(rand)
    adr1 += '.'
    rand = random.randint(0,256)
    adr1 += str(rand)

    adr2=""
    adr2 += '127.'
    rand = random.randint(0,256)
    adr2 += str(rand)
    adr2 += '.'
    rand = random.randint(0,256)
    adr2 += str(rand)
    adr2 += '.'
    rand = random.randint(0,256)
    adr2 += str(rand)

    adr3=""
    rand = random.randint(0,256)
    adr3 += str(rand)
    adr3 += '.'
    rand = random.randint(0,256)
    adr3 += str(rand)
    adr3 += '.'
    rand = random.randint(0,256)
    adr3 += str(rand)
    adr3 += '.'
    rand = random.randint(0,256)
    adr3 += str(rand)

    adr4=""
    adr4+='127.'
    rand = random.randint(0,256)
    adr4 += str(rand)
    adr4 += '.'
    rand = random.randint(0,256)
    adr4 += str(rand)
    adr4 += '.'
    rand = random.randint(0,256)
    adr4 += str(rand)

    lbl = Label(window,text="Какие адреса используются для обращения к своему компьютеру?")
    lbl.grid(column=0,row=0)
    lbl = Label(window,text=adr1)
    lbl.grid(column=0,row=1)
    lbl = Label(window,text=adr2)
    lbl.grid(column=0,row=2)
    lbl = Label(window,text=adr3)
    lbl.grid(column=0,row=3)
    lbl = Label(window,text=adr4)
    lbl.grid(column=0,row=4)
    lbl = Label(window,text="Введите ответ: ")
    lbl.grid(column=0,row=5)
    txt = Entry(window,width=30)  
    txt.grid(column=0, row=6)
    btn = Button(window, text="Ввести", command=click)  
    btn.grid(column=1, row=6)

    k1=0
    k2=0
    k3=0
    k4=0

    b=adr1.partition('.')#разбиваем строку до первой точки
    if int(b[0])==127:
        k1=1
    b=adr2.partition('.')#разбиваем строку до первой точки
    if int(b[0])==127:
         k2=1
    b=adr3.partition('.')#разбиваем строку до первой точки
    if int(b[0])==127:
         k3=1
    b=adr4.partition('.')#разбиваем строку до первой точки
    if int(b[0])==127:
         k4=1                

if j == 2:
    lbl = Label(window,text="Какие адреса используются только в локальных сетях?")
    lbl.grid(column=0,row=0)
    lbl = Label(window,text="1) 192.168.0.0 — 192.168.255.255")
    lbl.grid(column=0,row=1)
    lbl = Label(window,text="2) 172.16.0.0 — 172.31.255.255")
    lbl.grid(column=0,row=2)
    lbl = Label(window,text="3) 10.0.0.0 — 10.255.255.255")
    lbl.grid(column=0,row=3)
    lbl = Label(window,text="4) 193.0.0.0 — 193.255.255.255")
    lbl.grid(column=0,row=4)
    lbl = Label(window,text="Введите ответ: ")
    lbl.grid(column=0,row=5)
    txt = Entry(window,width=30)  
    txt.grid(column=0, row=6)
    btn = Button(window, text="Ввести", command=click)  
    btn.grid(column=1, row=6)
        
    k1=1
    k2=0
    k3=0
    k4=0

if j == 3:
    lbl = Label(window,text="Укажите номера всех значений, которые могут быть масками подсетей.")
    lbl.grid(column=0,row=0)
    lbl = Label(window,text="1) 255.255.255.224")
    lbl.grid(column=0,row=1)
    lbl = Label(window,text="2) 255.255.0.255")
    lbl.grid(column=0,row=2)
    lbl = Label(window,text="3) 255.255.0.0")
    lbl.grid(column=0,row=3)
    lbl = Label(window,text="4) 255.255.255.192")
    lbl.grid(column=0,row=4)
    lbl = Label(window,text="Введите ответ: ")
    lbl.grid(column=0,row=5)
    txt = Entry(window,width=30)  
    txt.grid(column=0, row=6)
    btn = Button(window, text="Ввести", command=click)  
    btn.grid(column=1, row=6)

    k1=1
    k2=0
    k3=1
    k4=1
    


window.mainloop()
#127.0.0.0 — 127.255.255.255
