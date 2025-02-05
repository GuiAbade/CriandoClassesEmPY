# Exercicio 1
# Estrutura basica de função

# def eh_maior_de_idade():
# Exemplo de função que processa e não retorna
'''
idade = int(input('Digite sua idade: '))
  if idade >= 18:
    print('Você é maior de idade')
  else:
    print('Você é menor de idade')


eh_maior_de_idade()
'''
# Exercicio 2
# Crie um algoritmo que permite que maiores de idade entrem na festa
# Exemplo de função que processa e retorna
'''
def pode_entrar_na_festa():
  idade = int(input('Digite sua idade: '))
  if idade >= 18:
    return True
  else:
    return False

if pode_entrar_na_festa () == True:
  print('Bem-vindo(a), pode entrar na festa')
else:
  print('Você não pode entrar')
'''


# Exercicio 3

def eh_maior_de_idade(possui_cnh):
    idade = int(input('Digite sua idade: '))
    if idade >= 18 and possui_cnh == True:
        print('Você é maior de idade e pode dirigir')
    else:
        print('Você é menor de idade e não pde dirigir')


eh_maior_de_idade(possui_cnh=True)
