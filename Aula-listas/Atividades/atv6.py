# 6. Remoção e Modificação
# Observe o código a seguir.
# Qual será o conteúdo final da lista planetas após a execução de todas as linhas?

planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter']
planetas.pop(1) # Remove o item no índice 1
planetas.insert(3, 'Saturno')
planetas[0] = 'Planeta Anão' # Renomeia o primeiro item
print(planetas)