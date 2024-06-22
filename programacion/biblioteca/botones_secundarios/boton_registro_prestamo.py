# botones_secundarios/registro_prestamo.py
import tkinter as tk

registros_prestamos = []

def registrar_prestamo(miembro, cedula, categoria, libro):
    registro = {
        "Miembro": miembro,
        "Confirmación de cédula": cedula,
        "Categoría del libro": categoria,
        "Nombre del libro": libro
    }
    registros_prestamos.append(registro)

def mostrar_registro_prestamo(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    if not registros_prestamos:
        label_no_prestamos = tk.Label(frame, text="No hay préstamos registrados", font=("Arial", 14))
        label_no_prestamos.pack(pady=10)
        return

    label_titulo = tk.Label(frame, text="Registro de Préstamos:", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=10)

    for index, prestamo in enumerate(registros_prestamos, start=1):
        texto_prestamo = f"Prestamo {index}:\n"
        texto_prestamo += f"Miembro: {prestamo['Miembro']}\n"
        texto_prestamo += f"Confirmación de cédula: {prestamo['Confirmación de cédula']}\n"
        texto_prestamo += f"Categoría del libro: {prestamo['Categoría del libro']}\n"
        texto_prestamo += f"Nombre del libro: {prestamo['Nombre del libro']}\n\n"
        tk.Label(frame, text=texto_prestamo, font=("Arial", 12)).pack(anchor="w", padx=20, pady=5)