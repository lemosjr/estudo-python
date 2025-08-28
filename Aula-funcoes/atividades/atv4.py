# PROJETO 4: CALCULADORA DE ESTATÍSTICAS
# Crie uma função `calcular_estatisticas` que recebe uma lista de números e retorna um dicionário com a média, o maior e o menor número.
def calcular_estatisticas(lista_numeros: list) -> dict:
    if not lista_numeros:
        return {"media": 0, "maior": 0, "menor": 0}

    media = sum(lista_numeros) / len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)

    return {"media": media, "maior": maior, "menor": menor}

print(calcular_estatisticas([10, 20, 30, 40, 50]))  # Exemplo de uso