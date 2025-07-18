# --------------------
# 10. Filtrando Nomes
# --------------------
# Dada a lista de nomes nomes = ["Ana", "Carlos", "Beatriz", "Daniel", "Amanda"],
# crie uma nova lista contendo apenas os nomes que começam com a letra 'A'. Use LIST COMPREHENSION para fazer isso.
# * Dica: Strings em Python podem ser tratadas como listas de caracteres. nome[0] lhe dará a primeira letra.

nomes = ["Ana", "Carlos", "Beatriz", "Daniel", "Amanda"]
nomes_com_a = [nome for nome in nomes if nome[0] == 'A']
print(nomes_com_a)
