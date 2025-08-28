# =================================================================================
# ATIVIDADES COM FUNÇÕES - 10 MINI-PROJETOS
#
# Instruções:
# 1. Leia o enunciado de cada projeto.
# 2. Escreva o código da função solicitada.
# 3. Descomente e execute os testes para garantir que sua função funciona corretamente.
# =================================================================================

import random
import string
import unicodedata
from datetime import datetime

# ---------------------------------------------------------------------------------
# NÍVEL FÁCIL
# ---------------------------------------------------------------------------------

# PROJETO 1: VERIFICADOR DE NÚMERO PAR
# Crie uma função `eh_par` que recebe um número e retorna True se ele for par e False caso contrário.
def eh_par(numero: int) -> bool:
    """Verifica se um número é par."""
    # SEU CÓDIGO VEM AQUI
    pass

# PROJETO 2: CONVERSOR DE TEMPERATURA
# Crie uma função `celsius_para_fahrenheit` que recebe uma temperatura em Celsius e a retorna em Fahrenheit.
# Fórmula: F = (C * 9/5) + 32
def celsius_para_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit."""
    # SEU CÓDIGO VEM AQUI
    pass

# PROJETO 3: CONTADOR DE VOGAIS
# Crie uma função `contar_vogais` que recebe uma string e retorna a quantidade de vogais (a, e, i, o, u) nela.
# A função não deve diferenciar maiúsculas de minúsculas.
def contar_vogais(texto: str) -> int:
    """Conta o número de vogais em uma string."""
    # SEU CÓDIGO VEM AQUI
    pass

# PROJETO 4: CALCULADORA DE ESTATÍSTICAS
# Crie uma função `calcular_estatisticas` que recebe uma lista de números e retorna um dicionário com a média, o maior e o menor número.
def calcular_estatisticas(lista_numeros: list) -> dict:
    """Calcula estatísticas básicas de uma lista de números."""
    # SEU CÓDIGO VEM AQUI
    pass

# ---------------------------------------------------------------------------------
# NÍVEL MÉDIO
# ---------------------------------------------------------------------------------

# PROJETO 5: FILTRO DE LISTA
# Crie uma função `filtrar_lista` que recebe uma lista de números e um número `limite`.
# A função deve retornar uma nova lista contendo apenas os números da lista original que são maiores que o `limite`.
def filtrar_lista(numeros: list, limite: int) -> list:
    """Filtra uma lista, retornando apenas números maiores que um determinado limite."""
    # SEU CÓDIGO VEM AQUI
    pass

# PROJETO 6: VALIDADOR DE CPF SIMPLES
# Crie uma função `validar_cpf_simples` que recebe uma string `cpf`.
# A função deve retornar True se o CPF tiver exatamente 11 dígitos numéricos e False caso contrário.
# Não é necessário validar os dígitos verificadores, apenas o formato.
def validar_cpf_simples(cpf: str) -> bool:
    """Valida se uma string de CPF tem o formato básico correto (11 dígitos)."""
    # SEU CÓDIGO VEM AQUI
    pass

# PROJETO 7: GERADOR DE SENHAS
# Crie uma função `gerar_senha` que recebe um `comprimento` e gera uma senha aleatória com letras e números.
def gerar_senha(comprimento: int) -> str:
    """Gera uma senha aleatória com o comprimento especificado."""
    # SEU CÓDIGO VEM AQUI
    pass

# ---------------------------------------------------------------------------------
# NÍVEL DIFÍCIL
# ---------------------------------------------------------------------------------

# PROJETO 8: CALCULADORA DE IDADE
# Crie uma função `calcular_idade` que recebe uma data de nascimento no formato "dd/mm/aaaa" (string).
# A função deve retornar a idade atual da pessoa em anos (inteiro). Use o módulo `datetime`.
def calcular_idade(data_nascimento_str: str) -> int:
    """Calcula a idade a partir de uma data de nascimento em string."""
    # SEU CÓDIGO VEM AQUI
    pass

# PROJETO 9: VERIFICADOR DE PALÍNDROMO
# Crie uma função `eh_palindromo` que verifica se uma palavra ou frase é um palíndromo.
# A função deve ignorar espaços, pontuações e diferenças entre maiúsculas e minúsculas.
# Um palíndromo é uma palavra que se lê da mesma forma de trás para frente (ex: "ovo", "Anotaram a data da maratona").
def eh_palindromo(texto: str) -> bool:
    """Verifica se um texto é um palíndromo, ignorando espaços e pontuação."""
    # SEU CÓDIGO VEM AQUI
    pass

# PROJETO 10: FORMATADOR DE NOMES DE ARQUIVOS
# Crie uma função `formatar_nomes_arquivos` que recebe uma lista de nomes de arquivos e `**kwargs` com regras de formatação.
# Regras possíveis: `para_minusculas=True`, `remover_espacos=True` (substitui por '_'), `remover_acentos=True`.
def formatar_nomes_arquivos(lista_nomes: list, **regras) -> list:
    """Formata uma lista de nomes de arquivos aplicando um conjunto de regras via kwargs."""
    # SEU CÓDIGO VEM AQUI
    pass


# =================================================================================
# ÁREA DE TESTES
# Descomente as linhas abaixo para testar suas funções.
# =================================================================================

print("--- Testes Nível Fácil ---")
# print(f"O número 4 é par? {eh_par(4)}")  # Esperado: True
# print(f"O número 7 é par? {eh_par(7)}")  # Esperado: False
# print(f"100°C em Fahrenheit é: {celsius_para_fahrenheit(100):.2f}°F")  # Esperado: 212.00
# print(f"Vogais em 'Python é Incrível': {contar_vogais('Python é Incrível')}")  # Esperado: 5
# print(f"Estatísticas de [10, 20, 30, 40, 50]: {calcular_estatisticas([10, 20, 30, 40, 50])}") # Esperado: {'media': 30.0, 'maior': 50, 'menor': 10}
print("-" * 30)

print("--- Testes Nível Médio ---")
# print(f"Números maiores que 20 em [10, 25, 5, 40, 15]: {filtrar_lista([10, 25, 5, 40, 15], 20)}") # Esperado: [25, 40]
# print(f"CPF '12345678900' é válido? {validar_cpf_simples('12345678900')}") # Esperado: True
# print(f"CPF '123.456.789-00' é válido? {validar_cpf_simples('123.456.789-00')}") # Esperado: False
# senha_media = gerar_senha(10)
# print(f"Senha média gerada (10 chars): {senha_media} (Tamanho: {len(senha_media)})") # Esperado: Uma string aleatória de 10 caracteres
print("-" * 30)

print("--- Testes Nível Difícil ---")
# print(f"Idade para quem nasceu em 15/05/1990: {calcular_idade('15/05/1990')} anos") # Esperado: A idade correta (ex: 35 se hoje for 2025)
# print(f"'Anotaram a data da maratona' é palíndromo? {eh_palindromo('Anotaram a data da maratona')}") # Esperado: True
# print(f"'Python' é palíndromo? {eh_palindromo('Python')}") # Esperado: False
# arquivos = ["Relatório Anual.docx", "FOTO DA REUNIÃO.JPEG"]
# print(f"Arquivos formatados: {formatar_nomes_arquivos(arquivos, para_minusculas=True, remover_espacos=True, remover_acentos=True)}")
# Esperado: ['relatorio_anual.docx', 'foto_da_reuniao.jpeg']
print("-" * 30)