# Conversor de temperatura:
# Menu:
def menu_conversor():
    print("MENU:")
    print("[0] SAIR")
    print("[1] Celsius -> Kelvin")
    print("[2] Celsius -> Fahrenheit")
    while True:
        try:
            opcao = int(input("Digite a opção escolhida:"))
            if opcao not in [1, 2]:
                print(f"Opção Inválida!")
            else:
                return opcao
        except ValueError:
            print(f"Valor Inválido, tente novamente!")
        except TypeError:
            print(f"Valor Inválido, tente novamente!")



def celsius_kelvin():
    while True:
        try:
            celsius = float(input("Digite a temperatura em Celsius:"))
            kelvin = celsius + 273
            return kelvin
        except ValueError:
            print("Digite em formato de número!")
        except TypeError:
            print("Tente novamente")




def celsius_fahrenheit():
    while True:
        try:
            celsius = float(input("Digite a temperatura em Celsius:"))
            c_x_1_8 = celsius * 1.8
            fahrenheit = c_x_1_8 + 32
            return fahrenheit
        except ValueError:
            print("Digite em formato de número!")
        except TypeError:
            print("Tente novamente!")



opcao = 1
while True:
    opcao = menu_conversor()
    while opcao != 0:
        if opcao == 1:
            print(f"O resultado é: {celsius_kelvin()}")
        elif opcao == 2:
            print(f"O resultado é: {celsius_fahrenheit()}")
        else:
            break

