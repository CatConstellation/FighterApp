def setPlataforma(self,plataforma):
    num= input("En cuantas plataformas se puede jugar?: ")
    lista=[]
    for i in range(num):
      temp=input(f"Ingrese la plataforma {num}: ")
      lista.append(temp)
    self.plataforma=lista

def getPlataforma(self):
    return self.plataforma

def verJuego(self):
    print("Informacion del Juego:")
    print(f"Nombre: {self.nombre}")
    print(f"Genero: {self.genero}")
    print(f"Plataforma(s): {self.plataforma}")