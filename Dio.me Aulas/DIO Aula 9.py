class Passaro:
    def voar (self):
        print('Voando...')

class pardal(Passaro):
    def vaor(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Aveztruz não pode voar...')

class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando... ')


def plano_voo(obj):
    obj.voar() 

p1 = pardal()
p2 = Avestruz()
p3 = Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)
