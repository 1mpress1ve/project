from tkinter import *
import random
window= Tk()
window.title("Адресация в локальных сетях")
window.geometry('800x500')
main=Frame(window)
main.grid()
def nastr():
    global main, window,z4
    main.destroy()
    main=Frame(window)
    main.pack()
    lbl = Label(main, text="Напишите количество заданий №4") 
    lbl.grid(column=0, row=0)
    z4 = Entry(main,width=30)  
    z4.grid(column=0, row=1)
    btn = Button(main, text="Перейти к тестовому режиму", command=test)  
    btn.grid(column=0, row=3)
    btn = Button(main, text="Сохранить", command=pol)  
    btn.grid(column=0, row=2)
def pol():
    global a,z4
    a=z4.get()
    a=int(a)
def test():
    global main, window
    main.destroy()
    main=Frame(window)
    main.pack()
        
    x = random.randint(2,255)

    s = ''
    s = str(x)

    otvet = ''
    def clicked():
        global otvet,a
        res = format(txt.get())
        otvet = res
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
    lbl = Label(main, text="Напишите маску сети, в которой может быть до") 
    lbl.grid(column=0, row=0) 
    lbl = Label(main, text=s)  
    lbl.grid(column=1, row=0) 
    lbl = Label(main, text="компьютеров: ")  
    lbl.grid(column=2, row=0)
    txt = Entry(main,width=30)  
    txt.grid(column=0, row=1) 
    btn = Button(main, text="Ввести", command=clicked)  
    btn.grid(column=1, row=1)
       

















    
lbl= Label(main,text="Главное меню")
lbl.grid(column=0,row=0)
btn = Button(main, text="Тестовый режим", command=nastr)  
btn.grid(column=0, row=1)

#btn = Button(window, text="Контрольный режим", command=clicked)  
#btn.grid(column=1, row=1)

window.mainloop()
