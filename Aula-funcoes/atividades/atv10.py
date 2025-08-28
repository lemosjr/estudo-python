# PROJETO 10: FORMATADOR DE NOMES DE ARQUIVOS
# Crie uma função `formatar_nomes_arquivos` que recebe uma lista de nomes de arquivos e `**kwargs` com regras de formatação.
# Regras possíveis: `para_minusculas=True`, `remover_espacos=True` (substitui por '_'), `remover_acentos=True`.
def formatar_nomes_arquivos(lista_nomes: list, **regras) -> list:
    def aplicar_regras(nome: str) -> str:
        if regras.get("para_minusculas"):
            nome = nome.lower()
        if regras.get("remover_espacos"):
            nome = nome.replace(" ", "_")
        if regras.get("remover_acentos"):
            nome = nome.normalize("NFKD").encode("ascii", "ignore").decode("utf-8")
        return nome

    return [aplicar_regras(nome) for nome in lista_nomes]

print(formatar_nomes_arquivos(["Arquivo 1.txt", "Arquivo 2.txt"], para_minusculas=True, remover_espacos=True))
"""Formata uma lista de nomes de arquivos aplicando um conjunto de regras via kwargs."""

