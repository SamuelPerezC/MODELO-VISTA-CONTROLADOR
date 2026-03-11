import tkinter as tk
from controlador.controlador import ControladorApp


class VistaTkinter:

    def __init__(self):

        self.controlador = ControladorApp() #esto esta mal, el controlador debe controlar la vista, no la vista al controlador

        self.ventana = tk.Tk()
        self.ventana.title("Calculadora MVC")

        tk.Label(self.ventana, text="Nombre").pack()
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.pack()

        tk.Label(self.ventana, text="Cedula").pack()
        self.entry_cedula = tk.Entry(self.ventana)
        self.entry_cedula.pack()

        tk.Button(self.ventana, text="Guardar Usuario",
                  command=self.guardar_usuario).pack()

        tk.Label(self.ventana, text="Numero 1").pack()
        self.entry_num1 = tk.Entry(self.ventana)
        self.entry_num1.pack()

        tk.Label(self.ventana, text="Numero 2").pack()
        self.entry_num2 = tk.Entry(self.ventana)
        self.entry_num2.pack()

        tk.Button(self.ventana, text="Sumar",
                  command=self.calcular_suma).pack()

        self.label_resultado = tk.Label(self.ventana, text="Resultado:")
        self.label_resultado.pack()

    def guardar_usuario(self):

        nombre = self.entry_nombre.get()
        cedula = self.entry_cedula.get()

        self.controlador.guardar_usuario(nombre, cedula)

    def calcular_suma(self, obj_controlador):

        n1 = self.entry_num1.get()
        n2 = self.entry_num2.get()

        self.controlador.guardar_numeros(n1, n2)

        resultado = self.controlador.calcular("suma")

        self.label_resultado.config(text=f"Resultado: {resultado}")

    def iniciar(self):
        self.ventana.mainloop()