from tkinter import *
import random
window= Tk()
window.title("Адресация в локальных сетях")
window.geometry('800x500')
main=Frame(window)
main.grid()
def nastr():
    global main, window,z4,z3,z2,z1
    main.destroy()
    main=Frame(window)
    main.pack()
    lbl = Label(main, text="Напишите количество заданий №1") 
    lbl.grid(column=0, row=0)
    z1 = Entry(main,width=30)  
    z1.grid(column=1, row=0)
    lbl = Label(main, text="Напишите количество заданий №2") 
    lbl.grid(column=0, row=1)
    z2 = Entry(main,width=30)  
    z2.grid(column=1, row=1)
    lbl = Label(main, text="Напишите количество заданий №3") 
    lbl.grid(column=0, row=2)
    z3 = Entry(main,width=30)  
    z3.grid(column=1, row=2)
    lbl = Label(main, text="Напишите количество заданий №4") 
    lbl.grid(column=0, row=3)
    z4 = Entry(main,width=30)  
    z4.grid(column=1, row=3)
    btn = Button(main, text="Перейти к тестовому режиму", command=test)  
    btn.grid(column=0, row=5)
    btn = Button(main, text="Сохранить", command=pol)  
    btn.grid(column=0, row=4)
def pol():
    global a,b,c,z2,z3,z4,z1,d
    if len(z4.get()) == 0:
        a=0
    else:
        a=z4.get()
        a=int(a)
    if len(z3.get()) == 0:
        b=0
    else:
        b=z3.get()
        b=int(b)
    if len(z2.get()) == 0:
        c=0
    else:
        c=z2.get()
        c=int(c)
    if len(z1.get()) == 0:
        d=0
    else:
        d=z1.get()
        d=int(d)
