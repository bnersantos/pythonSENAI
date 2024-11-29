def lado_1():
    while True:
        try:
            _1lado = float(input("Digite o valor do primeiro lado: "))
            return _1lado
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")

def lado_2():
    while True:
        try:
            _2lado = float(input("Digite o valor do segundo lado: "))
            return _2lado
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")

def lado_3():
    while True:
        try:
            _3lado = float(input("Digite o valor do terceiro: "))
            return _3lado
        except ValueError:
            print("Valor inválido!")
        except TypeError:
            print("Tente novamente!")

def class_triang(_lado1, _lado2, _lado3):
    if _lado1 == _lado2 and _lado1 == _lado3 and _lado2 == _lado1:
        return 'equilátero'
    elif _lado1 != _lado2 and _lado2 != _lado3 and _lado1 != _lado3:
        return 'escaleno'
    else:
        return 'isóceles'

def exibir_mensagem(class_triang):
    print(f"O triângulo é {class_triang}")

_lado1 = lado_1,()
_lado2 = lado_2()
_lado3 = lado_3()
class_triangulos = class_triang(_lado1, _lado2, _lado3)
exibir_mensagem(class_triang(_lado1, _lado2, _lado3))
