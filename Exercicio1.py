'''
Crie um programa que recebe um número e imprime o seu fatorial

#Método 5Q's para montar um algorítimo:
(Tente explicar esse problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender totalmente o problema.)

1. Quais são os dados de entradas necessários?
  - Número
2. O que devo fazer com esses dados?
  - Devo calcular o fatorial do número que for assado para o meu programa e o exibir na tela.
3. Quais são as restrições deste problema?
  - O número deve eve ser um valor positivo
  - O número deve ser um valor inteiro
4. Qual é o resultado esperado?
  - Resultado esperado é queo fatorial do número providênciado seja exibido.
5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado?
  input numero
  if numero > 0
  if numero = inteiro

  fatorial = 1
  loop de 1 a numero
      fatorial = fatorial * numero
  print(fatorial)
'''

numero = int(input('Digite um número'))
if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item
    print(fatorial)
