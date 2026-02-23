class Combustivel:
    def __init__(self, nome, distancia, consumo, preco): # Construtor do objeto
        self.nome = nome
        self.distancia = distancia
        self.consumo = consumo
        self.preco = preco

    def calcular_litros_gastos(self): # Método para calcular litros gastos pelo motorista
        return self.distancia / self.consumo
    
    def calcular_custo_total(self, litros_gastos): # Método para calcular o valor desses litros gastos
        return litros_gastos * self.preco
    