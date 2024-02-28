class alumno:
    def imprimir(self):
        self.nota = 0
        self.nombre = ""
        print(self.nota,self.nombre)

    def promociona(self):
        self.nota = 0
        self.nombre = 0
        if self.nota >= 5:
            return True
        else:
            return False


