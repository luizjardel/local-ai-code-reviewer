class Conta:

    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor


    def sacar(self, valor):
        if self.saldo <= valor:
            return False
        else:
            self.saldo -= valor
            return True



c1 = Conta(1, 123445521, "Jardel", 9000)
c1.depositar(500)
c1.sacar(1000)

valor_saque =  20000
resultado_saque = c1.sacar(valor_saque)
if resultado_saque:
    print(f"Saque de R$ {valor_saque} realizado com sucesso")
else:
    print(f"Saldo insuficiente")
print(f"Nome do titular na conta: {c1.nomeTitular}")
print(f"Numero da conta: {c1.numero}")
print(f"CPF do titular da conta: {c1.cpf}")
print(f"Saldo da conta: {c1.saldo}")