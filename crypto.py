class Crypto:
    def __init__(self, nombre:str, euros:float) -> None:
        self.nombre = nombre
        self.euros = euros

    def stoploss(self, min:float, max:float):
        self.min = min
        self.max = max

    def imprimir(self):
        print("El valor de",self.nombre,"tiene de valor de",self.euros)


if __name__ == '__main__':
    bitcoin = Crypto("bitcoin", 57000)
    bitcoin.imprimir()
        