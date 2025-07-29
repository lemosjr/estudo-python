# 2. Verificador de Aprovação Escolar
print("\n--- Exercício 2: Aprovação Escolar ---")
nota = float(input("Digite a nota do aluno (0-10): "))
if nota >= 7.0:
    print("Aprovado!")
elif nota >= 5.0: # Não precisa verificar se é < 7, pois isso já foi tratado pelo if
    print("Em Recuperação.")
else:
    print("Reprovado.")
