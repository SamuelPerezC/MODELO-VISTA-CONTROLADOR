class VistaConsola:
    def mostrar_mensaje(self, texto):
        print(texto)
        
    def pedir_numero1(self):
        numero1 = int(input("Ingresa el PRIMER numero: "))
        return numero1
    
    def pedir_numero2(self):
        numero2 = int(input("Ingresa el SEGUNDO numero: "))
        return numero2
    
    
    def mostrar_resultado(self, num1,num2,es_par1, es_par2):
        self.mostrar_mensaje("RESULTADO:")
        if es_par1 == True:
            print(f"Numero 1: {num1.get_numero()} es PAR ")
            
        else:
            print(f"Numero 1: {num1.get_numero()} es IMPAR ")
            
        if es_par2 == True:
            print(f"Numero 2: {num2.get_numero()} es PAR ")
            
        else:
            print(f"Numero 2: {num2.get_numero()} es PAR ")
            
            