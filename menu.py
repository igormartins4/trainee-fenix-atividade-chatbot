from produto import Produto


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
                print('Ok 1')
                break
            case 2:
                print('Ok 2')
                break
            case 3:
                print('Ok 3')
                break
            case 4:
                print('Ok 4')
                break
            case _:
                print('Opção inválida, tente novamente!')
