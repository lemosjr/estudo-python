# PROJETO 3: CONTADOR DE VOGAIS
# Crie uma função `contar_vogais` que recebe uma string e retorna a quantidade de vogais (a, e, i, o, u) nela.
# A função não deve diferenciar maiúsculas de minúsculas.
def contar_vogais(texto: str) -> int:
    texto = texto.lower()
    vogais = "aeiou"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais("Olá Mundo"))  # Exemplo de uso