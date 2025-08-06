# 3. Soma de Números em uma Lista

# Objetivo: Praticar a iteração sobre uma lista e o uso de uma variável acumuladora.

# Enunciado: Dada a lista numeros = [10, 5, 8, 20, 15], 
# escreva um programa que calcula a soma de todos os números na lista usando um laço for.

numeros = [10, 5, 8, 20, 15]
soma = 0
for n in numeros:
    soma += n
print(f"A soma dos números na lista é: {soma}")
