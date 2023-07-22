# Importamos las funciones que necesitamos
from flask import Flask, render_template, redirect, request, url_for
#Importamos los modelos
from models import db, Alumno

#Instanciamos flask
app = Flask(__name__)


### CONFIGURACION DE LA BASE DE DATOS SQLITE ###

# Indicamos la conexion a la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"

# Para desactivar el seguimiento de modificaciones en la base de datos con SQLALCHEMY. 
# Esto puede mejorar el rendimiento y evitar problemas de uso excesivo de memoria al no realizar un 
# seguimiento detallado de los cambios en los objetos de la base de datos.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

### TERMINA CONFIGURACION DE LA BASE DE DATOS SQLITE ###



# Inicializamos la base de datos
db.init_app(app)


## RUTA PARA VER LOS DATOS ##
@app.route("/")
def index():
    # Query para traer todos los datos
    alumnos = Alumno.query.all()
    # Para ver los datos que tenemos en la base de datos podemos iterar
    for alumno in alumnos:
        print(alumno.nombre)
    
    return render_template('index.html', alumnos=alumnos)
## TERMINA RUTA PARA VER LOS DATOS ##



## RUTA PARA AGREGAR ALUMNOS ##
@app.route("/agregar_alumnos", methods=["POST"]) # Agregamos el metodo post porque estamos enviando datos desde el cliente al servidor
def agregar_alumnos():

    if request.method == 'POST':
        # Recibimos los datos que necesitamos desde el frontend
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        colegio = request.form['colegio']
        
        # Instanciamos alumno con los datos que queremos agregar
        agregar_alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, colegio=colegio)
        # Usamos una query para guardar en la db
        db.session.add(agregar_alumno)
        # Confirmamos el cambio
        db.session.commit()
    # Redireccionamos al index o inicio
    return redirect(url_for('index'))
## TERMINA RUTA PARA AGREGAR ALUMNOS ##



## RUTA PARA ELIMINAR ALUMNO ##
@app.route("/eliminar_alumno/<id_alumno>", methods=["POST", 'GET'])
def eliminar_alumno(id_alumno):
    # Filtramos el alumno que tenemos que eliminar segun su id
    eliminar_alumno = Alumno.query.filter_by(id_alumno=id_alumno).first()

    # Eliminaos con session.delete
    db.session.delete(eliminar_alumno)
    # confirmamos cambios en la base de datos
    db.session.commit()
    
    return redirect(url_for('index'))
## TERMINA RUTA PARA ELIMINAR ALUMNO ##



## Challenge ##
# Crear la ruta para editar datos





## BREAKPOINT ##
if __name__ == "__main__":
    app.run (debug=True)
## TERMINA BREAKPOINT ##
