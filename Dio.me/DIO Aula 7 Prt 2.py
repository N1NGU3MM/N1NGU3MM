# Herança simples

class veiculo:
    def __init__(self, cor, placa, numero_rodas ): 
        self.cor = cor 
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print('Ligando motor...')
    
    def __str__(self):
        return self.cor

class moto (veiculo):
    pass

class carro (veiculo):
    pass

class caminhao (veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado): 
        super().__init__(cor, placa, numero_rodas) # super().__init__  is used for import a object of a class
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'SIM' if self.carregado else 'NÃO'} estar carregado.")


moto = veiculo('Branca', 'ABC-123', 2)
moto.ligar_motor()

carro = veiculo('Azul', 'ASD-321', 4)
carro.ligar_motor()

caminhao = caminhao('Rosa', 'HJK-532', 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)


