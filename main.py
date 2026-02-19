import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Pressione ENTER para continuar. . .")

def main():
    while True:
        clear()
        print("=== CALCULADOR DE COMBUSTIVEL ===\n")
        print("Escolha o Combustível:")
        print("(1) GASOLINA")
        print("(2) ETANOL")
        print("(3) DISEL")
        print("(0) SAIR")
        option = int(input("Sua opção: "))

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