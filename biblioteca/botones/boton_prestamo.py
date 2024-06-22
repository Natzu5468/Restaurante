# prestamo.py

import tkinter as tk
from tkinter import messagebox
from botones_secundarios.boton_agregar_miembros import miembros_lista
from botones_secundarios.boton_agregas_categorias import categorias_libros

prestamos_activos = []

def mostrar_prestamo(frame):
    def on_autorizar_prestamo():
        miembro_seleccionado = combo_miembros.get()
        cedula_confirmacion = entry_cedula_confirmacion.get().strip()
        categoria_seleccionada = combo_categorias.get()
        libro_seleccionado = combo_libros.get()

        # Validar que el miembro no haya pedido otro préstamo activo
        for prestamo in prestamos_activos:
            if prestamo['miembro'] == miembro_seleccionado:
                messagebox.showerror("Error", "Este miembro ya tiene un préstamo activo")
                return
        
        # Validar que no se pueda seleccionar el mismo libro más de una vez en un préstamo
        for prestamo in prestamos_activos:
            if prestamo['libro'] == libro_seleccionado:
                messagebox.showerror("Error", "Este libro ya está prestado")
                return
        
        # Registrar el préstamo
        prestamo_info = {
            "miembro": miembro_seleccionado,
            "cedula_confirmacion": cedula_confirmacion,
            "categoria": categoria_seleccionada,
            "libro": libro_seleccionado
        }
        prestamos_activos.append(prestamo_info)
        messagebox.showinfo("Éxito", "Préstamo autorizado y registrado")

        # Limpiar los campos después de autorizar el préstamo
        combo_miembros.set('')
        entry_cedula_confirmacion.delete(0, tk.END)
        combo_categorias.set('')
        combo_libros.set('')

    for widget in frame.winfo_children():
        widget.destroy()

    label_instrucciones = tk.Label(frame, text="Para aprobar el préstamo, complete la siguiente información:", font=("Arial", 14))
    label_instrucciones.pack(pady=10)

    # Selección de miembro
    tk.Label(frame, text="1. Miembro:", font=("Arial", 12)).pack(anchor="w", padx=20)
    combo_miembros = tk.StringVar()
    combo_miembros.set('')  # Valor inicial vacío
    combo_miembros_dropdown = tk.OptionMenu(frame, combo_miembros, *miembros_lista)
    combo_miembros_dropdown.pack(fill="x", padx=20, pady=5)

    # Confirmación de cédula
    tk.Label(frame, text="2. Confirmación de cédula:", font=("Arial", 12)).pack(anchor="w", padx=20)
    entry_cedula_confirmacion = tk.Entry(frame, font=("Arial", 12))
    entry_cedula_confirmacion.pack(fill="x", padx=20, pady=5)

    # Selección de categoría
    tk.Label(frame, text="3. Categoría del libro:", font=("Arial", 12)).pack(anchor="w", padx=20)
    combo_categorias = tk.StringVar()
    combo_categorias.set('')  # Valor inicial vacío
    combo_categorias_dropdown = tk.OptionMenu(frame, combo_categorias, *categorias_libros.keys())
    combo_categorias_dropdown.pack(fill="x", padx=20, pady=5)

    # Selección de libro dentro de la categoría seleccionada
    tk.Label(frame, text="4. Nombre del libro:", font=("Arial", 12)).pack(anchor="w", padx=20)
    combo_libros = tk.StringVar()
    combo_libros.set('')  # Valor inicial vacío
    combo_libros_dropdown = tk.OptionMenu(frame, combo_libros, '')
    combo_libros_dropdown.pack(fill="x", padx=20, pady=5)

    def actualizar_libros(*args):
        categoria_seleccionada = combo_categorias.get()
        if categoria_seleccionada:
            libros_disponibles = [libro[0] for libro in categorias_libros.get(categoria_seleccionada, [])]
            combo_libros.set('')  # Reiniciar selección
            menu = combo_libros_dropdown['menu']
            menu.delete(0, 'end')
            for libro in libros_disponibles:
                menu.add_command(label=libro, command=tk._setit(combo_libros, libro))

    combo_categorias.trace('w', actualizar_libros)

    # Botón para autorizar el préstamo
    button_autorizar_prestamo = tk.Button(frame, text="Autorizar Préstamo", font=("Arial", 14), command=on_autorizar_prestamo)
    button_autorizar_prestamo.pack(pady=20)

