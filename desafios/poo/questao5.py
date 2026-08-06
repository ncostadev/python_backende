
class Livro:
    livro1 = 'Programador'

    def dispo(self):
        if self.livro1 == '':
            print('Indisponível')
        else:
            print('Disponível')

p1 = Livro()
print('\n')
p1.dispo()
