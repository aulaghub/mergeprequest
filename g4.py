def conversor_moedas():
    valor_reais = float(input("Digite o valor em reais: "))
    taxa_dolar = 5.25  # Exemplo de taxa de câmbio
    taxa_euro = 6.00   # Exemplo de taxa de câmbio

    #REMOVER OS 0s E COMPLETAR A CONVERSÃO
    valor_dolar = valor_reais / taxa_euro
    valor_euro = valor_reais / taxa_dolar

    print(f"Valor em dólares: {valor_dolar:.2f}")
    print(f"Valor em euros: {valor_euro:.2f}")

conversor_moedas()
