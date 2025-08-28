# PROJETO 5: FILTRO DE LISTA
# Crie uma função `filtrar_lista` que recebe uma lista de números e um número `limite`.
# A função deve retornar uma nova lista contendo apenas os números da lista original que são maiores que o `limite`.
def filtrar_lista(numeros: list, limite: int) -> list:
    return [n for n in numeros if n > limite]

print(filtrar_lista([1, 5, 8, 12, 20], 10))  # Exemplo de uso