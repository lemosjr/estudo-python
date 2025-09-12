#4. Conta bancária
#Um banco deseja implementar um sistema de contas.

#• Cada conta tem número, titular e saldo.
#• Deve permitir depositar, sacar e mostrar o saldo.
#Questão:
#Implemente uma classe ContaBancaria que simule operações básicas. Crie duas
#contas diferentes e faça transferências entre elas.

class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado na conta {self.numero}.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado na conta {self.numero}.")
            return True
        elif valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        else:
            print(f"Saldo insuficiente na conta {self.numero}. Saldo atual: R$ {self.saldo:.2f}")
            return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            print(f"Transferência de R$ {valor:.2f} da conta {self.numero} para a conta {destino.numero} concluída.")
            return True
        else:
            print("Transferência cancelada.")
            return False
            
    def mostrar_saldo(self):
        print(f"Conta: {self.numero}, Titular: {self.titular}, Saldo: R$ {self.saldo:.2f}")

print("--- Criando Contas ---")
conta_joao = ContaBancaria("12345-6", "João Silva")
conta_maria = ContaBancaria("78901-2", "Maria Oliveira")

conta_joao.mostrar_saldo()
conta_maria.mostrar_saldo()

print("\n--- Operações de Depósito ---")

conta_joao.depositar(1000.00)
conta_joao.mostrar_saldo()

conta_maria.depositar(500.00)
conta_maria.mostrar_saldo()

print("\n--- Transferência entre Contas ---")
valor_transferencia = 300.00
conta_joao.transferir(valor_transferencia, conta_maria)

conta_joao.mostrar_saldo()
conta_maria.mostrar_saldo()

print("\n--- Tentativa de Saque e Transferência Inválida ---")

conta_joao.sacar(800.00)
conta_joao.transferir(500.00, conta_maria)

conta_joao.mostrar_saldo()
conta_maria.mostrar_saldo()