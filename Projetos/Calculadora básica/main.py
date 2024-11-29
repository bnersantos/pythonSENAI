number_1 = 0
number_2 = 0
option = 0
def menu():
    print('Menu\nCalculadora básica\nOpções:')
    print('[0] Sair;')
    print('[1] Adição;')
    print('[2] Subtração;')
    print('[3] Multiplicação;')
    print('[4] Divisão;')
    print('[5] Todas juntas.')

def receber_number_1():
    while True:
        try:
            number_1 = float(input("Digite o primeiro número: "))
            return number_1
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")

def receber_number_2():
    while True:
        try:
            number_2 = float(input("Digite o segundo número: "))
            return number_2
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")

def escolha_do_usuario():
    while True:
        try:
            escolha = int(input("Digite o número de escolha: "))
            if escolha not in [0, 1, 2, 3, 4,5]:
                print("Digite números de 0 - 4")
            else:
                return escolha
        except ValueError:
            print("Valor Inválido!")
        except TypeError:
            print("Tente novamente!")

def exibir_soma(number_1, number_2):
    print(f"O resultado da soma é: {number_1 + number_2}")

def exibir_menos(number_1, number_2):
    print(f"O resultado da subtração é: {number_1 - number_2}")

def exibir_multiplicacao(number_1, number_2):
    print(f"O resultado da divisão é: {number_1 * number_2}")

def exibir_divisao(number_1, number_2):
    print(f"O resultado da divisão é: {number_1 / number_2}")
def exibir_todos():
    exibir_soma(numero_1, numero_2)
    exibir_menos(numero_1, numero_2)
    exibir_multiplicacao(numero_1, numero_2)
    exibir_divisao(numero_1, numero_2)
while True:
    menu()
    escolha = escolha_do_usuario()
    if escolha == 5:
        numero_1 = receber_number_1()
        numero_2 = receber_number_2()
        exibir_todos()

    elif escolha == 1:
        numero_1 = receber_number_1()
        numero_2 = receber_number_2()
        exibir_soma(numero_1, numero_2)
    elif escolha == 2:
        numero_1 = receber_number_1()
        numero_2 = receber_number_2()
        exibir_menos(numero_1, numero_2)
    elif escolha == 3:
        numero_1 = receber_number_1()
        numero_2 = receber_number_2()
        exibir_multiplicacao(numero_1, numero_2)
    elif escolha == 4:
        numero_1 = receber_number_1()
        numero_2 = receber_number_2()
        exibir_divisao(numero_1, numero_2)
    elif escolha == 0:
        break
    else:
        menu()
        escolha()


