from tkinter import *
from tkinter import messagebox

tk = Tk()

listbox=Listbox(tk)
listbox.pack()

def agregarNota():
    try:
        nota=float(entry.get())
        listbox.insert(listbox.size()-1,nota)
        entry.delete(0,END)
    except:
        messagebox.showerror(message="Debe ingresar una nota válida", title="Error_notas")

def calcularPromedio():
    if listbox.size() <= 1:
        messagebox.showinfo(message="Tienes que tener más de una nota para poder sacar el promedio", title="Error_notas")
    else:
        suma = 0

        elementos=listbox.get(0,listbox.size())
        length=len(elementos)

        promedio=sum(elementos)/length if length>0 else 0
        mensaje="El promedio es: {}".format(round(promedio,3))

        # for elemento in elementos:
        #     suma = suma + elemento
        print(mensaje)
        messagebox.showinfo(message=mensaje, title="Promedio")

entry=Entry(tk)
entry.pack()
button_agregar=Button(tk, text="Nueva nota", fg="white", bg="black", command=agregarNota)
button_agregar.pack()

button=Button(tk, text="Calcular", fg="white", bg="black", command=calcularPromedio)
button.pack()

tk.mainloop()