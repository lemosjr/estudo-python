# ==============================================================================
# AULA COMPLETA SOBRE LAÇOS DE REPETIÇÃO EM PYTHON
# ==============================================================================

"""
Laços de repetição, ou loops, são uma das estruturas mais fundamentais
na programação. Eles nos permitem executar um bloco de código repetidamente,
economizando tempo e tornando nosso código mais limpo e eficiente.
Em Python, existem dois tipos principais de laços: o `for` e o `while`.
"""

# Para separar a saída de cada seção, vamos usar um print.
print("="*50)
print(">>> INÍCIO DA AULA SOBRE LAÇOS DE REPETIÇÃO <<<")
print("="*50 + "\n")


# ------------------------------------------------------------------------------
# 1. O Laço `for`
# ------------------------------------------------------------------------------
print("--- 1. O Laço `for` ---")
"""
O laço `for` em Python é usado para iterar sobre uma sequência
(como uma lista, tupla, dicionário, conjunto ou string).
"""

# Sintaxe básica:
# for item in sequencia:
#     # bloco de código a ser executado

# Exemplo com Listas:
print("\nIterando sobre uma lista de frutas:")
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Exemplo com Strings:
print("\nIterando sobre uma string:")
for letra in "Python":
    print(letra)

# --- 1.1 A Função `range()` ---
print("\n--- 1.1 Usando a função `range()` ---")
"""
A função `range()` gera uma sequência de números, sendo muito útil
para executar um laço um número específico de vezes.
"""
# Imprime números de 0 a 4
print("\nrange(5):")
for i in range(5):
    print(i)

# Imprime números de 2 a 5
print("\nrange(2, 6):")
for i in range(2, 6):
    print(i)

# Imprime números pares de 0 a 8
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)

# --- 1.2 A Função `enumerate()` ---
print("\n--- 1.2 Usando a função `enumerate()` ---")
"""
Quando você precisa tanto do índice quanto do item de uma sequência,
a função `enumerate()` adiciona um contador a um iterável.
"""
frutas = ["maçã", "banana", "cereja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# --- 1.3 Iterando sobre Dicionários ---
print("\n--- 1.3 Iterando sobre Dicionários ---")
aluno = {"nome": "Carlos", "idade": 22, "curso": "Engenharia"}

# Iterando sobre as chaves (comportamento padrão)
print("\nIterando sobre as chaves:")
for chave in aluno:
    print(chave)

# Iterando sobre os valores
print("\nIterando sobre os valores com .values():")
for valor in aluno.values():
    print(valor)

# Iterando sobre ambos (chave e valor)
print("\nIterando sobre chaves e valores com .items():")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("\n" + "="*50 + "\n")


# ------------------------------------------------------------------------------
# 2. O Laço `while`
# ------------------------------------------------------------------------------
print("--- 2. O Laço `while` ---")
"""
O laço `while` executa um bloco de código ENQUANTO uma determinada
condição for verdadeira. É ideal para situações onde o número de iterações
não é conhecido de antemão.
"""

# Sintaxe básica:
# while condicao:
#     # bloco de código a ser executado

print("\nContando de 0 a 4 com o laço `while`:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Essencial: atualiza a condição para evitar um laço infinito

# ATENÇÃO: É crucial garantir que a condição do `while` em algum momento
# se torne falsa para não criar um laço infinito.

print("\n" + "="*50 + "\n")


# ------------------------------------------------------------------------------
# 3. Controle de Laços (`break`, `continue`, `else`)
# ------------------------------------------------------------------------------
print("--- 3. Controle de Laços ---")

# --- 3.1 A declaração `break` ---
print("\n--- 3.1 Exemplo com `break` ---")
"""
A declaração `break` INTERROMPE o laço imediatamente.
"""
for numero in range(10):
    if numero == 5:
        print(f"Número é {numero}, o laço será interrompido!")
        break  # Para o laço quando o número for 5
    print(numero)
print("Laço finalizado.")

# --- 3.2 A declaração `continue` ---
print("\n--- 3.2 Exemplo com `continue` ---")
"""
A declaração `continue` PULA a iteração atual e vai para a próxima.
"""
print("Imprimindo apenas os números ímpares:")
for numero in range(10):
    if numero % 2 == 0:  # Se o número for par
        continue         # Pula para a próxima iteração
    print(numero)        # Só executa para os ímpares

# --- 3.3 A cláusula `else` em Laços ---
print("\n--- 3.3 Exemplo com a cláusula `else` ---")
"""
O bloco `else` é executado quando o laço termina normalmente
(sem ser interrompido por um `break`).
"""
print("\nLaço que termina normalmente:")
for i in range(3):
    print(f"Iteração {i}")
else:
    print("O laço terminou sem interrupções e o `else` foi executado.")

print("\nLaço que é interrompido por um `break`:")
for i in range(3):
    if i == 1:
        print(f"Interrompendo na iteração {i}")
        break
    print(f"Iteração {i}")
else:
    print("Esta mensagem não será impressa, pois o laço foi quebrado.")

print("\n" + "="*50 + "\n")


# ------------------------------------------------------------------------------
# 4. Laços Aninhados
# ------------------------------------------------------------------------------
print("--- 4. Laços Aninhados ---")
"""
Você pode colocar um laço dentro de outro. Isso é útil para trabalhar
com estruturas de dados bidimensionais, como matrizes ou para gerar
combinações.
"""
print("\nGerando uma mini tabuada com laços aninhados:")
for i in range(1, 4):      # Laço externo
    for j in range(1, 4):  # Laço interno
        print(f"{i} * {j} = {i*j}")
    print("---") # Separador para clareza


# ------------------------------------------------------------------------------
# FIM DA AULA
# ------------------------------------------------------------------------------
print("\n" + "="*50)
print(">>> FIM DA AULA. Pratique para dominar os laços! <<<")
print("="*50)