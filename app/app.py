from flask import Flask, render_template
import os
import database as db 

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'app', 'templates')

app=Flask(__name__, template_folder = template_dir) 

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM user")
    myresult= cursor.fetchall()
    #convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html')



@app.route('/')
def index():
    #return "Hola Mundo"
    return render_template('index.html')



@app.route('/pg_dona2')
def pg_dona2():
    #return la pagina de inciar session
    
    return render_template('pg_dona2.html')

@app.route('/crear_cuenta')
def crear_cuenta():
    #return la pagina de inciar session
    
    return render_template('crear_cuenta.html')

@app.route('/mapa')
def mapa():
    #return la pagina de inciar session
    
    return render_template('mapa.html')

@app.route('/contacto')
def contacto():
    #return la pagina de inciar session
    
    return render_template('contacto.html')

@app.route('/dia_hora_donacion')
def dia_hora_donacion():
    #return la pagina de inciar session
    
    return render_template('dia_hora_donacion.html')





if __name__ == '__main__':
    #lo que hay () sireve para poder editar sin reiniciar el server, modo depuracion
    
    app.run(debug=True, port=5000)