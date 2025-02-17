import os
from peliculas import Pelicula

class CatalogoPeliculas:
    #Maneja el catálogo de películas almacenado en un archivo de texto.
    
    def __init__(self, nombre_catalogo):
        self.__nombre = nombre_catalogo  # Atributo privado
        self.__ruta_archivo = nombre_catalogo + ".txt"  # Atributo privado

    @property
    def nombre(self):
        return self.__nombre

    @property
    def ruta_archivo(self):
        return self.__ruta_archivo

    def agregar_pelicula(self, pelicula):
        #Agrega una nueva película al catálogo.
        with open(self.__ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(pelicula.nombre + '\n')
        print(f"Película '{pelicula.nombre}' agregada al catálogo.")

    def listar_peliculas(self):
        #Lista todas las películas del catálogo.
        if os.path.exists(self.__ruta_archivo):
            with open(self.__ruta_archivo, 'r', encoding='utf-8') as archivo:
                peliculas = archivo.readlines()
                if peliculas:
                    print("\nCatálogo de Películas:")
                    for pelicula in peliculas:
                        print(f"- {pelicula.strip()}")
                else:
                    print("El catálogo está vacío.")
        else:
            print("El catálogo no existe.")

    def buscar_pelicula(self, nombre):
        #Busca una película en el catálogo sin importar mayúsculas o minúsculas.
        if os.path.exists(self.__ruta_archivo):
            with open(self.__ruta_archivo, 'r', encoding='utf-8') as archivo:
                peliculas = [line.strip().lower() for line in archivo.readlines()]  # Convertimos todo a minúsculas
                if nombre.lower() in peliculas: 
                    print(f"La película '{nombre}' **SÍ** está en el catálogo.")
                else:
                    print(f"La película '{nombre}' **NO** está en el catálogo.")
        else:
            print("El catálogo no existe.")

    def eliminar_catalogo(self):
        #Elimina el archivo del catálogo de películas.
        if os.path.exists(self.__ruta_archivo):
            os.remove(self.__ruta_archivo)
            print("El catálogo ha sido eliminado.")
        else:
            print("No existe un catálogo para eliminar.")
