import random

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

vopr ="Какие адреса используются для обращения к своему компьютеру?"
print(vopr)
print('1) ',adr1)
print('2) ',adr2)
print('3) ',adr3)
print('4) ',adr4)
print()
print('Введите ответ: ')
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

k5 = ''

if k1 == 1:
    k5 += '1'
if k2 == 1:
    k5 += '2'
if k3 == 1:
    k5 += '3'
if k4 == 1:
    k5 += '4'


otvet=input()

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
    print('Все верно!')
else:
    print('Не верно(')
    print('Ваш ответ: ',h1)
    print('Правильный ответ: ',k5)




#127.0.0.0 — 127.255.255.255
