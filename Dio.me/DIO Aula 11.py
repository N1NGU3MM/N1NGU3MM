class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def ano_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano

        return cls(idade, nome)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18




ps = Pessoa('Uzuma', 20)
print(ps.nome, ps.idade)


p = Pessoa.ano_nascimento(1998, 2, 21, 'Sukuma')
print(p.nome, p.idade)


print(Pessoa.maior_de_idade(18))

print(Pessoa.maior_de_idade(9))

