#3. Loja online
#Uma loja virtual precisa controlar seus produtos e pedidos.
#• Cada produto tem nome e preço.
#• O pedido pode ter vários produtos com uma quantidade.
#• O sistema deve calcular o total do pedido.
#Questão:
#Crie uma classe Produto e uma classe Pedido que permita adicionar produtos e
#calcular o valor total. Monte um pedido com pelo menos 3 produtos.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        self.itens.append({'produto': produto, 'quantidade': quantidade})
        print(f"Adicionado {quantidade}x {produto.nome} ao pedido.")

    def calcular_total(self):
        total = 0
        for item in self.itens:
            preco_item = item['produto'].preco * item['quantidade']
            total += preco_item
        return total

meu_pedido = Pedido()

print("--- Montagem do Pedido ---")

for i in range(1, 4):
    print(f"\nProduto {i}:")
    nome_produto = input("Digite o nome do produto: ")

    while True:
        try:
            preco_produto = float(input("Digite o preço do produto: R$ "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o preço.")

    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a quantidade.")

    produto = Produto(nome_produto, preco_produto)
    meu_pedido.adicionar_produto(produto, quantidade_produto)

total_final = meu_pedido.calcular_total()

print("\n--- Resumo do Pedido ---")
for item in meu_pedido.itens:
    produto = item['produto']
    quantidade = item['quantidade']
    subtotal = produto.preco * quantidade
    print(f"- {produto.nome}: {quantidade}x a R$ {produto.preco:.2f} = R$ {subtotal:.2f}")

print(f"\nTotal do Pedido: R$ {total_final:.2f}")