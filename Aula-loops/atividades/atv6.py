# 6. Validação de Entrada com break

# Objetivo: Praticar o while com break.

# Enunciado: Escreva um programa que peça ao usuário para digitar um número entre 1 e 10.
# Use um laço while para continuar pedindo a entrada até que o usuário digite um número válido.
# Se o número estiver dentro do intervalo, imprima uma mensagem de sucesso e use break para sair do laço.

while True:
    numero = int(input("Digite um número entre 1 e 10: "))
    if 1 <= numero <= 10:
        print("Número válido!")
        break
    print("Número inválido. Tente novamente.")