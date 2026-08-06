
class Contar:
    contador = 0

    def dimi(self):
        self.contador -= 1

    def aumen(self):
        self.contador += 1

tes = Contar()

print('\n')
print(tes.contador)
tes.aumen()
tes.aumen()
tes.aumen()
print(tes.contador)
tes.dimi()
print(tes.contador)
