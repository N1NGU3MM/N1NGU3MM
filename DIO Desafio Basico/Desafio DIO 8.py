# Sistema Bancário

lista_nome = []
agencia = '0001'
LIMITE = 500
LIMITE_SAQUE = 3

def saldo_conta(conta):
    return conta['saldo']

def nomes():
    return lista_nome

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
    
    elif menu == 2:
        cliente()
    
    elif menu == 3:
        print('Até logo!')

def criar_conta():
    start = int(input('Você deseja criar a sua conta?\n [1] para SIM\n [2] para NÃO.\n'))
    
    if start == 1:
        criando_conta()
    elif start == 2:
        menu_inicial()
    else:
        print('Opção inválida')
        criar_conta()

def criando_conta():
    cpf = int(input('Diga seu CPF? '))
    data_de_nascimento = int(input('Qual o ano do seu nascimento? '))
    nome = input('Digite seu nome completo: ')
    endereço_cidade = input('Qual sua cidade? ')
    rua = input('Qual o nome da sua rua? ')
    estado = input('Qual seu estado? ')
    
    localizacao = {'cidade': endereço_cidade, 'rua': rua, 'estado': estado}
    
    for conta in lista_nome:
        if cpf == conta['cpf']:
            print('Esse nome já foi informado!')
            menu_inicial()
    
    nova_conta = {
        'cpf': cpf,
        'nascimento': 2,
        'saldo': 1500,
        'numero_saque': 0,
        'extrato': [],
        'data_de_nascimente': data_de_nascimento,
        'localização': localizacao,
        'nome': nome,
        'agencia': agencia,
        'conta': len(lista_nome) + 1
    }
    
    lista_nome.append(nova_conta)
    
    print('Conta criada!\n O número da sua conta é: {}'.format(nova_conta['conta']))
    menu_inicial()

def cliente():
    print(f'Agência: {agencia}' )
    conta_numero = int(input('Qual o número da sua conta?'))
    
    for conta in lista_nome:
        if conta_numero == conta['conta']:
            print(f'Olá {conta["nome"]}, como podemos ajudar você hoje? ')
            print(f'Agência: {conta["agencia"]}')
            print(f'Conta: {conta["conta"]}')
            menu_cliente(conta)
            return
    
    criar = int(input('Você ainda não possui uma conta em nosso banco.\n Deseja criar uma?\n [1] Para SIM\n [2] Para NÃO '))
    
    if criar == 1:
        print('Vamos dar início à criação de sua conta.')
        criando_conta()
    elif criar == 2:
        menu_inicial()

def HOME():
    menu = '''
    [1] Saldo
    [2] Saque
    [3] Depósito
    [4] Extrato
    [5] Sair
    '''
    print(menu)

def SAQUE(conta):
    saques = 1
    valor = int(input('Qual o valor que deseja sacar? '))
    
    if valor > LIMITE:
        print(f'O valor de R${valor}, está acima do limite permitido em sua conta.\nO limite permitido em sua conta é de saque por vez em sua conta é de R${LIMITE}')
    
    if conta['saldo'] < valor:
        print('Saldo insuficiente, verifique o valor disponível em sua conta.')
    
    elif conta['numero_saque'] == LIMITE_SAQUE:
        print(f'Quantidade máxima de saque diário atingido.\nLimite diário de {LIMITE_SAQUE} saques diários.')
        menu_cliente(conta)
        return
    
    else:
        print(f'Saque no valor de R$ {valor} foi realizado com sucesso.')
        conta['numero_saque'] += saques 
        conta['saldo'] -= valor
        conta['extrato'].append(f'- R$ {valor}')
        menu_cliente(conta)

def depositar(conta):
    desposito = int(input('Qual o valor que você deseja depositar em sua conta?  '))
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
    
    elif opcao == 3:
        depositar(conta)
    
    elif opcao == 4:
        print(f'''Gerando extrato
        ==========
        {conta['extrato']}
        ==========
        Saldo total em sua conta:
        R$ {conta['saldo']}''')
        menu_cliente(conta)
        
    elif opcao == 5:
        menu_inicial()

menu_inicial()
