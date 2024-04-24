class Juego:

    def __init__(self,nombre,genero,plataforma):
        self.nombre=nombre
        self.genero=genero
        self.plataforma=plataforma
        
    def getNombre(self):
        return self.nombre
    
    def getGenero(self):
        return self.genero

    def setNombre(self,Nombre):
        self.nombre=input("Ingrese el nombre del Juego: ")

    def setGenero(self,Genero):
        self.Genero=input("Ingrese el genero del Juego: ")