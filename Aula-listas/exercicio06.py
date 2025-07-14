# --------------------
# 6. Lista de Compras Interativa
# --------------------
# Crie um programa que simule uma lista de compras. O programa deve permitir que o usuário:
# a. Adicione um item à lista.
# b. Remova um item da lista.
# c. Visualize a lista completa.
# O programa deve continuar rodando até que o usuário decida sair.
# * Dica: Use um laço 'while True' e peça a entrada do usuário (input()) para decidir qual ação tomar.

lista_compras = []

while True:
    menu = input(f'''
1 - Adicionar item
2 - Remover item
3 - Ver lista
4 - Sair                                    
Entrada:''')
    if menu == "1":
        adicionar = lista_compras.append(input("Digite o item a ser adicionado:"))
        print(lista_compras)
        print(len(lista_compras))
    elif menu == "2":
        item_para_remover = input("Digite o nome do item a ser removido: ")
        if item_para_remover in lista_compras:
            lista_compras.remove(item_para_remover)
            print(f"'{item_para_remover}' removido da lista.")
        else:
            print(f"'{item_para_remover}' não foi encontrado na lista.")
    elif menu == "3":
        print(lista_compras)
    elif menu == "4":
        print("Encerrando programa.")
        break
