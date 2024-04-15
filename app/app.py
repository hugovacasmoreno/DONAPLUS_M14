from flask import Flask, render_template,request, redirect , url_for
import os
import database as db



template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'app', 'templates')

app=Flask(__name__, template_folder = template_dir) 




@app.route('/')
def index2():
    #return "Hola Mundo"
    return render_template('index2.html')



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

@app.route('/lista_bamcos')
def lista_bamcos():
    #return la pagina de inciar session
    
    return render_template('lista_bamcos.html')

@app.route('/confirmar', methods=['POST'])
def confirmar():
    # Aquí puedes realizar cualquier lógica de confirmación que necesites
    # Por ejemplo, podrías guardar los datos del usuario en una base de datos
    # y luego redirigir al usuario a una página de confirmación

    # Por ahora, simplemente devolvemos una respuesta de confirmación al cliente
    return '¡Confirmación exitosa! Gracias por tu donación.'

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
    return render_template('pg_dona2.html', data=insertObject) # Mandamos los datos al html por medio de data
    # Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])  # /user se utilizará en el action del form
def addUser():  #request se importará como función externa para los datos de cabecera
    username = request.form['username']  # conseguimos el imput del dato del formulario
    email = request.form['email']
    password = request.form['password']

    if username and email and password:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        data = (username, email, password) # Grabamos los datos en la consulta 
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
    username = request.form['username']  # conseguimos el imput del dato del formulario
    email = request.form['email']
    password = request.form['password']

    if username and email and password:
        cursor = db.database.cursor()
        sql = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s"
        data = (username,email, password, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home')) # Redi


if __name__ == '__main__':
    #lo que hay () sireve para poder editar sin reiniciar el server, modo depuracion
    
    app.run(debug=True, port=5000)

    #prueba