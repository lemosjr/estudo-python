# 9. Sequência de Fibonacci

# Objetivo: Praticar a lógica de atualização de variáveis dentro de um laço.

# Enunciado: A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, ...).
# Peça ao usuário um número n e use um laço while ou for para gerar e imprimir os n primeiros números da sequência de Fibonacci.

# Exemplo: Se o usuário inserir n = 7, a saída deve ser 0, 1, 1, 2, 3, 5, 8.


n = int(input("Digite um número inteiro: "))
a, b = 0, 1
for i in range(n):
    print(a, end=', ' if i < n - 1 else '\n')
    a, b = b, a + b

