import tkinter as tk


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
        entry_frame = tk.Frame(window)
        entry_frame.grid(row=i + 2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

        entry_label = tk.Label(entry_frame, text=f"Enter number {i + 1}:")
        entry_label.grid(row=0, column=0)

        entry_var = tk.DoubleVar()
        entry_vars.append(entry_var)
        entry_field = tk.Entry(entry_frame, textvariable=entry_var)
        entry_field.grid(row=0, column=1)

        entry_frames.append(entry_frame)


window = tk.Tk()
window.title("Number Analyzer")


entry_frames = []
entry_vars = []


num_entries = int(input('¿Cuántos números desea analizar? '))

# Etiqueta para mostrar resultados
result_label = tk.Label(window, text="")
result_label.grid(row=num_entries + 3, column=0, columnspan=2, pady=10)

# Botón para calcular
calculate_button = tk.Button(window, text="Calculate", command=calculate_this)
calculate_button.grid(row=num_entries + 4, column=0, columnspan=2, pady=10)


create_entry_fields(num_entries)


window.mainloop()
