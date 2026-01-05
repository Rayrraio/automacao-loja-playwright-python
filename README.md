# 🚀 Automação de Testes E2E - Loja de Calçados

Projeto de automação de testes ponta a ponta (End-to-End) desenvolvido para validar as funcionalidades de uma loja virtual. O foco principal foi a implementação do padrão **Page Object Model (POM)** para garantir um código limpo e de fácil manutenção.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Framework de Testes:** Pytest
* **Ferramenta de Automação:** Playwright
* **Ambiente:** GitHub Codespaces (Linux)

## 🏗️ Arquitetura do Projeto (POM)
O projeto está organizado seguindo as melhores práticas de mercado:
* `pages/`: Contém os seletores e as ações da página (encapsulamento).
* `tests/`: Contém os scripts de teste reais que executam as validações.

## 🧪 Cenários Automatizados
1. **Adicionar Produto ao Carrinho:** O robô acessa a loja, localiza o item "Rasteirinha" e valida a interação com o botão de compra, lidando com diálogos de alerta do navegador.

## 🛡️ Desafios Técnicos Superados
Durante o desenvolvimento, foram aplicadas soluções de engenharia de QA para:
* **Configuração de Ambiente Linux:** Instalação de dependências de sistema para navegadores via `playwright install-deps`.
* **Execução Headless:** Configuração para rodar testes em servidores sem interface gráfica.
* **Tratamento de Timeouts:** Otimização de seletores (XPath e Role) para garantir a estabilidade dos testes.

## 📊 Resultados
Os testes são executados com sucesso em menos de 1 segundo, gerando evidências visuais (screenshots) de cada execução.

![Resultado do Teste](./resultado_final.png)