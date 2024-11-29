import random
number_aleatorio = random.randint(0, 5)
play_again = 0
opcao = 0
# Menu
while True:
    print("Menu Principal:\n")
    print("Bem vindo(a) a Par ou Ímpar")
    print("[1] Iniciar Jogo 😁")
    print("\n[2] Sair do Jogo😢")
    while True:
        try:
            opcao = int(input("\nDigite sua opcao: "))
            if opcao in [1, 2]:
                break
            else:
                print("Opção Inválida digite uma de 1 - 2.")
        except TypeError:
            print("valor inválido, tente 1 ou 2.")
        except ValueError:
            print("valor inválido, tente 1 ou 2.")

    while True:
        if opcao == 1:
            print("Jogo iniciado com sucesso😊.")
            while True:
                try:
                    par_impar = int(input("\nPar[1] ou Impar[2]: "))
                    if par_impar in [1 , 2]:
                        break
                    else:
                        print("Opção Inválida! Tente novamente opções de 1 ou 2..")
                except TypeError:
                    print("Valor inválido, tente 1 ou 2.")
                except ValueError:
                    print("Valor inválido, tente 1 ou 2.")

            while True:
                try:
                    numero_escolhido = int(input("\nDigite um número entre 1 e 5: "))
                    if numero_escolhido >= 0 and numero_escolhido <= 5:
                        break
                    else:
                        print("Número inválido, tente de 1 - 5.")
                except TypeError:
                    print("Valor invalido, tente de 1 a 5.")
                except ValueError:
                    print("Valor inválido, tente 1 a 5.")

            if par_impar == 1:
                print("Jogada Par!")

                soma = numero_escolhido + number_aleatorio
                resto = soma % 2
                if resto == 0:
                    print(f"Você venceu!Soma: {soma}😁")
                else:
                    print(f"Você perdeu!Soma: {soma}😢")

            elif par_impar == 2:
                print("Jogada Impar!")
                soma = numero_escolhido + number_aleatorio
                resto = soma % 2
                if resto == 0:
                    print(f"Você perdeu!Soma: {soma}😢")
                else:
                    print(f"Você ganhou!Soma: {soma}😁")

            while True:
                try:
                    play_again = int(input("Deseja jogar novamente? SIM [2] / NÃO [1]: ").lower())
                    if play_again == 1:
                        print("Te esperamos na próxima!😢")
                        break
                    elif play_again == 2:
                        number_aletorio = random.randint(1, 5)
                        break
                    elif play_again != 1 and 2:
                        print("Opção inválida! Digite '2' para jogar novamente ou '1' para sair.")
                    else:
                        raise TypeError
                except TypeError:
                    print("Opção Inválida. Tente 1 ou 2!")
                except ValueError:
                    print("Opção Inválida. Tente 1 ou 2!")

            if play_again == 1:
                break

        elif opcao == 2:
            print("Te esperamos na próxima😘")
            break

        else:
            print("Opcao invalida!")

    if play_again == 1:
        break
