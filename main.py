import untils as u

def main():
    while True:
        option = u.get_option()

        if option == 0:
            print("Programa encerrado")
            break
        
        if option in [1, 2, 3]:
            distancia = u.get_distancia_percorrida()
            u.pause()
main()