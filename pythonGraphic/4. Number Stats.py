import tkinter
from tkinter import *
show = ''

rows = int(input('¿Cuántos números quiere analizar? '))


window = Tk()

myList = []
myList_2 = []

numbers = DoubleVar()

def calculateThis():

    myList.append(numbers.get())

    addition = sum(myList)
    mean = addition / len(myList)
    minim = min(myList)
    maxim = max(myList)


    show = ('Addition: ', addition,
         'Mean: ', mean,
         'Min: ', minim,
         'max: ', maxim,
         )

    label.config(text=show)


for i in range(1, rows + 1):

    addition, mean, minim, maxim = (tkinter.DoubleVar() for _ in range(4))
    myList_2[i] = [addition, mean, minim, maxim]

    tkinter.Entry(window, textvariable=addition)
    tkinter.Entry(window, textvariable=mean)
    tkinter.Entry(window, textvariable=minim)
    tkinter.Entry(window, textvariable=maxim)

    tkinter.Button(window, text='Calculate', command=calculateThis)

    label = Label(window, text=show)


window.mainloop()
