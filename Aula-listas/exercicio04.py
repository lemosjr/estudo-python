# --------------------
# 4. Removendo Duplicatas
# --------------------
# Dada a lista numeros = [1, 2, 3, 2, 4, 5, 5, 6]
# crie um programa que gere uma nova lista contendo apenas os elementos únicos da lista original, sem repetições.
# A ordem dos elementos na nova lista não importa.
# * Dica: Considere usar um laço 'for' e verificar se o elemento já existe na nova lista antes de adicioná-lo.

numeros = [1, 2, 3, 2, 4, 5, 5, 6]
numeros_unicos = [] # Passo 1: Comece com uma lista vazia para elementos únicos

for numero in numeros: # Passo 2: Percorra a lista original
    if numero not in numeros_unicos: # Passo 3: Verifique se o elemento já está na nossa lista de únicos
        numeros_unicos.append(numero) # Passo 4: Se não estiver, adicione-o

print(numeros_unicos)

    