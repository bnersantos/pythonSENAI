import datetime

name_user = ""
while True:
    def saudacao():
        agr = datetime.datetime.now()
        msg = ""

        if (agr.hour < 12):
            msg = "Bom dia"
        elif (agr.hour < 19):
            msg = "Boa tarde"
        else:
            msg = "Boa noite", agr.hour
        return msg


    name_user = str(input("Digite o nome de usuário: "))
    temp = datetime.datetime.now()


    def mes():
        tempo = datetime.datetime.now()
        mes_write = ""

        if (tempo.month == 1):
            mes_write = "Janeiro"
        elif (tempo.month == 2):
            mes_write = "Fevereiro"
        elif (tempo.month == 3):
            mes_write = 'Março'
        elif (tempo.month == 4):
            mes_write = 'Abril'
        elif (tempo.month == 5):
            mes_write = 'Maio'
        elif (tempo.month == 6):
            mes_write = 'Junho'
        elif (tempo.month == 7):
            mes_write = 'Julho'
        elif (tempo.month == 8):
            mes_write = 'Agosto'
        elif (tempo.month == 9):
            mes_write = 'Septo'
        elif (tempo.month == 10):
            mes_write = 'Outubro'
        elif (tempo.month == 11):
            mes_write = 'Novembro'
        else:
            mes_write = 'Dezembro'
        return mes_write


    print(f"{saudacao()} {name_user}, agora são exatamente: {temp.hour}:{temp.minute} do dia {temp.day} do mês de {mes()} de {temp.year}")
