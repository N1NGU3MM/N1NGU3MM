## Criando um sistema bancário


def SISTEMA_BANCARIO():
    menu = '''
    d = Depositar
    s = Sacar
    e = Extrato
    q = Sair 
    '''
    saldo_da_conta = 1500
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    transacoes = []
    
    while True:
        
        opção = input(menu)
        
        if opção == 'd':
            print('Depósito')
            deposito = int(input('Qual o valor para depósito? '))
            saldo_da_conta += deposito
            transacoes.append(f'Depósito de R${deposito}')
            print(f'O valor em seu conta é de R${saldo_da_conta}')
            
        elif opção == 's':
                print('Sacar')
                valor_sacado = int(input("Qual o valor que deseja sacar? "))

                
                if numero_saques == LIMITE_SAQUES:
                    print(f'Limite de {LIMITE_SAQUES} saques diario maximo atingido')
                    
                elif valor_sacado <= limite:
                    if valor_sacado <= saldo_da_conta:
                        saldo_da_conta -= valor_sacado
                        numero_saques += 1
                    print(f'Você sacou o valor de R${valor_sacado}')
                    transacoes.append(f'Saque de R${valor_sacado}')
                else:
                        print(f'Limite maximo para saque R${limite}. ')
                        

        
        elif opção == 'e':
            print(f'Extrato: R${saldo_da_conta}')
            print(transacoes )

        elif opção == 'q':
            break
        
        
SISTEMA_BANCARIO()