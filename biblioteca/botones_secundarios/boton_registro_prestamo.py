# registro_prestamo.py

import tkinter as tk
from tkinter import scrolledtext
from botones.boton_prestamo import prestamos_activos
from botones_secundarios.confirmar_reembolso import confirmar_reembolso

def mostrar_registro_prestamo(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    if not prestamos_activos:
        label_no_prestamos = tk.Label(frame, text="No hay préstamos registrados", font=("Arial", 14))
        label_no_prestamos.pack(pady=10)
        return

    label_registro = tk.Label(frame, text="Registro de Préstamos Activos:", font=("Arial", 14))
    label_registro.pack(pady=10)

    text_registro = scrolledtext.ScrolledText(frame, width=100, height=20, wrap=tk.WORD)
    text_registro.pack(padx=20, pady=10)

    for prestamo in prestamos_activos:
        texto_prestamo = f"Miembro: {prestamo['miembro']}\nCédula de confirmación: {prestamo['cedula_confirmacion']}\nCategoría: {prestamo['categoria']}\nLibro: {prestamo['libro']}\n\n"
        text_registro.insert(tk.END, texto_prestamo)

    text_registro.config(state=tk.DISABLED)  # Para hacer el texto no editable

    # Botón para confirmar reembolso
    button_reembolso = tk.Button(frame, text="Confirmar Reembolso", font=("Arial", 14), command=lambda: confirmar_reembolso(frame))
    button_reembolso.pack(pady=20)