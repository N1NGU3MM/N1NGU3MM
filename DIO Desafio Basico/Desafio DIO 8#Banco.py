saldo = 1500
saque_m = 500
LIMITE = 3
saque_3 = 0

extrato = [] 

def saldo_conta():
    global saldo
    return saldo

def conta_1():
    


    def HOME():
        menu = '''
        [1] Saldo\n
        [2] Saque\n
        [3] Depósito\n
        [4] Extrato\n
        [5] Sair\n'''
        print(menu)
        
        
    def SAQUE():
        global saldo, saque_3
    
    
        valor = int(input('Qual o valor que deseja sacar? '))
            
        if valor >= saque_m:
            print(f'O valor de R${valor}, está acima do limite permitido em sua conta.\nO limite permitido em sua conta é de saque por vez em sua conta é de R${saque_m}')
            
        elif saldo < valor:
                print('Saldo insuficiente, verifique o valor disponível em sua conta.')
            
        elif saque_3 == LIMITE:
            print(f'Quantidade máximo de saque dirairo atingido.\nLimite diário de {LIMITE} saques diário.')
            
        else:
            print(f'Saque no valor de R$ {valor} foi realizado com sucesso.')
            
            saque_3 += 1
            saldo -= valor
            extrato.append(f'- R$ {valor}')

    def depositar():
        global saldo
        
        
        desposito = int(input('Qual o valor que voce deseja depositar em sua conta?  '))
        saldo = saldo + desposito
        
        extrato.append(f'+ R${desposito}')
        
                    
    while True:
        HOME()
        
        opcao = int(input('Selecione uma das opções acima: '))
        
        if opcao == 1: 
            print(saldo)
        
        elif opcao == 2:
            SAQUE()
        
        if opcao == 3:
            depositar()
        
        if opcao == 4:
            print(f'Gerando extrato\n==========\n{extrato}\n==========\nSaldo total em sua conta R${saldo}')
            
               
        if opcao == 5:
            break

saldo_conta2 = 1500
saque_m_conta2 = 500
LIMITE2 = 3
saque_2 = 0

extrato = [] 

def saldo_conta_2():
    global saldo_conta2
    return saldo_conta2

def conta_2():
    


    def HOME():
        menu = '''
        [1] Saldo\n
        [2] Saque\n
        [3] Depósito\n
        [4] Extrato\n
        [5] Sair\n'''
        print(menu)
        
        
    def SAQUE():
        global saldo_conta2, saque_2
    
    
        valor = int(input('Qual o valor que deseja sacar? '))
            
        if valor >= saque_m_conta2:
            print(f'O valor de R${valor}, está acima do limite permitido em sua conta.\nO limite permitido em sua conta é de saque por vez em sua conta é de R${saque_m_conta2}')
            
        elif saldo_conta2 < valor:
                print('Saldo insuficiente, verifique o valor disponível em sua conta.')
            
        elif saque_2 == LIMITE2:
            print(f'Quantidade máximo de saque dirairo atingido.\nLimite diário de {LIMITE2} saques diário.')
            
        else:
            print(f'Saque no valor de R$ {valor} foi realizado com sucesso.')
            
            saque_2 += 1
            saldo_conta2 -= valor
            extrato.append(f'- R$ {valor}')

    def depositar():
        global saldo_conta2
        
        
        desposito = int(input('Qual o valor que voce deseja depositar em sua conta?  '))
        saldo_conta2 = saldo_conta2 + desposito
        
        extrato.append(f'+ R${desposito}')
        
                    
    while True:
        HOME()
        
        opcao = int(input('Selecione uma das opções acima: '))
        
        if opcao == 1: 
            print(saldo_conta2)
        
        elif opcao == 2:
            SAQUE()
        
        if opcao == 3:
            depositar()
        
        if opcao == 4:
            print(f'Gerando extrato\n==========\n{extrato}\n==========\nSaldo total em sua conta R${saldo_conta2}')
            
               
        if opcao == 5:
            break


while True:
    
    print('''
          [1] Conta 1\n
          [2] Conta 2\n
          ''' )
    
    
    opcao = int(input('Qual opção você deseja escolher? '))
    
    if opcao == 1:
        conta_1()
    
    if opcao == 2:
        conta_2()
        