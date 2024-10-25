from flask import request, Flask, session
from twilio.twiml.messaging_response import MessagingResponse

menu = "*Digite a opção que você deseja:*\n 1. Realizar matrícula\n 2. Vestibular UNEX\n 3. Financeiro\n 4. Sair"

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/message', methods=['POST'])
def messagebot():
    message = request.form.get('Body', '').lower()  # Use .get to prevent KeyError
    response = MessagingResponse()
    print(f"mensagem recebida: {message}")
    print(f"session: {session}")  # Debug da sessão

    if 'opcao' in session:
        opcao = session['opcao']
        response.message(f"Você já selecionou a opção: {opcao}")
    else:
        if message == '1':
            session['opcao'] = 1
            response.message('Ainda não implementado')
        elif message == '2':
            session['opcao'] = 2
            response.message('Ainda não implementado')
        elif message == '3':
            session['opcao'] = 3
            response.message('Ainda não implementado')
        elif message == '4':
            session['opcao'] = 4
            response.message('Até logo, volte sempre')
        else:
            boasVindas = "Bem-vindo(a) a UNEX!"
            response.message(boasVindas + "\n" + menu)

    return str(response)

@app.route('/teste', methods=['GET'])
def teste():
    return 'Funcionou!'
