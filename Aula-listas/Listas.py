# -*- coding: utf-8 -*-
"""
listas tutorial

Este arquivo serve como um guia completo e prático sobre Listas em Python.
Ele contém exemplos de código para criação, manipulação e uso de listas,
ideal para estudo e referência.

Pode ser colocado em um repositório Git como material de aprendizado.
"""

# --- 1. O que é uma Lista? ---
# Uma lista é uma coleção ordenada e mutável de itens.
# Pode armazenar diferentes tipos de dados e é definida por colchetes [].


# --- 2. Criando Listas ---
print("--- 2. Criando Listas ---")
lista_vazia = []
numeros = [1, 5, 8, 25]
nomes = ["Ana", "Bia", "Carlos"]
misturada = [10, "gato", True, 3.14]

print(f"Lista vazia: {lista_vazia}")
print(f"Lista de números: {numeros}")
print(f"Lista de nomes: {nomes}")
print(f"Lista misturada: {misturada}\n")


# --- 3. Acessando Elementos (Indexação) ---
# O primeiro elemento está no índice 0.
print("--- 3. Acessando Elementos (Indexação) ---")
frutas = ["maçã", "banana", "laranja"]

# Acessando por índice positivo (do início para o fim)
primeira_fruta = frutas[0]
segunda_fruta = frutas[1]
print(f"Primeira fruta (índice 0): {primeira_fruta}")  # Saída: maçã
print(f"Segunda fruta (índice 1): {segunda_fruta}")  # Saída: banana

# Acessando por índice negativo (do fim para o início)
ultima_fruta = frutas[-1]
penultima_fruta = frutas[-2]
print(f"Última fruta (índice -1): {ultima_fruta}")      # Saída: laranja
print(f"Penúltima fruta (índice -2): {penultima_fruta}\n")# Saída: banana


# --- 4. Fatiamento (Slicing) ---
# Pega um "pedaço" da lista usando a sintaxe: lista[início:fim:passo]
print("--- 4. Fatiamento (Slicing) ---")
numeros_seq = list(range(10)) # Cria uma lista de 0 a 9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista original para fatiar: {numeros_seq}")

# Exemplos de fatiamento
fatia_1 = numeros_seq[2:5]   # Do índice 2 ao 4
fatia_2 = numeros_seq[:4]    # Do início ao índice 3
fatia_3 = numeros_seq[5:]    # Do índice 5 ao final
fatia_4 = numeros_seq[::2]   # A lista toda, pulando de 2 em 2
fatia_5 = numeros_seq[::-1]  # Inverte a lista

print(f"Fatia de 2 a 5: {fatia_1}")    # Saída: [2, 3, 4]
print(f"Fatia do início ao 4: {fatia_2}") # Saída: [0, 1, 2, 3]
print(f"Fatia do 5 ao fim: {fatia_3}") # Saída: [5, 6, 7, 8, 9]
print(f"Fatia com passo 2: {fatia_4}") # Saída: [0, 2, 4, 6, 8]
print(f"Lista invertida: {fatia_5}\n") # Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# --- 5. Modificando Listas ---
print("--- 5. Modificando Listas ---")
personagens = ["Mario", "Luigi", "Peach"]
print(f"Lista inicial: {personagens}")

# Alterar um item
personagens[2] = "Yoshi"
print(f"Após alterar 'Peach' para 'Yoshi': {personagens}")

# Adicionar ao final com .append()
personagens.append("Toad")
print(f"Após append('Toad'): {personagens}")

# Adicionar em uma posição específica com .insert()
personagens.insert(1, "Wario")
print(f"Após insert('Wario', 1): {personagens}")

# Remover um item pelo valor com .remove()
personagens.remove("Wario")
print(f"Após remove('Wario'): {personagens}")

# Remover um item pelo índice com .pop()
item_removido = personagens.pop(1) # Remove 'Luigi'
print(f"Item removido com pop(1): '{item_removido}'. Lista atual: {personagens}")

# Remover com del
del personagens[0] # Deleta 'Mario'
print(f"Após del personagens[0]: {personagens}\n")


# --- 6. Funções e Métodos Úteis ---
print("--- 6. Funções e Métodos Úteis ---")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista para os exemplos: {nums}")

# len() - Tamanho da lista
print(f"Tamanho da lista (len): {len(nums)}")

# .count() - Contar ocorrências
print(f"Quantidade de vezes que o '1' aparece (count): {nums.count(1)}")

# .index() - Encontrar índice de um valor
print(f"Índice do valor '9' (index): {nums.index(9)}")

# .copy() - Criar uma cópia
nums_copia = nums.copy()
print(f"Cópia da lista (copy): {nums_copia}")

# .sort() - Ordenar a lista original (in-place)
nums.sort()
print(f"Lista ordenada (sort): {nums}")

# .reverse() - Inverter a lista original (in-place)
nums.reverse()
print(f"Lista invertida (reverse): {nums}")

# .clear() - Limpar a lista
nums_copia.clear()
print(f"Lista copiada após clear(): {nums_copia}\n")


# --- 7. List Comprehensions ---
# Sintaxe concisa para criar listas. Formato: [expressao for item in iteravel]
print("--- 7. List Comprehensions ---")

# Exemplo 1: Criar uma lista com o quadrado dos números de 0 a 9
quadrados = [x**2 for x in range(10)]
print(f"Quadrados de 0 a 9: {quadrados}")

# Exemplo 2: Criar uma lista apenas com números pares de outra lista
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in valores if num % 2 == 0]
print(f"Números pares da lista {valores}: {pares}")

# Exemplo 3: Converter uma lista de strings para maiúsculas
palavras = ["python", "é", "demais"]
maiusculas = [p.upper() for p in palavras]
print(f"Palavras em maiúsculas: {maiusculas}\n")

print("--- Fim do Tutorial ---")