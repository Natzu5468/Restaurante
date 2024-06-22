import tkinter as tk

def mostrar_miembros():
    texto_miembros = """
Información sobre miembros

Aquí podrás encontrar información sobre nuestros miembros y sus derechos.

**Derechos de los miembros:**

* Acceso a la biblioteca física
* Acceso a la biblioteca digital
* acceso al sistema de prestamo de libros
"""
    return texto_miembros

def crear_botones_miembros(frame):
    button_miembros = tk.Button(frame, text="Miembros del sistema", font=("Arial", 18), bg="#A8C3A6", fg="white")
    button_miembros.pack(fill="x", pady=20)

    button_agregar_miembro = tk.Button(frame, text="Agregar miembro", font=("Arial", 18), bg="#A8C3A6", fg="white")
    button_agregar_miembro.pack(fill="x", pady=20)

    return button_miembros, button_agregar_miembro