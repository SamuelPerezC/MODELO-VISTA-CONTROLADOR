import tkinter as tk
from tkinter import ttk


class VistaTkinter:

    def __init__(self, controlador):

        # La vista recibe el controlador
        self.controlador = controlador

        self.ventana = tk.Tk()
        self.ventana.title("Calculadora MVC")

        # -------- USUARIO --------
        tk.Label(self.ventana, text="Nombre").pack()

        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.pack()

        tk.Label(self.ventana, text="Cedula").pack()

        self.entry_cedula = tk.Entry(self.ventana)
        self.entry_cedula.pack()

        tk.Button(
            self.ventana,
            text="Guardar Usuario",
            command=self.guardar_usuario
        ).pack(pady=5)

        # -------- TABLA --------
        self.crear_columnas_tabla()

        # -------- NUMEROS --------
        tk.Label(self.ventana, text="Numero 1").pack()

        self.entry_num1 = tk.Entry(self.ventana)
        self.entry_num1.pack()

        tk.Label(self.ventana, text="Numero 2").pack()

        self.entry_num2 = tk.Entry(self.ventana)
        self.entry_num2.pack()

        tk.Button(
            self.ventana,
            text="Sumar",
            command=self.calcular_suma
        ).pack(pady=5)

        # -------- RESULTADO --------
        self.label_resultado = tk.Label(self.ventana, text="Resultado:")
        self.label_resultado.pack()

    # -------- CREAR COLUMNAS TABLA --------

    def crear_columnas_tabla(self):

        self.tabla = ttk.Treeview(self.ventana)

        # definir columnas
        self.tabla["columns"] = ("Nombre", "Cedula")

        # eliminar columna fantasma
        self.tabla.column("#0", width=0, stretch=tk.NO)

        # configurar columnas
        self.tabla.column("Nombre", anchor=tk.CENTER, width=120)
        self.tabla.column("Cedula", anchor=tk.CENTER, width=120)

        # encabezados
        self.tabla.heading("Nombre", text="Nombre", anchor=tk.CENTER)
        self.tabla.heading("Cedula", text="Cedula", anchor=tk.CENTER)

        self.tabla.pack(pady=10)

    # -------- INSERTAR FILA EN TABLA --------

    def insertar_fila(self, nombre, cedula):

        self.tabla.insert(
            "",
            tk.END,
            values=(nombre, cedula)
        )

    # -------- EVENTOS DE LA VISTA --------

    def guardar_usuario(self):

        nombre = self.entry_nombre.get()
        cedula = self.entry_cedula.get()

        # enviar datos al controlador
        self.controlador.guardar_usuario(nombre, cedula)

        # mostrar en tabla
        self.insertar_fila(nombre, cedula)

    def calcular_suma(self):

        n1 = self.entry_num1.get()
        n2 = self.entry_num2.get()

        resultado = self.controlador.calcular_suma(n1, n2)

        self.label_resultado.config(text=f"Resultado: {resultado}")

    # -------- INICIAR INTERFAZ --------

    def iniciar(self):
        self.ventana.mainloop()