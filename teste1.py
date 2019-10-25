from flask import Flask

app = Flask(__name__) #o coração da api, ela q apondta tudo (padrão fazer sempre esse comando)

@app.route('/')#define qual complemento de url o metodo abaixo ira responder. ex: se bora só a "/" o metodo print é chamado
def print():
    return "isso é um print"

if __name__ == '__main__': #if para ter certeza de que ele esta rodando no main
    app.run()

