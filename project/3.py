import random
from tkinter import *
window = Tk()
window.title("Задание 3")
window.geometry('800x500')

s = '255.255.'
rand = random.randint(0,256)
s += str(rand)
s += '.'
rand = random.randint(0,1)
if rand == 0:
    rand = 240
else:
    rand = 0
s += str(rand)
def click():
    global otvet
    otvet=format(txt.get())
    mas = s.split('.')
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


    mas = s1.split('.')
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
        lbl = Label(window, text=" Верно!!! ")  
        lbl.grid(column=0, row=6)       
    else:
        lbl = Label(window, text="Неверно(")
        lbl.grid(column=0, row=6)
        lbl = Label(window, text=proverka)
        lbl.grid(column=0, row=7)

s1=""
rand = random.randint(0,256)
s1 += str(rand)
s1 += '.'
rand = random.randint(0,256)
s1 += str(rand)
s1 += '.'
rand = random.randint(0,256)
s1 += str(rand)
s1 += '.'
rand = random.randint(0,256)
if rand % 2 == 0:
    rand -= 1 
s1 += str(rand)
lbl = Label(window, text="Определите количество компьютеров по маске сети и IP адресу")  
lbl.grid(column=0, row=0)
lbl = Label(window, text="Маска сети:")  
lbl.grid(column=0, row=1)
lbl = Label(window, text=s)  
lbl.grid(column=1, row=1)
lbl = Label(window, text="IP адрес компьютера:")  
lbl.grid(column=0, row=2)
lbl = Label(window, text=s1)  
lbl.grid(column=1, row=2)
lbl = Label(window, text="Введите ответ:")  
lbl.grid(column=0, row=3)
txt = Entry(window,width=30)  
txt.grid(column=0, row=4)
btn = Button(window, text="Ввести", command=click)  
btn.grid(column=1, row=4)

mas = s.split('.')
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


mas = s1.split('.')
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






window.mainloop()





	# с конца mod 10
	#if mod 10=0 inc(k)
	#div 10
	#while mod 10<>1
	#объединяем ip адрес
	# с конца 4 цифры
	#перевод в 10
