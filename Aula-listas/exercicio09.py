# --------------------
# 9. Quadrados com List Comprehension
# --------------------
# Usando LIST COMPREHENSION, crie uma lista chamada 'quadrados' que contenha o quadrado dos números de 1 a 10. Imprima a lista resultante.
# * Exemplo de List Comprehension: nova_lista = [expressao for item in iteravel]

quadrados = [numero**2 for numero in range(1, 11)]
print(quadrados)
# Exemplo de saída: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]