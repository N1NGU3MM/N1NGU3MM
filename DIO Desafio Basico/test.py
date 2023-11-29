
lista_nome = []

# saldo = 1500
LIMITE = 500
LIMITE_SAQUE = 3
#numero_saque = 0

extrato = {} 

def saldo_conta():
    global saldo
    return saldo

def nomes():
        
    global lista_nome
    return lista_nome

while True:
    
    
    
    def menu_inicial():
        print(""" 
              Bem Vindo\n
              Selecione uma das opções abaixo\n
              
              [1] Criar uma conta
              [2] Já sou cliente
              [3] Sair""")
        
        
        menu = int(input('Qual opção você deseja? '))
        
        if menu == 1:
            criar_conta()
        
        if menu == 2:
            cliente()
        
        if menu == 3:
            print('''kkkkkkkkk\2 
                  Não deu pra para sair\n 
                  Acabou o FREIOOOOOO!''')
            
                 
    def criar_conta():
        
        start = int(input('Você deseja criar a sua conta?\n [1] para SIM\n [2] para NÃO.\n'))
        
        
        if start == 1:
            criando_conta()
        
        if start == 2:
            menu_inicial()
        else:
            print('Opção invalida')
            criar_conta()
            return
            

    def criando_conta():
        
       
             
        cpf = int(input('Diga seu CPF? '))
        data_de_nascimento = int(input('Qual a ano do seu nascimento? '))
        nome = input('Digite seu nome completo: ')
        endereço_cidade = input('Qual sua cidade? ')
        rua = input('Qual o nome da sua rua? ')
        estado = input('Qual seu estado? ')
        
        localizacao = {'cidade': endereço_cidade, 'rua': rua, 'estado': estado}
        
           
        #nascimento = int(input('Qual ano você nasceu? '))


        for conta in lista_nome:
            if cpf == conta['cpf']:
                print('Esse nome ja foi informado!')
                menu_inicial()
        
        else:
            nova_conta = {'cpf': cpf, 'nascimento': 2, 'saldo': 1500, 'numero_saque': 0, 'extrato': [], 
                          'data_de_nascimente': data_de_nascimento, 'cpf': cpf, 'localização': localizacao,'nome': nome } 
            
            lista_nome.append(nova_conta)
            print('Conta criada!')
            menu_inicial()
            return
            
            
        

        
        

    def cliente():

        
        cpf = int(input('Qual o seu CPF? '))
        
        for conta in lista_nome:
            if cpf == conta['cpf']:
                print('Olá', {conta['nome']}, 'como podemos ajudar você hoje? ')
                menu_cliente(conta)
                return
            
        else:   
            criar = int(input('Você ainda não possui uma conta em nosso branco.\n Deseja criar uma?\n [1] Para SIM\n [2] Para NÃO '))
            
            if criar == 1:
                print('Vamos dar inicio a criação de sua conta.')
                criando_conta()
            if criar == 2:
                menu_inicial()

    def HOME():
        menu = '''
        [1] Saldo\n
        [2] Saque\n
        [3] Depósito\n
        [4] Extrato\n
        [5] Sair\n'''
        print(menu)
             
    def SAQUE(conta):
        
        saques = 1
    
        valor = int(input('Qual o valor que deseja sacar? '))
            
        if valor > LIMITE:
            print(f'O valor de R${valor}, está acima do limite permitido em sua conta.\nO limite permitido em sua conta é de saque por vez em sua conta é de R${LIMITE}')
        
        
        if conta['saldo'] < valor:
            print('Saldo insuficiente, verifique o valor disponível em sua conta.')
            
       
        elif conta['numero_saque'] == LIMITE_SAQUE:
            print(f'Quantidade máximo de saque dirairo atingido.\nLimite diário de {LIMITE_SAQUE} saques diário.')
            
        else:
            print(f'Saque no valor de R$ {valor} foi realizado com sucesso.')
            
            conta['numero_saque'] += saques 
            conta['saldo'] -= valor
            conta['extrato'].append(f'- R$ {valor}')
            menu_cliente(conta)

    def depositar(conta):
        
        
        desposito = int(input('Qual o valor que voce deseja depositar em sua conta?  '))
        conta['saldo'] += desposito
        
        conta['extrato'].append(f'+ R${desposito}')
        menu_cliente(conta)
        
                    
    def menu_cliente(conta):
        HOME()
        
    
        
        opcao = int(input('Selecione uma das opções acima: '))
        
        if opcao == 1:
            print('Seu saldo é de R$', conta['saldo'] )
            menu_cliente(conta)
             
        elif opcao == 2:
            SAQUE(conta)
        
        if opcao == 3:
            depositar(conta)
        
        if opcao == 4:
        
            print(f'''Gerando extrato
            ==========
            {conta['extrato']}
            ==========
            Saldo total em sua conta:
            R$ {conta['saldo']}''')
            menu_cliente(conta)
            
               
        if opcao == 5:
            menu_inicial()
    
    
    
    menu_inicial()

   
   
   
   
   