#Faixa de Renda Anual Bruta                           Alíquota
#Até R$ 56.072,00                                     0%
#De R$ 56.072,01 a R$ 238.532,00                     7,50%
#De R$ 238.532,01 a R$ 522.400,00                    15%
#De R$ 522.400,01 a R$ 987.600,00                    22,50%
#Acima de R$ 987.600,00                              27,50%
while True:
    while True:
        try:
            renda = float(input("Digite o valor da renda: "))
            if renda < 0:
                print("Renda inválida, tente novamente!")
            else:
                break
        except ValueError:
            print("Valor inválido")
        except TypeError:
            print("Tente novamente")
    if renda <= 56072:
        print(f"Sua Renda não haverá descontos! Sendo assim R${renda:.2f}, o desconto é = 0.")
    elif renda <= 238532:
        desconto = renda * 0.075
        print(f"Sua Renda é R${renda:.2f}, o desconto é R${desconto:.2f}.")
    elif renda <= 522400:
        desconto = renda * 0.15
        renda_total = renda - desconto
        print(f"Sua Renda é R${renda:.2f}, o desconto é R${desconto:.2f}.")
    elif renda <= 987600:
        desconto = renda * 0.0225
        print(f"Sua Renda é R${renda:.2f}, o desconto é R${desconto:.2f}.")
    else:
        desconto = renda * 0.0275
        print(f"Sua Renda é R${renda:.2f}, o desconto é R${desconto:.2f}.")






