while True:
    try:
        number = float(input("Digite o número: "))
        if number > 0:
            print(f"{number} é positivo!👍")
        elif number < 0:
            print(f"{number} é negativo!👎")
        else:
            print("Seu número é = a zero, portanto neutro👉👈.")
    except ValueError:
        print("Valor inválido, tente novamente!.")

