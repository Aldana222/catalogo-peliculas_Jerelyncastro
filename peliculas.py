class Pelicula:
    #Representa una película con un atributo privado para el nombre.
    
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    @property
    def nombre(self):
        #Getter para acceder al nombre de la película.
        return self.__nombre

    def __str__(self):
        return self.__nombre
