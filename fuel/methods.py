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
    