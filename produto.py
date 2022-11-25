class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def adicionarProduto(self, nome, quantidade):
        print('==============================================')
        print('Ótimo! Informe o produto desejado e a quantidade a adicionar: ')
        print('Sua escolha: ')
