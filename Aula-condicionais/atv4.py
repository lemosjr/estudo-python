# 4. Verificador de Vogal ou Consoante
print("\n--- Exercício 4: Vogal ou Consoante ---")
letra = input("Digite uma letra: ").lower() # .lower() converte para minúscula
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")
