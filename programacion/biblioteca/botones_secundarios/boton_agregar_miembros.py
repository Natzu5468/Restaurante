import tkinter as tk
from tkinter import messagebox

miembros_lista = []

def agregar_miembro(frame):
    def on_agregar_click():
        nombre = entry_nombre.get()
        cedula = entry_cedula.get()
        telefono = entry_telefono.get()

        # Validación de teléfono
        if len(telefono) != 10 or not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe tener 10 dígitos y contener solo números")
            return

        # Validación de nombre y cédula únicos
        for miembro in miembros_lista:
            if miembro['nombre'] == nombre:
                messagebox.showerror("Error", "Ya existe un miembro con este nombre")
                return
            if miembro['cedula'] == cedula:
                messagebox.showerror("Error", "Ya existe un miembro con esta cédula")
                return

        # Agregar miembro a la lista
        miembro_info = {
            "nombre": nombre,
            "cedula": cedula,
            "telefono": telefono
        }
        miembros_lista.append(miembro_info)
        messagebox.showinfo("Éxito", "Miembro agregado con éxito")

        # Limpiar los campos
        entry_nombre.delete(0, tk.END)
        entry_cedula.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)

    for widget in frame.winfo_children():
        widget.destroy()

    label_instrucciones = tk.Label(frame, text="Para ser miembro se necesita la siguiente información:", font=("Arial", 14))
    label_instrucciones.pack(pady=10)

    tk.Label(frame, text="Nombre:", font=("Arial", 12)).pack(anchor="w", padx=20)
    entry_nombre = tk.Entry(frame, font=("Arial", 12))
    entry_nombre.pack(fill="x", padx=20, pady=5)

    tk.Label(frame, text="Cédula:", font=("Arial", 12)).pack(anchor="w", padx=20)
    entry_cedula = tk.Entry(frame, font=("Arial", 12))
    entry_cedula.pack(fill="x", padx=20, pady=5)

    tk.Label(frame, text="Teléfono:", font=("Arial", 12)).pack(anchor="w", padx=20)
    entry_telefono = tk.Entry(frame, font=("Arial", 12))
    entry_telefono.pack(fill="x", padx=20, pady=5)

    button_agregar = tk.Button(frame, text="Agregar", font=("Arial", 14), command=on_agregar_click)
    button_agregar.pack(pady=20)

def ver_miembros(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    if not miembros_lista:
        label_no_miembros = tk.Label(frame, text="No hay miembros agregados", font=("Arial", 14))
        label_no_miembros.pack(pady=10)
        return

    label_miembros = tk.Label(frame, text="Miembros del sistema:", font=("Arial", 14))
    label_miembros.pack(pady=10)

    for miembro in miembros_lista:
        miembro_texto = f"Nombre: {miembro['nombre']}, Cédula: {miembro['cedula']}, Teléfono: {miembro['telefono']}"
        tk.Label(frame, text=miembro_texto, font=("Arial", 12)).pack(anchor="w", padx=20, pady=2)
