# PROJETO 2: CONVERSOR DE TEMPERATURA
# Crie uma função `celsius_para_fahrenheit` que recebe uma temperatura em Celsius e a retorna em Fahrenheit.
# Fórmula: F = (C * 9/5) + 32
def celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

print(celsius_para_fahrenheit(0))  # Exemplo de uso