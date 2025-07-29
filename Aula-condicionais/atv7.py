# 7. Calculadora de IMC
print("\n--- Exercício 7: Calculadora de IMC ---")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}") # :.2f formata para 2 casas decimais
if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc < 25:
    print("Classificação: Peso normal.")
elif imc < 30:
    print("Classificação: Sobrepeso.")
else:
    print("Classificação: Obesidade.")