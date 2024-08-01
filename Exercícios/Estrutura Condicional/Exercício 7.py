while True:
    while True:
        try:
            numero = int(input("Digite o número de sua escolha: "))
            if numero < 0 or numero > 12:
                print("Número inválido, tente de 1-12!")
            else:
                break
        except ValueError:
            print("Valor inválido")
        except TypeError:
            print("Tente novamente")
    if numero == 1:
        mes = 'Janeiro'
    elif numero == 2:
        mes = 'Fevereiro'
    elif numero == 3:
        mes = 'Março'
    elif numero == 4:
        mes = 'Abril'
    elif numero == 5:
        mes = 'Maio'
    elif numero == 6:
        mes = 'Junho'
    elif numero == 7:
        mes = 'Julho'
    elif numero == 8:
        mes = 'Agosto'
    elif numero == 9:
        mes = 'Setembro'
    elif numero == 10:
        mes = 'Outubro'
    elif numero == 11:
        mes = 'Novembro'
    else:
        mes = 'Dezembro'
    print(f"O número {numero}, corresponde ao {mes}")