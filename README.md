                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Para instalar el entorno virtual
  pip install virtualenv
Para montar el entorno virtual en env
  virtualenv -p python3 env
Para dar permisos de debloquear la prohibicin de ejecutar scripts
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Para entrar en el entorno vurtual 
  .\env\Scripts\activate
Instalamos el FLASK
  pip install flask
Para listar lo instalado
  pip list
Para instalar la base de datos 
  pip install flask_mysqldb
Iniciar la applicación
  python .\app\app.py                                         
hoola

 pip install mysql-connector-python==8.0.29
