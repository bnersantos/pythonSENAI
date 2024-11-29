from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base, Fornecedor, Produto, Categoria, Funcionario, Movimentacao  # Importar suas classes de modelo

# Configuração do banco de dados
engine = create_engine('sqlite:///DataBase.db')
db_session = scoped_session(sessionmaker(bind=engine))

def view_data():
    # Visualizando Fornecedores
    print("Fornecedores:")
    fornecedores = db_session.query(Fornecedor).all()
    for fornecedor in fornecedores:
        print(f"ID: {fornecedor.id_fornecedor}, Nome: {fornecedor.nome_fornecedor}, "
              f"Telefone: {fornecedor.telefone_fornecedor}, Email: {fornecedor.email_fornecedor}")

    # Visualizando Produtos
    print("\nProdutos:")
    produtos = db_session.query(Produto).all()
    for produto in produtos:
        print(f"ID: {produto.id_produto}, Nome: {produto.nome_produto}, Preço: {produto.preco_produto}, "
              f"Descrição: {produto.descricao}, Validade: {produto.validade_produto}, "
              f"Garantia: {produto.garantia_produto} meses, Peso: {produto.peso_produto} kg, "
              f"Medida: {produto.medida_produto} cm, ID Fornecedor: {produto.id_fornecedor}, "
              f"ID Categoria: {produto.id_categoria_prod}")

    # Visualizando Categorias
    print("\nCategorias:")
    categorias = db_session.query(Categoria).all()
    for categoria in categorias:
        print(f"ID: {categoria.id_categoria_prod}, Nome: {categoria.nome_categoria_prod}")

    # Visualizando Funcionários
    print("\nFuncionários:")
    funcionarios = db_session.query(Funcionario).all()
    for funcionario in funcionarios:
        print(f"ID: {funcionario.id_funcionario}, Nome: {funcionario.nome_funcionario}, "
              f"CPF: {funcionario.cpf_funcionario}, Email: {funcionario.email_funcionario}, "
              f"Telefone: {funcionario.telefone_funcionario}, Cargo: {funcionario.cargo_funcionario}")

    # Visualizando Movimentações
    print("\nMovimentações:")
    movimentacoes = db_session.query(Movimentacao).all()
    for movimentacao in movimentacoes:
        print(f"ID: {movimentacao.id_movimento}, Entrada: {movimentacao.entrada}, "
              f"Saída: {movimentacao.saida}, Data: {movimentacao.data_movimento}, "
              f"Valor: {movimentacao.valor_movimento}, Volume: {movimentacao.volume_movimento}, "
              f"ID Funcionário: {movimentacao.id_funcionario}, ID Produto: {movimentacao.id_produto}")

if __name__ == '__main__':
    view_data()
