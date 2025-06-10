# 💰 Payment API com WebSocket


## ✨ Sobre o Projeto
Desenvolvi esta API como parte da minha jornada de estudos em desenvolvimento back-end. Ela simula todo o fluxo de um pagamento Pix, desde a geração do QR Code até a confirmação em tempo real usando WebSocket - tudo isso com Python e Flask!

## 🚀 Destaques Técnicos
Tecnologias que dominei neste projeto:

Flask para construção da API RESTful

WebSocket para comunicação em tempo real

SQLAlchemy para persistência de dados

Geração dinâmica de QR Codes

##⚡ Funcionalidades Incríveis
Criação instantânea de pagamentos Pix com QR Code

Monitoramento em tempo real do status do pagamento

Sistema de webhook para confirmação de transações

Interface amigável para visualização do QR Code

## 🛠️ Como Rodar Localmente
bash
### Clone o projeto
git clone https://github.com/FourYak/Payment-API-Websocket.git
cd Payment-API-Websocket

### Prepare o ambiente
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

### Instale as dependências
pip install -r requirements.txt

### Inicie o servidor
flask run

## 📌 O Que Aprendi
Padrões de API REST

Comunicação bidirecional com WebSocket

Gerenciamento de banco de dados com SQLAlchemy

Geração e manipulação de QR Codes

Boas práticas de estruturação de projetos Flask
