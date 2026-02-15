import tkinter as tk
import math

# FUNCIONES

def calcular_cuadratica():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            resultado.set("No es ecuación cuadrática")
            return

        d = b**2 - 4*a*c

        if d < 0:
            resultado.set("No tiene soluciones reales")
        else:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            resultado.set(f"x1 = {x1:.4f}\nx2 = {x2:.4f}")
    except:
        resultado.set("Error en los datos")


def calcular_fibonacci():
    try:
        n = int(entry_fib.get())

        if n < 0:
            resultado.set("Ingrese número positivo")
            return

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b

        resultado.set(f"Fibonacci({n}) = {a}")
    except:
        resultado.set("Error en los datos")


def es_primo(n, divisor=2):
    if n < 2:
        return False
    if divisor > math.sqrt(n):
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor + 1)


def verificar_primo():
    try:
        n = int(entry_primo.get())
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
        n = int(entry_fact.get())
        if n < 0:
            resultado.set("Ingrese número positivo")
            return
        resultado.set(f"{n}! = {factorial(n)}")
    except:
        resultado.set("Error en los datos")


# INTERFAZ

ventana = tk.Tk()
ventana.title("Calculadora Matemática")
ventana.geometry("600x650")
ventana.config(bg="#1e1e2f")

titulo = tk.Label(
    ventana,
    text="CALCULADORA MATEMÁTICA",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
titulo.pack(pady=15)

# CUADRÁTICA

frame1 = tk.LabelFrame(ventana, text="Ecuación Cuadrática", bg="#2b2b3d", fg="white")
frame1.pack(pady=10, fill="x", padx=20)

entry_a = tk.Entry(frame1)
entry_b = tk.Entry(frame1)
entry_c = tk.Entry(frame1)

tk.Label(frame1, text="a:", bg="#2b2b3d", fg="white").grid(row=0, column=0)
entry_a.grid(row=0, column=1)
tk.Label(frame1, text="b:", bg="#2b2b3d", fg="white").grid(row=1, column=0)
entry_b.grid(row=1, column=1)
tk.Label(frame1, text="c:", bg="#2b2b3d", fg="white").grid(row=2, column=0)
entry_c.grid(row=2, column=1)

tk.Button(frame1, text="Calcular", command=calcular_cuadratica, bg="#4CAF50").grid(row=3, columnspan=2, pady=5)

# FIBONACCI

frame2 = tk.LabelFrame(ventana, text="Fibonacci", bg="#2b2b3d", fg="white")
frame2.pack(pady=10, fill="x", padx=20)

entry_fib = tk.Entry(frame2)
tk.Label(frame2, text="Posición n:", bg="#2b2b3d", fg="white").grid(row=0, column=0)
entry_fib.grid(row=0, column=1)

tk.Button(frame2, text="Calcular", command=calcular_fibonacci, bg="#2196F3").grid(row=1, columnspan=2, pady=5)

# PRIMO

frame3 = tk.LabelFrame(ventana, text="Número Primo (Recursivo)", bg="#2b2b3d", fg="white")
frame3.pack(pady=10, fill="x", padx=20)

entry_primo = tk.Entry(frame3)
tk.Label(frame3, text="Número:", bg="#2b2b3d", fg="white").grid(row=0, column=0)
entry_primo.grid(row=0, column=1)

tk.Button(frame3, text="Verificar", command=verificar_primo, bg="#FF9800").grid(row=1, columnspan=2, pady=5)

# FACTORIAL

frame4 = tk.LabelFrame(ventana, text="Factorial (Recursivo)", bg="#2b2b3d", fg="white")
frame4.pack(pady=10, fill="x", padx=20)

entry_fact = tk.Entry(frame4)
tk.Label(frame4, text="Número:", bg="#2b2b3d", fg="white").grid(row=0, column=0)
entry_fact.grid(row=0, column=1)

tk.Button(frame4, text="Calcular", command=calcular_factorial, bg="#E91E63").grid(row=1, columnspan=2, pady=5)

# RESULTADO

resultado = tk.StringVar()

output = tk.Label(
    ventana,
    textvariable=resultado,
    bg="#12121c",
    fg="#00ffcc",
    font=("Consolas", 11),
    justify="left",
    wraplength=550
)
output.pack(pady=20, padx=20, fill="both")

ventana.mainloop()
