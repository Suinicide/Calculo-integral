import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sympy import sympify, lambdify, Symbol

# Crea la ventana raíz de Tkinter
root = tk.Tk()
root.title("Calculadora de sólidos en revolución")

# Crea un marco para contener los widgets
frame = tk.Frame(root)
frame.pack()

# Crea los widgets para ingresar la función a girar, los límites de integración y el eje de revolución
function_label = tk.Label(frame, text="Ingrese la función a girar:")
function_label.pack()
function_entry = tk.Entry(frame, width=50)
function_entry.pack()

integration_limits_label = tk.Label(frame, text="Ingrese los límites de integración (ejemplo: 0,2):")
integration_limits_label.pack()
integration_limits_entry = tk.Entry(frame, width=50)
integration_limits_entry.pack()

revolution_axis_label = tk.Label(frame, text="Ingrese el eje de revolución (x o y):")
revolution_axis_label.pack()
revolution_axis_entry = tk.Entry(frame, width=50)
revolution_axis_entry.pack()

def calculate_and_show_graficas():
    try:
        function = function_entry.get()
        integration_limits = list(map(float, integration_limits_entry.get().split(',')))
        revolution_axis = revolution_axis_entry.get().strip().lower()

        if revolution_axis not in ['x', 'y']:
            raise ValueError("El eje de revolución debe ser 'x' o 'y'.")

        x = Symbol('x')
        func = sympify(function)
        f = lambdify(x, func, modules='numpy')

        t = np.linspace(0, 2 * np.pi, 100)
        x_vals = np.linspace(integration_limits[0], integration_limits[1], 100)
        X, T = np.meshgrid(x_vals, t)

        if revolution_axis == 'x':
            Y = f(X)
            Z = X
            X = Y * np.cos(T)
            Y = Y * np.sin(T)
        elif revolution_axis == 'y':
            Y = X
            Z = f(X)
            X = Z * np.cos(T)
            Z = Z * np.sin(T)

        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap=cm.viridis, edgecolor='k')
        ax.set_title(f"Sólido de revolución alrededor del eje {revolution_axis}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()

        messagebox.showinfo("Resultado", "Cálculo realizado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {str(e)}")

calculate_button = tk.Button(frame, text="Calcular y mostrar gráficas", command=calculate_and_show_graficas)
calculate_button.pack()

root.mainloop()

