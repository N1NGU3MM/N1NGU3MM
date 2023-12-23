# Melhorando o sistema bancario



class Menu: # Hare is homepage 
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


class CriandoConta: # Class for news accounts
    
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
            'agencia': '0001'
        }
    
        
        return nova_conta
    def __str__(self):
        return f'InformacaoClientes: {self.informacoes_clientes}'
    

        
class InformacaoClientes: # Info abouto all dados of claints
    def __init__(self):
        super().__init__()
        self.informacoes_clientes = [{'cpf': 1, 'nascimento': 2000, 'saldo': 1500, 'numero_saque': 0, 'extrato': [],
                                       'nome': 'Test', 'cidade': 'UI', 'rua': 'NP', 'estado': 'SP',
                                       'agencia': '0001', 'numero_conta': 1}, {'cpf': 2, 'nascimento': 2000, 'saldo': 1500, 'numero_saque': 0, 'extrato': [],
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
    
    def _Contas(self, contas): # aqui é possiivel acessar todas as info dos clintes 
        contas = self.informacoes_clientes
        self.contas = contas
        return self.contas



# class BancoDeDados (InformacaoClientes):
#     def __init__(self):
#         super().__init__()
#         self._DadosClientes = [] 
# 
#     def Dados (self):
#         return self._DadosClientes
#     
#     def adcionar_clinte(self):
#         
#         self._DadosClientes.append(self.informacoes_clientes)
# bc = BancoDeDados()
        

class ContaCorrente:
    def __init__(self, informacao_clientes, cliente_menu):
        self.informacoes_clientes = informacao_clientes
        self.cliente_menu = cliente_menu

    def buscar_cliente(self, numero_conta):
       
        for cliente in self.informacoes_clientes.clientes_inf():
            if cliente['numero_conta'] == numero_conta:
                return [cliente]  # Retorna uma lista com o cliente encontrado

        return []  # Retorna uma lista vazia se o cliente não for encontrado

    def exibir_conta_corrente(self, cpf):
        print("Bem vindo ao nosso banco!")
        cpf = int(input('Digite o seu CPF para que possamos, validar seu acesso: '))
        contas_encontradas = self.buscar_cliente(cpf)

        if contas_encontradas:
            cliente = contas_encontradas[0]
            print(f'Sua conta foi encontrada: {cliente}')

            print(f'Ola {cliente["nome"]}')
            self.cliente_menu.exibir_menu_cliente()
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

    def exibir_menu_cliente(self):
        print(self.menu_cliente)
    




def PaginaInicial():
    opcao_menu_principal = menu_principal.exibir_menu()

    if opcao_menu_principal == 1:
        nova_conta = criar_conta.CriarConta()
        conta_criada = informacao_clientes.novo_cliente(nova_conta)
        
        if conta_criada:
            print('Conta criada com sucesso!')
            PaginaInicial()
    
    elif opcao_menu_principal == 2:
       numero_conta = int(input('Qual o numero da sua conta? '))
       corrente.exibir_conta_corrente(numero_conta)
    
    #    cliente_cpf = [cliente['cpf'] for cliente in clientes.clientes_inf()]
    #    print(cliente_cpf)
    
    

#        iof = Cliente()
#        iof.oo()
#
#        menu_do_cliente = MenuDoCliente()
#        menu_do_cliente.exibir_menu_cliente()


menu_principal = Menu()
criar_conta = CriandoConta()
informacao_clientes = InformacaoClientes()
cliente_menu = MenuDoCliente()
corrente = ContaCorrente(informacao_clientes, cliente_menu)
menu_cliente = MenuDoCliente()


PaginaInicial()

