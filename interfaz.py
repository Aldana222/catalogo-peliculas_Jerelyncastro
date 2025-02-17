import tkinter as tk
from tkinter import messagebox
from catalogo_peliculas import CatalogoPeliculas
from peliculas import Pelicula

class CatalogoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Películas")
        
        # Etiqueta para el nombre del catálogo
        self.label = tk.Label(root, text="Nombre del Catálogo:")
        self.label.pack()

        # Entrada de texto para el nombre del catálogo
        self.entry_catalogo = tk.Entry(root)
        self.entry_catalogo.pack()

        # Botón para crear el catálogo
        self.boton_crear = tk.Button(root, text="Cargar Catálogo", command=self.cargar_catalogo)
        self.boton_crear.pack()

        # Entrada de texto para películas
        self.entry_pelicula = tk.Entry(root)
        self.entry_pelicula.pack()

        # Botón para agregar películas
        self.boton_agregar = tk.Button(root, text="Agregar Película", command=self.agregar_pelicula)
        self.boton_agregar.pack()

        # Botón para listar películas
        self.boton_listar = tk.Button(root, text="Listar Películas", command=self.listar_peliculas)
        self.boton_listar.pack()

        # Botón para buscar películas
        self.boton_buscar = tk.Button(root, text="Buscar Película", command=self.buscar_pelicula)
        self.boton_buscar.pack()

        # Botón para eliminar el catálogo
        self.boton_eliminar = tk.Button(root, text="Eliminar Catálogo", command=self.eliminar_catalogo)
        self.boton_eliminar.pack()

        # Área de texto para mostrar la lista de películas
        self.text_area = tk.Text(root, height=10, width=40)
        self.text_area.pack()

    def cargar_catalogo(self):
        nombre_catalogo = self.entry_catalogo.get()
        if nombre_catalogo:
            self.catalogo = CatalogoPeliculas(nombre_catalogo)
            messagebox.showinfo("Catálogo", f"Catálogo '{nombre_catalogo}' cargado con éxito.")
        else:
            messagebox.showwarning("Error", "Ingrese un nombre para el catálogo.")

    def agregar_pelicula(self):
        nombre_pelicula = self.entry_pelicula.get()
        if nombre_pelicula:
            pelicula = Pelicula(nombre_pelicula)
            self.catalogo.agregar_pelicula(pelicula)
            messagebox.showinfo("Película", f"Película '{nombre_pelicula}' agregada.")
        else:
            messagebox.showwarning("Error", "Ingrese un nombre para la película.")

    def listar_peliculas(self):
        self.text_area.delete('1.0', tk.END)
        if hasattr(self, 'catalogo'):
            if not self.catalogo.listar_peliculas():
                self.text_area.insert(tk.END, "No hay películas en el catálogo.")
        else:
            messagebox.showwarning("Error", "Debe cargar un catálogo primero.")

    def buscar_pelicula(self):
        nombre_pelicula = self.entry_pelicula.get()
        if nombre_pelicula:
            self.catalogo.buscar_pelicula(nombre_pelicula)
        else:
            messagebox.showwarning("Error", "Ingrese un nombre de película para buscar.")

    def eliminar_catalogo(self):
        if hasattr(self, 'catalogo'):
            self.catalogo.eliminar_catalogo()
            messagebox.showinfo("Catálogo", "El catálogo ha sido eliminado.")
        else:
            messagebox.showwarning("Error", "Debe cargar un catálogo primero.")

# Ejecutar la interfaz gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogoGUI(root)
    root.mainloop()
