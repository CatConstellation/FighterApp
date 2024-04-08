class Torneo:
    def __init__(self, ID, inscripcion, juego, premios, participantesNum, requisito):
        self.ID = ID
        self.inscripcion = inscripcion
        self.juego = juego
        self.premios = premios
        self.participantesNum = participantesNum
        self.requisito = requisito

    def registrarTorneo(self):
        self.ID = input("Ingrese ID del torneo: ")
        self.inscripcion = input("Ingrese fecha de inscripción: ")
        self.juego = input("Ingrese nombre del juego: ")
        self.premios = input("Ingrese detalles de premios: ")
        self.participantesNum = int(input("Ingrese número de participantes: "))
        self.requisito = input("Ingrese requisitos del torneo: ")

    def modificarTorneo(self):
        print("Modificar Torneo:")
        self.ID = input("Nuevo ID del torneo: ")
        self.inscripcion = input("Nueva fecha de inscripción: ")
        self.juego = input("Nuevo nombre del juego: ")
        self.premios = input("Nuevos detalles de premios: ")
        self.participantesNum = int(input("Nuevo número de participantes: "))
        self.requisito = input("Nuevos requisitos del torneo: ")

    def eliminarTorneo(self):
        confirmacion = input("¿Está seguro que desea eliminar el torneo? (S/N): ")
        if confirmacion.upper() == 'S':
            print("Torneo eliminado correctamente.")
        else:
            print("Operación de eliminación cancelada.")

    def verTorneo(self):
        print("Detalles del Torneo:")
        print(f"ID: {self.ID}")
        print(f"Inscripción: {self.inscripcion}")
        print(f"Juego: {self.juego}")
        print(f"Premios: {self.premios}")
        print(f"Número de participantes: {self.participantesNum}")
        print(f"Requisitos: {self.requisito}")


#Ejemplo de uso
#torneo1 = Torneo("", "", "", "", 0, "")

#torneo1.registrarTorneo()

#torneo1.verTorneo()

#torneo1.modificarTorneo()
#torneo1.verTorneo()

#torneo1.eliminarTorneo()
