while True:
    while True:
        try:
            number = int(input("Digite o número de seu escolha:"))
            if number <= 0 or number > 7:
                print("Valor inválido!")
            else:
                break
        except ValueError:
            print("Valor inválido, tente de 1 - 7!")
        except TypeError:
            print("Tente novamente")
    if number == 1:
        print("Domingo")
    elif number == 2:
        print("Segunda")
    elif number == 3:
        print("Terça")
    elif number == 4:
        print("Quarta")
    elif number == 5:
        print("Quinta")
    elif number == 6:
        print("Sexta")
    elif number == 7:
        print("Sábado")
    else:
        print("Número inválido.")