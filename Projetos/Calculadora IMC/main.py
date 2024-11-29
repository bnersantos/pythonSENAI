def input_peso():
    while True:
        try:
            peso = float(input("Digite o peso: "))
            return peso
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")
def input_altura():
    while True:
        try:
            altura = float(input('Digite sua altura: '))
            if altura < 2.5 and altura > 1.0:
                return altura
            else:
                print("Digite a altura utilizando '.'")
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")
def calcular(peso, altura):
    imc = peso / (altura * altura)
    return imc
def class_imc(imc):
    msg = ""
    if imc  < 18.5:
        msg = "Abaixo do peso"
    elif imc <= 24.9:
        msg = "Peso ideal"
    elif imc <= 29.9:
        msg = "Sobrepeso"
    elif imc <= 39.9:
        msg = "Obesidade"
    else:
        msg = "Obesidade grave"
    return msg

peso = input_peso()
altura = input_altura()
imc = calcular(peso, altura)
imc_class = class_imc(imc)
print(f" {imc:.2f} {imc_class} ")