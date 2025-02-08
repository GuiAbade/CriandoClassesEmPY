from datetime import datetime

print(datetime.now())       # Inprimindo data de hoje
print(datetime.now().day)   # Imprimindo o dia de hoje
print(datetime.now().month)  # Inprimindo o mês
print(datetime.now().year)  # Inprimindo o ano

# Criando data
lançamento_app = datetime(2021, 5, 28)
print(lançamento_app)
# Quero receber a data de lançamento do meu app
data_de_lancamento = datetime.strptime(
    input('Quando devemos lançar esse app: '), '%d/%m/%Y')
print(type(data_de_lancamento))

# '%d/%m/%Y' = Serve para converter para o formato que usamos no Brasil
# Calciçar o intervalo entre datas
data_atual = datetime.now()
aniversario = datetime(2025, 7, 13)
prazo = aniversario - data_atual + 1
print(prazo.days)
