# Exercício 8: Ordenando uma Lista de Tuplas
# Você tem uma lista de tuplas representando alunos e suas notas finais:
# alunos_notas = [('Carlos', 8.5), ('Ana', 9.5), ('Beatriz', 7.0), ('Daniel', 8.0)]
# Escreva um código para ordenar essa lista em ordem decrescente com base na nota do aluno (o segundo item da tupla).
# Imprima a lista ordenada.

# Dica: Pesquise sobre o parâmetro key da função sorted() ou do método .sort() e o uso de funções lambda.

alunos_notas = [('Carlos', 8.5), ('Ana', 9.5), ('Beatriz', 7.0), ('Daniel', 8.0)]
# Usamos uma função lambda para dizer ao sorted() que deve usar o segundo elemento (índice 1) para ordenar
# O reverse=True faz a ordenação ser decrescente
lista_ordenada = sorted(alunos_notas, key=lambda aluno: aluno[1], reverse=True)
print(f"Alunos ordenados por nota (decrescente): {lista_ordenada}\n")