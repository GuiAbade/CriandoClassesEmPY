# Valores aleatórios com random
import random

# print(random.random())  # Gera um valor de 0.0 a 1.0
# Gera um valor decimal de valor minimo a valor maximo
print(random.randint(4, 10))  # retora um valor inteiro aleatorio entre 4 e 10
cores = ['verde', 'vermelho', 'azul']
# A letra K serve para colocar a quantidade de itens que seseja selecionar de uma só vez
print(random.choices(cores, k=2))

# Embaralhar uma lista
baralho = ['carta1', 'carta2', 'carta3', 'carta4']  # Embaralhar uma lista
print(random.shuffle(baralho))
print(baralho)
