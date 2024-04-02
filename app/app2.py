from flask import Flask, render_template,request, redirect , url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'app', 'templates')

app=Flask(__name__, template_folder = template_dir) 

<<<<<<< HEAD
=======


>>>>>>> 9f87519a0721ebe70bc9f7abef7eaea894f7d572
@app.route('/')
def home():
    #return "Hola Mundo"
    return render_template('index.html')


<<<<<<< HEAD
if __name__ == '__main__':
    app.run(debug=True, port=5001)
=======

if __name__ == '__main__':
    #lo que hay () sireve para poder editar sin reiniciar el server, modo depuracion
    
    app.run(debug=True, port=5001)

#puer
>>>>>>> 9f87519a0721ebe70bc9f7abef7eaea894f7d572
