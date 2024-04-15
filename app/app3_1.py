from flask import Flask, render_template,request, redirect , url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'app', 'templates')

app=Flask(__name__, template_folder = template_dir) 


@app.route('/')
def home():
    #return "Hola Mundo"
    return render_template('lista_bamcos.html')



if __name__ == '__main__':
    app.run(debug=True, port=5002)

