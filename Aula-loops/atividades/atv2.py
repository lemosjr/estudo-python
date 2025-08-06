# 2. Tabuada de um Número

# Objetivo: Praticar input(), for e formatação de strings.

# Enunciado: Peça ao usuário para inserir um número inteiro.
#  Em seguida, use um laço for para calcular e imprimir a tabuada desse número, do 1 ao 10.

numero = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
