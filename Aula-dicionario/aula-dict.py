# ==============================================================================
#                      AULA COMPLETA SOBRE DICIONÁRIOS EM PYTHON
# ==============================================================================
#
# Este arquivo serve como um guia prático e executável sobre dicionários.
# Execute este script para ver os exemplos em ação.

# ------------------------------------------------------------------------------
# Seção 1: O que é um Dicionário?
# ------------------------------------------------------------------------------
# É uma coleção de dados que armazena pares de `chave: valor`.
# - Chaves: Identificadores únicos e imutáveis (strings, números, tuplas).
# - Valores: Qualquer tipo de dado (números, strings, listas, outros dicionários).
#
# Pense nele como uma agenda: a 'chave' é o nome da pessoa, o 'valor' são os dados dela.
# ------------------------------------------------------------------------------

print("===== Seção 2: Criação de Dicionários =====")

# A forma mais comum de criar um dicionário é usando chaves {}
produto = {
    "nome": "Smartwatch",
    "preco": 799.90,
    "marcas_compativeis": ["Samsung", "Apple", "Xiaomi"],
    "em_estoque": True
}

print("Dicionário criado:", produto)

# Criando um dicionário vazio para preencher depois
estoque_loja = {}
print("Dicionário vazio:", estoque_loja)
print("-" * 20)


# ------------------------------------------------------------------------------
# Seção 3: Operações Fundamentais
# ------------------------------------------------------------------------------
print("===== Seção 3: Operações Fundamentais =====")

# a) Acessando um valor pela sua chave
print(f"Nome do produto: {produto['nome']}")
print(f"Preço: R$ {produto['preco']}")
# print(produto['garantia'])  # Isso geraria um erro (KeyError), pois a chave não existe.

# b) Adicionando um novo par chave-valor
produto['cor'] = 'Preto'
print("Dicionário após adicionar 'cor':", produto)

# c) Modificando um valor existente (a sintaxe é a mesma)
produto['preco'] = 749.99
print("Dicionário após modificar 'preco':", produto)

# d) Removendo um item com 'del'
del produto['em_estoque']
print("Dicionário após remover 'em_estoque':", produto)
print("-" * 20)


# ------------------------------------------------------------------------------
# Seção 4: Métodos Essenciais (A Caixa de Ferramentas)
# ------------------------------------------------------------------------------
print("===== Seção 4: Métodos Essenciais =====")

# a) Acesso seguro com .get() para evitar erros
# Se a chave não existir, ele retorna None (ou um valor padrão que você definir)
garantia = produto.get('garantia')
print(f"Buscando a chave 'garantia' com .get(): {garantia}")

garantia_padrao = produto.get('garantia', '90 dias')
print(f"Buscando com .get() e valor padrão: {garantia_padrao}")

# b) Verificando se uma chave existe com 'in'
if 'preco' in produto:
    print("'preco' é uma chave que existe no dicionário.")

if 'peso' not in produto:
    print("'peso' NÃO é uma chave que existe no dicionário.")

# c) Obtendo o número de itens com len()
print(f"O dicionário 'produto' tem {len(produto)} itens.")

# d) Obtendo todas as chaves com .keys()
chaves = produto.keys()
print(f"Todas as chaves: {chaves}")

# e) Obtendo todos os valores com .values()
valores = produto.values()
print(f"Todos os valores: {valores}")

# f) Obtendo todos os pares (chave, valor) com .items() - MUITO ÚTIL PARA LOOPS!
itens = produto.items()
print(f"Todos os itens (pares): {itens}")

# g) Removendo um item com .pop() (ele remove e retorna o valor)
cor_removida = produto.pop('cor')
print(f"A cor removida foi: {cor_removida}")
print("Dicionário após o .pop():", produto)

# h) Juntando dois dicionários com .update()
informacoes_adicionais = {
    'origem': 'Importado',
    'garantia': '1 ano' # Esta chave não existia, será adicionada
}
produto.update(informacoes_adicionais)
print("Dicionário após .update():", produto)
print("-" * 20)


# ------------------------------------------------------------------------------
# Seção 5: Como Percorrer o Dicionário (Loops)
# ------------------------------------------------------------------------------
print("===== Seção 5: Loops em Dicionários =====")

# A maneira mais eficiente e clara é usando .items()
print("\n--- Detalhes do Produto (usando .items()) ---")
for chave, valor in produto.items():
    # .capitalize() deixa a primeira letra maiúscula
    print(f"{str(chave).capitalize()}: {valor}")

# Também é possível iterar apenas pelas chaves...
print("\n--- Apenas as chaves ---")
for chave in produto.keys(): # ou simplesmente `for chave in produto:`
    print(chave)

# ... ou apenas pelos valores
print("\n--- Apenas os valores ---")
for valor in produto.values():
    print(valor)
print("-" * 20)


# ------------------------------------------------------------------------------
# Seção 6: Tópicos Avançados (Bônus)
# ------------------------------------------------------------------------------
print("===== Seção 6: Tópicos Avançados =====")

# a) Dictionary Comprehension: uma forma rápida de criar dicionários
quadrados = {x: x * x for x in range(1, 6)}
print("Dicionário de quadrados:", quadrados)

# b) Dicionários Aninhados: um dicionário dentro de outro
usuarios = {
    'alice': {
        'nome_completo': 'Alice Silva',
        'idade': 30,
        'cidade': 'São Paulo'
    },
    'bruno': {
        'nome_completo': 'Bruno Costa',
        'idade': 25,
        'cidade': 'Recife'
    }
}

# Acessando um dado aninhado
cidade_bruno = usuarios['bruno']['cidade']
print(f"A cidade de Bruno é: {cidade_bruno}")
print("-" * 20)

# ------------------------------------------------------------------------------
# Fim da Aula.
# Pratique criando seus próprios dicionários e manipulando-os!
# ------------------------------------------------------------------------------