import random

number_aletorio = random.randint(1, 100)
tentativas = 0
play_again = 0
opcao = 0

while opcao != 2:
    # Menu
    print("\nMenu Principal:\n")
    print("Bem-vindo(a) ao Guessing game")
    print("[1] Iniciar Jogo😁")
    print("[2] Sair do Jogo😢")
    # Tratamento da variável
    try:
        # Escolha do usuário
        opcao = int(input("Selecione sua escolha desejada: "))
        if opcao not in [1, 2]:
            print("Opção inválida! Digite 1 para iniciar o jogo ou 2 para sair.")
    except ValueError:
        print("Opção inválida! Digite um número válido.")
    except TypeError:
        print("Opção inválida! Digite um número válido.")

    if opcao == 1:
        name_user = input("Digite o nome do Usuário: ")
        print(f"\nBem-vindo(a), {name_user}! Esperamos que sua experiência supere as expectativas!")

        while True:
            while True:
                try:
                    number_escolhido = int(input("Digite o número escolhido para a tentativa de acerto: "))
                    if number_escolhido < 1 or number_escolhido > 100:
                        print("Digite um número de 1 - 100.")
                    else:
                        break
                except ValueError:
                    print("Digite um número válido.")
                except TypeError:
                    print("Digite um número válido.")

            tentativas += 1

            if number_escolhido == number_aletorio:
                print(f"Parabéns, você acaba de acertar o número em {tentativas} tentativas!😁")
                while True:
                    try:
                        play_again = int(input("Deseja jogar novamente? [2] SIM / [1] NÃO: ").lower())
                        if play_again == 1:
                            print("Te esperamos na próxima!😢")
                            break
                        elif play_again == 2:
                            number_aletorio = random.randint(1, 100)
                            tentativas = 0
                            break
                        elif play_again != 1 and 2:
                            print("Opção inválida! Digite '2' para jogar novamente ou '1' para sair.")
                        else:
                            raise TypeError
                    except TypeError:
                        print("Opção Inválida. Tente 1 ou 2!")
                    except ValueError:
                        print("Opção Inválida. Tente 1 ou 2!")

            elif number_escolhido > number_aletorio:
                print("Seu número é maior que o número sorteado😉.")

            elif number_escolhido < number_aletorio:
                print("Seu número é menor que o número sorteado😎.")

            if play_again == 1:
                opcao = 2
                break

    elif opcao == 2:
        print("Te esperamos na próxima😢!")
    else:
        print("Opção inválida! Digite 1 para iniciar o jogo ou 2 para sair.")





