from numero_modelo import numero
from vista import VistaConsola
from controlador import ControladorParImpar
if __name__ == "__main__":
    print("APP PAR/IMPAR = ESTRUCTURA MVC")
    Controlador=ControladorParImpar()
    Controlador.iniciar()