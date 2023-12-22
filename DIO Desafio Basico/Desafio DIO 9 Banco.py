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
            'data_de_nascimento': data_de_nascimento,
            'nome': nome,
            'cidade': endereco_cidade,
            'rua': rua, 
            'estado': estado,
            'agencia': '0001'
        }
    
        
        return nova_conta
    def __str__(self):
        return f'InformacaoClientes: {self.informacoes_clientes}'
    
    
    


        
class InformacaoClientes:
    def __init__(self):
        super().__init__()
        self.informacoes_clientes = []
    
    def clientes_inf(self): # aqui é possiivel acessar todas as info dos clintes 
        return self.informacoes_clientes
    
    def novo_cliente(self, nova_conta):
        nova_conta['numero_conta'] = len(self.informacoes_clientes) + 1
        self.informacoes_clientes.append(nova_conta)
        print(f'''Conta criada com sucesso!\n
        O numero de sua conta é: {nova_conta['numero_conta']}''')
        
        PaginaInicial()


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
        

class Cliente(InformacaoClientes):
    def __init__ (self):
        self.agencia = self.informacoes_clientes['agencia']
        
    def oo (self):
        print(f'Agencia {self.agencia}')


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
        return



menu_principal = Menu()
criar_conta = CriandoConta()
clientes = InformacaoClientes()
cliente_menu = MenuDoCliente()


# bc = BancoDeDados()

def PaginaInicial():
    opcao_menu_principal = menu_principal.exibir_menu()

    if opcao_menu_principal == 1:
        nova_conta = criar_conta.CriarConta()
        clientes.novo_cliente(nova_conta)
    
    if opcao_menu_principal == 2:
        cliente_cpf = [cliente['cpf'] for cliente in clientes.clientes_inf()]
        print(cliente_cpf)
        PaginaInicial()

#        iof = Cliente()
#        iof.oo()
#
#        menu_do_cliente = MenuDoCliente()
#        menu_do_cliente.exibir_menu_cliente()




PaginaInicial()

