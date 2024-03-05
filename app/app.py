from flask import Flask, render_template, url_for

app=Flask(__name__)


@app.route('/')
def index():
    #return "Hola Mundo"
    return render_template('index.html')

@app.route('/index.html')
def index():
    #return "Hola Mundo"
    return render_template('index.html')

@app.route('/pg_dona2.html')
def pg_dona2():
    #return la pagina de inciar session
    
    return render_template('pg_dona2.html')

@app.route('/mapa.html')
def mapa():
    #return la pagina de inciar session
    
    return render_template('mapa.html')

@app.route('/contacto.html')
def contacto():
    #return la pagina de inciar session
    
    return render_template('contacto.html')




if __name__ == '__main__':
    #lo que hay () sireve para poder editar sin reiniciar el server, modo depuracion
    
    app.run(debug=True, port=5000)