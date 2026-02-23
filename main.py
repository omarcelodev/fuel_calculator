import untils as u
import fuel as f

PRECOS = {
    1: ("Gasolina", 6.19),
    2: ("Etanol", 4.59),
    3: ("Diesel", 5.29)
}

def main():
    while True:
        option = u.get_option()

        if option == 0:
            print("Programa encerrado. . .")
            break

        nome, preco = PRECOS[option]
        
        distancia = u.get_float_positivo("Digite a distância (km): ")
        consumo = u.get_float_positivo("Digite o consumo (km/L): ")
        u.clear()

        combustivel = f.Combustivel(nome, distancia, consumo, preco)

        litros_gastos = combustivel.calcular_litros_gastos()
        custo_total = combustivel.calcular_custo_total(litros_gastos)
        
        u.resultado(combustivel, litros_gastos, custo_total)
        u.pause()

if __name__ == "__main__":
    main() 