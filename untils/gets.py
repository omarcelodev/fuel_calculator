from .ui import clear, pause, menu, header

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
def get_option(mensagem):
    while True:
        clear()
        menu()
        user_input = input(mensagem)
        
        try:
            option = int(user_input)

            if option in [0, 1, 2, 3]:
                return option

        except ValueError:
            pass
        
        print("\nOpção inválida! Tente novamente.")
        pause()

# Função para ler número float positivo 
def get_float_positivo(mensagem):
    while True:
        clear()
        header()
        user_input = input(mensagem)

        try:
            valor = float(user_input.replace(",", "."))
            if valor > 0:
                return valor
        except ValueError:
            pass

        print("\nValor Inválido! Tente novamente.")
        pause()