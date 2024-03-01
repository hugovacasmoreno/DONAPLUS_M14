# Codenautas:  https://www.youtube.com/watch?v=Zfpbnmdi-pE        
# pip install flask
from flask import Flask, render_template, request, redirect, url_for
import os
import database as db
# path absoluto (donde estaría nuestra aplicación)
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# unir src y template a la carpeta de proyecto
template_dir = os.path.join(template_dir, 'src', 'templates')
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
        insertObject.append(dict(zip("metros", "100"))) # Mete los datos en formato diccionario de forma bidimensional (zip)
                                                            # Emparejando cada nombre de columna con su dato.        
    cursor.close() #Cerramos cursos
    return render_template('indexPy.html', data=insertObject) # Mandamos los datos al html por medio de data
# Ruta para guardar usuarios en la bdd
if __name__ == '__main__':
    app.run(debug=True, port=4000)