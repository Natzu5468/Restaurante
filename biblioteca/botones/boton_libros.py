import tkinter as tk
from botones_secundarios.boton_agregas_categorias import categorias_libros, agregar_categoria

def mostrar_categorias(frame):
    def mostrar_libros_categoria(categoria):
        for widget in frame.winfo_children():
            widget.destroy()
        label_categoria = tk.Label(frame, text=categoria, font=("Arial", 18))
        label_categoria.pack(pady=10)
        for libro, autor in categorias_libros.get(categoria, []):
            label_libro = tk.Label(frame, text=f"- {libro} ------------- autor {autor}", font=("Arial", 14))
            label_libro.pack(anchor="w", padx=20, pady=2)

    for widget in frame.winfo_children():
        widget.destroy()

    label_instrucciones = tk.Label(frame, text="Seleccione una categoría de libros:", font=("Arial", 14))
    label_instrucciones.pack(pady=10)

    categories_frame = tk.Frame(frame)
    categories_frame.pack()

    row = 0
    column = 0
    for categoria in categorias_libros:
        button_categoria = tk.Button(categories_frame, text=categoria, font=("Arial", 12), width=15,
                                     command=lambda c=categoria: mostrar_libros_categoria(c))
        button_categoria.grid(row=row, column=column, padx=5, pady=5)
        column += 1
        if column == 5:
            column = 0
            row += 1

    button_agregar_categoria = tk.Button(frame, text="Agregar Categoría", font=("Arial", 14),
                                         command=lambda: agregar_categoria(frame))
    button_agregar_categoria.pack(pady=20)