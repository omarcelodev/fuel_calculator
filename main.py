import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Pressione ENTER para continuar. . .")

# Função para exibir o menu
def menu():
    print("=== CALCULADOR DE COMBUSTIVEL ===\n")
    print("Escolha o Combustível:")
    print("(1) GASOLINA")
    print("(2) ETANOL")
    print("(3) DISEL")
    print("(0) SAIR")

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
        
def main():
    while True:
        option = get_option()

        if option == 1:
            print("Gasolina")
            pause()
        elif option == 2:
            print("Etanol")
            pause()
        elif option == 3:
            print("Disel")
            pause()
        elif option == 0:
            print("\nPrograma encerrado. . .")
            break
        else:
            print("\nOpção Inválida!")
            pause()
main()