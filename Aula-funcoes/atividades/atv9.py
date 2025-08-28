# PROJETO 9: VERIFICADOR DE PALÍNDROMO
# Crie uma função `eh_palindromo` que verifica se uma palavra ou frase é um palíndromo.
# A função deve ignorar espaços, pontuações e diferenças entre maiúsculas e minúsculas.
# Um palíndromo é uma palavra que se lê da mesma forma de trás para frente (ex: "ovo", "Anotaram a data da maratona").
def eh_palindromo(texto: str) -> bool:
    texto = texto.lower().replace(" ", "").replace(".", "").replace(",", "")
    return texto == texto[::-1]

print(eh_palindromo("Anotaram a data da maratona"))  # Exemplo de uso