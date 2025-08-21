# Atividade 5 : Contador de Palavras

# Enunciado: Dada a frase a casa é amarela e a porta da casa é marrom, crie um programa que conte a frequência de cada palavra.
# O resultado deve ser um dicionário onde a chave é a palavra e o valor é o número de vezes que ela aparece.

# Dica: Primeiro, use o método .split() na string para obter uma lista de palavras.
# Depois, percorra essa lista e use um dicionário para armazenar a contagem.
# Se a palavra já estiver no dicionário, incremente o valor; senão, adicione-a com o valor 1.

# Resultado Esperado:

# {'a': 3, 'casa': 2, 'é': 2, 'amarela': 1, 'e': 1, 'porta': 1, 'da': 1, 'marrom': 1}


frase = "a casa é amarela e a porta da casa é marrom"

palavras = frase.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)
