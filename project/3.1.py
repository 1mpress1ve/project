import random

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

print('Маска сети: ',s)
print('IP адрес компьютера: ',s1)

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

print('//',proverka)


print('Введите ответ: ')
otvet = int(input())
if otvet == proverka:
	print('Верно!')
else:
	print('Неверно(')









	# с конца mod 10
	#if mod 10=0 inc(k)
	#div 10
	#while mod 10<>1
	#объединяем ip адрес
	# с конца 4 цифры
	#перевод в 10
