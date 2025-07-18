# --------------------
# 7. Invertendo Palavras
# --------------------
# Crie um programa que peça ao usuário para digitar uma frase.
# Em seguida, o programa deve criar uma lista onde cada elemento é uma palavra da frase, mas em ORDEM INVERSA.
# Por exemplo, se a entrada for "Eu amo programar em Python", a saída deve ser ['Python', 'em', 'programar', 'amo', 'Eu'].
# * Dica: Use o método .split() para transformar a string em uma lista de palavras e, em seguida, use fatiamento ([::-1]) ou o método .reverse().

# Solicita ao usuário para digitar uma frase
frase = input("Digite uma frase: ")

# Cria uma lista com as palavras da frase em ordem inversa
palavras_invertidas = frase.split()[::-1]

# Exibe a lista de palavras invertidas
print(palavras_invertidas)