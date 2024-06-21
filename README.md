

import tkinter as tk
from tkinter import ttk, messagebox

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")
        
        self.libros = {
            "Acción": [("Libro A1", "Autor A1"), ("Libro A2", "Autor A2"), ("Libro A3", "Autor A3"), ("Libro A4", "Autor A4"), ("Libro A5", "Autor A5"), ("Libro A6", "Autor A6"), ("Libro A7", "Autor A7"), ("Libro A8", "Autor A8"), ("Libro A9", "Autor A9"), ("Libro A10", "Autor A10")],
            "Fantasía": [("Libro F1", "Autor F1"), ("Libro F2", "Autor F2"), ("Libro F3", "Autor F3"), ("Libro F4", "Autor F4"), ("Libro F5", "Autor F5"), ("Libro F6", "Autor F6"), ("Libro F7", "Autor F7"), ("Libro F8", "Autor F8"), ("Libro F9", "Autor F9"), ("Libro F10", "Autor F10")],
            "Informativo": [("Libro I1", "Autor I1"), ("Libro I2", "Autor I2"), ("Libro I3", "Autor I3"), ("Libro I4", "Autor I4"), ("Libro I5", "Autor I5"), ("Libro I6", "Autor I6"), ("Libro I7", "Autor I7"), ("Libro I8", "Autor I8"), ("Libro I9", "Autor I9"), ("Libro I10", "Autor I10")],
            "Historia": [("Libro H1", "Autor H1"), ("Libro H2", "Autor H2"), ("Libro H3", "Autor H3"), ("Libro H4", "Autor H4"), ("Libro H5", "Autor H5"), ("Libro H6", "Autor H6"), ("Libro H7", "Autor H7"), ("Libro H8", "Autor H8"), ("Libro H9", "Autor H9"), ("Libro H10", "Autor H10")],
            "Terror": [("Libro T1", "Autor T1"), ("Libro T2", "Autor T2"), ("Libro T3", "Autor T3"), ("Libro T4", "Autor T4"), ("Libro T5", "Autor T5"), ("Libro T6", "Autor T6"), ("Libro T7", "Autor T7"), ("Libro T8", "Autor T8"), ("Libro T9", "Autor T9"), ("Libro T10", "Autor T10")]
        }

        self.cantidades = {k: {libro[0]: 1 for libro in v} for k, v in self.libros.items()}
        self.prestamos = {}
        self.miembros = []

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_main_page()
        
    def create_main_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.registrar_miembro_button = tk.Button(self.main_frame, text="Registrar Miembro", command=self.registrar_miembro)
        self.registrar_miembro_button.grid(row=0, column=0, padx=10, pady=10)
        
        tk.Label(self.main_frame, text="MIembros:").grid(row=1, column=0, padx=10, pady=10)
        self.usuario_combobox = ttk.Combobox(self.main_frame, values=[miembro["nombre"] for miembro in self.miembros], width=28, state="readonly")
        self.usuario_combobox.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.main_frame, text="Categoría:").grid(row=2, column=0, padx=10, pady=10)
        self.categoria_combobox = ttk.Combobox(self.main_frame, values=list(self.libros.keys()), width=28, state="readonly")
        self.categoria_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.categoria_combobox.bind("<<ComboboxSelected>>", self.update_libros_list)

        
        tk.Label(self.main_frame, text="Libro:").grid(row=3, column=0, padx=10, pady=10)
        self.libro_combobox = ttk.Combobox(self.main_frame, width=28, state="readonly")
        self.libro_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.libro_combobox.bind("<<ComboboxSelected>>", self.update_autor_label)
        
        tk.Label(self.main_frame, text="Autor:").grid(row=4, column=0, padx=10, pady=10)
        self.autor_label = tk.Label(self.main_frame, text="", width=30)
        self.autor_label.grid(row=4, column=1, padx=10, pady=10)
        
        self.solicitar_button = tk.Button(self.main_frame, text="Solicitar Préstamo", command=self.solicitar_prestamo)
        self.solicitar_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.ver_registros_button = tk.Button(self.main_frame, text="Ver Registros de prestamo", command=self.ver_registros)
        self.ver_registros_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.ver_miembros_button = tk.Button(self.main_frame, text="Ver Miembros", command=self.ver_miembros)
        self.ver_miembros_button.grid(row=7, column=0, columnspan=2, pady=10)
        
    def registrar_miembro(self):
        self.registro_window = tk.Toplevel(self.root)
        self.registro_window.title("Registrar Miembro")
        self.registro_window.geometry("300x200")
        
        tk.Label(self.registro_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_entry = tk.Entry(self.registro_window, width=30)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.registro_window, text="Cédula:").grid(row=1, column=0, padx=10, pady=10)
        self.cedula_entry = tk.Entry(self.registro_window, width=30)
        self.cedula_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.registro_window, text="Número Telefónico:").grid(row=2, column=0, padx=10, pady=10)
        self.telefono_entry = tk.Entry(self.registro_window, width=30)
        self.telefono_entry.grid(row=2, column=1, padx=10, pady=10)
        self.telefono_entry.bind("<KeyRelease>", self.validate_telefono)
        
        self.guardar_button = tk.Button(self.registro_window, text="Guardar", command=self.guardar_miembro)
        self.guardar_button.grid(row=3, column=0, columnspan=2, pady=10)
        
    def validate_telefono(self, event):
        texto = self.telefono_entry.get()
        if not texto.isdigit() or len(texto) > 10:
            self.telefono_entry.delete(len(texto)-1, tk.END)
            
    def guardar_miembro(self):
        nombre = self.nombre_entry.get()
        cedula = self.cedula_entry.get()
        telefono = self.telefono_entry.get()
        
        if not nombre or not cedula or not telefono or len(telefono) != 10:
            messagebox.showerror("Error", "Por favor, completa todos los campos correctamente.")
            return
        
        self.miembros.append({"nombre": nombre, "cedula": cedula, "telefono": telefono})
        self.registro_window.destroy()
        self.usuario_combobox['values'] = [miembro["nombre"] for miembro in self.miembros]
        
    def update_libros_list(self, event):
        categoria = self.categoria_combobox.get()
        libros = [libro[0] for libro in self.libros[categoria]]
        self.libro_combobox['values'] = libros
    
    def update_autor_label(self, event):
        categoria = self.categoria_combobox.get()
        libro = self.libro_combobox.get()
        for libro_nombre, autor in self.libros[categoria]:
            if libro_nombre == libro:
                self.autor_label.config(text=autor)
                break
    
    def solicitar_prestamo(self):
        usuario = self.usuario_combobox.get()
        categoria = self.categoria_combobox.get()
        libro = self.libro_combobox.get()
        
        if not usuario or not categoria or not libro:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return
        
        if usuario in self.prestamos:
            messagebox.showerror("Error", "El usuario ya tiene un libro prestado.")
            return
        
        if self.cantidades[categoria][libro] == 0:
            messagebox.showerror("Error", "El libro ya está prestado.")
            return
        
        self.cantidades[categoria][libro] -= 1
        self.prestamos[usuario] = (categoria, libro)
        messagebox.showinfo("Éxito", f"Préstamo de '{libro}' autorizado para {usuario}.")
    
    def ver_registros(self):
        registros_window = tk.Toplevel(self.root)
        registros_window.title("Registros de Préstamos")
        registros_window.geometry("400x300")
        
        registros_text = tk.Text(registros_window)
        registros_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for usuario, (categoria, libro) in self.prestamos.items():
            registros_text.insert(tk.END, f"Usuario: {usuario}, Libro: {libro}, Categoría: {categoria}\n")
        
        tk.Button(registros_window, text="Devolver Libro", command=self.devolver_libro).pack(pady=10)
        
    def devolver_libro(self):
        usuario = self.usuario_combobox.get()
        if usuario not in self.prestamos:
            messagebox.showerror("Error", "El usuario no tiene libros prestados.")
            return
        
        categoria, libro = self.prestamos.pop(usuario)
        self.cantidades[categoria][libro] += 1
        messagebox.showinfo("Éxito", f"Libro '{libro}' devuelto por {usuario}.")
        self.ver_registros()

    def ver_miembros(self):
        miembros_window = tk.Toplevel(self.root)
        miembros_window.title("Miembros Registrados")
        miembros_window.geometry("400x300")
        
        miembros_text = tk.Text(miembros_window)
        miembros_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for miembro in self.miembros:
            miembros_text.insert(tk.END, f"Nombre: {miembro['nombre']}, Cédula: {miembro['cedula']}, Teléfono: {miembro['telefono']}\n")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

