# 7. Padrão de Asteriscos

# Objetivo: Praticar laços aninhados.

# Enunciado: Escreva um programa que use laços aninhados para imprimir o seguinte padrão de asteriscos:

#                                             *
#                                             **
#                                             ***
#                                             ****
#                                             *****

# Dica: O laço externo controla as linhas e o laço interno controla o número de asteriscos a serem impressos em cada linha.

linhas = 5
for i in range(1, linhas + 1):
    for j in range(i):
        print('*', end='')
    print()