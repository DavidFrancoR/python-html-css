import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

#print("Hello world!")

#configuração
DATABASE = "blog.db"
SECRET_KEY = 'pudim'

app = Flask(__name__)

@app.route('/hello')
def pagina_inicial():
    return "Hello World"