class Caluculo:
    def __init__(self,num1:float, num2:float):
        self.num1 = num1
        self.num2 = num2

    
    def suma(self):
        suma = (self.num1 + self.num2)

        print(suma)

    def resta(self):
        resta = (self.num1 - self.num2)

        print(resta)
    
    def multi(self):
        multi = (self.num1 * self.num2)
        print(multi)
    
    def div(self):
        div = (self.num1 / self.num2)
        print(div)
    

if __name__ == '__main__':

    print("dame los numeros:")
    numeros = Caluculo(int(input()),int(input()))
    print("Elige del 1 al 4:")
    elec = int(input())
    if elec == 1:
        numeros.suma()
    elif elec == 2:
        numeros.resta()
    elif elec == 3:
        numeros.multi()
    elif elec == 4:
        numeros.div()

