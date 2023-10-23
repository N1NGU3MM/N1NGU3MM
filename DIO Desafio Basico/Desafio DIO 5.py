def mensagem(nivel_energia):
    if nivel_energia <= 8000:
        return 'Inseto!'
    else:
        return 'Mais de 8000!'


C = int(input())

for _ in range(C):
    nivel_energia= int(input())
    resposta = mensagem(nivel_energia)
    print(resposta)