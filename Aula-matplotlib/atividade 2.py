#2. Sistema de alunos
#Uma instituição quer cadastrar alunos.
#• Cada aluno tem nome, curso e notas.
#• Deve ser possível adicionar notas e calcular a média do aluno.
#Questão:
#Implemente uma classe Aluno que permita registrar notas e calcular a média final.
#Teste criando pelo menos dois alunos com notas diferentes.

class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        self.notas = []  

    def adicionar_nota(self, nota):
        """Adiciona uma nova nota à lista de notas do aluno."""
        self.notas.append(nota)
        print(f"Nota {nota} adicionada para o(a) aluno(a) {self.nome}.")

    def calcular_media(self):
        """Calcula a média das notas do aluno."""
        if not self.notas:
            return 0 
        total_notas = sum(self.notas)
        media = total_notas / len(self.notas)
        return media

aluno1 = Aluno("João Silva", "Engenharia de Software")
print(f"Aluno: {aluno1.nome}, Curso: {aluno1.curso}")

aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(7.0)
aluno1.adicionar_nota(9.2)

media_aluno1 = aluno1.calcular_media()
print(f"Notas de {aluno1.nome}: {aluno1.notas}")
print(f"Média final de {aluno1.nome}: {media_aluno1:.2f}\n")

aluno2 = Aluno("Maria Oliveira", "Análise e Desenvolvimento de Sistemas")
print(f"Aluno: {aluno2.nome}, Curso: {aluno2.curso}")

aluno2.adicionar_nota(6.5)
aluno2.adicionar_nota(8.0)

media_aluno2 = aluno2.calcular_media()
print(f"Notas de {aluno2.nome}: {aluno2.notas}")
print(f"Média final de {aluno2.nome}: {media_aluno2:.2f}")