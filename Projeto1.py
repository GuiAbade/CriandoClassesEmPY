from datetime import datetime
import random

print('-------------Olá, ben-vindo(a) a nossa empresa-------------')
nome = input('Qual o seu nome?')
idade = int(input('Qual sua idade? '))
data_do_cadastro = datetime.today().strftime('%d/%m/%Y')
cartoes = ['R$ 50,00', 'R$250,00', 'R$120,00']
cartoes = random.choices(cartoes)
aniversario = datetime.strptime(
    input('Digite sua data de aniversário no formado dd/mm/aaaa: '),
    '%d/%m/%Y')

print(f'Olá {nome} seu registro foi concluido com sucesso no dia {data_do_cadastro}. \n'
      f'Parabéns!! houve um sorteio e você ganhou um cartão de compras no valor de {cartoes}')
