def numeros_de_garrafas(N, K):
    garrafas_cheias = N
    garrafas_vazias = N
    
    while garrafas_vazias >= K:
        trocas = garrafas_vazias // K
        garrafas_cheias += trocas
        garrafas_vazias -= trocas % K + garrafas_vazias
    
    return garrafas_cheias

T = int(input())
resultados= []

for _ in range(T):
    N, K = map(int, input().split())
    resultado = numeros_de_garrafas(N, K)
    resultados.append(resultado)
    
for resultado in resultados:
    print(resultado)
    
    
    

