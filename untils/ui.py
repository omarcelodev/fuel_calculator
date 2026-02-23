import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Pressione ENTER para continuar. . .")

def header():
    print("=== CALCULADOR DE COMBUSTIVEL ===\n")

# Função para exibir o menu
def menu():
    header()
    print("Escolha o Combustível:")
    print("(1) GASOLINA  -  R$6,19")
    print("(2) ETANOL    -  R$4,59")
    print("(3) DIESEL    -  R$5,29")
    print("(0) SAIR")

def resultado(combustivel, litros_gastos, custo_total):
    header()
    print("Resumo do consumo: ")
    print(f"Combustivel      : {combustivel.nome}")
    print(f"Litros gastos    : {litros_gastos:.2f}L")
    print(f"Custo total      : R${custo_total:.2f} ")