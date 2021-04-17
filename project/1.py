import random

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

print('Подсчитайте количество ',c,' в двоичной записи маски подсети: ',s)

mas = s.split('.')
mas1 = []

proverka = 0
m = 0

for i in range(len(mas)):
	mas1.append('')
	m = int(mas[i])
	while m > 0:
		m, a = divmod(m, 2)
		mas1[i] = str(a) + mas1[i]
	mas1[i] = mas1[i].count(c)
	proverka += mas1[i]

print('//',proverka)
print('Введите ответ: ')
otvet = int(input())

if proverka == otvet:
	print('Верно!')
else:
	print('Неверно(')