from tkinter import *

w = Tk()

string = StringVar()


def upperCase():

    string.set(string.get().upper())


def lowerCase():

    string.set(string.get().lower())


def clear():

    string.set('')


entry = Entry(w, textvariable=string)
button_1 = Button(w, text='Upper Case', command=upperCase)
button_2 = Button(w, text='Lower Case', command=lowerCase)
button_3 = Button(w, text='Clear', command=clear)

entry.pack()
button_1.pack()
button_2.pack()
button_3.pack()

w.mainloop()
