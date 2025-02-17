from catalogo_peliculas import CatalogoPeliculas
from peliculas import Pelicula

def menu():
    #Función principal para mostrar el menú interactivo.
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPeliculas(nombre_catalogo)

    while True:
        print("\nMenú:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Buscar Película")
        print("4. Eliminar catálogo de películas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == "2":
            catalogo.listar_peliculas()
        elif opcion == "3":
            nombre_pelicula = input("Ingrese el nombre de la película que desea buscar: ")
            catalogo.buscar_pelicula(nombre_pelicula)
        elif opcion == "4":
            catalogo.eliminar_catalogo()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
