from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import MySQLdb

from config import config

app = Flask(__name__)

conexion = MySQL(app)
db = MySQLdb.connect("localhost", "root", "12345", "practicas")


@app.route('/profesores')
def listar_profesores():
    try:
        cursor = db.cursor()

        sql = "SELECT * FROM profesor"

        cursor.execute(sql)

        datos = cursor.fetchall()

        profesores = []
        for fila in datos:
            profesor = {
                "id": fila[0],
                "nombre": fila[1],
                "apellidos": fila[2],
                "password": fila[3],
                "correo": fila[4]
            }
            profesores.append(profesor)

        return jsonify({'Profesores': profesores})
    except Exception as ex:
        return "Error"


@app.route('/empresas')
def listar_empresas():
    try:
        cursor = db.cursor()

        sql = "SELECT * FROM empresa"

        cursor.execute(sql)

        datos = cursor.fetchall()

        empresas = []
        for fila in datos:
            empresa = {
                "id": fila[0],
                "nombre": fila[1],
                "telefono": fila[2],
                "correo": fila[3],
                "responsable": fila[4],
                "observaciones": fila[5]
            }
            empresas.append(empresa)

        return jsonify({'Empresa': empresas})
    except Exception as ex:
        return "Error"


@app.route('/alumno/empresa/<id>')
def listar_empresa_alumno(id):
    try:
        cursor = db.cursor()

        sql = "SELECT e.* FROM empresa e, alumno a WHERE e.id = a.empresa AND a.id = '{0}'".format(id)

        cursor.execute(sql)

        datos = cursor.fetchone()

        if datos != None:
            empresa = {
                "id": datos[0],
                "nombre": datos[1],
                "telefono": datos[2],
                "correo": datos[3],
                "responsable": datos[4],
                "observaciones": datos[5]
            }

        return jsonify({'Empresa': empresa})
    except Exception as ex:
        return "Error"


@app.route('/alumnos')
def listar_alumnos():
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM alumno"
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno = {
                "id": fila[0],
                "nombre": fila[1],
                "apellidos": fila[2],
                "password": fila[3],
                "dni": fila[4],
                "nacimiento": fila[5],
                "correo": fila[6],
                "telefono": fila[7],
                "totaldual": fila[8],
                "totalfct": fila[9],
                "observaciones": fila[10],
                "profesor": fila[11],
                "empresa": fila[12]
            }
            alumnos.append(alumno)
        return jsonify({'Alumnos': alumnos})
    except Exception as ex:
        return "Error"


@app.route('/profesor/alumnos/<id>')
def listar_alumnos_profesor(id):
    try:
        cursor = db.cursor()
        sql = "SELECT a.* FROM alumno a, profesor p WHERE a.profesor = p.id AND a.profesor = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno = {
                "id": fila[0],
                "nombre": fila[1],
                "apellidos": fila[2],
                "password": fila[3],
                "dni": fila[4],
                "nacimiento": fila[5],
                "correo": fila[6],
                "telefono": fila[7],
                "totaldual": fila[8],
                "totalfct": fila[9],
                "observaciones": fila[10],
                "profesor": fila[11],
                "empresa": fila[12]
            }
            alumnos.append(alumno)
        return jsonify({'Alumnos': alumnos})
    except Exception as ex:
        return "Error"


"""Método que obtiene un listado de actividades"""


@app.route('/actividades')
def listar_actividades():
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM actividad"

        cursor.execute(sql)

        datos = cursor.fetchall()
        actividades = []
        for fila in datos:
            actividad = {
                "id": fila[0],
                "fecha": fila[1],
                "horas": fila[2],
                "actividad": fila[3],
                "observaciones": fila[4],
                "alumno": fila[5],
            }
            actividades.append(actividad)
        return jsonify({'Actividades': actividades})
    except Exception as ex:
        return "Error"


