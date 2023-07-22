from flask import Flask, render_template, redirect, request, url_for
from models import db, Alumno

#Instanciamos flask
app = Flask(__name__)

# configurar la base de datos SQLite

# Indicamos la conexion a la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"

# Para desactivar el seguimiento de modificaciones en la base de datos con SQLALCHEMY. 
#Esto puede mejorar el rendimiento y evitar problemas de uso excesivo de memoria al no realizar un 
# seguimiento detallado de los cambios en los objetos de la base de datos.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)


# Ruta para ver
@app.route("/")
def index():
    # Query para traer todos los datos
    alumnos = Alumno.query.all()
    # Para imprimir los datos
    for alumno in alumnos:
        print(alumno.nombre)
    
    return render_template('index.html', alumnos=alumnos)

# Ruta para agregar
@app.route("/agregar_alumnos", methods=["POST"]) # Agregamos el metodo post porque estamos enviando datos desde el front
def agregar_alumnos():

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        colegio = request.form['colegio']
        
        # Instanciamos alumno con los datos que queremos agregar
        agregar_alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, colegio=colegio)
        # Usamos un query para guardar en la db
        db.session.add(agregar_alumno)
        # Confirmamos el cambio
        db.session.commit()

    return redirect(url_for('index'))

# Ruta para eliminar
@app.route("/eliminar_alumno/<id_alumno>", methods=["POST", 'GET']) 
def eliminar_alumno(id_alumno):
    # Filtramos el alumno que tenemos que eliminar segun su id
    eliminar_alumno = Alumno.query.filter_by(id_alumno=id_alumno).first()

    # Eliminaos con session.delete
    db.session.delete(eliminar_alumno)
    # confirmamos cambios en la base de datos
    db.session.commit()
    
    return redirect(url_for('index'))

## Breakpoint ##
if __name__ == "__main__":
    app.run (debug=True)
