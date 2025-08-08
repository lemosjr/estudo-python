# Exercício 5: Desempacotamento de Tuplas
# Escreva uma função chamada obter_dados_usuario que recebe um ID de usuário (um número inteiro)
# e retorna uma tupla contendo o nome, email e idade do usuário 
# (você pode usar dados fixos dentro da função, por exemplo: 'Ana Souza', 'ana.souza@email.com', 28).
# Depois, chame essa função e desempacote o resultado em três variáveis: nome, email e idade. Imprima cada uma das variáveis.

def obter_dados_usuario(user_id):
  # Simulando uma busca no banco de dados
  if user_id == 1:
    return ('Ana Souza', 'ana.souza@email.com', 28)
  return (None, None, None)

# Chamando a função e desempacotando
nome, email, idade = obter_dados_usuario(1)
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"Idade: {idade}\n")
