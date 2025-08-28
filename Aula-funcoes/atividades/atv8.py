# PROJETO 8: CALCULADORA DE IDADE
# Crie uma função `calcular_idade` que recebe uma data de nascimento no formato "dd/mm/aaaa" (string).
# A função deve retornar a idade atual da pessoa em anos (inteiro). Use o módulo `datetime`.

from datetime import datetime


def calcular_idade(data_nascimento_str: str) -> int:
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    return idade

print(calcular_idade("15/04/1990"))  # Exemplo de uso  