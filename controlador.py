from numero_modelo import numero
from vista  import VistaConsola

class ControladorParImpar:
    def __init__(self):
        self.vista = VistaConsola()
        
    def iniciar(self):
        # Vista pide datos
        num1_valor = self.vista.pedir_numero1()
        num2_valor = self.vista.pedir_numero2()
        
        # Controlador crea objetos Modelo con los datos
        num1 = numero(num1_valor)
        num2 = numero(num2_valor)
        
        #Controlador pide a Modelo procesar Logica de negocio
        es_par1 = num1.es_par()
        es_par2 = num2.es_par()
        
        # Controlador usa GETTERS del Modelo para extraer datos y los pasa a la vista para mostrar
        self.vista.mostrar_resultado(num1,num2,es_par1,es_par2)
        