def test():
    global main, window,b,a,c,d
    main.destroy()
    main=Frame(window)
    main.pack()
    if d>0:
        j = random.randint(1,3)
        k1 = 0
        k2 = 0
        k3 = 0
        k4 = 0
        def clic():
            global otvet,d,j
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
                lbl = Label(main, text=" Верно!!! ")  
                lbl.grid(column=3, row=4)
            else:
                lbl = Label(main, text="Неверно(")  
                lbl.grid(column=3, row=4)
                lbl = Label(main, text="Ваш ответ: ")  
                lbl.grid(column=3, row=5)
                lbl = Label(main, text=h1)  
                lbl.grid(column=4, row=5)
                lbl = Label(main, text="Правильный ответ: ")  
                lbl.grid(column=3, row=6)
                lbl = Label(main, text=k5)  
                lbl.grid(column=4, row=6)
            if d>0:
                btn = Button(main, text="Следующее задание", command=test)
                btn.grid(column=1, row=2)
                d-=1
   

        
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

            lbl = Label(main,text="Задание 1")
            lbl.grid(column=0,row=0)
            lbl = Label(main,text="Какие адреса используются для обращения к своему компьютеру?")
            lbl.grid(column=0,row=1)
            lbl = Label(main,text=adr1)
            lbl.grid(column=0,row=2)
            lbl = Label(main,text=adr2)
            lbl.grid(column=0,row=3)
            lbl = Label(main,text=adr3)
            lbl.grid(column=0,row=4)
            lbl = Label(main,text=adr4)
            lbl.grid(column=0,row=5)
            lbl = Label(main,text="Введите ответ: ")
            lbl.grid(column=0,row=6)
            txt = Entry(main,width=30)  
            txt.grid(column=0, row=7)
            btn = Button(main, text="Ввести", command=clic)  
            btn.grid(column=1, row=7)

            k1=0
            k2=0
            k3=0
            k4=0

            xx=adr1.partition('.')#разбиваем строку до первой точки
            if int(xx[0])==127:
                k1=1
            xx=adr2.partition('.')#разбиваем строку до первой точки
            if int(xx[0])==127:
                k2=1
            xx=adr3.partition('.')#разбиваем строку до первой точки
            if int(xx[0])==127:
                k3=1
            xx=adr4.partition('.')#разбиваем строку до первой точки
            if int(xx[0])==127:
                k4=1

        if j == 2:
            lbl = Label(main,text="Задание 1")
            lbl.grid(column=0,row=0)
            lbl = Label(main,text="Какие адреса используются только в локальных сетях?")
            lbl.grid(column=0,row=1)
            lbl = Label(main,text="1) 192.168.0.0 — 192.168.255.255")
            lbl.grid(column=0,row=2)
            lbl = Label(main,text="2) 172.16.0.0 — 172.31.255.255")
            lbl.grid(column=0,row=3)
            lbl = Label(main,text="3) 10.0.0.0 — 10.255.255.255")
            lbl.grid(column=0,row=4)
            lbl = Label(main,text="4) 193.0.0.0 — 193.255.255.255")
            lbl.grid(column=0,row=5)
            lbl = Label(main,text="Введите ответ: ")
            lbl.grid(column=0,row=6)
            txt = Entry(main,width=30)  
            txt.grid(column=0, row=7)
            btn = Button(main, text="Ввести", command=clic)  
            btn.grid(column=1, row=7)
            k1=1
            k2=0
            k3=0
            k4=0

        if j == 3:
            lbl = Label(main,text="Задание 1")
            lbl.grid(column=0,row=0)
            lbl = Label(main,text="Укажите номера всех значений, которые могут быть масками подсетей.")
            lbl.grid(column=0,row=1)
            lbl = Label(main,text="1) 255.255.255.224")
            lbl.grid(column=0,row=2)
            lbl = Label(main,text="2) 255.255.0.255")
            lbl.grid(column=0,row=3)
            lbl = Label(main,text="3) 255.255.0.0")
            lbl.grid(column=0,row=4)
            lbl = Label(main,text="4) 255.255.255.192")
            lbl.grid(column=0,row=5)
            lbl = Label(main,text="Введите ответ: ")
            lbl.grid(column=0,row=6)
            txt = Entry(main,width=30)  
            txt.grid(column=0, row=7)
            btn = Button(main, text="Ввести", command=clic)  
            btn.grid(column=1, row=7)

            k1=1
            k2=0
            k3=1
            k4=1
            
            
    if c>0 and d==0:
        s3 = '255.255.'
        rand = random.randint(0,256)
        s3 += str(rand)
        s3 += '.'
        rand = random.randint(0,1)
        if rand == 0:
            rand = 240
        else:
            rand = 0
        s3 += str(rand)
        def click():
            global otvet,c
            otvet=format(txt.get())
            mas = s3.split('.')
            mas1 = []
            m = 0
            k=0
            mask=""

            for i in range(len(mas)):
                mas1.append('')
                m = int(mas[i])
                while m > 0:
                    m, a = divmod(m, 2) #в одно число в инт
                    mas1[i] = str(a) + mas1[i]#dl9 ip adresa
                if i>1:
                    mask+=mas1[i]
            if mas[i]=='0':
                mask+='00000000'


            i=len(mask)-1
            while mask[i]!='1':
                k+=1
                i -= 1


            mas = s4.split('.')
            mas1 = []
            m = 0
            ip=""

            for i in range(len(mas)):
                mas1.append('')
                m = int(mas[i])
                while m > 0:
                    m, a = divmod(m, 2) #в одно число в инт
                    mas1[i] = str(a) + mas1[i]#dl9 ip adresa
                    if i>1:
                        ip+=mas1[i]
            while len(ip)!=k:
                ip=ip[1:len(ip)] 
            proverka=int(ip, base = 2)
            proverka=str(proverka)

            if otvet == proverka:
                lbl = Label(main, text=" Верно!!! ")  
                lbl.grid(column=0, row=6)       
            else:
                lbl = Label(main, text="Неверно(")
                lbl.grid(column=0, row=6)
                lbl = Label(main, text=proverka)
                lbl.grid(column=0, row=7)
            if c>0:
                btn = Button(main, text="Следующее задание", command=test)
                btn.grid(column=1, row=2)
                c-=1

        s4=""
        rand = random.randint(0,256)
        s4 += str(rand)
        s4 += '.'
        rand = random.randint(0,256)
        s4 += str(rand)
        s4 += '.'
        rand = random.randint(0,256)
        s4 += str(rand)
        s4 += '.'
        rand = random.randint(0,256)
        if rand % 2 == 0:
            rand -= 1 
        s4 += str(rand)
        lbl = Label(main, text="Задание 2.") 
        lbl.grid(column=0, row=0)
        lbl = Label(main, text="Определите количество компьютеров по маске сети и IP адресу")  
        lbl.grid(column=0, row=1)
        lbl = Label(main, text="Маска сети:")  
        lbl.grid(column=0, row=2)
        lbl = Label(main, text=s3)  
        lbl.grid(column=1, row=2)
        lbl = Label(main, text="IP адрес компьютера:")  
        lbl.grid(column=0, row=3)
        lbl = Label(main, text=s4)  
        lbl.grid(column=1, row=3)
        lbl = Label(main, text="Введите ответ:")  
        lbl.grid(column=0, row=4)
        txt = Entry(main,width=30)  
        txt.grid(column=0, row=5)
        btn = Button(main, text="Ввести", command=click)  
        btn.grid(column=1, row=5)

        mas = s3.split('.')
        mas1 = []
        m = 0
        k=0
        mask=""

        for i in range(len(mas)):
            mas1.append('')
            m = int(mas[i])
            while m > 0:
                m, a = divmod(m, 2) #в одно число в инт
                mas1[i] = str(a) + mas1[i]#dl9 ip adresa
            if i>1:
                mask+=mas1[i]
        if mas[i]=='0':
            mask+='00000000'


        i=len(mask)-1
        while mask[i]!='1':
            k+=1
            i -= 1


        mas = s4.split('.')
        mas1 = []
        m = 0
        ip=""

        for i in range(len(mas)):
            mas1.append('')
            m = int(mas[i])
            while m > 0:
                m, a = divmod(m, 2) #в одно число в инт
                mas1[i] = str(a) + mas1[i]#dl9 ip adresa
                if i>1:
                    ip+=mas1[i]
        while len(ip)!=k:
            ip=ip[1:len(ip)] 
        proverka=int(ip, base = 2)
        proverka=str(proverka)
        




    if b>0 and c==0 and d==0:
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
        c1 = str(random.randint(0,1))
        def clk():
            global otvet,b
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
                    mas1[i] = mas1[i].count(c1)
                proverka += mas1[i]
            proverka = str(proverka)
            if proverka == otvet:
                lbl = Label(main, text=" Верно!  ")
                lbl.grid(column=0, row=4)
            else:
                lbl = Label(main, text="Неверно(")  
                lbl.grid(column=0, row=4)
                lbl = Label(main, text=proverka)
                lbl.grid(column=0, row=5)
            if b>0:
                    btn = Button(main, text="Следующее задание", command=test)
                    btn.grid(column=1, row=2)
                    b-=1
        lbl = Label(main, text="Задание 3.") 
        lbl.grid(column=0, row=0)
        lbl = Label(main, text="Подсчитайте количество") 
        lbl.grid(column=0, row=1) 
        lbl = Label(main, text=c)  
        lbl.grid(column=1, row=1) 
        lbl = Label(main, text="в двоичной записи маски подсети:")  
        lbl.grid(column=2, row=1)
        lbl = Label(main, text=s)  
        lbl.grid(column=3, row=1) 
        txt = Entry(main,width=30)  
        txt.grid(column=0, row=2) 
        btn = Button(main, text="Ввести", command=clk)  
        btn.grid(column=1, row=2)
    if a>0 and b==0 and c==0 and d==0:        
        x = random.randint(2,255)

        s = ''
        s = str(x)

        otvet = ''
        def clicked():
            global otvet,a
            otvet = format(txt.get())
            k = otvet.count('.')
            if k != 3:
                lbl = Label(main, text="Неверно(")  
                lbl.grid(column=0, row=4)
            else:
                massiv = otvet.split('.')
                if massiv[0] != '255' or massiv[1] != '255' or massiv[2] != '255':
                    lbl = Label(main, text="Неверно(")  
                    lbl.grid(column=0, row=4)
                else: 
                    if int(massiv[3]) != (254-x):
                        lbl = Label(main, text="Неверно(")  
                        lbl.grid(column=0, row=4)
                    else:
                        lbl = Label(main, text=" Верно!!! ")  
                        lbl.grid(column=0, row=4)
            if a>0:
                btn = Button(main, text="Следующее задание", command=test)
                btn.grid(column=1, row=2)
                a-=1
        lbl = Label(main, text="Задание 4.") 
        lbl.grid(column=0, row=0)
        lbl = Label(main, text="Напишите маску сети, в которой может быть до") 
        lbl.grid(column=0, row=1) 
        lbl = Label(main, text=s)  
        lbl.grid(column=1, row=1) 
        lbl = Label(main, text="компьютеров: ")  
        lbl.grid(column=2, row=1)
        txt = Entry(main,width=30)  
        txt.grid(column=0, row=2) 
        btn = Button(main, text="Ввести", command=clicked)  
        btn.grid(column=1, row=2)
       

lbl= Label(main,text="Главное меню")
lbl.grid(column=0,row=0)
btn = Button(main, text="Тестовый режим", command=nastr)  
btn.grid(column=0, row=1)

#btn = Button(window, text="Контрольный режим", command=clicked)  
#btn.grid(column=1, row=1)

window.mainloop()
