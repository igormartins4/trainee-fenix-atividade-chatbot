from produto import adicionarProduto
# from carrinho import Carrinho, mostrarCarrinho, fecharCarrinho


def mostrarMenu():

    print('==============================================')
    print('Bem vindo ao Chatbot de atendimento!! :)')
    print('Os seguintes comandos estão disponíveis:')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Mostrar carrinho')
    print('4 - Fechar carrinho de compras')
    print('==============================================')

    while True:
        print('Sua escolha: ')

        escolha = int(input())

        match (escolha):
            case 1:
                adicionarProduto()
                break
            case 2:
                # remover = Produto.removerProduto()
                break
            case 3:
                # mostrar = Carrinho.mostrarCarrinho()
                break
            case 4:
                # finalizar = Carrinho.fecharCarrinho()
                break
            case _:
                print('Opção inválida, tente novamente!')
