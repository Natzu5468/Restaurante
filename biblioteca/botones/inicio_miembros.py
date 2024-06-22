# inicio_miembros.py

import tkinter as tk
from botones_secundarios.el_cerebro_del_codigo import mostrar_mensaje_cerebro

def mostrar_miembros():
    texto_miembros = """ Información sobre miembros
    Aquí podrás encontrar información sobre nuestros miembros y sus derechos.
    **Derechos de los miembros:**
    * Acceso a la biblioteca física
    * Acceso a la biblioteca digital
    * acceso al sistema de préstamo de libros """
    return texto_miembros

def crear_botones_miembros(frame):
    button_cerebro = tk.Button(frame, text="El cerebro del código", font=("Arial", 18), bg="#A8C3A6", fg="white", command=lambda: mostrar_mensaje_cerebro(frame))
    button_cerebro.pack(fill="x", pady=20)

    button_agregar_miembro = tk.Button(frame, text="Agregar miembro", font=("Arial", 18), bg="#A8C3A6", fg="white")
    button_agregar_miembro.pack(fill="x", pady=20)

    return button_cerebro, button_agregar_miembro