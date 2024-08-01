while True:
    while True:
        try:
            number = float(input("Digite o primeiro número:"))
            if number < 0:
                print("Seu número é menor que zero!")
            else:
                break
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")
    while True:
        try:
            number1 = float(input("Digite o segundo número:"))
            if number1 < 0:
                print("Seu número é menor que zero!")
            else:
                break
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")
    while True:
        try:
            number2 = float(input("Digite o terceiro número:"))
            if number2 < 0:
                print("Seu número é menor que zero!")
            else:
                break
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")
    if number1 < number > number2:
        print(f"O número {number} é o maior.")
    elif number < number1 > number2:
        print(f"O número {number1} é o maior.")
    elif number < number2 > number1:
        print(f"O número {number2} é o maior.")
    elif number1 == number2 and number < number1 and number2:
        print(f"Os números {number1} e {number2} são maiores.")
    elif number == number1 and number2 < number and number1:
        print(f"Os números {number} e {number1} são maiores.")
    elif number == number2 and number1 < number and number2:
        print(f"Os números {number} e {number2} são maiores.")

    else:
        print("Os número são iguais.")