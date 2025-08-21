# Atividade 4: Verificação de Aluno Aprovado

# Enunciado: Crie um dicionário para representar um aluno, contendo as chaves nome e nota.
# Em seguida, escreva um código que verifica se a nota do aluno é maior ou igual a 7.
# Se for, imprima "Aluno(a) [nome] foi aprovado(a)!". Caso contrário, imprima "Aluno(a) [nome] foi reprovado(a)".

# Dica: Use um if/else para checar o valor associado à chave nota.

# Resultado Esperado (se a nota for 8):

# Aluno(a) Maria foi aprovado(a)!

aluno = {
    "nome": "Maria",
    "nota": 8
}

if aluno["nota"] >= 7:
    print(f"Aluno(a) {aluno['nome']} foi aprovado(a)!")
else:
    print(f"Aluno(a) {aluno['nome']} foi reprovado(a).")

