#
# Orientação de objetos (POO)


# (POO) paradigma de progamação 

class Bike:
    def __init__(self, cor, modelo, ano, valor): 
        self.cor = cor  
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('plin, plin')
    
    def stop(self):
        print('Stop Bike')
    
    def run(self):
        print('Vrummmmmmm...') 
    
#    def __str__(self):
#        return f'Bike: {self.cor}, {self.modelo}, {self.ano}. {self.valor}' 
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    
#    def get_cor(self):
#       return self.cor

bmx = Bike('vermelha', 'bmx', 2022, 600)  

bmx.buzinar()
bmx.run()
bmx.stop()
print(bmx.cor, bmx.modelo, bmx.ano, bmx.valor)

#b2 = Bike('Blue', 'Caloi', '2002', '200')

#Bike.stop(b2)
#print(b2.get_cor()) 