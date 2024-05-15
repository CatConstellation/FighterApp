#Funcion por cada proceso

#import controllers y class y al bd
#clase de classmodelUsuario, funciones crearusuario, los datos están en el objeto y se guardan en el bd (dos condiciones: respuestas al view)
#consultas- funciones 
# le envia la sentencia al bd y apartir de eso le envia las respuestas al controller 
import usuario


def crearUsuario(rol, id, email, password):
        usuario.rol = rol
        usuario.id = id
        usuario.email = email
        usuario.password = password


def verUsuario(id):
        print('El usuario es:', usuario.username, 'con el rol de', usuario.rol)

def setUser(username):
usuario.user = username

def setRol(rol):
usuario.rol = rol

def setEmail(email):
usuario.email = email

def setPassword(password):
usuario.passwords = password

