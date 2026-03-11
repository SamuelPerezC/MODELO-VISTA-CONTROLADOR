from modelo.usuario import Usuario
from modelo.numero import Numero
from modelo.calculadora import Calculadora


class ControladorApp:

    def __init__(self):

        self.usuario = Usuario("", "")
        self.num1 = Numero("")
        self.num2 = Numero("")
        self.calculadora = Calculadora()

    def guardar_usuario(self, nombre, cedula):

        self.usuario.set_nombre(nombre)
        self.usuario.set_id(cedula)

    def guardar_numeros(self, n1, n2):

        self.num1.set_numero(n1)
        self.num2.set_numero(n2)

    def calcular(self, operacion):

        resultado = self.calculadora.hacer_operacion(
            self.num1.get_numero(),
            self.num2.get_numero(),
            operacion
        )

        return resultado