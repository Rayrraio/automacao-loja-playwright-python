import pytest
from playwright.sync_api import sync_playwright
from pages.loja_page import LojaPage

def test_clique_adicionar_rasteirinha():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        loja = LojaPage(page)
        
        # Ouve o alerta do navegador e imprime a mensagem no terminal
        page.on("dialog", lambda dialog: print(f"\nSucesso: {dialog.message}") or dialog.accept())
        
        loja.abrir()
        loja.adicionar_rasteirinha()
        
        # Tira print para conferir se o botão foi clicado
        page.screenshot(path="resultado_final.png")
        
        browser.close()