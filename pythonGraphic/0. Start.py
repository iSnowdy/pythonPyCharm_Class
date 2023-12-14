from tkinter import *  # importamos paquete para interfaces gráficas

'''

w = Tk()  # Inicializa la ventana a la que se le irán agregando cosas. Siempre irá al principio
w.mainloop()  # Mete en bucle el programa. De forma que sólo hará algo después de que el usuario lo indique. Va al final



Widgets. Es cualquier cosa que uno pueda poder dentro de una ventana gráfica

- etiquetas o label. Sirven para mostrar datos. Es como el print
- botones o button. Sirven para hacer algo en el programa. Llama a funciones
- campos de entrada o entry. Sirven para ingresar datos al programa. Es como el input

'''


def saludar():


# Creamos una función para asociarla al botón. Se llama controlador. Los controladores deben ser
# funciones que no pidan parámetros. Los widgets se inicializan verticalmente. Por lo que las funciones deben de
# estar al principio.

    print('Told you to don\'t click here')


w = Tk()

b1 = Button(w, text='Don\'t click here', command=saludar)  # Crea el botón asociado a w. Pero no lo hemos agregado aún
b2 = Button(w, text='Get me out of here', command=exit)
l = Label(w, text='Hey there')
e = Entry(w)

l.pack()
b1.pack()
b2.pack()
e.pack()  # Así inicializamos los widgets en el contenedor (w). El orden en que inicializamos importa.

w.mainloop()


'''

Las interfaces no tienen memoria por naturaleza. Tenemos que crear un modelo. Los modelos son datos almacenados
asociados a una interfaz. De esta forma, usando modelos lograremos que la interfaz vaya cambiando a medida que
se hagan acciones.

Por lo general se debe de crear un modelo para cada dato asociado a la interfaz. Hay muchos tipos de modelos.

Se usan modelos y no las variables que Python trae por defecto porque los modelos son capaces de reaccionar
cuando su valor cambia.

'''

m = StringVar()

m.set('hey')  # Así modificamos el valor del modelo m

s = m.get()  # Para llamar al modelo. Antes sólo lo hemos creado. Aquí s tomará el valor 'hey'.

a = StringVar()
b = StringVar()

a.set(5)
a.set(8)

print(a.get() + b.get())  # Imprimirá 58. Son strings
print(int(a.get() + b.get()))  # Imprimirá 13

