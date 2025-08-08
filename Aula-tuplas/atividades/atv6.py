# Exercício 6: Tuplas em Listas
# Você tem uma lista de tuplas, onde cada tupla contém o nome de um produto e seu preço:
# produtos = [('Maçã', 5.50), ('Banana', 4.75), ('Leite', 6.00), ('Pão', 8.50), ('Queijo', 25.00)]
# Escreva um código que percorra essa lista e imprima apenas os nomes dos produtos que custam mais de R$ 5,00.

produtos = [('Maçã', 5.50), ('Banana', 4.75), ('Leite', 6.00), ('Pão', 8.50), ('Queijo', 25.00)]
print("Produtos que custam mais de R$ 5,00:")
for produto, preco in produtos: # Desempacotamento direto no for
  if preco > 5.00:
    print(produto)
print("") # Linha em branco para separar