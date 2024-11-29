numero = 0
numero2 = 0
while True:
    while True:
        try:
            numero = float(input("Digite o primeiro número: "))
            if numero < 0:
                print("Seu número é negativo, tente um positivo!")
            else:
                break
        except ValueError:
            print("Valor inválido, tente novamente!")
        except TypeError:
            print("Valor incerto, tente outro!")
    while True:
        try:
            numero2 = float(input("Digite o segundo número: "))
            if numero < 0:
                print("Seu número é negativo, tente um positivo!")
            else:
                break
        except ValueError:
            print("Valor inválido, tente novamente!")
        except TypeError:
            print("Valor incerto, tente outro!")
    if numero > numero2:
        print(f"O número {numero} é maior que o número {numero2}!")
    if numero < numero2:
        print(f"O número {numero2} é maior que o número {numero}!")
    else:
        print("Os número são iguais!")
