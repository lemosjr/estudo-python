######################## LISTAS ########################################

# Criando uma lista vazia
lista_vazia = []
print(f"Lista vazia: {lista_vazia}")

# Criando uma lista de números inteiros
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Criando uma lista de strings (textos)
frutas = ["maçã", "banana", "laranja"]
print(f"Lista de frutas: {frutas}")

# Criando uma lista mista (heterogênea)
lista_mista = [10, "Python", True, 3.14]
print(f"Lista mista: {lista_mista}")

# Listas podem conter outras listas (listas aninhadas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Lista aninhada (matriz): {matriz}")

################ Acessando Elementos (Indexação) #####################

# Para acessar um item específico em uma lista, você usa seu índice (sua posição).
# A contagem de índices em Python sempre começa em zero (0).
# Você também pode usar índices negativos, onde -1 se refere ao último item, -2 ao penúltimo, 
# e assim por diante.


alunos = ["Ana", "Bruno", "Carla", "Daniel"]

# Acessando o primeiro elemento (índice 0)
primeiro_aluno = alunos[0]
print(f"Primeiro aluno: {primeiro_aluno}")  # Saída: Ana

# Acessando o terceiro elemento (índice 2)
terceiro_aluno = alunos[2]
print(f"Terceiro aluno: {terceiro_aluno}")  # Saída: Carla

# Acessando o último elemento com índice negativo
ultimo_aluno = alunos[-1]
print(f"Último aluno: {ultimo_aluno}")  # Saída: Daniel

# Acessando o penúltimo elemento
penultimo_aluno = alunos[-2]
print(f"Penúltimo aluno: {penultimo_aluno}") # Saída: Carla


###################### Fatiamento (Slicing) ################################

# Fatiamento é uma técnica poderosa para extrair uma sub-lista (uma parte da lista original). 
# A sintaxe é: 

# lista[inicio:fim:passo].

# inicio: O índice onde a fatia começa (inclusivo). Se omitido, começa do início da lista.
# fim: O índice onde a fatia termina (exclusivo). Se omitido, vai até o final da lista.
# passo: O intervalo entre os itens. Se omitido, o padrão é 1.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pega os elementos do índice 2 até o 5 (5 não incluso)
fatia1 = numeros[2:5]
print(f"numeros[2:5] -> {fatia1}")  # Saída: [2, 3, 4]

# Pega os 4 primeiros elementos
fatia2 = numeros[:4]
print(f"numeros[:4] -> {fatia2}")   # Saída: [0, 1, 2, 3]

# Pega os elementos a partir do índice 6
fatia3 = numeros[6:]
print(f"numeros[6:] -> {fatia3}")   # Saída: [6, 7, 8, 9]

# Copia a lista inteira
copia_total = numeros[:]
print(f"numeros[:] -> {copia_total}") # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pega os elementos de 2 em 2
passo2 = numeros[::2]
print(f"numeros[::2] -> {passo2}")   # Saída: [0, 2, 4, 6, 8]

# Inverte a lista usando fatiamento!
invertida = numeros[::-1]
print(f"numeros[::-1] -> {invertida}") # Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

