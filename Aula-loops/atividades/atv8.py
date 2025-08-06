# 8. Verificador de Número Primo

# Objetivo: Praticar o uso de for com a cláusula else.

# Enunciado: Peça ao usuário um número inteiro. Escreva um programa que determine se o número é primo ou não.
# Um número primo é aquele que só é divisível por 1 e por ele mesmo.

# Dica: Use um laço for para verificar se o número tem algum divisor entre 2 e a sua metade. Se encontrar um divisor, use break.
# A cláusula else do laço for é perfeita para imprimir que o número é primo se o laço terminar sem ser interrompido.

numero = int(input("Digite um número inteiro: "))
for i in range(2, numero // 2 + 1):
    if numero % i == 0:
        print("O número não é primo.")
        break
else:
    print("O número é primo.")
