# Atividade 8 (Difícil): Combinando Dados de Vendas

# Enunciado: Você tem dois dicionários. O primeiro (precos) contém os preços dos produtos e o segundo (estoque) contém as quantidades.

# Python

# precos = {"banana": 2.50, "maçã": 3.00, "laranja": 2.75, "abacaxi": 4.50}
# estoque = {"banana": 150, "maçã": 100, "laranja": 200, "uva": 50}
# Crie um novo dicionário que combine essas informações, mas apenas para os produtos que existem em ambos os dicionários.
# O novo dicionário deve ter o nome do produto como chave e, como valor, outro dicionário contendo preco e quantidade.

# Dica: Percorra as chaves de um dos dicionários (por exemplo, precos.keys()) 
# e verifique se a mesma chave existe no outro dicionário (estoque) antes de adicionar os dados ao novo dicionário.

# Resultado Esperado:

# {
#     'banana': {'preco': 2.5, 'quantidade': 150},
#     'maçã': {'preco': 3.0, 'quantidade': 100},
#     'laranja': {'preco': 2.75, 'quantidade': 200}
# }

precos = {"banana": 2.50, "maçã": 3.00, "laranja": 2.75, "abacaxi": 4.50}
estoque = {"banana": 150, "maçã": 100, "laranja": 200, "uva": 50}

produtos_disponiveis = {}
for produto in precos.keys():
    if produto in estoque:
        produtos_disponiveis[produto] = {
            "preco": precos[produto],
            "quantidade": estoque[produto]
        }

print(produtos_disponiveis)
