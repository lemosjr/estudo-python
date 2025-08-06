# 5. Adivinhe o Número

# Objetivo: Praticar o laço while para repetição indefinida.

# Enunciado: Escreva um jogo onde o computador "pensa" em um número inteiro de 1 a 100 e o jogador tenta adivinhar.
# O programa deve usar um laço while para continuar pedindo um palpite ao jogador até que ele acerte.
# Após cada palpite, o programa deve dizer se o número correto é "maior" ou "menor" que o palpite.

# Dica: Você pode definir o número secreto no início do código, por exemplo: numero_secreto = 42.

import random

numero_secreto = random.randint(1, 100)
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    if palpite < numero_secreto:
        print("O número é maior.")
    elif palpite > numero_secreto:
        print("O número é menor.")
print("Parabéns! Você adivinhou o número.")
