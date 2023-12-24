# Melhorando o sistema bancario

class Menu:
    def __init__(self):
        self.menu = ("""
          Bem Vindo\n
          Selecione uma das opções abaixo\n
          [1] Criar uma conta
          [2] Já sou cliente
          [3] Sair""")
        
    def exibir_menu(self):
        print(self.menu)

        return int(input('Qual opção você deseja? '))


class CriandoConta:
    def CriarConta(self):
        cpf = int(input('Diga seu CPF? '))
        data_de_nascimento = int(input('Qual o ano do seu nascimento? '))
        nome = input('Digite seu nome completo: ')
        endereco_cidade = input('Qual sua cidade? ')
        rua = input('Qual o nome da sua rua? ')
        estado = input('Qual seu estado? ')

        nova_conta = {
            'cpf': cpf,
            'nascimento': data_de_nascimento,
            'saldo': 1500,
            'numero_saque': 0,
            'extrato': [],
            'nome': nome,
            'cidade': endereco_cidade,
            'rua': rua, 
            'estado': estado,
            'agencia': '0001',
            'numero_conta': 1  
        }
    
        return nova_conta


class InformacaoClientes:
    def __init__(self):
        self.informacoes_clientes = [{'cpf': 1, 'nascimento': 2000, 'saldo': 1500, 'numero_saque': 0, 'extrato': [],
                                       'nome': 'Test', 'cidade': 'UI', 'rua': 'NP', 'estado': 'SP',
                                       'agencia': '0001', 'numero_conta': 1},
                                      {'cpf': 2, 'nascimento': 2000, 'saldo': 1500, 'numero_saque': 0, 'extrato': [],
                                       'nome': 'Test2', 'cidade': 'UI', 'rua': 'NP', 'estado': 'SP',
                                       'agencia': '0001', 'numero_conta': 2}]

    def clientes_inf(self):
        return self.informacoes_clientes

    def novo_cliente(self, nova_conta):
        nova_conta['numero_conta'] = len(self.informacoes_clientes) + 1
        self.informacoes_clientes.append(nova_conta)
        print(f'''Conta criada com sucesso!\n
        O numero de sua conta é: {nova_conta['numero_conta']}''')
        
        return nova_conta


class ContaCorrente:
    def __init__(self, informacao_clientes, cliente_menu):
        self.informacoes_clientes = informacao_clientes
        self.cliente_menu = cliente_menu

    def buscar_cliente(self, numero_conta):
        for cliente in self.informacoes_clientes.clientes_inf():
            if cliente['numero_conta'] == numero_conta:
                return [cliente]
        return []

    def exibir_conta_corrente(self, numero_conta):
        print("Bem vindo ao nosso banco!")
        numero_conta = int(input('Digite o numero associado à sua conta corrente: '))
        contas_encontradas = self.buscar_cliente(numero_conta)

        if contas_encontradas:
            cliente = contas_encontradas[0]
            print(f'Sua conta foi encontrada: {cliente}')

            print(f'Ola {cliente["nome"]}')
            self.cliente_menu.exibir_menu_cliente(cliente)
        else:
            print('Conta não encontrada!')


class MenuDoCliente:
    def __init__(self):
        self.menu_cliente = '''
    [1] Saldo
    [2] Saque
    [3] Depósito
    [4] Extrato
    [5] Sair
    '''

    def exibir_menu_cliente(self, cliente):
        while True:
            print(self.menu_cliente)
            opcao = int(input('Escolha uma opção: '))

            if opcao == 1:
                self.mostrar_saldo(cliente)
            elif opcao == 2:
                self.realizar_saque(cliente)
            elif opcao == 3:
                self.realizar_deposito(cliente)
            elif opcao == 4:
                self.mostrar_extrato(cliente)
            elif opcao == 5:
                print('Saindo...')
                PaginaInicial()
            else:
                print('Opção inválida. Tente novamente.')

    def mostrar_saldo(self, cliente):
        print(f'Seu saldo atual é: R${cliente["saldo"]}')

    def realizar_saque(self, cliente):
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        if valor_saque > cliente['saldo']:
            print('Saldo insuficiente.')
        else:
            cliente['saldo'] -= valor_saque
            cliente['numero_saque'] += 1
            cliente['extrato'].append(f'Saque de R${valor_saque}')
            print(f'Saque de R${valor_saque} realizado com sucesso. Novo saldo: R${cliente["saldo"]}')

    def realizar_deposito(self, cliente):
        valor_deposito = float(input('Digite o valor que deseja depositar: '))
        cliente['saldo'] += valor_deposito
        cliente['extrato'].append(f'Depósito de R${valor_deposito}')
        print(f'Depósito de R${valor_deposito} realizado com sucesso. Novo saldo: R${cliente["saldo"]}')

    def mostrar_extrato(self, cliente):
        print('Extrato:')
        for operacao in cliente['extrato']:
            print(operacao)


def PaginaInicial():
    opcao_menu_principal = menu_principal.exibir_menu()

    if opcao_menu_principal == 1:
        nova_conta = criar_conta.CriarConta()
        conta_criada = informacao_clientes.novo_cliente(nova_conta)
        
        if conta_criada:
            print('Conta criada com sucesso!')
            PaginaInicial()
    
    elif opcao_menu_principal == 2:
        numero_conta = int(input('''Deseja acessar sua conta corrente?\n
                                [1] SIM
                                [2] NÃO '''))
        if numero_conta == 1: 
            corrente.exibir_conta_corrente(numero_conta)
        else:
            print('Erro')
            for i in range(10):
                print(i)
            PaginaInicial()

    elif opcao_menu_principal == 3:
        return None



menu_principal = Menu()
criar_conta = CriandoConta()
informacao_clientes = InformacaoClientes()
cliente_menu = MenuDoCliente()
corrente = ContaCorrente(informacao_clientes, cliente_menu)
menu_cliente = MenuDoCliente()

PaginaInicial()
