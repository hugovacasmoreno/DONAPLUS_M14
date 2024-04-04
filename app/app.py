from flask import Flask, render_template,request, redirect , url_for
import os
import database as db

<<<<<<< Updated upstream
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'app', 'templates')

app=Flask(__name__, template_folder = template_dir) 
=======
app=Flask(__name__)
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
>>>>>>> Stashed changes



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


@app.route('/confirmar', methods=['POST'])
def confirmar():
    # Aquí puedes realizar cualquier lógica de confirmación que necesites
    # Por ejemplo, podrías guardar los datos del usuario en una base de datos
    # y luego redirigir al usuario a una página de confirmación

    # Por ahora, simplemente devolvemos una respuesta de confirmación al cliente
    return '¡Confirmación exitosa! Gracias por tu donación.'

db_config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'pythonbd',
    'raise_on_warnings': True
}

@app.route('/lista_bancos_alimentos')
def listar_bancos_de_alimentos():
    # Conexión a la base de datos
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Consulta para recuperar los bancos de alimentos
    query = "SELECT * FROM `banco_alimentos`"
    cursor.execute(query)
    bancos = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    cursor.close()
    connection.close()

    # Renderizar la plantilla HTML con los bancos de alimentos
    return render_template('lista_bancos.html', bancos=bancos)

if __name__ == '__main__':
    #lo que hay () sireve para poder editar sin reiniciar el server, modo depuracion
    
    app.run(debug=True, port=5000)

    #prueba