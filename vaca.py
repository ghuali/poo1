"""
1. Qué palabra reservada se utiliza en lugar de animal (nombre de la clase) para acceder al atributo patas
 Self
2.Qué palabra reservada hay que utilizar para crear un nuevo objeto

"""


class animal:
    

    def caminar(self):
        self.patas = 0
        print("caminando con", self.patas ,"patas")


def main():
    vaca = animal()
    vaca.patas = 4
    vaca.caminar()

    pato = animal()
    pato.caminar()

    vaca.caminar()

if __name__ == "__main__":
    main()