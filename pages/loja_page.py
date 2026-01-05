class LojaPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://rayrraio.github.io/site-para-teste-login/"

    def abrir(self):
        self.page.goto(self.url)

    def adicionar_rasteirinha(self):
        # Em vez de XPath complexo, vamos clicar no botão que tem o texto exato
        # Como existem vários, o '.last' garante que pegamos a Rasteirinha (último item)
        botao = self.page.get_by_role("button", name="Adicionar no Carrinho").last
        botao.click()