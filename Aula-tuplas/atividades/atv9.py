# Exercício 9: Agrupando Dados com Tuplas
# Dada a seguinte lista de registros de vendas, onde cada tupla é (produto, regiao):
# vendas = [('Notebook', 'Sudeste'), ('Celular', 'Nordeste'), ('Notebook', 'Sul'), ('TV', 'Sudeste'), ('Celular', 'Sudeste'), ('Celular', 'Sul')]
# Crie um dicionário que agrupe os produtos por região. As chaves do dicionário
# devem ser as regiões e os valores devem ser listas com os nomes dos produtos vendidos em cada região.
# O resultado esperado para a região 'Sudeste' seria ['Notebook', 'TV', 'Celular'].

vendas = [('Notebook', 'Sudeste'), ('Celular', 'Nordeste'), ('Notebook', 'Sul'), ('TV', 'Sudeste'), ('Celular', 'Sudeste'), ('Celular', 'Sul')]
vendas_por_regiao = {}

for produto, regiao in vendas:
  if regiao not in vendas_por_regiao:
    vendas_por_regiao[regiao] = [] # Cria a lista se a região não existir no dicionário
  vendas_por_regiao[regiao].append(produto)

print(f"Vendas agrupadas por região: {vendas_por_regiao}\n")