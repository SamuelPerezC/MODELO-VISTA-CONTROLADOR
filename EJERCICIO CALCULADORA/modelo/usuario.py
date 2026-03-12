class Usuario:

    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        
    
    def validar_nombre(self):

        # quitar espacios al inicio y final
        nombre_limpio = self.nombre.strip()

        if not nombre_limpio:
            return False
        
        if len(nombre_limpio) <= 3:
            return False

        return True