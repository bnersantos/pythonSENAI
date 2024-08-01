nota = 0
nota2 = 0

while True:
    while True:
        try:
            nota = float(input('Digite a primeira nota: '))
            if 0 < nota > 100:
                print("Valor inválido!")
            else:
                break
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("TypeError")
    while True:
        try:
            nota2 = float(input('Digite a segunda nota: '))
            if 0 < nota2 > 100:
                print("Valor inválido!")
            else:
                break
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("TypeError")
    soma = nota + nota2
    divisao = soma / 2
    if divisao >= 70:
        print(f"Você foi aprovado👍! Média do aluno foi: {divisao}".format(divisao))
    else:
        print(f"Você foi reprovado👎! Média do aluno foi: {divisao}".format(divisao))