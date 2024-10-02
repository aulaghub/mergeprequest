def converter_unidades():
    print("1. Metros para Quilômetros")
    print("2. Celsius para Fahrenheit")
    
    escolha = int(input("Escolha uma conversão (1-2): "))
    
    if escolha == 1:
        metros = float(input("Digite a quantidade em metros: "))
        km = metros / 1000
        print(f"{metros} metros são {km:.2f} quilômetros.")
    elif escolha == 2:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C são {fahrenheit:.2f}°F.")
    else:
        print("Opção inválida!")

converter_unidades()
