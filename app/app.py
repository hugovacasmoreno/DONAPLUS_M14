from flask import Flask, render_template, url_for

app=Flask(__name__)


@app.route('/')
def index():
    #return "Hola Mundo"
    return render_template('index.html')

if __name__ == '__main__':
    #lo que hay () sireve para poder editar sin reiniciar el server, modo depuracion
    
    app.run(debug=True, port=5000)