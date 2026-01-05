import pytest
from playwright.sync_api import sync_playwright
from pages.loja_page import LojaPage

# Cenário 1: Garante que o botão de adicionar funciona e gera evidência visual
def test_clique_adicionar_rasteirinha():
    with sync_playwright() as p:
        # headless=True é obrigatório para rodar no ambiente do GitHub
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        loja = LojaPage(page)
        
        # Aceita o alerta automaticamente para o teste não travar
        page.on("dialog", lambda dialog: dialog.accept())
        
        loja.abrir()
        loja.adicionar_rasteirinha()
        
        # Gera a screenshot que você verá na barra lateral
        page.screenshot(path="evidencia_clique.png")
        browser.close()

# Cenário 2: Valida se o texto da mensagem de sucesso está correto (Regra de Negócio)
def test_validar_texto_sucesso():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        loja = LojaPage(page)
        
        mensagens = []
        # Captura o texto real que aparece no alerta do seu site
        page.on("dialog", lambda d: mensagens.append(d.message) or d.accept())
        
        loja.abrir()
        loja.adicionar_rasteirinha()
        
        # Verificação técnica (Assertion): O teste falha se a mensagem estiver errada
        assert len(mensagens) > 0, "O alerta de sucesso não apareceu!"
        assert "adicionado" in mensagens[0].lower(), f"Texto inesperado: {mensagens[0]}"
        
        print(f"\n✅ Texto validado com sucesso: {mensagens[0]}")
        browser.close()