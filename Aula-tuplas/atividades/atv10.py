# Exercício 10: Processamento com Tuplas Nomeadas (namedtuple)
# Use o módulo collections para criar uma namedtuple chamada Funcionario com os campos id, nome e cargo.
# Em seguida, crie uma lista de tuplas normais com dados de funcionários:
# dados_brutos = [(101, 'Marcos', 'Analista'), (102, 'Helena', 'Gerente'), (103, 'Pedro', 'Desenvolvedor')]
# Converta essa lista de tuplas normais em uma lista de tuplas nomeadas Funcionario.
# Por fim, itere sobre a nova lista 
# e imprima uma frase para cada funcionário que seja 'Gerente', no formato: "A funcionária Helena (ID: 102) é Gerente.".

from collections import namedtuple

# Criando a namedtuple
Funcionario = namedtuple('Funcionario', ['id', 'nome', 'cargo'])

dados_brutos = [(101, 'Marcos', 'Analista'), (102, 'Helena', 'Gerente'), (103, 'Pedro', 'Desenvolvedor')]

# Convertendo a lista
lista_funcionarios = [Funcionario(*dados) for dados in dados_brutos] # O * desempacota a tupla para os argumentos

# Processando a lista
print("Procurando por gerentes:")
for func in lista_funcionarios:
  if func.cargo == 'Gerente':
    print(f"A funcionária {func.nome} (ID: {func.id}) é {func.cargo}.")