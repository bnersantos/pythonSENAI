import datetime

temp = datetime.datetime.now()

# Solicitar nome ao usuário
def solicita_nome():
    nome = input('Digite seu nome: ')
    return nome

# Saudação
def saudacao():
    agr = datetime.datetime.now()
    msg = ""
    if (agr.hour < 5):
        msg = "Boa madrugada"
    if (agr.hour < 12):
        msg = "Bom dia"
    elif (agr.hour < 19):
        msg = "Boa tarde"
    else:
        msg = "Boa noite", agr.hour
    return msg

# Printar o resultado
print(
    f"{saudacao()} {solicita_nome()}, agora são exatamente: {temp.hour}:{temp.minute} do dia {temp.day} do mês  {temp.month} de {temp.year}")
