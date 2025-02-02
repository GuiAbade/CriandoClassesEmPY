# CamelCase
class Radar:

    def __init__(self, velocidade_maxima, multa_leve, multa_grave,
                 multa_gravissima):
        self.velocidade_maxima = velocidade_maxima
        self.multa_leve = multa_leve
        self.multa_grave = multa_grave
        self.multa_gravissima = multa_gravissima

    # A função deve exibir o valor da multa que será aplicada de acordo com a gravidade
    def obter_valor_multa(self, nivel_multa):
        if nivel_multa == 'Multa Leve':
            print(f'O valor da multa é R${self.multa_leve}')
        elif nivel_multa == 'Multa Grave':
            print(f'O valor da multa é R${self.multa_grave}')
        else:
            print(f'O valor da multa é de R${self.multa_gravissima}')

    def calcular_multa(self, velocidade):
        if velocidade <= self.velocidade_maxima:
            print('Nao levou multa')

        elif velocidade > self.velocidade_maxima and velocidade <= self.velocidade_maxima + 10:
            print('Levou multa leve')

        elif velocidade >= self.velocidade_maxima + 11 and velocidade <= self.velocidade_maxima + 20:
            print('Levou multa grave')

        elif velocidade > self.velocidade_maxima + 20:
            print('Levou multa gravissima')

    def aplicar_penalizacao_carteira(self, nivel_multa):
        if nivel_multa == 'Multa leve':
            print('Perdeu 3 pontos na carteira')

        elif nivel_multa == 'Multa grave':
            print('Perdeu 5 pontos na carteira')

        else:
            print('Perdeu 7 pontos na carteira')


radar1 = Radar(velocidade_maxima=100,
               multa_leve=180,
               multa_grave=550,
               multa_gravissima=1500)
# print(radar1.velocidade_maxima)
# radar1.obter_valor_multa('Multa Grave')
# radar1.calcular_multa(200)
radar1.aplicar_penalizacao_carteira('Multa Grave')


'''
radar1 = Radar(velocidade_maxima=100, multa_leve= 180, multa_grave= 550, multa_gravissima=1500)
print(radar1.velocidade_maxima)
print(radar1.multa_leve)
print(radar1.multa_grave)
print(radar1.multa_gravissima)

radar2 = Radar(velocidade_maxima=120, multa_leve= 200, multa_grave= 300, multa_gravissima=500)
print(radar2.velocidade_maxima)
print(radar2.multa_leve)
print(radar2.multa_grave)
print(radar2.multa_gravissima)

'''
