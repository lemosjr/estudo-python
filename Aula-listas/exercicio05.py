# --------------------
# 5. Separando Pares e Ímpares
# --------------------
# Crie uma lista com 10 números inteiros. Seu programa deve criar duas novas listas:
# uma contendo apenas os números PARES da lista original e outra contendo apenas os números ÍMPARES. Ao final, imprima as três listas.
# * Dica: O operador '%' (módulo) é útil aqui. numero % 2 == 0 significa que o número é par.

numeros = [1,2,3,4,5,6,7,8,9,10]
par = []
impar = []
for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(par)
print(impar)