import untils as u

class Combustivel:
    def __init__(self, nome, distancia, consumo, preco):
        self.nome = nome
        self.distancia = distancia
        self.consumo = consumo
        self.preco = preco

    def calcular_litros_gastos(self):
        return self.distancia / self.consumo
    
    def calcular_custo_total(self):
        litros_gastos = self.calcular_litros_gastos()
        return litros_gastos * self.preco
    
PRECOS = {
    1: ("Gasolina", 6.19),
    2: ("Etanol", 4.59),
    3: ("Diesel", 5.29)
}

def main():
    while True:
        option = u.get_option()

        if option == 0:
            print("Programa encerrado")
            break

        nome, preco = PRECOS[option]
        
        distancia = u.get_distancia_percorrida()
        consumo = u.get_consumo_medio()
        u.pause()

        combustivel = Combustivel(nome, distancia, consumo, preco)
        litros_gastos= combustivel.calcular_litros_gastos()
        custo_total = combustivel.calcular_custo_total()

        print(combustivel.nome)
        print(f"Litros gastos: {litros_gastos:.2f} L")
        print(f"Custo total: R$ {custo_total:.2f} ")
        u.pause()
main() 