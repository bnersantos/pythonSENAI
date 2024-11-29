from utils import *

acoes = {
    "nome": "",
    "valor": "0",
    "quantidade": "0",
}
lista_acoes = []

while True:
    escolha = menu()
    if escolha == 1:
        print("Você selecionou adicionar valores e ações!")
        acoes['nome'] = receber_da_acao()
        acoes['valor'] = receber_valor()
        acoes['quantidade'] = receber_quantidade()
        lista_acoes.append(acoes.copy())
    elif escolha == 2:
        for acao in lista_acoes:
            print(acao)
    elif escolha == 3:
        print("Você desejou sair!")
        break


