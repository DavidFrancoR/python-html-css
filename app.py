from flask import Flask
#print("Hello world!")

app = Flask(__name__)

@app.route('/hello')
def pagina_inicial():
    return "Hello World"