import tkinter as tk
from botones.boton_inicio import mostrar_inicio, crear_botones_inicio
from botones.inicio_miembros import mostrar_miembros, crear_botones_miembros
from botones_secundarios.boton_agregar_miembros import agregar_miembro, ver_miembros
from botones.boton_libros import mostrar_categorias
from botones.boton_prestamo import mostrar_prestamo
from botones_secundarios.boton_registro_prestamo import mostrar_registro_prestamo 

# Crear ventana principal
root = tk.Tk()
root.geometry("1000x700")  # Tamaño de la ventana
root.title("Biblioteca Virtual")  # Título de la ventana

# Forzar ventana a aparecer en la esquina superior izquierda
root.attributes("-topmost", True)
root.update_idletasks()
root.attributes("-topmost", False)

# Crear marco superior con rectángulo verde
top_frame = tk.Frame(root, bg="#104D31", height=125, width=1000)
top_frame.pack(fill="x")

# Agregar etiqueta con texto "Biblioteca" en blanco
label_biblioteca = tk.Label(top_frame, text="Biblioteca", fg="white", bg="#104D31", font=("Arial", 24))
label_biblioteca.place(x=100, y=50)

# Crear frame lateral izquierdo con rectángulo verde claro
left_frame = tk.Frame(root, bg="#A8C3A6", width=200, height=575)
left_frame.pack(side="left", fill="y")

# Crear frame derecho con texto de bienvenida
right_frame = tk.Frame(root, width=800, height=575)
right_frame.pack(side="right", fill="both", expand=True)

# Agregar botones en frame lateral izquierdo con colores personalizados
def mostrar_inicio_callback():
    for widget in right_frame.winfo_children():
        widget.destroy()
    texto_inicio = mostrar_inicio()
    label_inicio = tk.Label(right_frame, text=texto_inicio, font=("Arial", 14), wraplength=750)
    label_inicio.pack(fill="both", expand=True)

button_inicio = tk.Button(left_frame, text="Inicio", font=("Arial", 18), bg="#A8C3A6", fg="white", command=mostrar_inicio_callback)
button_inicio.pack(fill="x", pady=20)

def mostrar_miembros_callback():
    for widget in right_frame.winfo_children():
        widget.destroy()
    texto_miembros = mostrar_miembros()
    label_miembros = tk.Label(right_frame, text=texto_miembros, font=("Arial", 14), wraplength=750)
    label_miembros.pack(fill="both", expand=True)

    # Crear botones miembros
    button_miembros, button_agregar_miembro = crear_botones_miembros(right_frame)
    button_agregar_miembro.config(command=lambda: agregar_miembro(right_frame))

button_membresia = tk.Button(left_frame, text="Miembros", font=("Arial", 18), bg="#A8C3A6", fg="white", command=mostrar_miembros_callback)
button_membresia.pack(fill="x", pady=20)

def ver_miembros_callback():
    ver_miembros(right_frame)

button_ver_miembros = tk.Button(left_frame, text="Ver Miembros", font=("Arial", 18), bg="#A8C3A6", fg="white", command=ver_miembros_callback)
button_ver_miembros.pack(fill="x", pady=20)

def mostrar_categorias_callback():
    mostrar_categorias(right_frame)

button_libros = tk.Button(left_frame, text="Libros", font=("Arial", 18), bg="#A8C3A6", fg="white", command=mostrar_categorias_callback)
button_libros.pack(fill="x", pady=20)

def mostrar_prestamo_callback():
    mostrar_prestamo(right_frame)

button_prestamo = tk.Button(left_frame, text="Préstamo", font=("Arial", 18), bg="#A8C3A6", fg="white", command=mostrar_prestamo_callback)
button_prestamo.pack(fill="x", pady=20)

# Nuevo botón "Registro de Préstamo"
def mostrar_registro_prestamo_callback():
    mostrar_registro_prestamo(right_frame)

button_registro_prestamo = tk.Button(left_frame, text="Registro de Préstamo", font=("Arial", 18), bg="#A8C3A6", fg="white", command=mostrar_registro_prestamo_callback)
button_registro_prestamo.pack(fill="x", pady=20)

mostrar_inicio_callback()  # Mostrar la página de inicio al inicio
root.mainloop()