@app.route('/actividades/alumno/<id>')
def listar_actividades_alumno(id):
    try:
        cursor = db.cursor()
        sql = "SELECT a.* FROM actividad a, alumno al WHERE a.alumno = al.id AND a.alumno = '{0}'".format(id)

        cursor.execute(sql)

        datos = cursor.fetchall()
        actividades = []
        for fila in datos:
            actividad = {
                "id": fila[0],
                "fecha": fila[1],
                "horas": fila[2],
                "actividad": fila[3],
                "observaciones": fila[4],
                "alumno": fila[5],
            }
            actividades.append(actividad)
        return jsonify({'Actividades': actividades})
    except Exception as ex:
        return "Error"


@app.route('/profesores/<id>', methods=['GET'])
def obtener_profesor_id(id):
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM profesor WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            profesor = {
                "id": datos[0],
                "nombre": datos[1],
                "apellidos": datos[2],
                "password": datos[3],
                "correo": datos[4]
            }
        return jsonify({'Profesor': profesor})
    except Exception as ex:
        return "Error"


@app.route('/empresas/<id>', methods=['GET'])
def obtener_empresa_id(id):
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM empresa WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            empresa = {
                "id": datos[0],
                "nombre": datos[1],
                "telefono": datos[2],
                "correo": datos[3],
                "responsable": datos[4],
                "observaciones": datos[5]
            }
        return jsonify({'Empresa': empresa})
    except Exception as ex:
        return "Error"


@app.route('/alumnos/<id>', methods=['GET'])
def obtener_alumnos_id(id):
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM alumno WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            alumno = {
                "id": datos[0],
                "nombre": datos[1],
                "apellidos": datos[2],
                "password": datos[3],
                "dni": datos[4],
                "nacimiento": datos[5],
                "correo": datos[6],
                "telefono": datos[7],
                "totaldual": datos[8],
                "totalfct": datos[9],
                "observaciones": datos[10],
                "profesor": datos[11],
                "empresa": datos[12]
            }
        return jsonify({'Alumnos': alumno})
    except Exception as ex:
        return "Error"


@app.route('/actividades/<id>', methods=['GET'])
def obtener_actividad_id(id):
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM actividad WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            actividad = {
                "id": datos[0],
                "fecha": datos[1],
                "horas": datos[2],
                "actividad": datos[3],
                "observaciones": datos[4],
                "alumno": datos[5],
            }
        return jsonify({'Actividad': actividad})
    except Exception as ex:
        return "Error"


