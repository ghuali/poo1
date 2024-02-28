class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print(self.nombre,self.edad)

    def cumpleanos(self):
        cumple = self.edad + 1
        print(cumple)


def main():
        Aday = Persona("Aday",19)
        Aday.imprimir()
        Aday.cumpleanos()


main()