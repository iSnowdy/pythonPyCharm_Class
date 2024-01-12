from tkinter import *


def calculate_this():
    numbers = []
    for entry_var in entry_vars:
        value = entry_var.get()
        if value:
            number = float(value)
            numbers.append(number)

    if numbers:
        addition = sum(numbers)
        average = addition / len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)

        result_text = (
            f"Sum: {round(addition, 2)}\n"
            f"Average: {round(average, 2)}\n"
            f"Min: {minimum}\n"
            f"Max: {maximum}"
        )
        result_label.config(text=result_text)


def create_entry_fields(num_entries):

    for i in range(num_entries):
        entry_frame = Frame(window) # Creamos el Frame
        # Frame encapsula un label y un entry juntos asociados al input
        entry_frame.pack()

        entry_label = Label(entry_frame, text=f"Enter number {i + 1}:")
        entry_label.pack()

        entry_var = DoubleVar()
        entry_vars.append(entry_var)
        entry_field = Entry(entry_frame, textvariable=entry_var)
        entry_field.pack()

        entry_frames.append(entry_frame)


window = Tk()
window.title("Number Stats")

entry_frames = []
entry_vars = []

# Preguntar al usuario cuántos números desea analizar
num_entries = int(input('¿Cuántos números desea analizar? '))

result_label = Label(window, text="")
result_label.pack()

calculate_button = Button(window, text="Calculate", command=calculate_this)
calculate_button.pack()

# Crear campos de entrada llamando a la función que depende del input
create_entry_fields(num_entries)

window.mainloop()
