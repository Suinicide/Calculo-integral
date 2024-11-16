import tkinter as tk
from tkinter import messagebox

# Crea la ventana raíz de Tkinter
root = tk.Tk()
root.title("Calculadora de sólidos en re{{-volución")

# Crea un marco para contener los widgets
frame = tk.Frame(root)
frame.pack()

# Crea los widgets para ingresar la función a girar, los límites de integración y el eje de revolución
function_label = tk.Label(frame, text="Ingrese la función a girar:")
function_label.pack()
function_entry = tk.Entry(frame, width=50)
function_entry.pack()

integration_limits_label = tk.Label(frame, text="Ingrese los límites de integración:")
integration_limits_label.pack()
integration_limits_entry = tk.Entry(frame, width=50)
integration_limits_entry.pack()

revolution_axis_label = tk.Label(frame, text="Ingrese el eje de revolución (x o y):")
revolution_axis_label.pack()
revolution_axis_entry = tk.Entry(frame, width=50)
revolution_axis_entry.pack()

# Crea un botón para enviar los datos al módulo de cálculo y mostrar las gráficas
def calculate_and_show_graficas():
    # Obtiene los datos ingresados por el usuario
    function = function_entry.get()
    integration_limits = integration_limits_entry.get()
    revolution_axis = revolution_axis_entry.get()

    # Envía los datos al módulo de cálculo y muestra las gráficas
    # (Aquí va el código para realizar el cálculo y mostrar las gráficas)
    # Por ejemplo, puedes usar la biblioteca Matplotlib para mostrar gráficas
    import matplotlib.pyplot as plt # type: ignore
    # ...

    # Muestra un mensaje de confirmación si el cálculo fue exitoso
    messagebox.showinfo("Resultado", "Cálculo realizado con éxito")

calculate_button = tk.Button(frame, text="Calcular y mostrar gráficas", command=calculate_and_show_graficas)
calculate_button.pack()

# Corre la aplicación Tkinter
root.mainloop()

git remoto agregar origen https://github.com/Suinicide/Calculo-integral.git
 git rama -M principal 
git push -u origen principal
