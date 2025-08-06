# 4. Contagem de Vogais

# Objetivo: Praticar a iteração sobre uma string com uma condição if.

# Enunciado: Escreva um programa que conte o número de vogais (a, e, i, o, u) em uma string fornecida pelo usuário.
# O programa não deve diferenciar maiúsculas de minúsculas.

# Dica: Você pode usar if letra.lower() in 'aeiou':.


string = input("Digite uma frase: ")
contador_vogais = 0
for letra in string:
    if letra.lower() in 'aeiou':
        contador_vogais += 1
print(f"Número de vogais na frase: {contador_vogais}")