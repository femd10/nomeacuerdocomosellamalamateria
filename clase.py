import tkinter as tk
import math
import cmath

# ==============================
# FUNCIONES MATEMÁTICAS
# ==============================

def calcular_cuadratica():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())

        if a == 0:
            resultado.set("No es ecuación cuadrática")
            return

        d = b**2 - 4*a*c

        x1 = (-b + cmath.sqrt(d)) / (2*a)
        x2 = (-b - cmath.sqrt(d)) / (2*a)

        def formatear_complejo(z):
            real = round(z.real, 4)
            imag = round(z.imag, 4)

            if imag == 0:
                return f"{real}"
            if real == 0:
                return f"{imag}i"
            if imag > 0:
                return f"{real} + {imag}i"
            return f"{real} - {abs(imag)}i"

        resultado.set(
            f"x1 = {formatear_complejo(x1)}\n"
            f"x2 = {formatear_complejo(x2)}"
        )

    except:
        resultado.set("Error en los datos")



def calcular_fibonacci():
    try:
        n = int(entry1.get())

        if n < 0:
            resultado.set("Ingrese número positivo")
            return

        a, b = 0, 1
        cadena = []

        for _ in range(n):
            cadena.append(str(a))
            a, b = b, a + b

        resultado.set("Secuencia:\n" + " , ".join(cadena))

    except:
        resultado.set("Error en los datos")


def es_primo(n, divisor=3):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if divisor > math.sqrt(n):
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor + 2)  # solo impares


def verificar_primo():
    try:
        n = int(entry1.get())

        if es_primo(n):
            resultado.set(f"{n} es primo")
        else:
            resultado.set(f"{n} no es primo")

    except:
        resultado.set("Error en los datos")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def calcular_factorial():
    try:
        n = int(entry1.get())

        if n < 0:
            resultado.set("Ingrese número positivo")
            return

        resultado.set(f"{n}! = {factorial(n)}")

    except:
        resultado.set("Error en los datos")


# ==============================
# CONTROL DE MENÚ
# ==============================

def actualizar_vista(opcion):

    for widget in frame_inputs.winfo_children():
        if not isinstance(widget, tk.Entry):
            widget.destroy()

    entry1.grid_forget()
    entry2.grid_forget()
    entry3.grid_forget()

    resultado.set("")

    if opcion == "Cuadrática":

        tk.Label(frame_inputs, text="a:", bg=bg_color, fg="white").grid(row=0, column=0)
        entry1.grid(row=0, column=1)

        tk.Label(frame_inputs, text="b:", bg=bg_color, fg="white").grid(row=1, column=0)
        entry2.grid(row=1, column=1)

        tk.Label(frame_inputs, text="c:", bg=bg_color, fg="white").grid(row=2, column=0)
        entry3.grid(row=2, column=1)

        boton.config(command=calcular_cuadratica)

    else:

        tk.Label(frame_inputs, text="Número:", bg=bg_color, fg="white").grid(row=0, column=0)
        entry1.grid(row=0, column=1)

        if opcion == "Fibonacci":
            boton.config(command=calcular_fibonacci)

        elif opcion == "Primo":
            boton.config(command=verificar_primo)

        elif opcion == "Factorial":
            boton.config(command=calcular_factorial)


# ==============================
# INTERFAZ GRÁFICA
# ==============================

bg_color = "#1e1e2f"

ventana = tk.Tk()
ventana.title("Calculadora Matemática Avanzada")
ventana.geometry("500x500")
ventana.config(bg=bg_color)

titulo = tk.Label(
    ventana,
    text="CALCULADORA MATEMÁTICA",
    font=("Segoe UI", 18, "bold"),
    bg=bg_color,
    fg="#00ffcc"
)
titulo.pack(pady=15)

# MENÚ DESPLEGABLE

opcion_var = tk.StringVar()
opcion_var.set("Cuadrática")

menu = tk.OptionMenu(ventana, opcion_var, "Cuadrática", "Fibonacci", "Primo", "Factorial",
                     command=actualizar_vista)
menu.config(bg="#2b2b3d", fg="white", width=15)
menu.pack(pady=10)

# FRAME INPUTS

frame_inputs = tk.Frame(ventana, bg=bg_color)
frame_inputs.pack(pady=10)

entry1 = tk.Entry(frame_inputs)
entry2 = tk.Entry(frame_inputs)
entry3 = tk.Entry(frame_inputs)

# BOTÓN

boton = tk.Button(
    ventana,
    text="Calcular",
    bg="#4CAF50",
    fg="white",
    width=15
)
boton.pack(pady=10)

# RESULTADO

resultado = tk.StringVar()

output = tk.Label(
    ventana,
    textvariable=resultado,
    bg="#12121c",
    fg="#00ffcc",
    font=("Consolas", 11),
    justify="left",
    wraplength=450
)
output.pack(pady=20, padx=20, fill="both")

# Inicializar vista
actualizar_vista("Cuadrática")

ventana.mainloop()

