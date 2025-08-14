# 10. Cópia vs. Referência (Mutabilidade)
# Analise o bloco de código abaixo com atenção. Qual será a saída final do comando print(lista_A)?

lista_A = [1, 2, 3]

# 'lista_B' recebe a referência de 'lista_A'
lista_B = lista_A 
lista_B.append(4)

# 'lista_C' recebe uma CÓPIA de 'lista_A'
lista_C = lista_A.copy()
lista_C.append(5)

print(lista_A)

# a) [1, 2, 3]
# b) [1, 2, 3, 4]
# c) [1, 2, 3, 5]
# d) [1, 2, 3, 4, 5]

# resposta correta: b