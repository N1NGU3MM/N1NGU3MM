from sqlalchemy import (create_engine, 
                        Column, 
                        Integer, 
                        String, 
                        ForeignKey
                        )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (relationship, 
                            Session
                            )

engine = create_engine('sqlite:///banco.db', echo=True)

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(11))
    address = Column(String(255))
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo_conta = Column(String)  # Adicionando o tipo de conta
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship('Cliente', back_populates='contas')

# Criando tabelas
Base.metadata.create_all(bind=engine)

# Criando uma sessão
session = Session(engine)

# Inserindo dados de exemplo
cliente1 = Cliente(nome='João',
                   cpf='12345678901',
                   address='Rua ABC, 123')
conta1 = Conta(tipo_conta='Corrente', agencia='0001', num=12345, saldo=1000, cliente=cliente1)

cliente2 = Cliente(nome='Luiz',
                   cpf='87654327811',
                   address='Rua ABC, 124')
conta2 = Conta(tipo_conta='Poupança', agencia='0001', num=54321, saldo=1000, cliente=cliente2)

session.add(cliente1)
session.add(conta1)
session.add(cliente2)
session.add(conta2)
session.commit()