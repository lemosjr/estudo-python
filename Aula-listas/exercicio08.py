# --------------------
# 8. Encontrando o Maior e o Menor Valor
# --------------------
# Crie uma lista de números e escreva um programa que encontre e imprima o MAIOR e o MENOR número da lista,
# sem usar as funções max() e min().
# * Dica: Inicialize duas variáveis, 'maior' e 'menor', com o primeiro elemento da lista.
# Depois, percorra o restante da lista com um laço 'for', atualizando os valores de 'maior' e 'menor' conforme necessário.

# Cria uma lista de números
numeros = [34, 12, 5, 67, 23, 89, 1, 45]
# Inicializa as variáveis 'maior' e 'menor' com o primeiro elemento da lista
maior = menor = numeros[0]
# Percorre o restante da lista para encontrar o maior e o menor número
for numero in numeros[1:]:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
# Exibe o maior e o menor número encontrado
print("Maior número:", maior)
print("Menor número:", menor)