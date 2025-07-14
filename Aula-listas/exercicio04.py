# --------------------
# 4. Removendo Duplicatas
# --------------------
# Dada a lista numeros = [1, 2, 3, 2, 4, 5, 5, 6]
# crie um programa que gere uma nova lista contendo apenas os elementos únicos da lista original, sem repetições.
# A ordem dos elementos na nova lista não importa.
# * Dica: Considere usar um laço 'for' e verificar se o elemento já existe na nova lista antes de adicioná-lo.

numeros = [1, 2, 3, 2, 4, 5, 5, 6]

for i in numeros:
    if len(numeros[i]) == numeros(i):
        numeros.remove(i)
    print(numeros)