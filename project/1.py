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
print('k1= ',k1)
print('k2= ',k2)
print('k3= ',k3)
print('k4= ',k4)

otvet=str(input())

h=str()
for c in otvet:
    # isdigit проверяет символ, является ли он цифрой
    if c.isdigit():
        h += c
otvet = h #теперь в строке только варианты ответа без лишних символов
print(otvet)
proverka=0
for i in range(len(otvet)):
    if (otvet[i]==1 and k1==1):
        proverka=1
    else:
        false=1
    if (otvet[i]==2 and k2==1):
        proverka=1
    else:
        false=1
    if (otvet[i]==3 and k3==1):
        proverka=1
    else:
        false=1
    if (otvet[i]==4 and k4==1):
        proverka=1
    else:
        false=1
    print(i)
print(false)
print(proverka)
#127.0.0.0 — 127.255.255.255
