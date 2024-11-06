import random

def simular_dado():
    lados = int(input("Digite o número de lados do dado: "))
    lancamento = random.randint(1, lados)
    print(f"O resultado do lançamento do dado é: {lancamento}")

simular_dado()
