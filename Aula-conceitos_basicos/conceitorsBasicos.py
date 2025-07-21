# Isto é um comentário. Ele não será executado.
print("Olá, Mundo!") # Comentários também podem vir após o código.

# Variaveis e tipos de dados

# Atribuindo valores a variáveis
nome_usuario = "Alex"
pontuacao = 100
media_acertos = 85.5
esta_ativo = True

# Exibindo os valores e seus tipos
print(nome_usuario)      # Saída: Alex
print(type(pontuacao))   # Saída: <class 'int'>
print(type(media_acertos)) # Saída: <class 'float'>
print(type(esta_ativo))   # Saída: <class 'bool'>

# Operadores Aritméticos
soma = 10 + 5        # 15
e_igual = (soma == 15) # True
e_diferente = (soma != 15) # False

# Usando operadores lógicos
tem_pontos = True
tem_vidas = True
pode_jogar = tem_pontos and tem_vidas # True
# Exibindo resultados
print("Pode jogar:", pode_jogar)  # Saída: Pode jogar: True
