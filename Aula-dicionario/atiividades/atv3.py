# Atividade 3: Glossário de Termos

# Enunciado: Crie um dicionário com três termos de programação e suas definições.

# Em seguida, use um laço for e o método .items() para imprimir cada termo e sua definição de forma organizada.

# Dica: O laço for chave, valor in dicionario.items(): é perfeito para esta tarefa.

# Resultado Esperado (Exemplo):

#   Termo: Variavel
#   Definicao: Espaco na memoria para armazenar dados que podem mudar.

#   Termo: Loop
#   Definicao: Estrutura de repeticao que executa um bloco de codigo varias vezes.

#   Termo: Funcao
#   Definicao: Bloco de codigo reutilizavel que realiza uma tarefa especifica.

glossario = {
    "Variavel": "Espaco na memoria para armazenar dados que podem mudar.",
    "Loop": "Estrutura de repeticao que executa um bloco de codigo varias vezes.",
    "Funcao": "Bloco de codigo reutilizavel que realiza uma tarefa especifica."
}

for termo, definicao in glossario.items():
    print(f"  Termo: {termo}")
    print(f"  Definicao: {definicao}")
    print()