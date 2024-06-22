# confirmar_reembolso.py

import tkinter as tk
from tkinter import Toplevel, StringVar, Listbox, Entry, messagebox
from botones.boton_prestamo import prestamos_activos

def confirmar_reembolso(parent_frame):
    def actualizar_lista(event):
        search_term = entry_nombre_usuario.get().lower()
        lista_nombres.delete(0, tk.END)
        for prestamo in prestamos_activos:
            if search_term in prestamo['miembro'].lower():
                lista_nombres.insert(tk.END, prestamo['miembro'])

    def on_seleccionar(event):
        seleccion = lista_nombres.get(lista_nombres.curselection())
        entry_nombre_usuario.delete(0, tk.END)
        entry_nombre_usuario.insert(0, seleccion)

    def realizar_reembolso():
        nombre_usuario = entry_nombre_usuario.get()
        if not nombre_usuario:
            messagebox.showerror("Error", "Por favor, seleccione un usuario para reembolsar.")
            return

        for prestamo in prestamos_activos:
            if prestamo['miembro'] == nombre_usuario:
                prestamos_activos.remove(prestamo)
                messagebox.showinfo("Éxito", f"Préstamo reembolsado para {nombre_usuario}.")
                entry_nombre_usuario.delete(0, tk.END)
                lista_nombres.delete(0, tk.END)
                for prestamo in prestamos_activos:
                    lista_nombres.insert(tk.END, prestamo['miembro'])
                mostrar_registro_prestamo(parent_frame)  # Actualizar el registro de préstamos en la ventana principal
                return

        messagebox.showerror("Error", "El usuario seleccionado no tiene préstamos activos.")

    # Crear una nueva ventana
    ventana_reembolso = Toplevel(parent_frame)
    ventana_reembolso.title("Confirmar Reembolso")
    ventana_reembolso.geometry("400x400")

    label_instruccion = tk.Label(ventana_reembolso, text="Seleccione el nombre del usuario para confirmar reembolso:", font=("Arial", 12))
    label_instruccion.pack(pady=10)

    entry_nombre_usuario = Entry(ventana_reembolso, font=("Arial", 12))
    entry_nombre_usuario.pack(pady=10)
    entry_nombre_usuario.bind("<KeyRelease>", actualizar_lista)

    lista_nombres = Listbox(ventana_reembolso, font=("Arial", 12))
    lista_nombres.pack(pady=10)
    lista_nombres.bind("<<ListboxSelect>>", on_seleccionar)

    # Inicialmente llenar la lista con todos los nombres
    for prestamo in prestamos_activos:
        lista_nombres.insert(tk.END, prestamo['miembro'])

    # Botón para realizar reembolso
    button_reembolso = tk.Button(ventana_reembolso, text="Reembolso", font=("Arial", 14), command=realizar_reembolso)
    button_reembolso.pack(pady=20)