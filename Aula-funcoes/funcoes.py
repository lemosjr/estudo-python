# funcoes_python_aula.py

"""
Este arquivo serve como um guia de estudo e anotações sobre
as funções em Python. Cada seção aborda um conceito fundamental.
"""

# -----------------------------------------------------------------------------
# 1. O QUE É UMA FUNÇÃO E ESTRUTURA BÁSICA
# -----------------------------------------------------------------------------
# Definição: Bloco de código reutilizável que realiza uma tarefa específica.
# Vantagens: Organização, reutilização e facilidade de manutenção.

def somar(a, b):
    """
    Esta é uma docstring.
    Ela explica que a função recebe dois números (a e b) e retorna sua soma.
    """
    resultado = a + b
    return resultado

# Para executar (ou "chamar") a função:
soma_exemplo = somar(10, 5)
print(f"1. Resultado da função somar: {soma_exemplo}")
print("-" * 20)


# -----------------------------------------------------------------------------
# 2. TIPOS DE ARGUMENTOS E PARÂMETROS
# -----------------------------------------------------------------------------

# a) Argumentos Posicionais: A ordem da passagem importa.
def saudacao(nome, mensagem):
    """Exibe uma saudação formatada."""
    print(f"2a. Argumento Posicional: {mensagem}, {nome}!")

saudacao("Maria", "Olá")

# b) Argumentos Nomeados (Keyword Arguments): A ordem não importa.
def dados_pessoais(nome, idade, cidade):
    """Exibe informações pessoais."""
    print(f"2b. Argumento Nomeado: Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

dados_pessoais(idade=30, cidade="Fortaleza", nome="Carlos")

# c) Parâmetros com Valor Padrão: Torna o argumento opcional na chamada.
def potencia(base, expoente=2):
    """Calcula a potência de um número. O expoente padrão é 2."""
    return base ** expoente

quadrado = potencia(5)      # Usa o expoente padrão 2
cubo = potencia(5, 3)     # Fornece um novo valor para o expoente
print(f"2c. Valor Padrão: O quadrado de 5 é {quadrado}")
print(f"2c. Valor Padrão: O cubo de 5 é {cubo}")
print("-" * 20)


# -----------------------------------------------------------------------------
# 3. ARGUMENTOS FLEXÍVEIS: *ARGS E **KWARGS
# -----------------------------------------------------------------------------

# a) *args: Agrupa múltiplos argumentos posicionais em uma TUPLA.
def calcular_media(*notas):
    """Calcula a média de uma quantidade variável de notas."""
    print(f"3a. *args recebe os valores como uma tupla: {notas}")
    if not notas:
        return 0
    return sum(notas) / len(notas)

media_aluno1 = calcular_media(10, 8, 9.5)
media_aluno2 = calcular_media(7, 6)
print(f"3a. A média do aluno 1 é: {media_aluno1:.2f}")
print(f"3a. A média do aluno 2 é: {media_aluno2:.2f}")

# b) **kwargs: Agrupa múltiplos argumentos nomeados em um DICIONÁRIO.
def montar_perfil(**informacoes):
    """Monta um perfil de usuário a partir de dados variáveis."""
    print("3b. **kwargs recebe os valores como um dicionário:")
    for chave, valor in informacoes.items():
        print(f"   - {chave.capitalize()}: {valor}")

montar_perfil(nome="Ana", idade=28, profissao="Engenheira", hobby="Leitura")
print("-" * 20)


# -----------------------------------------------------------------------------
# 4. ESCOPO DE VARIÁVEIS (LEGB)
# -----------------------------------------------------------------------------
# Local -> Enclosing -> Global -> Built-in

variavel_global = "Eu sou global"  # G - Global

def funcao_externa():
    variavel_enclosing = "Eu sou enclosing"  # E - Enclosing

    def funcao_interna():
        variavel_local = "Eu sou local"  # L - Local
        
        print(f"4. Acesso da função interna -> {variavel_local}")
        print(f"4. Acesso da função interna -> {variavel_enclosing}")
        print(f"4. Acesso da função interna -> {variavel_global}")

    funcao_interna()

funcao_externa()
# print(variavel_local) # -> Isso geraria um erro!
print("-" * 20)


# -----------------------------------------------------------------------------
# 5. FUNÇÕES ANÔNIMAS (LAMBDA)
# -----------------------------------------------------------------------------
# Funções pequenas, de uma única linha e sem nome.
# Sintaxe: lambda argumentos: expressao

dobro = lambda x: x * 2
print(f"5. Lambda: O dobro de 7 é {dobro(7)}")

# Exemplo de uso com a função sorted()
produtos = [('Produto A', 50), ('Produto B', 25), ('Produto C', 75)]
# Ordena a lista de produtos pelo preço (o segundo item da tupla)
produtos_ordenados = sorted(produtos, key=lambda item: item[1])
print(f"5. Lambda com sorted: {produtos_ordenados}")
print("-" * 20)


# -----------------------------------------------------------------------------
# 6. BOAS PRÁTICAS: DOCSTRINGS E TYPE HINTS
# -----------------------------------------------------------------------------
# Anotações de tipo (Type Hints) ajudam na legibilidade e na detecção de erros.

def enviar_email(destinatario: str, assunto: str, corpo: str) -> bool:
    """
    Simula o envio de um e-mail.

    Args:
        destinatario (str): O e-mail do destinatário.
        assunto (str): O assunto da mensagem.
        corpo (str): O conteúdo do e-mail.

    Returns:
        bool: Retorna True se o e-mail foi enviado com sucesso, False caso contrário.
    """
    print(f"\n6. Enviando e-mail com Type Hints...")
    print(f"   Para: {destinatario}")
    print(f"   Assunto: {assunto}")
    
    if destinatario and assunto and corpo:
        return True
    return False

# Exemplo de chamada da função bem documentada
sucesso = enviar_email("usuario@exemplo.com", "Aula de Python", "Aprendendo sobre funções.")
print(f"   Status do envio: {'Sucesso' if sucesso else 'Falha'}")

# Acessando a docstring da função
# print("\nDocstring da função enviar_email:")
# print(enviar_email.__doc__)