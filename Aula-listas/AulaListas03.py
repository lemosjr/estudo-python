######################### Métodos Úteis para Listas #########################################

# len(lista) Retorna o número de elementos na lista.
# len([1, 2, 3]) # → 3

# lista.sort() Ordena a lista original (in-place).
# x = [3, 1, 2]; x.sort() # → x vira [1, 2, 3]

# sorted(lista) Retorna uma nova lista ordenada.
# x = [3, 1, 2]; y = sorted(x) # → y é [1, 2, 3], x continua [3, 1, 2]

# lista.reverse() Inverte a ordem dos elementos na lista original.
# x = [1, 2, 3]; x.reverse() # → x vira [3, 2, 1]

# lista.count(valor) Conta quantas vezes um valor aparece na lista.
# [1, 2, 2, 3].count(2) # → 2

# lista.index(valor) Retorna o índice da primeira ocorrência de um valor.
# ['a', 'b', 'c'].index('b') # → 1

# lista.copy() Retorna uma cópia superficial da lista.
# nova = antiga.copy()

##################################################################################
# Importante: lista.sort() e sorted(lista) podem receber o argumento             #
# reverse=True para ordenar em ordem decrescente. Ex: numeros.sort(reverse=True).#
##################################################################################

# # Percorrendo uma Lista (Iteração):
# A forma mais comum de passar por todos os itens de uma lista é usando um laço for.

planetas = ["Mercúrio", "Vênus", "Terra", "Marte"]

# Loop simples
print("\n--- Loop Simples ---")
for planeta in planetas:
    print(planeta)

# Loop com índice usando enumerate()
print("\n--- Loop com enumerate ---")
for indice, planeta in enumerate(planetas):
    print(f"Planeta {indice + 1}: {planeta}")


# Compreensão de Listas (List Comprehension)

# Esta é uma maneira elegante e "Pythônica" de criar listas baseadas em outras listas ou sequências. 
# É uma sintaxe concisa que combina um laço for e a criação de elementos em uma única linha.
# Formato básico: nova_lista = [expressao for item in iteravel]

#Exemplo 1: Quadrado dos números

numeros = [1, 2, 3, 4, 5]

# Forma tradicional
quadrados_tradicional = []
for n in numeros:
    quadrados_tradicional.append(n**2)

# Com List Comprehension
quadrados_comprehension = [n**2 for n in numeros]

print(f"Tradicional: {quadrados_tradicional}")
print(f"Comprehension: {quadrados_comprehension}")
#Formato com condicional: nova_lista = [expressao for item in iteravel if condicao]

#Exemplo 2: Apenas números pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Com List Comprehension e if
pares = [n for n in numeros if n % 2 == 0]

print(f"Números pares: {pares}") # Saída: [2, 4, 6, 8, 10]

# Conclusão
# As listas são incrivelmente poderosas e você as usará constantemente em seus projetos Python.
# Elas são a base para lidar com coleções de dados de forma dinâmica.

# Resumo Rápido:

# Crie com [].

# Acesse com lista[indice].

# Adicione com append(), insert() ou extend().

# Remova com remove(), pop() ou del.

# Ordene com sort() (modifica a original) ou sorted() (cria uma nova).

# Use laços for para percorrer os itens.

# Use List Comprehensions para criar novas listas de forma concisa e eficiente.