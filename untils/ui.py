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
    print("(1) GASOLINA")
    print("(2) ETANOL")
    print("(3) DIESEL")
    print("(0) SAIR")

def resultado(combustivel, litros_gastos, custo_total):
    header()
    print("Resumo do consumo: ")
    print(f"Combustivel      : {combustivel.nome}")
    print(f"Litros gastos    : {litros_gastos:.2f}L")
    print(f"Custo total      : R${custo_total:.2f} ")