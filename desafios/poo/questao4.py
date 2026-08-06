
class Produto:
    valor = 350
    def desconto(self):
        des = (self.valor * 15) / 100
        self.valor -= des
        return f'R${self.valor} Com desconto de 15%'

cliente1 = Produto()

print(cliente1.valor)
print(cliente1.desconto())

