class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print(self.nombre,self.edad)

    def cumpleaños(self):
        cumple = self.edad + 1
        print(cumple)


def main():
        Aday = persona("Aday",19)
        Aday.imprimir()
        Aday.cumpleaños()


main()