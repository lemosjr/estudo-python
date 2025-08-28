# PROJETO 1: VERIFICADOR DE NÚMERO PAR
# Crie uma função `eh_par` que recebe um número e retorna True se ele for par e False caso contrário.
def eh_par(numero: int) -> bool:
    return numero % 2 == 0

print(eh_par(4))  # Exemplo de uso