# 10. Sistema de Aprovação de Empréstimo
print("\n--- Exercício 10: Aprovação de Empréstimo ---")
renda = float(input("Qual sua renda mensal? R$ "))
idade = int(input("Qual sua idade? "))
valor_emprestimo = float(input("Qual o valor do empréstimo desejado? R$ "))
parcelas = int(input("Em quantas parcelas? "))

valor_parcela = valor_emprestimo / parcelas
limite_parcela = renda * 0.30

if not (22 <= idade <= 65):
    print("Empréstimo Negado: A idade deve estar entre 22 e 65 anos.")
elif valor_emprestimo < 1000:
     print("Empréstimo Negado: O valor mínimo do empréstimo é de R$ 1.000,00.")
elif valor_parcela > limite_parcela:
    print(f"Empréstimo Negado: O valor da parcela (R$ {valor_parcela:.2f}) excede 30% da sua renda (R$ {limite_parcela:.2f}).")
else:
    print("Empréstimo Aprovado!")
    print(f"O valor da sua parcela será de R$ {valor_parcela:.2f}.")