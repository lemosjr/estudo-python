# 9. Validação de Ano Bissexto
print("\n--- Exercício 9: Ano Bissexto ---")
ano = int(input("Digite um ano para verificar se é bissexto: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")