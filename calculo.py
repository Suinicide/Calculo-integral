import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sympy import sympify, lambdify, Symbol, pi

BACKGROUND_COLOR = "#fdf6e3"
ACCENT_COLOR = "#2aa198"
TEXT_COLOR = "#657b83"

root = tk.Tk()
root.title("Sólidos en Revolución")
root.geometry("600x450")
root.config(bg=BACKGROUND_COLOR)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TLabel",
    font=("Helvetica", 12),
    background=BACKGROUND_COLOR,
    foreground=TEXT_COLOR,
)
style.configure(
    "TEntry",
    font=("Helvetica", 12),
    padding=5,
)
style.configure(
    "TButton",
    font=("Helvetica", 12, "bold"),
    background=ACCENT_COLOR,
    foreground="white",
    borderwidth=0,
    padding=10,
)
style.map("TButton", background=[("active", "#268bd2")])

title_label = ttk.Label(
    root,
    text="💿Calculadora de solidos de revolución💿",
    font=("Helvetica", 16, "bold"),
    anchor="center",
)
title_label.pack(pady=(20, 10))

input_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
input_frame.pack(pady=10, padx=20, fill="x")

function_label = ttk.Label(input_frame, text="Función a girar:")
function_label.grid(row=0, column=0, sticky="w", pady=10)
function_entry = ttk.Entry(input_frame, width=40)
function_entry.grid(row=0, column=1, pady=10, padx=10)

integration_limits_label = ttk.Label(input_frame, text="Límites de integración, puede ser ingresado en radianes (ejemplo: 0, pi):")
integration_limits_label.grid(row=1, column=0, sticky="w", pady=10)
integration_limits_entry = ttk.Entry(input_frame, width=40)
integration_limits_entry.grid(row=1, column=1, pady=10, padx=10)

revolution_axis_label = ttk.Label(input_frame, text="Eje de revolución (x o y):")
revolution_axis_label.grid(row=2, column=0, sticky="w", pady=10)
revolution_axis_entry = ttk.Entry(input_frame, width=40)
revolution_axis_entry.grid(row=2, column=1, pady=10, padx=10)

def calculate_and_show_graficas():
    try:
        function = function_entry.get()
        limits = integration_limits_entry.get().split(',')
        revolution_axis = revolution_axis_entry.get().strip().lower()

        if revolution_axis not in ['x', 'y']:
            raise ValueError("El eje de revolución debe ser 'x' o 'y'.")

        lower_limit = float(sympify(limits[0].strip()))
        upper_limit = float(sympify(limits[1].strip()))

        x = Symbol('x')
        func = sympify(function)
        f = lambdify(x, func, modules='numpy')

        t = np.linspace(0, 2 * np.pi, 100)
        x_vals = np.linspace(lower_limit, upper_limit, 100)
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
        ax.plot_surface(X, Y, Z, cmap=cm.plasma, edgecolor='k')
        ax.set_title(f"Solido de revolución alrededor del eje {revolution_axis}", color=TEXT_COLOR)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()

        messagebox.showinfo("Resultado", "Cálculo exitoso :D")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {str(e)}")

calculate_button = ttk.Button(
    root,
    text="Calcular y Mostrar Gráficas 📈",
    command=calculate_and_show_graficas,
    style="TButton",
)
calculate_button.pack(pady=20)

root.mainloop()


