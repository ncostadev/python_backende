
class Banco:
    def __init__(self, saldo = 0):
        self.__saldo = saldo

    @property # Isso faz com que pra acessar o "self.saldo" tenha que usar uma função, fazendo com informações fique mais seguro.
    def saldo_E50(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            print('Valor deve ser positivo')
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            print('Não é possível sacar')
        
        if self.__saldo <= 0:
            print('Saldo insuficiente!')
        
        self.__saldo -= valor
            
            


# p1 = Banco()
# p1.depositar(100)
# print(p1.saldo_E50)
# p1.sacar(-100)
# print(p1.saldo_E50)


# Herança 
class Conta(Banco):
    def __init__(self, num_conta, cliente, agencia = 455, saldo=0):
        super().__init__(saldo)
        self.num_conta = num_conta
        self.clinte = cliente
        self.agencia = agencia
        

    def info(self):
        print('-'*20)
        print(f'Agencia: {self.agencia}\nConta: {self.num_conta}\nNome: {self.clinte}\nSaldo: R${self.saldo_E50}')
        print('-'*20)

p2 = Conta(23232323, 'Nathan', saldo = 15000)
p2.info()

