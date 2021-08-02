class Funcionario:
    def __init__(self, nome, horas):
        self.nome = nome
        self.horas = horas

    def registra_horas(self, horas):
        print('Horas registradas...')
        self.horas += horas

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


# mixin
class Hipster:
    def __str__(self):
        return f"Hipster, {self.nome}"


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior("Jose", 7)
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

luan = Pleno("Luan", 8)
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

luan = Senior("Luan", 10)
print(luan)

# mixins são casos em que eu não a instâncie, mas somente herde dela os seus comportamentos. se quiser,
# dependendo somente dos atributos da classe, é uma boa prática não instância-la.

# Sempre na herança multipla, o objeto procurará a implementação ou nele, ou no ancestral, mas sempre indo até o
# ancestral para depois passar para o proximo das classes herdadas se não achar a implementação de imediato ou,
# se caso da primeira hierarquia não tiver o método, e houver duplicatas de heranças (funcionario > caelum >
# funcionario), então ele removerá pois não considera uma boa cabeça para usar o método, então ele passa para a outra
# subclasse.
