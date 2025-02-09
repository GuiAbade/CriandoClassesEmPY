import random

# Jogo de cara ou coroa
moeda = ['cara', 'coroa']
print(random.choices(moeda))
print('------------------------')
# Sorteio lista de nomes
nome = ['Guilherme', 'João', 'Maria', 'Gabriela', 'Bruna']
print(random.choices(nome))

# Escolher um valor aleatorio entre 10 e 100

print(random.randint(10, 100))
