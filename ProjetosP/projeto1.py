PAGAR = -1


while PAGAR != 0:  

    VIAGEM = float(input('Digite quantos quílometros tera a sua viajem: '))
    VALOR_DA_VIAGEM = 0.90  
    VALOR = VIAGEM * VALOR_DA_VIAGEM 
    
    if VALOR > 0:
        print(f'O valor que custará a sua viagem é R${round(VALOR, 3)}!')
    
    elif VALOR == 0:
        break
