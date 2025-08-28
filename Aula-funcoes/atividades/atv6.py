# PROJETO 6: VALIDADOR DE CPF SIMPLES
# Crie uma função `validar_cpf_simples` que recebe uma string `cpf`.
# A função deve retornar True se o CPF tiver exatamente 11 dígitos numéricos e False caso contrário.
# Não é necessário validar os dígitos verificadores, apenas o formato.
def validar_cpf_simples(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit()

print(validar_cpf_simples("12345678901"))  # Exemplo de uso