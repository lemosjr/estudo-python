# PROJETO 7: GERADOR DE SENHAS
# Crie uma função `gerar_senha` que recebe um `comprimento` e gera uma senha aleatória com letras e números.

import random
import string


def gerar_senha(comprimento: int) -> str:
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

print(gerar_senha(12))  # Exemplo de uso