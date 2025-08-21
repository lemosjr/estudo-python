# Atividade 1 : Informações Pessoais

# Enunciado: Crie um dicionário para armazenar informações sobre um livro.
# Ele deve conter as seguintes chaves: titulo, autor, ano_publicacao e genero.
# Em seguida, imprima o valor de cada uma das chaves no formato "Chave: Valor".

# Dica: Crie o dicionário primeiro e depois use a função print() para cada par chave-valor.

# Resultado Esperado (Exemplo):

# Titulo: Cem Anos de Solidão
# Autor: Gabriel García Márquez
# Ano de Publicacao: 1967
# Genero: Realismo Mágico

livro = {
    "titulo": "Cem Anos de Solidão",
    "autor": "Gabriel García Márquez",
    "ano_publicacao": 1967,
    "genero": "Realismo Mágico"
}

for chave, valor in livro.items():
    print(f"{chave.capitalize()}: {valor}")