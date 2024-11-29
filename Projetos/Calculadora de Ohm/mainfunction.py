from utils import *


while True:
    escolha = menu()
    if escolha == 1:
        exibir_resistencia(calculadora_resistencia())
    elif escolha == 2:
        exibir_resistencia(calculadora_corrente_eletrica())
    elif escolha == 3:
        exibir_resistencia(calculadora_tensao_eletrica())
    elif escolha == 4:
        exibir_resistentia_resistor(calculadora_resistencia_resistor())
    else:
        print("Até a próxima!")
        break


