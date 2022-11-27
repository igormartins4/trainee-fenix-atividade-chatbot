class Carrinho:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade

    def mostrarCarrinho(self):
        print('==============================================')
        print('Claro! Seu carrinho atualmente possui: ')
        print('')

    def fecharCarrinho(self):
        print('==============================================')
        print('Sua compra ficou no total de R$: ')
        print('Obrigado pela preferência ;)')

    @property
    def item(self):
        return self._item

    def quantidade(self):
        return self._quantidade
