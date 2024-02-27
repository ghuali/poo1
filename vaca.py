class animal:
    patas = 0

    def caminar():
        print("caminando con",animal.patas,"patas")


def main():
    vaca = animal
    vaca.patas = 4
    vaca.caminar()

    pato = animal
    pato.caminar()

if __name__ == "__main__":
    main()