from .ui import clear, pause, menu

# Função para ler a opção do usuário
def read_option():
    return input("Sua opção: ")

# Função para validar a opção do usuário
def validar_option(option):
    try:
        option = int(option)
        if option in [0, 1, 2, 3]:
            return option
        else:
            return None
    except ValueError:
        return None

# Função para obter a opção do usuário, garantindo que seja válida
def get_option():
    while True:
        clear()
        menu()
        user_input = read_option()
        option = validar_option(user_input)

        if option is not None:
            return option
        else:
            print("\nOpção inválida! Tente novamente.")
            pause()

# Função para ler a distância percorrida
def read_distancia_percorrida():
    return input("Digite a distância percorrida (km): ")

# Função para validar a distância percorrida
def validar_distancia_percorrida(distancia):
    try:
        distancia = float(distancia)
        if distancia > 0:
            return distancia
        else:
            return None
    except ValueError:
        return None

# Função para obter a distância percorrida do usuário
def get_distancia_percorrida():
    while True:
        clear()
        print("=== CALCULADOR DE COMBUSTIVEL === \n")

        user_input = read_distancia_percorrida()
        distancia = validar_distancia_percorrida(user_input)

        if distancia is not None:
            return distancia
        else:
            print("\nDistância inválida! Tente novamente.")
            pause()

# Função para ler o consumo médio do veículo
def read_consumo_medio():
    return input("Digite o consumo médio (km/L): ")

# Função para validar o consumo médio do veículo
def validar_consumo_medio(consumo):
    try:
        consumo = float(consumo)
        if consumo > 0:
            return consumo
        else:
            return None
    except ValueError:
        return None

# Função para obter o consumo médio do veículo
def get_consumo_medio():
    while True:
        clear()
        print("=== CALCULADOR DE COMBUSTIVEL === \n")

        user_input = read_consumo_medio()
        consumo = validar_consumo_medio(user_input)

        if consumo is not None:
            return consumo
        else:
            print("\nConsumo médio inválido! Tente novamente.")
            pause()