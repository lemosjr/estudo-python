# Atividade 9 (Difícil): Agrupando Pessoas por Cidade

# Enunciado: Você recebeu uma lista de dicionários, onde cada dicionário representa uma pessoa.

# Python

# pessoas = [
#     {"nome": "Ana", "cidade": "São Paulo"},
#     {"nome": "Bruno", "cidade": "Rio de Janeiro"},
#     {"nome": "Carla", "cidade": "São Paulo"},
#     {"nome": "Daniel", "cidade": "Belo Horizonte"},
#     {"nome": "Eduarda", "cidade": "Rio de Janeiro"}
# ]
# Crie um programa que agrupe essas pessoas por cidade.
# O resultado deve ser um dicionário onde a chave é o nome da cidade e o valor é uma lista com os nomes das pessoas que moram nela.

# Dica: Crie um dicionário vazio para o resultado.
# Percorra a lista pessoas. Para cada pessoa, verifique se a cidade dela já é uma chave no seu dicionário de resultado.
# Se não for, crie a chave com uma nova lista contendo o nome da pessoa.
#  Se já existir, apenas adicione (.append()) o nome da pessoa à lista existente.

# Resultado Esperado:

# {
#     'São Paulo': ['Ana', 'Carla'],
#     'Rio de Janeiro': ['Bruno', 'Eduarda'],
#     'Belo Horizonte': ['Daniel']
# }

pessoas = [
    {"nome": "Ana", "cidade": "São Paulo"},
    {"nome": "Bruno", "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "cidade": "São Paulo"},
    {"nome": "Daniel", "cidade": "Belo Horizonte"},
    {"nome": "Eduarda", "cidade": "Rio de Janeiro"}
]

resultado = {}
for pessoa in pessoas:
    cidade = pessoa["cidade"]
    nome = pessoa["nome"]
    if cidade not in resultado:
        resultado[cidade] = []
    resultado[cidade].append(nome)

print(resultado)    