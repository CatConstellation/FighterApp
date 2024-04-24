class Usuario:
    def __init__(self, rol, username):
        self.user = username
        self.rol = rol
    
    def getUser(self):
        return self.user
    
    def getRol(self):
        return self.rol
    
    def setUser(self, user):
        self.user = user
    
    def setRol(self, rol):
        self.rol = rol
   