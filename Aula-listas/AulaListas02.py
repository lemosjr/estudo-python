######################### Modificando Listas ###########################
# Como são mutáveis, as listas podem ser alteradas de várias formas.

# Alterando um Elemento
# Você pode substituir um elemento acessando-o pelo seu índice.

frutas = ["maçã", "banana", "laranja"]
print(f"Antes: {frutas}")
frutas[1] = "morango"  # Substitui "banana" por "morango"
print(f"Depois: {frutas}") # Saída: ['maçã', 'morango', 'laranja']

# Adicionando Elementos:

# append(item): Adiciona um item ao final da lista.

# insert(indice, item): Adiciona um item em uma posição específica.

# extend(outra_lista): Adiciona todos os itens de outra lista ao final da lista atual.

cores = ["vermelho", "verde"]
print(f"Início: {cores}")

# Adiciona ao final
cores.append("azul")
print(f"Após append('azul'): {cores}")  # Saída: ['vermelho', 'verde', 'azul']

# Insere na posição 1
cores.insert(1, "amarelo")
print(f"Após insert(1, 'amarelo'): {cores}") # Saída: ['vermelho', 'amarelo', 'verde', 'azul']

# Adiciona outra lista
cores_extras = ["preto", "branco"]
cores.extend(cores_extras)
print(f"Após extend(['preto', 'branco']): {cores}") # Saída: ['vermelho', 'amarelo', 'verde', 'azul', 'preto', 'branco']


# Removendo Elementos

# remove(valor): Remove a primeira ocorrência de um valor específico.

# pop(indice): Remove e retorna o item de um índice específico. Se o índice for omitido, remove e retorna o último item.

# del lista[indice]: Remove o item de um índice específico (não o retorna).

# clear(): Remove todos os itens da lista.

letras = ['a', 'b', 'c', 'd', 'b', 'e']
print(f"Início: {letras}")

# Remove pelo valor 'b' (só a primeira ocorrência)
letras.remove('b')
print(f"Após remove('b'): {letras}") # Saída: ['a', 'c', 'd', 'b', 'e']

# Remove e retorna o item do índice 2 ('d')
item_removido = letras.pop(2)
print(f"Item removido com pop(2): {item_removido}") # Saída: d
print(f"Lista após pop(2): {letras}") # Saída: ['a', 'c', 'b', 'e']

# Remove o último item
ultimo_item = letras.pop()
print(f"Item removido com pop(): {ultimo_item}") # Saída: e
print(f"Lista após pop(): {letras}") # Saída: ['a', 'c', 'b']

# Remove usando del
del letras[0]
print(f"Após del letras[0]: {letras}") # Saída: ['c', 'b']

# Limpa a lista
letras.clear()
print(f"Após clear(): {letras}") # Saída: []