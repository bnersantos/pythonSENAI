print("Calculadora de Ohm:")
print("Menu:")
print("\n[0] Sair")
print("[1] Ache a Resistência")
print("[2] Ache a Tensão Elétrica")
print("[3] Ache a Resistência do resistor ")
print("[4] Ache a resistência do resistor")

escolha = int(input("\nDigite sua escolha:"))

while escolha != 0:
    if escolha == 1:
        print("Resistência:")
        print("")
        while True:
            try:
                t = float(input("\nDigite o valor da tensão:"))
                if t > 0:
                    break
            except ValueError:
                print("Valor invalido. Digite um número utilizando o ponto como separador Ex: 1.0")
        while True:
            try:
                cl = float(input("\nDigite o valor da corrente elétrica:"))
                if cl > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número utlizando o ponto como separador Ex: 1.0")
        r = t / cl
        print(f"A resistência é: {r:.2f}")
    elif escolha == 2:
        print("Tensão:")
        print("")
        while True:
            try:
                c = float(input("Digite o valor da tensão em AMP:"))
                if c > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número utilizando o ponto como separador Ex: 1.0")
        while True:
            try:
                r = float(input("Digite o valor da resistência em Ohm:"))
                if r > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número utilizando o ponto como separador Ex: 1.0")
        t = r * c
        print(f"A tensão é: {t:.2f}Volts.")
    elif escolha == 3:
        print("Resistência do resistor:")
        print("")
        while True:
            try:
                t = float(input("Digite o valor da tensão da fonte em Volts:"))
                if t > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número utilizando o ponto como separador Ex: 1.0")
        while True:
            try:
                cl = float(input("Digite o valor da corrente do led em AMP:"))
                if cl > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número utilizando o ponto como separador Ex: 1.0")
        while True:
            try:
                tl = float(input("Digite o valor da tensão do led em Volts:"))
                if tl > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número utilizando o ponto como separador Ex: 1.0")
        r = (t - tl) / cl
        print(f"A resistência do resistor é: {r:.2f}")
    elif escolha == 4:
        print("corrente")
        print("")
        while True:
            try:
                t = float(input("Digite o valor da tensão em Volts:"))
                if t > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número utilizando o ponto como separador Ex: 1.0")
        while True:
            try:
                r = float(input("Digite o valor da resistência em Ohm:"))
                if r > 0:
                    break
            except ValueError:
                print("Valor Inválido. Digite um número ultilizando o ponto como separador Ex: 1.0")
        c = t / r
        print(f"O valor da corrente é: {c:.2f}")
    else:
        print("Escolha Inválida!")
    print("")
    print("Calculadora de Ohm:")
    print("Menu:")
    print("\n[0] Sair")
    print("[1] Ache a Resistência")
    print("[2] Ache a Tensão Elétrica")
    print("[3] Ache a Resistência do resistor ")
    print("[4] Ache a resistência do resistor")

    escolha = int(input("\nDigite sua escolha:"))


