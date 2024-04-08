# Codenautas:  https://www.youtube.com/watch?v=Zfpbnmdi-pE        
# pip install flask
from flask import Flask, render_template, request, redirect, url_for
import os
import database as db
# path absoluto (donde estaría nuestra aplicación)
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# unir src y template a la carpeta de proyecto
template_dir = os.path.join(template_dir, 'app', 'templates')
# name para poder lanzar la aplicación, atraves de un puerto
# indica donde esta el directorio html
app = Flask(__name__, template_folder = template_dir)

# Rutas de la aplicación
@app.route('/') # ruta principal, accedemos aplicación
def home(): # Viculamos función
    cursor = db.database.cursor() # LLamamos a la base de datos mediante la función cursor
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall() # Obtenemos los datos de la búsqueda
    # Convertir los datos a diccionario para obtener una clave de cada uno de los datos
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult: # En record accedemosa a cada uno de los registros de la consulta myresult 
        insertObject.append(dict(zip(columnNames, record))) # Mete los datos en formato diccionario de forma bidimensional (zip)
                                                            # Emparejando cada nombre de columna con su dato.        
    cursor.close() #Cerramos cursos
    return render_template('index.html', data=insertObject) # Mandamos los datos al html por medio de data
    # Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])  # /user se utilizará en el action del form
def addUser():  #request se importará como función externa para los datos de cabecera
    username = request.form['username']  # conseguimos el imput del dato del formulario
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        data = (username, name, password) # Grabamos los datos en la consulta 
        cursor.execute(sql, data)
        db.database.commit() # Grabamos en base de datos
    return redirect(url_for('home')) # Actualizamos la vista redireccionando a 
                                     # la función home 
#  Ruta para borrar registros de la bdd
@app.route('/delete/<string:id>') # Parámetro que urilizaremo como clave de registro
def delete(id):  # Pasamos parámetro
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))
# Ruta para editar registros de la bdd
@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = db.database.cursor()
        sql = "UPDATE users SET username = %s, name = %s, password = %s WHERE id = %s"
        data = (username, name, password, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home')) # Redi

if __name__ == '__main__':
    app.run(debug=True, port=5001)