class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def adicionarProduto(self):
        print('==============================================')
        print('Ótimo! Informe o produto desejado e a quantidade a adicionar: ')
        print('Sua escolha: ')

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

print(produtoUm.nome, produtoUm.quantidade)
