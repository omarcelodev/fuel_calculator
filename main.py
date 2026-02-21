from untils import clear, pause, menu, get_option

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