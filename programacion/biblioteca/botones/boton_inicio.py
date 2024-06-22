# miembros/zbotones/inicio.py
import tkinter as tk

def mostrar_inicio():
    texto_inicio = """
Bienvenido al sistema de biblioteca virtual

Bienvenido al Sistema de Biblioteca Virtual
¡Hola y bienvenido al Sistema de Biblioteca Virtual! Este servicio está diseñado para atenderte en todas tus necesidades relacionadas con la búsqueda, el préstamo y la gestión de libros y recursos digitales. Nuestra misión es facilitar el acceso a una amplia gama de materiales educativos y de entretenimiento para apoyar tu aprendizaje y disfrute personal.

Si necesitas ayuda en cualquier momento, no dudes en utilizar las siguientes opciones de soporte:

Búsqueda de Libros : Explora nuestro catálogo en línea para encontrar libros disponibles en formato digital y físico.
Préstamo de Libros : Solicita el préstamo de libros directamente desde nuestra plataforma y gestiona tus reservas.
"""
    return texto_inicio

def crear_botones_inicio(frame):
    button_inicio = tk.Button(frame, text="Inicio", font=("Arial", 18), bg="#A8C3A6", fg="white")
    button_inicio.pack(fill="x", pady=20)

    return button_inicio