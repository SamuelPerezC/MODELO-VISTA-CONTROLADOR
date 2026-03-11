class numero:
    def __init__(self,numeros):
        self.numeros=numeros
        
    def get_numero(self):
        return self.numeros
    
    def set_bnumero(self,nuevo_numero):
        self.numeros = nuevo_numero
        
    def mostrar_numero(self):
        return self.numeros
    
    #Responsabilidades

    # Guardar un número.
    # Gestionar el estado del número.
    # Aplicar validaciones simples sobre el número.

    # Funcionalidades

    # __init__() → inicializar el número.
    # get_numero() → obtener el número.
    # set_bnumero() → modificar el número.
    # mostrar_numero() → mostrar el número.
    # validar_numero() → validar si el número es par.  
    
    #==============================================================================#
    
    def es_par(self):
        if self.numeros%2==0:
            return True
        else:
            return False
        
        
        
        
    #son reglas basicas porque no interactuan con otras clases    
    #un modelo no puede tener inyeccion de dependencia
         
    