info = []


class Test:
    def __init__(self, nome, idade, voce):
        self.nome = nome
        self.idade = idade
        self.voce = voce        

nome_input = input('nome: ')
idade_input = int(input('Idade: '))




c1 = Test(nome_input, idade_input, 'vcoe nao sabe')

info.append(c1)

for obj in info:
    
    print(obj.nome)
    
    if obj.idade == 21:
        print('Como assim? ')
    else:
        print(obj.voce)



       



        