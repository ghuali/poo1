class alumno:
    def nota(self):
        self.nota = 0
        return self.nota

    def nombre(self):
        self.nombre = ""
        return self.nombre
    
    def promociona(self):
        if self.nota >= 5:
            return True
        else:
            return False



def main():
    Alumno1 = alumno()
    Alumno1.nota = 6
    Alumno1.nombre = "Ángel"
    Alumno1.promociona

    



if __name__ == "__main__":
    main()