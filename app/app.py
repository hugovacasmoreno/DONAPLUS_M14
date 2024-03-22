from flask import Flask, render_template,request, redirect , url_for
import os
import database as db 

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'app', 'templates')

app=Flask(__name__, template_folder = template_dir) 

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult= cursor.fetchall()
    #convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)
#Ruta para guardar usuarios a la base de datos
@app.route('/user', methods=['POST'])
def addUser():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        data=(username, name, password)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))
#consulta eliminar un user
@app.route('/delete/<string:id>')
def delete(id):
      cursor = db.database.cursor()
      sql = "DELETE FROM users WHERE id=%s)"
      data=(id,)
      cursor.execute(sql, data)
      db.database.commit()
      return redirect(url_for('home'))

@app.route('/edit/<string:id>',methods=['POST'])
def edit(id):
      username = request.form['username']
      name = request.form['name']
      password = request.form['password']
#para modificar los datos
      if username and name and password:
        cursor = db.database.cursor()
        sql = "UPDATE  users SET username = %s, name= %s, password=%s WHERE id =%s"
        data=(username, name, password)
        cursor.execute(sql, data)
        db.database.commit()
      return redirect(url_for('home'))

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


@app.route('/confirmar', methods=['POST'])
def confirmar():
    # Aquí puedes realizar cualquier lógica de confirmación que necesites
    # Por ejemplo, podrías guardar los datos del usuario en una base de datos
    # y luego redirigir al usuario a una página de confirmación

    # Por ahora, simplemente devolvemos una respuesta de confirmación al cliente
    return '¡Confirmación exitosa! Gracias por tu donación.'



if __name__ == '__main__':
    #lo que hay () sireve para poder editar sin reiniciar el server, modo depuracion
    
    app.run(debug=True, port=5000)