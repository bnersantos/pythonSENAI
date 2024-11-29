from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from faker import Faker
from models import Fornecedor, Categoria, Produto, Funcionario, Movimentacao, init_db
from datetime import datetime, timedelta
import random

# Configuração do banco de dados
engine = create_engine('sqlite:///DataBase.db')
db_session = scoped_session(sessionmaker(bind=engine))
fake = Faker('pt_BR')

def format_date_as_string(date_obj):
    """Converte um objeto de data em string no formato dd-mm-yyyy."""
    return date_obj.strftime("%d-%m-%Y")

def generate_random_date(start, end):
    """Gera uma data aleatória entre duas datas."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def insert_random_data(session):
    """Insere dados aleatórios no banco de dados."""

    # Criando e adicionando fornecedores
    fornecedores = [Fornecedor(
        nome_fornecedor=fake.company(),
        telefone_fornecedor=fake.phone_number(),
        email_fornecedor=fake.unique.email()
    ) for _ in range(5)]

    session.add_all(fornecedores)
    session.commit()

    # Criando e adicionando categorias
    categorias = [Categoria(
        nome_categoria_prod=cat
    ) for cat in ['Smartphones', 'Laptops', 'Televisores', 'Acessórios', 'Tablets']]

    session.add_all(categorias)
    session.commit()

    # Definindo o intervalo de datas
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31)

    # Listas de produtos eletrônicos
    produtos_eletronicos = [
        'Smartphone Samsung Galaxy S21', 'iPhone 13', 'Laptop Dell XPS 13',
        'MacBook Pro', 'Televisor LG OLED', 'Televisor Samsung QLED',
        'Fone de Ouvido JBL', 'Mouse Gamer Logitech', 'Teclado Mecânico Razer',
        'Tablet Samsung Galaxy Tab'
    ]

    # Criando e adicionando produtos
    produtos = [Produto(
        nome_produto=random.choice(produtos_eletronicos),
        preco_produto=round(random.uniform(500, 5000), 2),  # Preços ajustados
        descricao=fake.sentence(),
        validade_produto=format_date_as_string(generate_random_date(start_date, end_date)),
        garantia_produto=random.randint(6, 24),  # Garantia entre 6 meses e 2 anos
        peso_produto=round(random.uniform(0.5, 3.0), 2),  # Peso em kg
        medida_produto=round(random.uniform(20, 100), 2),  # Tamanho em cm
        id_fornecedor=random.randint(1, 5),  # ID do fornecedor
        id_categoria_prod=random.randint(1, 5)  # ID da categoria
    ) for _ in range(10)]

    session.add_all(produtos)
    session.commit()

    # Criando e adicionando funcionários
    funcionarios = [Funcionario(
        nome_funcionario=fake.name(),
        cpf_funcionario=fake.unique.ssn(),
        email_funcionario=fake.unique.email(),
        telefone_funcionario=fake.phone_number(),
        cargo_funcionario=fake.job()
    ) for _ in range(5)]

    session.add_all(funcionarios)
    session.commit()

    # Criando e adicionando movimentações
    movimentacoes = [Movimentacao(
        entrada=format_date_as_string(generate_random_date(start_date, end_date)),
        saida=format_date_as_string(generate_random_date(start_date, end_date)),
        data_movimento=format_date_as_string(generate_random_date(start_date, end_date)),
        valor_movimento=round(random.uniform(100, 10000), 2),
        volume_movimento=random.randint(1, 100),
        id_funcionario=random.randint(1, 5),  # Ajuste se tiver mais ou menos funcionários
        id_produto=random.randint(1, 10)  # ID do produto
    ) for _ in range(10)]

    session.add_all(movimentacoes)
    session.commit()


if __name__ == '__main__':
    with db_session() as session:
        init_db()  # Cria as tabelas
        insert_random_data(session)  # Insere os dados
