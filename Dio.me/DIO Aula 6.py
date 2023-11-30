# construtores e destrutores 
# conhecendo __init__ e __del__

# Esses tipos de codigos são chamados de codigos 
# expeciais e é super importante saber as funções,
# de cada um deles.



# Método CONSTRUTOR
class dog:
    def __init__(self, nome, cor, acordado=True):
        
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self): # Assim que tudo for executado o  DEL ira excluir tudo, sempre sera excutado no final.
        print('Removendo instancia da classe.')
    
    def talk (self):
         
            print('Au Au...')


c1 = dog("Kiko", "Preto e Branco")
c1.talk()

        
# Método DESTRUTOR

# __del__ é usado para fazer uma função antes de ser excluido uma ação

class dog:
    def __del__(self):
        print('Destruindo a instância')

c = dog 
del c   

