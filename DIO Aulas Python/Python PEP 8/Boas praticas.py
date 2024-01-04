from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

engine = create_engine('sqlite:///banco.db', echo=True)  # Corrigido o caminho da string de conexão

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship('Cliente', back_populates='contas')

# Criando tabelas
Base.metadata.create_all(bind=engine)

# Criando uma sessão
session = Session(engine)

# Inserindo dados de exemplo
cliente1 = Cliente(nome='João')
conta1 = Conta(saldo=1000, cliente=cliente1)

session.add(cliente1)
session.commit()
