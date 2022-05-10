"""

Desafio Média Aluno

Classe aluno possui os atributos
    Nome    --> Str
    Status  --> Aprovado ou não aprovado (Bool)
    Nota1   --> float
    Nota2   --> float
    Media   --> float

Tambem possui os metodos:
    mostrar_informacoes --> Fala o nome do aluno e se ele foi aprovado ou não.
    calcular_media --> Calcula e retorna a media do aluno
    inserir_nota --> Adiciona valor nas notdas do aluno

Regras:
    Para passar é preciso de 6 ou mais
    Nome será enviado no construtor.
    Nota1 e Nota2 serão enviadas por parametro.

"""

class Aluno(object):

    status = False
    entry = False
    nota1 = 0
    nota2 = 0
    nome = "null"

    def mostrar_informacoes(self):
        if (self.status) and (self.nome):
            print("Media do aluno\n\tNome:", self.nome, "\n\tMédia:", self.media, "\n\tStatus: Aprovado!\n\n")
        elif self.entry and not self.status:
            print("Media do aluno\n\tNome:", self.nome, "\n\tMédia:", self.media, "\n\tStatus: Reprovado\n\n")
        else:
            print("!!!Por Favor, entre com as notas do aluno primeiro!!!")

    def calcular_media(self):
        self.media = ( self.nota1 + self.nota2 ) / 2
        if (self.media >= 6):
            self.status = True

    def inserir_nota(self, nome, nota1, nota2):
        self.nome = nome
        self.entry = True
        self.nota1 = nota1
        self.nota2 = nota2

alberto = Aluno()
beatriz = Aluno()
carlos = Aluno()

alberto.inserir_nota("Alberto", 9, 8)
beatriz.inserir_nota("Beatriz", 4, 7)

alberto.calcular_media()
beatriz.calcular_media()

alberto.mostrar_informacoes()
beatriz.mostrar_informacoes()
carlos.mostrar_informacoes()
