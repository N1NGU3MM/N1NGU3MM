class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'

def mostar_valor(*objs):
    for obj in objs:
        print(obj)


aluno1 = Estudante ('Umpa', 1)
aluno2 = Estudante ('Lumpa', 2)

print(aluno1)
print(aluno2)

aluno1.matricula = 1
mostar_valor(aluno1, aluno2)

Estudante.escola = "Py"
aluno3 = Estudante('Up', 3)
print(aluno3)
