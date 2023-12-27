class Pessoa:
    def __init__(self, nome, ano_nascimeto):
        self._nome = nome
        self._ano_nascimento = ano_nascimeto

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2023

        return _ano_atual - self._ano_nascimento

        
pessoa = Pessoa('Tk', 1998)

print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}")
