#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AULA COMPLETA SOBRE CONDICIONAIS EM PYTHON

Este arquivo serve como uma aula e um script executável.
Leia os comentários para entender os conceitos e veja o código em ação.

Para executar, salve como um arquivo .py e rode no terminal:
python nome_do_arquivo.py
"""

# =============================================================================
# O BÁSICO: IF, ELIF E ELSE
# =============================================================================
# As estruturas condicionais permitem que o código tome decisões.
# Elas executam ações diferentes com base em se uma condição é verdadeira ou falsa.

print("--- Seção: O Básico: if, elif e else ---")

# --- 1. A Declaração `if` ---
# A declaração `if` testa uma condição. Se for True (verdadeira),
# o bloco de código indentado abaixo dela é executado.

print("\n[Exemplo 1: Usando if]")
idade = 20
print(f"Testando com idade = {idade}")

if idade >= 18:
    print("✅ Acesso permitido! Você é maior de idade.")

# Se a idade fosse 15, nada seria impresso nesta parte.


# --- 2. A Declaração `else` ---
# O `else` executa um bloco de código quando a condição do `if` é False (falsa).
# Ele funciona como um "caso contrário".

print("\n[Exemplo 2: Usando if-else]")
idade = 15
print(f"Testando com idade = {idade}")

if idade >= 18:
    print("✅ Acesso permitido! Você é maior de idade.")
else:
    print("🚫 Acesso negado! Você é menor de idade.")


# --- 3. A Declaração `elif` ---
# O `elif` (else if) permite verificar múltiplas condições em sequência.
# O Python executa o bloco da primeira condição verdadeira que encontrar e ignora o resto.

print("\n[Exemplo 3: Usando if-elif-else]")
idade = 14
print(f"Testando com idade = {idade} para classificação de filmes.")

if idade >= 18:
    print("Você pode assistir a qualquer filme.")
elif idade >= 16:
    print("Você pode assistir a filmes de classificação até 16 anos.")
elif idade >= 12:
    print("Você pode assistir a filmes com classificação até 12 anos.")
else:
    print("Você só pode assistir a filmes com classificação livre.")


# =============================================================================
# CONDICIONAIS E OPERADORES LÓGICOS (and, or, not)
# =============================================================================
# Para criar condições mais complexas.
# and: Verdadeiro somente se AMBAS as condições forem verdadeiras.
# or:  Verdadeiro se PELO MENOS UMA das condições for verdadeira.
# not: Inverte o resultado da condição (True vira False, False vira True).

print("\n\n--- Seção: Operadores Lógicos ---")

# --- 4. Usando o operador `and` ---
print("\n[Exemplo 4: Usando 'and' para login]")
usuario_correto = "admin"
senha_correta = "12345"
usuario_digitado = "admin"
senha_digitada = "12345"
print(f"Tentativa de login com usuário '{usuario_digitado}' e senha '{senha_digitada}'.")

if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
    print("✅ Login bem-sucedido!")
else:
    print("🚫 Usuário ou senha incorretos.")

# --- 5. Usando o operador `or` ---
print("\n[Exemplo 5: Usando 'or' para verificar fim de semana]")
dia_semana = "Sábado"
print(f"Verificando se '{dia_semana}' é fim de semana.")

if dia_semana == "Sábado" or dia_semana == "Domingo":
    print("🎉 É fim de semana!")
else:
    print("É dia de semana.")


# =============================================================================
# TÓPICOS AVANÇADOS
# =============================================================================
print("\n\n--- Seção: Tópicos Avançados ---")

# --- 6. Condicionais Aninhadas ---
# É possível colocar uma estrutura condicional dentro de outra.
# Útil para verificações em múltiplos níveis.

print("\n[Exemplo 6: Condicionais Aninhadas para descontos]")
eh_membro = True
valor_compra = 150
print(f"Cliente é membro? {eh_membro}. Valor da compra: R${valor_compra}")

if eh_membro:
    print("Cliente é membro. Verificando valor da compra...")
    if valor_compra > 100:
        print("🎉 Parabéns! Você ganhou um desconto especial de 15%.")
    else:
        print("Como membro, você ainda ganha 5% de desconto.")
else:
    print("Torne-se membro para aproveitar nossos descontos!")


# --- 7. Operador Ternário (Expressão Condicional) ---
# Uma forma compacta de escrever um if-else simples, geralmente para atribuição de valores.
# Sintaxe: valor_se_verdadeiro if condicao else valor_se_falso

print("\n[Exemplo 7: Operador Ternário]")
idade = 20
print(f"Usando operador ternário para a idade = {idade}")

status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(f"Status: {status}")


# --- 8. Verdadeiro ou Falso Implícito (Truthiness) ---
# Em Python, vários valores são avaliados como False:
# - Números zero (0, 0.0)
# - Coleções vazias ([], (), {}, "")
# - O objeto None
# Quase todo o resto é avaliado como True.

print("\n[Exemplo 8: Truthiness para verificar listas]")

lista_de_compras_cheia = ["Maçã", "Banana", "Leite"]
lista_de_compras_vazia = []

# Testando com a lista cheia
print(f"\nTestando com a lista: {lista_de_compras_cheia}")
if lista_de_compras_cheia: # Em vez de `if len(lista_de_compras_cheia) > 0:`
    print("Sua lista de compras não está vazia.")
else:
    print("Sua lista de compras está vazia.")

# Testando com a lista vazia
print(f"\nTestando com a lista: {lista_de_compras_vazia}")
if lista_de_compras_vazia:
    print("Sua lista de compras não está vazia.")
else:
    print("Sua lista de compras está vazia.")


print("\n\nFim da aula sobre condicionais!")