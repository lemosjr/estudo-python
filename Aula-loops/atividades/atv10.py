# 10. Contador de Frequência de Palavras

# Objetivo: Combinar laços, dicionários e manipulação de strings.

# Enunciado: Escreva um programa que receba uma frase do usuário e conte a frequência de cada palavra na frase.
# O resultado deve ser armazenado em um dicionário onde a chave é a palavra e o valor é a contagem.
# O programa não deve diferenciar maiúsculas de minúsculas e deve ignorar pontuações básicas (como vírgula e ponto final).

# Exemplo de entrada: "A aula de Python é sobre Python e é muito legal."

# Exemplo de saída (dicionário):

# {'a': 1, 'aula': 1, 'de': 1, 'python': 2, 'é': 2, 'sobre': 1, 'e': 1, 'muito': 1, 'legal': 1}

# Dica: Use o método .split() para separar a frase em palavras e, em seguida, itere sobre a lista de palavras para preencher o dicionário.
#Evite usar funções prontas de contagem, o objetivo é praticar a lógica de contagem manualmente.

frase = input("Digite uma frase: ").lower()
palavras = frase.replace(',', '').replace('.', '').split()
frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print("\nFrequência das palavras encontradas:")
print(frequencia)