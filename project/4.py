import random


x = random.randint(2,255)

print('Напишите маску сети, в которой может быть до ',x,' компьютеров:')

otvet = input()

#   3 штучки 3 точки и еще одна правильная штучка которая 254-x

k = otvet.count('.')
if k != 3:
	print('Неверно(1')
else:
	massiv = otvet.split('.')
	if massiv[0] != '255' or massiv[1] != '255' or massiv[2] != '255':
		print('Неверно(2')
	else: 
		if int(massiv[3]) != (254-x):
			print('Неверно(3')
		else:
			print('Верно!!') 