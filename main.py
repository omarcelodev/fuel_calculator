import untils as u

def main():
    while True:
        option = u.get_option()

        if option == 1:
            print("Gasolina")
            distancia = u.get_distancia_percorrida()
            u.pause()
        elif option == 2:
            print("Etanol")
            distancia = u.get_distancia_percorrida()
            u.pause()
        elif option == 3:
            print("Disel")
            distancia = u.get_distancia_percorrida()
            u.pause()
        elif option == 0:
            print("\nPrograma encerrado. . .")
            break
        else:
            print("\nOpção Inválida!")
            u.pause()
main()