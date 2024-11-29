
def receber_quantidade():
    try:
        quantidade = int(input("Digite a quantidade de ações:"))
        if quantidade <= 0:
            print("Quantidade Inválida, tente mais que 0.")
        else:
            return quantidade
    except ValueError:
        print("Valor Inválido!")
    except TypeError:
        print("Tente novamente!")

def receber_da_acao():
    try:
        acao = input('Digite o nome da Ação: ')
        return acao
    except ValueError:
        print("Valor Inválido!")
    except TypeError:
        print("Tente novamente!")
def receber_valor():
    try:
        valor = float(input('Digite o valor da ação: '))
        return valor
    except ValueError:
        print("Valor Inválido!")
    except TypeError:
        print("Tente novamente!")
def menu():
    print('='*40)
    print('{:^40}'.format('MENU'))
    print('='*40)
    print("[1] Adicionar ação e valor.")
    print("[2] Mostrar Ações e Valores Calculados.")
    print("[3] Sair")
    print("Oque deseja realizar?")
    try:
        escolha = int(input("Digite sua escolha: "))
        if escolha not in [1, 2, 3]:
            print("Opção Inválida")
        else:
            print("Opção Escolhida!")
            return escolha
    except ValueError:
        print("Valor Inválido!")
    except TypeError:
        print("Tente novamente!")

