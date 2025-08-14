# 8. List Comprehension com Condição

# Usando list comprehension, escreva uma única linha de código que crie uma nova lista chamada palavras_longas.
# Essa nova lista deve conter apenas as palavras da lista frase que tenham mais de 4 letras.

frase = ["uma", "lista", "em", "python", "é", "muito", "poderosa"]
palavras_longas = [palavra for palavra in frase if len(palavra) > 4]

print(palavras_longas)