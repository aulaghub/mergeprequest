import random

def gerador_nomes():
    nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
    sobrenomes = ["Silva", "Souza", "Pereira", "Oliveira", "Costa"]
    
    nome_completo = f"{random.choice(sobrenomes)} {random.choice(nomes)}"
    print(f"Nome gerado: {nome_completo}")

gerador_nomes()
