# Transforme o codigo abaixo em uma classe:
# Classe Artista

nome_do_artista = 'Artista'
genero_de_musica = 'rock'
albuns = ['Album 1', 'Album 2', 'Album 3']


class Artista():
    def __init__(self, nome_do_artista, genero_de_musica, albuns):
        self.nome_do_artista = nome_do_artista
        self.genero_de_musica = genero_de_musica
        self.albuns = albuns

    # Função adicionar albuns
    def adicionar_albuns(self, nome_album):
        self.albuns.append(nome_album)
        print(f'Foi adicionado um album chamado de {nome_album}')

    # Função de listar albuns
    def listar_albuns(self):
        for album in self.albuns:
            print(album)


artista1 = Artista('Artista 1', 'rock', ['Album 1', 'Album 2', 'Album 3'])
artista1.adicionar_albuns('O melhor do Rock')
artista1.listar_albuns()
