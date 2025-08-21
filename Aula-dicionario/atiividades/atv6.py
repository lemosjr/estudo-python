#  Atividade 6 : Cadastro de Alunos e Notas

# Enunciado: Crie um dicionário aninhado para armazenar as notas de alunos.
# A estrutura deve ser: a chave principal é o nome do aluno, e o valor é outro dicionário contendo as chaves matematica,
#  portugues e ciencias, com suas respectivas notas (uma lista de 2 notas para cada matéria).

# Python

#  Estrutura Exemplo
# {'Ana': {'matematica': [8, 9], 'portugues': [7, 8], 'ciencias': [9, 10]}}

# Seu programa deve calcular e imprimir a média de um aluno específico em uma matéria específica.
# Por exemplo, a média de 'João' em 'matemática'.

# Dica: Para acessar um valor aninhado, use múltiplos colchetes: boletim['Joao']['matematica'].
# Para calcular a média, some os elementos da lista e divida pelo tamanho dela (len()).

# Resultado Esperado (para o aluno João e a matéria matemática com notas [9, 10]):

# A media de Joao em matematica e: 9.5

notas_alunos = {
    'Joao': {'matematica': [9, 10], 'portugues': [8, 7], 'ciencias': [10, 9]},
    'Ana': {'matematica': [8, 9], 'portugues': [7, 8], 'ciencias': [9, 10]}
}

aluno = 'Joao'
materia = 'matematica'

media = sum(notas_alunos[aluno][materia]) / len(notas_alunos[aluno][materia])
print(f"A media de {aluno} em {materia} e: {media}")
