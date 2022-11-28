class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    def quantidade(self):
        return self._quantidade

    @nome.setter
    def nome(self, value):
        self._nome = value

    def quantidade(self, value):
        self._quantidade = value


produtoUm = Produto('Carro', 4)
produtoDois = Produto('Avião', 14)
produtoTres = Produto('Barcos', 7)
produtoQuatro = Produto('Moto', 8)

estoque = [produtoUm, produtoDois, produtoTres, produtoQuatro]

# print(produtoUm.nome, produtoUm.quantidade)


def PerguntaItemCarrinho():
    print('==============================================')
    print('Ótimo! Informe o produto desejado e a quantidade a adicionar no carrinho: ')

    nomeProdutoEscolhido = input('Nome produto: ')
    quantidadeProdutoEscolhido = int(input('Quantidade produto: '))

    verificaEstoque(nomeProdutoEscolhido, quantidadeProdutoEscolhido)


def verificaEstoque(nomeProdutoEscolhido, quantidadeProdutoEscolhido):
    for i in estoque:
        if nomeProdutoEscolhido == i.nome:
            adicionaItemCarrinho(nomeProdutoEscolhido,
                                 quantidadeProdutoEscolhido)
            break
            # print(produtoEscolhido.nome, produtoEscolhido.quantidade)
        else:
            print('Item inexistente no estoque')


def adicionaItemCarrinho(nomeProdutoEscolhido, quantidadeProdutoEscolhido):
    Produto(nomeProdutoEscolhido, quantidadeProdutoEscolhido)
    print('Item adicionado ao carrinho')
