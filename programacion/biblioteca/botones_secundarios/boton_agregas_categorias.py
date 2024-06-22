import tkinter as tk
from tkinter import messagebox

categorias_libros = {
    "Accion": [
        ("Accion1", "AutorAccion1"),
        ("Accion2", "AutorAccion2"),
        ("Accion3", "AutorAccion3"),
        ("Accion4", "AutorAccion4"),
        ("Accion5", "AutorAccion5"),
        ("Accion6", "AutorAccion6"),
    ],
    "Historia": [
        ("Historia1", "AutorHistoria1"),
        ("Historia2", "AutorHistoria2"),
        ("Historia3", "AutorHistoria3"),
    ],
    "Fantasia": [
        ("Fantasia1", "AutorFantasia1"),
        ("Fantasia2", "AutorFantasia2"),
    ],
    "Informativos": [
        ("Informativos1", "AutorInformativos1"),
        ("Informativos2", "AutorInformativos2"),
    ],
    "Cocina": [
        ("Cocina1", "AutorCocina1"),
        ("Cocina2", "AutorCocina2"),
    ],
    "Deportes": [
        ("Deportes1", "AutorDeportes1"),
        ("Deportes2", "AutorDeportes2"),
    ]
}

def agregar_categoria(frame):
    def on_agregar_click():
        nombre_categoria = entry_nombre_categoria.get().strip()
        libros_info = []

        # Validación de nombre de categoría
        if not nombre_categoria or nombre_categoria.isdigit():
            messagebox.showerror("Error", "El nombre de la categoría debe contener al menos un carácter y no puede ser numérico")
            return

        # Validación de libros
        libros_existentes = set()
        for libros in categorias_libros.values():
            for libro, _ in libros:
                libros_existentes.add(libro.lower())

        for i in range(5):
            nombre_libro = entry_libros[i].get().strip()
            cantidad_libro = entry_cantidad[i].get().strip()
            if not nombre_libro or not cantidad_libro:
                messagebox.showerror("Error", "Todos los campos de nombre de libro y cantidad deben estar llenos")
                return
            if nombre_libro.lower() in libros_existentes:
                messagebox.showerror("Error", f"El nombre del libro '{nombre_libro}' ya existe en otra categoría")
                return
            if not cantidad_libro.isdigit() or int(cantidad_libro) == 0:
                messagebox.showerror("Error", "La cantidad debe ser un número mayor que 0")
                return
            libros_info.append((nombre_libro, cantidad_libro))

        # Agregar la nueva categoría
        categorias_libros[nombre_categoria] = libros_info
        messagebox.showinfo("Éxito", "Categoría agregada con éxito")

        # Limpiar los campos
        entry_nombre_categoria.delete(0, tk.END)
        for i in range(5):
            entry_libros[i].delete(0, tk.END)
            entry_cantidad[i].delete(0, tk.END)

    for widget in frame.winfo_children():
        widget.destroy()

    label_instrucciones = tk.Label(frame, text="Agregar una nueva categoría de libros:", font=("Arial", 14))
    label_instrucciones.pack(pady=10)

    tk.Label(frame, text="Nombre de la categoría:", font=("Arial", 12)).pack(anchor="w", padx=20)
    entry_nombre_categoria = tk.Entry(frame, font=("Arial", 12))
    entry_nombre_categoria.pack(fill="x", padx=20, pady=5)

    entry_libros = []
    entry_cantidad = []

    for i in range(5):
        frame_libro = tk.Frame(frame)
        frame_libro.pack(fill="x", padx=20, pady=5)
        
        tk.Label(frame_libro, text=f"Nombre del libro {i+1}:", font=("Arial", 12)).pack(side="left")
        entry_libro = tk.Entry(frame_libro, font=("Arial", 12))
        entry_libro.pack(side="left", padx=5, fill="x", expand=True)
        entry_libros.append(entry_libro)
        
        tk.Label(frame_libro, text="Cantidad:", font=("Arial", 12)).pack(side="left", padx=5)
        entry_cantidad_libro = tk.Entry(frame_libro, font=("Arial", 12), width=5)
        entry_cantidad_libro.pack(side="left")
        entry_cantidad.append(entry_cantidad_libro)

    button_agregar_categoria = tk.Button(frame, text="Agregar Categoría", font=("Arial", 14), command=on_agregar_click)
    button_agregar_categoria.pack(pady=20)