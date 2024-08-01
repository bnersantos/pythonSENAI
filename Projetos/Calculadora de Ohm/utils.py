from time import sleep


def menu():
    while True:
        print("=" * 80)
        print("Calculadora de Ohm:")
        print("Menu:")
        print("\n[1] Ache a Resistência")
        print("[2] Ache a Corrente Elétrica")
        print("[3] Ache a Tensão Elétrica")
        print("[4] Ache a resistência do resistor")
        print("[0] Sair")
        print("-" * 80)
        try:
            escolha = int(input("\nDigite sua escolha:"))
            if escolha not in [0, 1, 2, 3, 4]:
                print("Opção Inválida!")
            else:
                print("Processando a informação...")
                sleep(0.5)
                print("Escolha selecionada!")
                return escolha

        except ValueError:
            print("Valor Inválido!")
        except TypeError:
            print("Tente novamente!")


def receber_corrente():
    while True:
        try:
            corrente = float(input("Digite o valor da corrente: "))
            if corrente < 0:
                print("Valor inválido, deve ser maior que 0.")
            else:
                sleep(0.5)
                print("Processando a informação...")
                sleep(0.3)
                print("Informação recebida!")
                return corrente
        except ValueError:
            print("Valor Inválido!")
        except TypeError:
            print("Tente novamente!")


def receber_tensao():
    while True:
        try:
            tensao = float(input("Digite o valor da tensao: "))
            if tensao < 0:
                print("Valor inválido, deve ser maior que 0.")
            else:
                print("...")
                sleep(0.5)
                print("Processando a informação...")
                sleep(0.3)
                print("Informação recebida!")
                return tensao
        except ValueError:
            print("Valor Inválido!")
        except TypeError:
            print("Tente novamente!")


def receber_resistencia():
    while True:
        try:
            resistencia = float(input("Digite o valor da resistencia: "))
            if resistencia < 0:
                print("Valor Inválido!")
            else:
                print("...")
                sleep(0.5)
                print("Processando a informação...")
                sleep(0.3)
                print("Informação recebida!")
                return resistencia
        except ValueError:
            print("Valor Inválido!")
        except TypeError:
            print("Tente novamente!")


def receber_tesao_font():
    while True:
        try:
            tensao_font = float(input("Digite o valor da tensão da fonte: "))
            if tensao_font <= 0:
                print("Valor inválido, deve ser maior que 0.")
            else:
                print("...")
                sleep(0.5)
                print("Processando a informação...")
                sleep(0.3)
                print("Informação recebida!")
                return tensao_font
        except ValueError:
            print("Valor Inválido!")
        except TypeError:
            print("Tente novamente!")


def receber_tensao_led():
    while True:
        try:
            tensao_led = float(input("Digiteo valor da tensão do led: "))
            if tensao_led <= 0:
                print(("Valor inválido, dever ser maior que 0."))
            else:
                print("...")
                sleep(0.5)
                print("Processando a informação...")
                sleep(0.3)
                print("Informação recebida!")
                return tensao_led
        except ValueError:
            print("Valor Inválido!")
        except TypeError:
            print("Tente novamente!")


def calculadora_resistencia():
    tensao = receber_tensao()
    corrente = receber_corrente()
    resistencia = tensao / corrente
    return resistencia


def calculadora_corrente_eletrica():
    tensao = receber_tensao()
    resistencia = receber_resistencia()
    corrente = tensao / resistencia
    return corrente


def calculadora_tensao_eletrica():
    resistencia = receber_resistencia()
    corrente = receber_corrente()
    tensao = resistencia * corrente
    return tensao


def calculadora_resistencia_resistor():
    tensao_font = receber_tesao_font()
    corrente = receber_corrente()
    tensao_led = receber_tensao_led()
    r_menos = tensao_font - tensao_led
    resistencia_resistor = r_menos / corrente
    return resistencia_resistor


def exibir_resistencia(resistencia):
    print("...")
    sleep(0.5)
    print("Processando a informação...")
    print(f"O valor da resistência é:{resistencia} ")


def exibir_corrente(corrente):
    print("-" * 80)
    print("...")
    sleep(0.5)
    print("Processando a informação...")
    print(f"O valor de corrente é:{corrente}")
    print("-" * 80)


def exibir_tensao(tensao):
    print("-" * 80)
    print("...")
    sleep(0.5)
    print("Processando a informação...")
    print(f"O valor da tensão é: {tensao} ")
    print("-" * 80)


def exibir_resistentia_resistor(resistencia_resistor):
    print("-" * 80)
    print("...")
    sleep(0.5)
    print("Processando a informação...")
    print(f"O valor da tensão é: {resistencia_resistor}")
    print("-" * 80)
