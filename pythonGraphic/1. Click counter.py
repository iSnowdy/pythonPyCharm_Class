from tkinter import *
n = 0

w = Tk()

label = Label(w, text=n)


def increase():

    global n
    n += 1

    label.config(text=n)  # Podemos cambiar los widgets dentro de las funciones al darle a button


button_1 = Button(w, text='+1', command=increase)
button_2 = Button(w, text='Exit', command=exit)

label.pack()
button_1.pack()
button_2.pack()

w.mainloop()
