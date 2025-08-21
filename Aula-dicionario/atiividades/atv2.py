# Atividade 2: Atualizando Inventário

# Enunciado: Você tem um dicionário que representa o estoque de uma pequena loja de eletrônicos.

# Python
# estoque = {"Smartphones": 30, "Notebooks": 15, "Fones de Ouvido": 50}
# Adicione um novo produto: "Teclados", com 25 unidades em estoque.

# Atualize a quantidade de "Smartphones" para 25, pois 5 foram vendidos.

# Imprima o dicionário final.

# Dica: Para adicionar, use a sintaxe dicionario['nova_chave'] = valor. Para atualizar, use a mesma sintaxe com uma chave que já existe.

# Resultado Esperado:

# {'Smartphones': 25, 'Notebooks': 15, 'Fones de Ouvido': 50, 'Teclados': 25}

estoque = {"Smartphones": 30, "Notebooks": 15, "Fones de Ouvido": 50}
estoque['Teclados'] = 25
estoque['Smartphones'] = 25
print(estoque)

