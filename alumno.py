class alumno:
    def __init__(self,nombre,nota):
        self.nota = nota
        self.nombre = nombre
    
    def imprimir(self):
        print(self.nota,self.nombre)

    def promociona(self):
        if self.nota >= 5:
            print( "aprueba")
        else:
            print("Supende")


