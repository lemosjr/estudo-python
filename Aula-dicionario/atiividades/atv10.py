# Atividade 10 (Difícil): Análise de Votos em Enquete

# Enunciado: Você tem um dicionário que representa uma enquete sobre a melhor linguagem de programação,
# com as opções e seus votos iniciais zerados. Você também tem uma lista de votos de vários desenvolvedores.

# Python

# enquete = {"Python": 0, "JavaScript": 0, "Java": 0, "C#": 0}
# votos = ["Python", "JavaScript", "Java", "Python", "JavaScript", "Python", "C#", "Java", "JavaScript"]
# Crie um programa que conte os votos da lista e atualize o dicionário enquete.

# Calcule a porcentagem de votos para cada linguagem (considere o total de votos válidos).

# Imprima um relatório final mostrando a contagem e a porcentagem de cada um, e declare a linguagem vencedora (a que teve mais votos).

# Dica: Primeiro, percorra a lista votos para preencher o dicionário enquete. Depois, calcule o total de votos.
# Em um segundo loop, percorra o dicionário enquete para calcular as porcentagens e imprimir o relatório.
# Mantenha variáveis para rastrear o vencedor e o maior número de votos.

# Resultado Esperado:

# Resultado da Enquete:
# --------------------
# Python: 3 votos (33.33%)
# JavaScript: 3 votos (33.33%)
# Java: 2 votos (22.22%)
# C#: 1 votos (11.11%)
# --------------------
# A(s) linguagem(ns) vencedora(s) e(sao): Python, JavaScript com 3 votos cada.

enquete = {"Python": 0, "JavaScript": 0, "Java": 0, "C#": 0}
votos = ["Python", "JavaScript", "Java", "Python", "JavaScript", "Python", "C#", "Java", "JavaScript"]

# Contando os votos
for voto in votos:
    if voto in enquete:
        enquete[voto] += 1

# Calculando o total de votos
total_votos = sum(enquete.values())

# Imprimindo o relatório
print("Resultado da Enquete:")
print("---------------------")
vencedor = []
maior_votos = 0
for linguagem, contagem in enquete.items():
    porcentagem = (contagem / total_votos * 100) if total_votos > 0 else 0
    print(f"{linguagem}: {contagem} votos ({porcentagem:.2f}%)")
    if contagem > maior_votos:
        maior_votos = contagem
        vencedor = [linguagem]
    elif contagem == maior_votos:
        vencedor.append(linguagem)

print("---------------------")
print(f"A(s) linguagem(ns) vencedora(s) e(sao): {', '.join(vencedor)} com {maior_votos} votos cada.")
