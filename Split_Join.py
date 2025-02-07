frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'jhonatan, rafael, carol, amanda, jefferson'
print(frase.split())
print(frase.split(','))
hashtags = 'music #guitar #gamer #coder #puthon'
print(frase.split())
print(frase.split('#'))
print(frase.split('#', 3))
# Como concatenar (combinar) strings
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))
