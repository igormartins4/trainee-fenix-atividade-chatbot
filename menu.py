
def mostrarMenu():

    print('==============================================')
    print('Bem vindo ao Chatbot de atendimento!! :)')
    print('Os seguintes comandos estão disponíveis:')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Mostrar carrinho')
    print('4 - Fechar carrinho de compras')
    print('==============================================')
    print('Sua escolha: ')

    escolha = input()

    print(escolha)

    if escolha == 1:
        Produto.adicionarProduto()