# MÉTODOS POST
@app.route('/profesores', methods=['POST'])
def registrar_profesor():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO profesor(nombre, apellidos, password, correo) 
        VALUES ('{0}', '{1}', '{2}', '{3}')""".format(request.json['nombre'],
                                                      request.json['apellidos'],
                                                      request.json['password'],
                                                      request.json['correo'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Profesor añadido con éxito"})
    except Exception as ex:
        return "Error"


@app.route('/empresas', methods=['POST'])
def registrar_empresa():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO empresa(nombre, telefono, correo, responsable, observaciones) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(request.json['nombre'],
                                                             request.json['telefono'],
                                                             request.json['correo'],
                                                             request.json['responsable'],
                                                             request.json['observaciones'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Empresa añadida con éxito"})
    except Exception as ex:
        return "Error"


@app.route('/alumnos', methods=['POST'])
def registrar_alumno():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO alumno(nombre, apellidos, password, dni, nacimiento, correo, telefono, totaldual, totalfct, observaciones, profesor, empresa) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')""".format(
            request.json['nombre'],
            request.json['apellidos'],
            request.json['password'],
            request.json['dni'],
            request.json['nacimiento'],
            request.json['correo'],
            request.json['telefono'],
            request.json['totaldual'],
            request.json['totalfct'],
            request.json['observaciones'],
            request.json['profesor'],
            request.json['empresa'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Alumno añadido con éxito"})
    except Exception as ex:
        return "Error"


@app.route('/actividades', methods=['POST'])
def registrar_actividad():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO actividad(fecha, horas, actividad, observaciones, alumno) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(request.json['fecha'],
                                                             request.json['horas'],
                                                             request.json['actividad'],
                                                             request.json['observaciones'],
                                                             request.json['alumno'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Actividad añadida con éxito"})
    except Exception as ex:
        return "Error"


# MÉTODOS DELETE
@app.route('/profesores/<id>', methods=['DELETE'])
def eliminar_profesor_id(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM profesor WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Profesor con ID '{0}' eliminado con éxito".format(id)})
    except Exception as ex:
        return "Error"


@app.route('/empresas/<id>', methods=['DELETE'])
def eliminar_empresas_id(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM empresa WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Empresa con ID '{0}' eliminada con éxito".format(id)})
    except Exception as ex:
        return "Error"


@app.route('/alumnos/<id>', methods=['DELETE'])
def eliminar_alumno_id(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM alumno WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Alumno con ID '{0}' eliminado con éxito".format(id)})
    except Exception as ex:
        return "Error"


@app.route('/actividades/<id>', methods=['DELETE'])
def aliminar_actividad_id(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM actividad WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Actividad con ID '{0}' eliminada con éxito".format(id)})
    except Exception as ex:
        return "Error"


# MÉTODOS PUT
@app.route('/profesores/<id>', methods=['PUT'])
def actualizar_profesor(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE profesor SET nombre = '{0}', apellidos = '{1}', password = '{2}', correo = '{3}' 
        WHERE id = '{4}'""".format(request.json['nombre'],
                                   request.json['apellidos'],
                                   request.json['password'],
                                   request.json['correo'],
                                   id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Profesor con ID '{0}' actualizado con éxito".format(id)})
    except Exception as ex:
        return jsonify({'Mensaje': "Error"})


@app.route('/empresas/<id>', methods=['PUT'])
def actualizar_empresa(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE empresa SET nombre = '{0}', telefono = '{1}', correo = '{2}', responsable = '{3}', observaciones = '{4}' 
        WHERE id = '{5}'""".format(request.json['nombre'],
                                   request.json['telefono'],
                                   request.json['correo'],
                                   request.json['responsable'],
                                   request.json['observaciones'],
                                   id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Profesor con ID '{0}' actualizado con éxito".format(id)})
    except Exception as ex:
        return jsonify({'Mensaje': "Error"})


@app.route('/alumnos/<id>', methods=['PUT'])
def actualizar_alumno(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE alumno SET nombre = '{0}', apellidos = '{1}', password = '{2}', dni = '{3}', nacimiento = '{4}', 
        correo = '{5}', telefono = '{6}', totaldual = '{7}', totalfct = '{8}', observaciones = '{9}', profesor = '{10}', empresa = '{11}',
        WHERE id = '{12}'""".format(request.json['nombre'],
                                    request.json['apellidos'],
                                    request.json['password'],
                                    request.json['dni'],
                                    request.json['nacimiento'],
                                    request.json['correo'],
                                    request.json['telefono'],
                                    request.json['totaldual'],
                                    request.json['totalfct'],
                                    request.json['observaciones'],
                                    request.json['profesor'],
                                    request.json['empresa'],
                                    id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Alumno con ID '{0}' actualizado con éxito".format(id)})
    except Exception as ex:
        return jsonify({'Mensaje': "Error"})


@app.route('/actividades/<id>', methods=['PUT'])
def actualizar_actividad(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE actividad SET fecha = '{0}', horas = '{1}', actividad = '{2}', observaciones = '{3}', alumno = '{4}' WHERE id = '{5}'""".format(
            request.json['fecha'],
            request.json['horas'],
            request.json['actividad'],
            request.json['observaciones'],
            request.json['alumno'],
            id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'Mensaje': "Actividad con ID '{0}' actualizada con éxito".format(id)})
    except Exception as ex:
        return jsonify({'Mensaje': "Error"})


@app.route('/horas/alumno/<id>')
def obtener_horas_alumno(id):
    global total_dual, total_fct
    try:
        cursor = db.cursor()
        sql = "SELECT totaldual, totalfct FROM alumno WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos is not None:
            total_dual = datos['totaldual']
            total_fct = datos['totalfct']

        return jsonify({"Total DUAL:", total_dual, "Total FCT:", total_fct})
    except Exception as ex:
        return "Error"


def pagina_no_encontrada(error):
    return "<h1>PÁGINA NO ENCONTRADA</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
