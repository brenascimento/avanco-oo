# Quero fazer objetos de filme, e séries para uma playlist
# Filmes: nome do filme, ano, duração
# Series: nome da série, ano, temporada
# Terá um sistema de likes
# Os atributos precisam ser protegidos, ou até privados


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1
        return self._likes

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def likes(self):
        return self._likes

    def imprime(self):
        print(f"{self.nome} - {self.ano} - {self.likes} Likes")


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.duracao} Minutos - {self.likes} Likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f"{self.nome} - {self.temporada} Temporadas - {self.likes} Likes"





homem_aranha = Filme("Homem Aranha - longe de casa", 2018, 160)
pinky_blinders = Serie("Pinky Blinders", 2020, 1)


homem_aranha.dar_like()
pinky_blinders.dar_like()
pinky_blinders.dar_like()
print(homem_aranha)
print(pinky_blinders)
