import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import secrets
import string
import pyperclip

def generar_contrasena(longitud, complejidad):
    alfabeto = string.ascii_lowercase
    if complejidad >= 2:
        alfabeto += string.ascii_uppercase
    if complejidad >= 3:
        alfabeto += string.digits
    if complejidad >= 4:
        alfabeto += string.punctuation
    return ''.join(secrets.choice(alfabeto) for i in range(longitud))

def accion_generar():
    longitud = int(spin_longitud.get())
    complejidad = combo_complejidad.current() + 1
    contrasena = generar_contrasena(longitud, complejidad)
    label_resultado.config(text=contrasena)

def copiar_portapapeles():
    contrasena = label_resultado.cget("text")
    if contrasena:
        pyperclip.copy(contrasena)
        messagebox.showinfo("Información", "Contraseña copiada al portapapeles")

ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
estilo = ttk.Style()
estilo.theme_use('clam')

label_intro = ttk.Label(ventana, text="Bienvenido al Generador de Contraseñas Seguras")
label_intro.pack(pady=10)

label_longitud = ttk.Label(ventana, text="Longitud de la contraseña:")
label_longitud.pack()

spin_longitud = ttk.Spinbox(ventana, from_=8, to=32, width=5)
spin_longitud.pack()

label_complejidad = ttk.Label(ventana, text="Nivel de complejidad:")
label_complejidad.pack()

combo_complejidad = ttk.Combobox(ventana, values=["Básico", "Intermedio", "Avanzado", "Muy Avanzado"], state="readonly")
combo_complejidad.pack()
combo_complejidad.current(2)

boton_generar = ttk.Button(ventana, text="Generar Contraseña", command=accion_generar)
boton_generar.pack(pady=10)

boton_copiar = ttk.Button(ventana, text="Copiar al Portapapeles", command=copiar_portapapeles)
boton_copiar.pack(pady=5)

label_resultado = ttk.Label(ventana, text="", font=('Segoe UI', 12), wraplength=300)
label_resultado.pack(pady=20)

ventana.mainloop()