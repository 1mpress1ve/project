import random
from tkinter import *

window = Tk()
window.title("Задание 4")
window.geometry('800x500')

x = random.randint(2,255)

s = ''
s = str(x)

otvet = ''
def clicked():
	global otvet
	res = format(txt.get())
	otvet = res
	k = otvet.count('.')
	if k != 3:
		lbl = Label(window, text="Неверно(")  
		lbl.grid(column=0, row=4)
	
	else:
		massiv = otvet.split('.')
		if massiv[0] != '255' or massiv[1] != '255' or massiv[2] != '255':
			lbl = Label(window, text="Неверно(")  
			lbl.grid(column=0, row=4)
		
		else: 
			if int(massiv[3]) != (254-x):
				lbl = Label(window, text="Неверно(")  
				lbl.grid(column=0, row=4)
			
			else:
				lbl = Label(window, text=" Верно!!! ")  
				lbl.grid(column=0, row=4)

lbl = Label(window, text="Напишите маску сети, в которой может быть до") 
lbl.grid(column=0, row=0) 
lbl = Label(window, text=s)  
lbl.grid(column=1, row=0) 
lbl = Label(window, text="компьютеров: ")  
lbl.grid(column=2, row=0)
txt = Entry(window,width=30)  
txt.grid(column=0, row=1) 
btn = Button(window, text="Ввести", command=clicked)  
btn.grid(column=1, row=1)

window.mainloop()
