from flask_sqlalchemy import SQLAlchemy

# Instanciamos SqlAlchemy
db = SQLAlchemy()

#Creamos nuestros modelos(Tablas)
class Alumno(db.Model): # Hacemos una clase que herede el modelo de la base de datos para asi usarlo mas adelante como un objeto y poder acceder a los datos
    # Creamos las columnas de acuerdo a los datos que vamos a necesitar
    id_alumno = db.Column(db.Integer, primary_key=True) # primary key o llave primaria, en pocas palabras hace que vaya agregando el id automaticamente y hace que sea un valor unico, para mas info pueden googlear :)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    edad = db.Column(db.Integer)
    colegio = db.Column(db.String(50))

