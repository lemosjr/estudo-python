# Exercício 7: Tuplas como Chaves de Dicionário
# Crie um dicionário chamado estoque onde as chaves são tuplas (produto, tamanho) e os valores são a quantidade em estoque.
# Adicione os seguintes itens ao dicionário:

# ('Camiseta', 'M'): 15

# ('Calça', '42'): 10

# ('Camiseta', 'G'): 12

# ('Tênis', '40'): 8
# Por fim, imprima a quantidade de camisetas tamanho 'M' em estoque, acessando o valor através da chave ('Camiseta', 'M').

estoque = {
    ('Camiseta', 'M'): 15,
    ('Calça', '42'): 10,
    ('Camiseta', 'G'): 12,
    ('Tênis', '40'): 8,
}
chave_busca = ('Camiseta', 'M')
print(f"Estoque de {chave_busca[0]} tamanho '{chave_busca[1]}': {estoque[chave_busca]}\n")

