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