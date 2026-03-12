from modelo.usuario import Usuario
from modelo.numero import Numero
from modelo.calculadora import Calculadora
from vista.vista_tkinter import VistaTkinter


class ControladorApp:

    def __init__(self):

        # ----- LLAMAMOS CARPETA MODELOS -----
        self.usuario = Usuario("", "")
        self.num1 = Numero("")
        self.num2 = Numero("")
        self.calculadora = Calculadora()

        # -----LLAMAMOS CARPETA VISTA -----
        self.vista = VistaTkinter(self)

    # -----------------------------
    # GUARDAR USUARIO
    # -----------------------------
    def guardar_usuario(self, nombre, cedula):

        self.usuario.set_nombre(nombre)
        self.usuario.set_id(cedula)
        
        if not self.usuario.validar_nombre():

            print("ERROR: El nombre debe tener más de 3 caracteres")
        return
    
    

    # -----------------------------
    # GUARDAR NUMEROS
    # -----------------------------
    def guardar_numeros(self, n1, n2):

        self.num1.set_numero(n1)
        self.num2.set_numero(n2)

    # -----------------------------
    # CALCULAR SUMA
    # -----------------------------
    def calcular_suma(self, n1, n2):

        # Guardar números en el modelo
        self.guardar_numeros(n1, n2)

        # Realizar operación usando el modelo calculadora
        resultado = self.calculadora.hacer_operacion(
            self.num1.get_numero(),
            self.num2.get_numero(),
            "suma"
        )

        return resultado