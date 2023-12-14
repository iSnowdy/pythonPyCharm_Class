from tkinter import *
a = ''


window = Tk()

temp = DoubleVar()


def toCelsius():

    temperature = temp.get()
    temperature = (temperature - 32) * 5/9

    a = str(temp.get()) + ' ' + 'F = ' + str(round(temperature, 1)) + ' ' + 'C'

    label.config(text=a)


entry = Entry(window, textvariable=temp)
button = Button(window, text='F -> Cº', command=toCelsius)
label = Label(window, text=a)

entry.pack()
button.pack()
label.pack()

window.mainloop()
