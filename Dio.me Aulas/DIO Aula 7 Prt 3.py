class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Ave (Animal):
    def __init__(self, cor_bico, **kw ):
        self.cor_bico = cor_bico
        super().__init__(**kw)    
       
        



class Mamifero (Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        



    
#class Cachorro (Mamifero):
#    pass

class Cat (Mamifero):   
    pass

#class Leao (Mamifero):
#    pass

class Ornitorrinco (Mamifero, Ave):
    pass

gato = Cat(nmr_patas=4, cor_pelo="Preto")


ornitorrinco = Ornitorrinco(nmr_patas=2, cor_pelo="Marrom", cor_bico="Preto")

print(gato)