from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select
from sqlalchemy.orm import declarative_base, relationship, Session 

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User (id={self.id}, name={self.name}, fullname={self.fullname}) "


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable = False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Address (id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# Cindo as class como tabela no banco de dados
Base.metadata.create_all(engine)

# Investiga os esquema de banco de dados
insp = inspect(engine)

print(insp.has_table("user_account"))
print(insp.get_table_names())
print(insp.default_schema_name)


with Session(engine) as session:
    juliana = User(
        name = 'juliana',
        fullname = 'Juliana Silva',
        address = [Address(email_address = 'julianasilva@gmail.com')]
        
    )
    
    sandy = User(
        name = 'sandy',
        fullname = 'Sandy Silva',
        address = [Address(email_address = 'sandysilva@gmail.com'),
                  Address(email_address = 'sandysil@gmail.com')]
        
    )

    patrick = User(name = 'patrick', fullname = 'Patrick Silva')

    # Enviando para o BD "Banco de dados"
    session.add_all([juliana, sandy, patrick])
        
    session.commit()


stmt = select(User).where(User.name.in_(["juliana"])) 
print('\nRecuperando usuáros a parti de condição de filtragem')
for user in session.scalars(stmt):
    print(user)
    
stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando os endereços de email de Sandy')
for address in session.scalars(stmt_address):
    print(address)

