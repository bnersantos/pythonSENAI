from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean, Date
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

engine = create_engine('sqlite:///DataBase.db', pool_size=10, max_overflow=20, pool_timeout=30)  # Corrigido o pool_size
db_session = scoped_session(sessionmaker(bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funcionarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(Base):
    __tablename__ = 'TAB_USER'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)  # Armazena o hash da senha
    is_admin = Column(Boolean, default=False)

    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.is_admin = is_admin
        self.set_password(password)  # Chamando corretamente o método de hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # Armazena o hash da senha

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # Verifica a senha

    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'is_admin': self.is_admin,
        }

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def create_user(username, password, is_admin=False):
    try:
        user = User(username=username, password=password, is_admin=is_admin)
        db_session.add(user)
        db_session.commit()
    except Exception as e:
        db_session.rollback()  # Reverte a transação em caso de erro
        print(f"Erro ao criar usuário: {e}")


def verify_user(username, password):
    user = db_session.query(User).filter_by(username=username).first()
    if user and user.check_password(password):
        return True  # Senha correta
    return False  # Senha incorreta


class Fornecedor(Base):
    __tablename__ = 'FORNECEDOR'
    id_fornecedor = Column(Integer, primary_key=True)
    nome_fornecedor = Column(String(30), nullable=False, index=True)
    telefone_fornecedor = Column(String(14), nullable=False, unique=True)
    email_fornecedor = Column(String(80), nullable=False, unique=True, index=True)

    produtos = relationship('Produto', back_populates='fornecedor')

    def __str__(self):
        return f'<Fornecedor: {self.nome_fornecedor}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        return {
            'id': self.id_fornecedor,
            'nome': self.nome_fornecedor,
            'telefone': self.telefone_fornecedor,
            'email': self.email_fornecedor,
        }


class Produto(Base):
    __tablename__ = 'PRODUTO'
    id_produto = Column(Integer, primary_key=True)
    nome_produto = Column(String(30), nullable=False, index=True)
    preco_produto = Column(Float, nullable=False)
    descricao = Column(String(80), nullable=False)
    validade_produto = Column(String, nullable=False)
    garantia_produto = Column(Integer, nullable=False)  # Garantia em meses
    peso_produto = Column(Float, nullable=False)  # Em kg
    medida_produto = Column(String, nullable=False)  # Em cm

    id_fornecedor = Column(Integer, ForeignKey('FORNECEDOR.id_fornecedor'), nullable=False)
    fornecedor = relationship('Fornecedor', back_populates='produtos')
    id_categoria_prod = Column(Integer, ForeignKey('CATEGORIA_PROD.id_categoria_prod'), nullable=False)
    categoria = relationship('Categoria', back_populates='produtos')

    def __str__(self):
        return f'<Produto: {self.nome_produto}, Preço: {self.preco_produto}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        return {
            'id': self.id_produto,
            'nome': self.nome_produto,
            'preco': self.preco_produto,
            'descricao': self.descricao,
            'validade': self.validade_produto,
            'garantia': self.garantia_produto,
            'peso': self.peso_produto,
            'medida': self.medida_produto,
            'fornecedor_id': self.id_fornecedor,
            'categoria_id': self.id_categoria_prod,
        }


class Categoria(Base):
    __tablename__ = 'CATEGORIA_PROD'
    id_categoria_prod = Column(Integer, primary_key=True)
    nome_categoria_prod = Column(String(30), nullable=False, index=True)
    produtos = relationship('Produto', back_populates='categoria')

    def __str__(self):
        return f'<Categoria: {self.nome_categoria_prod}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        return {
            'id': self.id_categoria_prod,
            'nome': self.nome_categoria_prod,
        }

class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id_funcionario = Column(Integer, primary_key=True)
    nome_funcionario = Column(String(40), nullable=False, index=True)
    cpf_funcionario = Column(String(14), nullable=False, unique=True, index=True)
    email_funcionario = Column(String(80), nullable=False, unique=True, index=True)
    cargo_funcionario = Column(String(30), nullable=False)
    telefone_funcionario = Column(String, nullable=False, default="Não informado")

    movimentacoes = relationship('Movimentacao', back_populates='funcionario')

    def __str__(self):
        return f'<Funcionario: {self.nome_funcionario}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        return {
            'id': self.id_funcionario,
            'nome': self.nome_funcionario,
            'cpf': self.cpf_funcionario,
            'email': self.email_funcionario,
            'cargo': self.cargo_funcionario,
            'telefone': self.telefone_funcionario,
        }

class Movimentacao(Base):
    __tablename__ = 'MOVIMENTACAO'
    id_movimento = Column(Integer, primary_key=True)
    entrada = Column(Boolean, nullable=False)
    saida = Column(Boolean, nullable=False)
    data_movimento = Column(Date, nullable=False)
    valor_movimento = Column(Float, nullable=False)
    volume_movimento = Column(Integer, nullable=False)

    id_funcionario = Column(Integer, ForeignKey('FUNCIONARIO.id_funcionario'), nullable=False)
    funcionario = relationship('Funcionario', back_populates='movimentacoes')

    id_produto = Column(Integer, ForeignKey('PRODUTO.id_produto'), nullable=False)
    produto = relationship('Produto')

    def __init__(self, **kwargs):
        # Certificando-se que a data_movimento está no formato correto
        if 'data_movimento' in kwargs:
            kwargs['data_movimento'] = formatar_data(kwargs['data_movimento'])
        super().__init__(**kwargs)

    def __str__(self):
        tipo = "Entrada" if self.entrada else "Saída"
        return f'<Movimentacao: {tipo}, Valor: {self.valor_movimento}>'

    def save(self):
        # Certificando-se de que a data é salva no formato correto
        if isinstance(self.data_movimento, str):
            self.data_movimento = formatar_data(self.data_movimento)
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        return {
            'id': self.id_movimento,
            'entrada': self.entrada,
            'saida': self.saida,
            'data': self.data_movimento,
            'valor': self.valor_movimento,
            'volume': self.volume_movimento,
            'funcionario_id': self.id_funcionario,
            'produto_id': self.id_produto,
        }

def formatar_data(data_str):
    """ Função para garantir que a data seja no formato ISO 'YYYY-MM-DD' """
    try:
        return datetime.strptime(data_str, '%d-%m-%Y').date()
    except ValueError:
        raise ValueError(f"Data '{data_str}' no formato inválido. Use 'DD-MM-YYYY'.")


# Inicializar o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()