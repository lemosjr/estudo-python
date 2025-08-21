# Atividade 7: Invertendo um Dicionário

# Enunciado: Dado um dicionário com nomes de países e suas capitais,
# crie um novo dicionário onde as chaves são as capitais e os valores são os países.
# (Considere que não há capitais com o mesmo nome para este exercício).

# Python

# paises_capitais = {"Brasil": "Brasília", "Japão": "Tóquio", "Argentina": "Buenos Aires"}
# Dica: Crie um dicionário vazio. Percorra o dicionário original com .items().
# Em cada iteração, use o valor como a nova chave e a chave como o novo valor.

# Resultado Esperado:

# {'Brasília': 'Brasil', 'Tóquio': 'Japão', 'Buenos Aires': 'Argentina'}

paises_capitais = {
    "Brasília": "Brasil",
    "Tóquio": "Japão",
    "Buenos Aires": "Argentina"
}

capitais_paises = {}
for pais, capital in paises_capitais.items():
    capitais_paises[capital] = pais

print(capitais_paises)