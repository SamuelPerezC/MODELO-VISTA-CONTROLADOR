class Calculadora:

    def __init__(self):
        self.operacion = ""
        self.resultado = None
        self.fecha = ""
        self.texto_tabla = ""

    def hacer_suma(self, num1, num2):
        self.resultado = int(num1) + int(num2)
        return self.resultado

    def hacer_resta(self, num1, num2):
        self.resultado = int(num1) - int(num2)
        return self.resultado

    def hacer_operacion(self, num1, num2, operacion):

        if operacion == "suma":
            return self.hacer_suma(num1, num2)

        elif operacion == "resta":
            return self.hacer_resta(num1, num2)

        else:
            return None