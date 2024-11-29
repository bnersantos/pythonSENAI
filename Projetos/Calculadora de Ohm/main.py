r = ""
cE = ""
tE = ""
escolha = ""

# Escolha do comando:
while True:
    print("Calculadora de Ohm:")
    print("Menu:")
    print("\n[1] Ache a Resistência")
    print("[2] Ache a Corrente Elétrica")
    print("[3] Ache a Tensão Elétrica")
    print("[4] Ache a resistência do resistor")
    print("[0] Sair")
    escolha = int(input("\nDigite sua escolha:"))

    if escolha == 0:
        break
    elif escolha == 1:
        print(f"Sua escolha é 1, sendo assim, descobriremos a resistência:")
        controle = True
        while controle:
            cE = float(input("Digite o valor da Corrente Elétrica em Ampere:"))
            tE = float(input("Digite o valor da Tensão Elétrica em Volts:"))
        controle = cE <= 0 or tE <= 0
        if controle:
            print("Valores Inválidos! Ambos os valores devem ser maiores que zero.")

        r = tE / cE
        print(f"O valor da Resistência é: {r:.2f} Ohm.")

    elif escolha == 2:
        print(f"Sua escolha é 2, descobriremos a Corrente Elétrica")
        controle = True
        while controle:
            r = float(input("Digite a Resistência em Ohm:"))
            tE = float(input("Digite a Tensão Elétrica Volts:"))
            controle = r <= 0 or tE <= 0
            if controle:
                print("Valores Inválidos! Ambos os valores devem ser maiores que zero.")
        cE = tE / r
        print(f"O valor da Corrente Elétrica é: {cE:.2f} Ampere.")

    elif escolha == 3:
        print(f"Sua escolha é 3, descobrimremos a Tensão Elétrica")
        controle = True
        while controle:
            r = float(input("Digite a Resistência em Ohm:"))
            cE = float(input("Digite a Corrente Elétrica em Ampere:"))
            controle = r <= 0 or cE <= 0
            if controle:
                print("Valores Inválidos! Ambos os valores devem ser maiores que zero.")
        tE = r * cE
        print(f"O valor da Tensão Elétrica é: {tE} Volts.")

    elif escolha == 4:
        print(f"Sua escolha é 4, descobriremos a Resistência do Resistor")
        controle = True
        while controle:
            tF = float(input("Digite a Tensão da Fonte em Volts:"))
            tL = float(input("Digite a Tensão do LED em Volts:"))
            cL = float(input("Digite a Corrente do LED em Ampere:"))
            controle = tF <= 0 or tL <= 0 or cL <= 0
            if controle:
                print("Valores Inválidos! Todos os valores devem ser maiores que zero.")
        rr = tF - tL
        rR = rr / cL
        print(f"O valor da Resistência do Resistor é: {rR:.2f} Ohm.")

    else:
        print("Opção Inválida!")


