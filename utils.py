from models import Produto, Funcionario, Fornecedor, db_session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


# Funções Fornecedor
def inserir_fornecedor():
    try:
        fornecedor = Fornecedor(
            nome_fornecedor=input('Nome: ').strip(),
            email_fornecedor=input('Email: ').strip(),
            telefone_fornecedor=input('Telefone: ').strip()
        )
        db_session.add(fornecedor)
        db_session.commit()
        print(f'Fornecedor {fornecedor.nome_fornecedor} inserido com sucesso.')
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao inserir fornecedor: {e}')


def consultar_fornecedor():
    try:
        fornecedores = db_session.execute(select(Fornecedor)).scalars().all()
        if fornecedores:
            for fornecedor in fornecedores:
                print(fornecedor)
        else:
            print("Nenhum fornecedor encontrado.")
    except SQLAlchemyError as e:
        print(f'Erro ao consultar fornecedores: {e}')


def atualizar_fornecedor():
    try:
        nome_fornecedor = input('Nome do fornecedor: ').strip()
        fornecedor = db_session.execute(
            select(Fornecedor).where(Fornecedor.nome_fornecedor == nome_fornecedor)).scalar_one_or_none()

        if fornecedor:
            novo_nome = input('Novo nome (deixe vazio para não alterar): ').strip()
            novo_endereco = input('Novo endereço (deixe vazio para não alterar): ').strip()

            if novo_nome:
                fornecedor.nome_fornecedor = novo_nome
            if novo_endereco:
                fornecedor.endereco = novo_endereco

            db_session.commit()
            print('Fornecedor atualizado com sucesso.')
        else:
            print('Fornecedor não encontrado.')
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao atualizar fornecedor: {e}')


def deletar_fornecedor():
    try:
        nome_fornecedor = input('Nome do fornecedor: ').strip()
        fornecedor = db_session.execute(select(Fornecedor).where(Fornecedor.nome_fornecedor == nome_fornecedor)).scalars().all()
        if fornecedor:
            db_session.delete(fornecedor)
            db_session.commit()
            print(f'Fornecedor {fornecedor} deletado com sucesso')
        else:
            print('Fornecedor não encontrado')
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao deletar fornecedor: {e}')


# Funções Produto
def inserir_produto():
    try:
        # Solicita os dados para inserir o produto
        id_fornecedor = int(input('ID do fornecedor: ').strip())  # Solicita o ID do fornecedor
        fornecedor = db_session.execute(select(Fornecedor).where(Fornecedor.id == id_fornecedor)).scalar_one_or_none()

        if not fornecedor:
            print(f"Fornecedor com ID {id_fornecedor} não encontrado. A operação será abortada.")
            return  # Retorna sem realizar a inserção, caso o fornecedor não exista

        produto = Produto(
            nome_produto=input('Nome: ').strip(),
            preco_produto=float(input('Preço: ').strip()),
            descricao=input('Descrição: ').strip(),
            validade_produto=input('Data de adição: ').strip(),
            garantia_produto=int(input('Garantia em meses: ').strip()),
            peso_produto=float(input('Peso em gramas: ').strip()),
            medida_produto=float(input('Medida em centímetros: ').strip()),
        )

        # Adiciona o produto no banco de dados
        db_session.add(produto)
        db_session.commit()

        print(f'Produto {produto.nome_produto} inserido com sucesso.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao inserir produto: {e}')


def consultar_produto():
    try:
        produtos = db_session.execute(select(Produto)).scalars().all()
        if produtos:
            for produto in produtos:
                print(produto)
        else:
            print("Nenhum produto encontrado.")
    except SQLAlchemyError as e:
        print(f'Erro ao consultar produtos: {e}')


