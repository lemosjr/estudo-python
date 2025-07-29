# 8. Desconto da Loja (Operador Ternário)
print("\n--- Exercício 8: Desconto com Operador Ternário ---")
valor_compra = float(input("Digite o valor da compra: R$ "))
valor_final = valor_compra * 0.9 if valor_compra > 50 else valor_compra
print(f"O valor final a pagar é R$ {valor_final:.2f}")
