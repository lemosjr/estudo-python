# 6. Classificação de Triângulos
print("\n--- Exercício 6: Classificação de Triângulos ---")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))
if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é Escaleno.")
