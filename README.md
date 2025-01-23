# Documentação do Projeto: MyWppBot

## Visão Geral

**MyWppBot** é um bot desenvolvido em Python utilizando o Flask e a biblioteca Twilio para automatizar interações via WhatsApp. O projeto inclui um menu de opções e permite respostas personalizadas baseadas na escolha do usuário.

## Requisitos

### Dependências do Projeto:

1. **Python 3.8 ou superior**
2. **Flask** (para criar o servidor web)
   - Instalação: `pip install flask`
3. **Twilio** (para interações via WhatsApp)
   - Instalação: `pip install twilio`
4. **ngrok** (para expor o servidor local para a internet)
   - Instalação: Baixe e configure o [ngrok](https://ngrok.com/)

### Configurações do Ambiente Virtual

1. Criar o ambiente virtual:
   ```bash
   python -m venv myWppbot
   ```
2. Ativar o ambiente virtual:
   - No Windows (CMD):
     ```bash
     myWppbot\Scripts\activate
     ```
3. Instalar dependências:
   ```bash
   pip install flask twilio
   ```

## Estrutura do Projeto

```
myWppbot/
|-- myWppbot.py       # Arquivo principal do bot
|-- venv/             # Ambiente virtual
|-- README.md         # Documentação do projeto
```

## Implementação

### Funcionalidades do Bot

1. **Menu Inicial**:

   - Exibe um menu com quatro opções para o usuário.

2. **Persistência de Escolhas**:

   - Utiliza sessões do Flask para armazenar a opção selecionada.

3. **Interação Personalizada**:

   - Responde dinamicamente com base na opção escolhida.

4. **Mensagens Não Implementadas**:

   - Indica funcionalidades ainda não implementadas para opções específicas.

### Endpoints

- ``:

  - Tipo: `POST`
  - Função: Recebe mensagens do Twilio e responde dinamicamente com base na entrada do usuário.

- ``:


## Exposição do Servidor Local (ngrok)

Para testar o bot com o Twilio, você precisa expor o servidor local usando o ngrok:

1. Execute o ngrok na porta onde o Flask está rodando (padrão 5000):
   ```bash
   ngrok http 5000
   ```
2. Copie a URL gerada pelo ngrok (algo como `https://<ngrok-id>.ngrok-free.app`).
3. Configure essa URL como webhook no painel do Twilio.

## Configuração do Twilio

1. Crie uma conta no [Twilio](https://www.twilio.com/).
2. Obtenha um número de telefone no Twilio.
3. Configure o webhook para apontar para o endpoint `/message`:
   - URL do webhook: `https://<ngrok-id>.ngrok-free.app/message`

## Testes

- Envie uma mensagem para o número configurado no Twilio.
- O bot deve responder com o menu inicial ou com base na opção escolhida.

## Conclusão

O **MyWppBot** é um projeto inicial que demonstra como integrar o Flask com o Twilio para criar um bot interativo no WhatsApp. Ele pode ser expandido para incluir funcionalidades mais complexas e integrações adicionais.

