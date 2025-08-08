# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# ARQUIVO DE ESTUDO: AULA COMPLETA SOBRE TUPLAS EM PYTHON
# -----------------------------------------------------------------------------

# --- 1. Definição de Tuplas ---
# Uma tupla é uma coleção de elementos ordenada e IMUTÁVEL.
# Sintaxe: Elementos entre parênteses (), separados por vírgulas.

print("--- 1. Definição ---")
minha_tupla = (1, "olá", 3.14, True)
print(f"Exemplo de tupla: {minha_tupla}")
print(f"Tipo da variável: {type(minha_tupla)}\n")

# --- 2. Características Principais ---
# A característica mais importante é a IMUTABILIDADE.
# Uma vez criada, seus elementos não podem ser alterados, adicionados ou removidos.

print("--- 2. Imutabilidade ---")
# A linha abaixo causará um erro (TypeError) se for descomentada,
# pois não é possível alterar um item da tupla.
# minha_tupla[0] = 99
print("Tuplas são imutáveis. O código 'minha_tupla[0] = 99' resultaria em erro.\n")

# --- 3. Operações Comuns ---
print("--- 3. Operações Comuns ---")

# Acessando elementos por índice (começa em 0)
frutas = ("maçã", "banana", "cereja", "uva")
print(f"Acessando o primeiro elemento: {frutas[0]}")
print(f"Acessando o último elemento: {frutas[-1]}\n")

# Fatiamento (Slicing) - Gera uma NOVA tupla
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
fatia = numeros[2:5]  # Do índice 2 ao 4 (o 5 não é incluído)
print(f"Tupla original: {numeros}")
print(f"Fatia [2:5]: {fatia}\n")

# Concatenação (+) - Gera uma NOVA tupla
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2
print(f"Concatenação: {tupla1} + {tupla2} = {tupla_concatenada}\n")

# Repetição (*) - Gera uma NOVA tupla
som = ("eco",) * 3
print(f"Repetição: ('eco',) * 3 = {som}\n")

# IMPORTANTE: Tupla com um único elemento
# É necessário ter uma vírgula no final.
tupla_de_um_elemento = (42,)
nao_e_tupla = (42) # Isso será um inteiro (int)
print(f"Tupla com um elemento: {tupla_de_um_elemento} (tipo: {type(tupla_de_um_elemento)})")
print(f"Isto NÃO é uma tupla: {nao_e_tupla} (tipo: {type(nao_e_tupla)})\n")

# --- 4. Desempacotamento (Unpacking) ---
# Uma forma elegante de atribuir os valores de uma tupla a variáveis.
print("--- 4. Desempacotamento ---")
# Exemplo 1: Coordenadas
coordenadas = (10, 20)
x, y = coordenadas
print(f"A tupla {coordenadas} foi desempacotada em x={x} e y={y}\n")

# Exemplo 2: Função retornando múltiplos valores (na verdade, retorna uma tupla)
def obter_nome_completo():
  nome = "João"
  sobrenome = "Silva"
  return (nome, sobrenome) # O parêntese é opcional aqui: return nome, sobrenome

primeiro_nome, ultimo_nome = obter_nome_completo()
print(f"Função retornou a tupla ('{primeiro_nome}', '{ultimo_nome}')")
print(f"Valores desempacotados: primeiro_nome='{primeiro_nome}', ultimo_nome='{ultimo_nome}'\n")


# --- 5. Tuplas Nomeadas (Named Tuples) ---
# Tornam o código mais legível ao permitir acesso aos elementos por nome.
# Precisam ser importadas do módulo `collections`.
print("--- 5. Tuplas Nomeadas ---")

from collections import namedtuple

# 1. Definir o "molde" da tupla nomeada
#    Sintaxe: namedtuple('NomeDoTipo', ['campo1', 'campo2', ...])
Ponto = namedtuple('Ponto', ['x', 'y', 'z'])

# 2. Criar uma instância (a tupla nomeada em si)
p1 = Ponto(10, 20, 5)

# 3. Acessar os valores pelo nome (mais legível) ou pelo índice
print(f"Tupla nomeada: {p1}")
print(f"Acessando por nome (p1.x): {p1.x}")
print(f"Acessando por índice (p1[1]): {p1[1]}\n")


# --- 6. Casos de Uso ---
print("--- 6. Casos de Uso ---")

# Como chaves de dicionário (listas não podem ser usadas)
localizacoes = {
    ("São Paulo", "SP"): "Sudeste",
    ("Fortaleza", "CE"): "Nordeste",
    ("Curitiba", "PR"): "Sul"
}

cidade_estado = ("Fortaleza", "CE")
print(f"Usando a tupla {cidade_estado} como chave de dicionário:")
print(f"A região é: {localizacoes[cidade_estado]}\n")


# Para garantir a integridade dos dados
# Ex: Configurações que não devem mudar durante a execução
CONFIGURACOES_DB = ("localhost", "5432", "meu_usuario", "senha_secreta")
print(f"Configurações do banco (não devem ser alteradas): {CONFIGURACOES_DB}")