def atualizar_produto():
    try:
        # Solicita o ID do produto
        id_produto = int(input('ID do produto a ser atualizado: ').strip())

        # Busca o produto com o ID fornecido
        produto = db_session.execute(select(Produto).where(Produto.id_produto == id_produto)).scalar_one_or_none()

        if produto:
            # Exibe os detalhes do produto encontrado
            print(f'Produto encontrado: {produto}')

            # Solicita os novos valores para os campos
            novo_nome = input("Novo nome (deixe em branco para não alterar): ").strip()
            novo_preco = input("Novo preço (deixe em branco para não alterar): ").strip()

            # Atualiza os campos se o usuário forneceu novos valores
            if novo_nome:
                produto.nome_produto = novo_nome
            if novo_preco:
                produto.preco_produto = float(novo_preco)

            # Commit da alteração no banco de dados
            db_session.commit()
            print("Produto atualizado com sucesso.")
        else:
            print("Produto não encontrado com esse ID.")
    except ValueError:
        print("Erro: Certifique-se de fornecer um ID válido.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao atualizar produto: {e}')



def deletar_produto():
    try:
        nome_produto = input('Nome do produto: ').strip()
        produto = db_session.execute(select(Produto).where(Produto.nome_produto == nome_produto)).scalar_one_or_none()

        if produto:
            db_session.delete(produto)
            db_session.commit()
            print(f'Produto {nome_produto} removido com sucesso.')
        else:
            print("Produto não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao deletar produto: {e}')


# Funções Funcionário
def inserir_funcionario():
    try:
        funcionario = Funcionario(
            nome_funcionario=input('Nome: ').strip(),
            email_funcionario=input('E-mail: ').strip(),
            telefone_funcionario=str(input('Telefone: ').strip()),
            cargo_funcionario=input('Cargo: ').strip(),
            cpf_funcionario=str(input('CPF: ').strip())
        )
        db_session.add(funcionario)
        db_session.commit()

        print(f'Funcionário {funcionario.nome_funcionario} inserido com sucesso.')

    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao inserir funcionário: {e}')


def consultar_funcionario():
    try:
        funcionarios = db_session.execute(select(Funcionario)).scalars().all()
        if funcionarios:
            for funcionario in funcionarios:
                print(funcionario)
        else:
            print("Nenhum funcionário encontrado.")
    except SQLAlchemyError as e:
        print(f'Erro ao consultar funcionários: {e}')


def atualizar_funcionario():
    try:
        nome_funcionario = input('Nome do funcionário: ').strip()
        funcionario = db_session.execute(
            select(Funcionario).where(Funcionario.nome_funcionario == nome_funcionario)).scalar_one_or_none()

        if funcionario:
            novo_nome = input('Novo nome (deixe vazio para não alterar): ').strip()
            if novo_nome:
                funcionario.nome_funcionario = novo_nome

            db_session.commit()
            print('Funcionário atualizado com sucesso.')
        else:
            print('Funcionário não encontrado.')
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao atualizar funcionário: {e}')


def deletar_funcionario():
    try:
        nome_funcionario = input('Nome do funcionário: ').strip()
        funcionario = db_session.execute(
            select(Funcionario).where(Funcionario.id_funcionario == nome_funcionario)).scalar_one_or_none()

        if funcionario:
            db_session.delete(funcionario)
            db_session.commit()
            print(f'Funcionário {nome_funcionario} removido com sucesso.')
        else:
            print("Funcionário não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f'Erro ao deletar funcionário: {e}')


# Menu principal
def main():
    while True:
        print('----------------')
        print('Menu Geral')
        print('[1] Menu Produto')
        print('[2] Menu Funcionário')
        print('[3] Menu Fornecedor')
        escolha_menu = input('Sua escolha: ').strip()

        if escolha_menu == '1':
            print('----------------')
            print('Menu Produto')
            print('[1] Inserir Produto')
            print('[2] Consultar Produto')
            print('[3] Atualizar Produto')
            print('[4] Deletar Produto')
            escolha = input('Sua escolha: ').strip()

            if escolha == '1':
                inserir_produto()
            elif escolha == '2':
                consultar_produto()
            elif escolha == '3':
                atualizar_produto()
            elif escolha == '4':
                deletar_produto()
            else:
                print("Opção inválida.")

        elif escolha_menu == '2':
            print('----------------')
            print('Menu Funcionário')
            print('[1] Inserir Funcionário')
            print('[2] Consultar Funcionário')
            print('[3] Atualizar Funcionário')
            print('[4] Deletar Funcionário')
            escolha = input('Sua escolha: ').strip()

            if escolha == '1':
                inserir_funcionario()
            elif escolha == '2':
                consultar_funcionario()
            elif escolha == '3':
                atualizar_funcionario()
            elif escolha == '4':
                deletar_funcionario()
            else:
                print("Opção inválida.")

        elif escolha_menu == '3':
            print('----------------')
            print('Menu Fornecedor')
            print('[1] Inserir Fornecedor')
            print('[2] Consultar Fornecedor')
            print('[3] Atualizar Fornecedor')
            print('[4] Deletar Fornecedor')
            escolha = input('Sua escolha: ').strip()

            if escolha == '1':
                inserir_fornecedor()
            elif escolha == '2':
                consultar_fornecedor()
            elif escolha == '3':
                atualizar_fornecedor()
            elif escolha == '4':
                atualizar_fornecedor()
            else:
                print("Opção inválida.")
        else:
            print("Menu inválido.")


if __name__ == '__main__':
    main()
