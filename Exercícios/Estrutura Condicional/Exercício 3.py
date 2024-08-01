while True:
    while True:
        try:
            ano = int(input("Digite o ano de nascimento:"))
            if ano >= 2025:
                print("Ano de nascimento inválido!")
            else:
                break
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")
    idade = 2024 - ano
    if idade >= 18 and idade <= 59:
      print(f"Sua idade é: {idade} e sua faixa etária é ADULTO👨👩/.")
    elif idade < 18 and idade >= 11:
      print(f"Sua idade é: {idade} e sua faixa etária é ADOLESCENTE🧑/👱‍♀️.")
    elif idade <= 10:
      print(f"Sua idade é: {idade} e sua faixa etária é CRIANÇA🧒/👧.")
    else:
      print(f"Sua idade é: {idade} e sua faixa etária é IDOSO👴/👵.")
    