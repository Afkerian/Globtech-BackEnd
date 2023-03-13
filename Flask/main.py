from flask import Flask, request, send_file
from flask import render_template
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS
import os
from uuid import uuid4

from image import proces_image
from usuarios import registrar_usuario, login, editar_password, eliminar_usuario
from noticias import get_noticias, get_noticia, eliminar_noticia, set_noticia
from metricas import actualizar_metricas, obtener_metricas
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
app.config['MONGO_URI'] = 'mongodb+srv://Admin:Globtech@sciencecodes.kbi2kns.mongodb.net/Globtech'

mongo = PyMongo(app)


############# LOGIN - REGISTRAR NUEVO ADMIN - ELIMINAR ADMIN - CAMBIAR PASSWORD ##########################

@app.route('/APILogin', methods=['POST'])
def login_usuario():
    db = mongo.db
    
    print('Ingresando Administrador')#hdhshs, dshfhsfh
    
    print(request.json)
    usuario = request.json['usuario']
    password = request.json['password']
    
    if login(usuario,password, db):
        return {'message':'Ingreso Exitoso',
                    'flag': True}
    else:
        return {'message':'Usuario o Contraseña Incorrectos',
                    'flag': False}

@app.route('/APIRegistrarUsuario', methods=['POST'])
def ingresar_usuario():
    db = mongo.db

    print('Registrando Administrador')

    print(request.json)
    usuario = request.json['usuario']
    password = request.json['password']
    rol = request.json['rol']

    if registrar_usuario(usuario, password, rol, db):
        return {'message':'Administrador Registrado Correctamente',
                    'flag': True}
    else:
        return {'message':'El usuario ya existe!',
                    'flag': False}

@app.route('/APIEliminarUsuario', methods=['DELETE'])
def eliminar_administrador():
    db = mongo.db

    print('Eliminando Administrador')

    print(request.json)
    usuario = request.json['usuario']
    password = request.json['password']
    usuario_del = request.json['usuario_del']
    
    if eliminar_usuario(usuario, password, usuario_del, db):
        return {'message':'Usuario Eliminado Correctamente',
                    'flag': True}
    else:
        return {'message':'Error al Eliminar Usuario',
                    'flag': False}


@app.route('/APICambiarPassword', methods=['PUT'])
def cambiar_password():
    db = mongo.db

    print('Cambiando Password')

    print(request.json)
    usuario = request.json['usuario']
    password = request.json['password']
    new_password = request.json['new_password']
    
    if editar_password(usuario, password, new_password, db):
        return {'message':'Password Actualizado',
                    'flag': True}
    else:
        return {'message':'Verifique los datos ingresados',
                    'flag': False}
     
###########################################################################################


########## OBTENER NOTICIAS - OBTENER NOTICIA - AGREGAR NOTICIA - ELIMINAR NOTICIA ###################
@app.route('/APINoticias', methods=['GET'])
def obtener_noticias():
    db = mongo.db

    resultado = get_noticias(db)

    return resultado

@app.route('/APINoticia', methods=['GET'])
def obtener_noticia():
    db = mongo.db

    id = request.json['id']
    resultado = get_noticia(id, db)
    
    if resultado is False:
        return {'message':'La noticia no existe en la Base de Datos',
                    'flag': False}
    else:
        return resultado

@app.route('/APIAgregarNoticia', methods=['POST'])
def agregar_noticia():
    db = mongo.db
    titulo = request.json['titulo']
    cuerpo = request.json['cuerpo']
    image = request.files['image']
    
    image = proces_image(image)
    
    if set_noticia(titulo, cuerpo, image, db):
        return {'message':'Noticia Registrada Exitosamente',
                    'flag': True}
    else:
        return {'message':'La Noticias no se pudo registrar',
                    'flag': False}

@app.route('/APIEliminarNoticia', methods=['DELETE'])
def del_noticia():
    db = mongo.db
    
    id = request.json['id']
    
    if eliminar_noticia(id, db):
        return {'message':'Noticia Eliminada Exitosamente',
                    'flag': True}
    else:
        return {'message':'Error al Eliminar',
                    'flag': False}
    
###########################################################################################

######################## ACTUALIZAR METRICAS - OBTENER METRICAS ##########################
@app.route('/APIActualizarMetricas', methods=['PUT'])
def update_metricas():
    db = mongo.db
    
    id = request.json['id']
    proyectos = request.json['proyectos']
    clientes = request.json['clientes']
    km = request.json['km']
    socios = request.json['socios']
    convenios = request.json['convenios']
    ventas = request.json['ventas']
    proformas = request.json['proformas']
    
    if actualizar_metricas(id, proyectos, clientes, km, socios, convenios, ventas, proformas ,db):
        return {'message':'Metrica Actualizada Exitosamente',
                        'flag': True}
    else:
        return {'message':'Error al Actualizar Metrica',
                        'flag': False}

@app.route('/APIObtenerMetricas', methods=['GET'])
def get_metricas():
    db = mongo.db
    
    metrica = obtener_metricas(id, db)
    if metrica is False:
        return {'message':'Error al recuperar Metrica',
                        'flag': False}
    else: 
        return metrica
############################################################################################

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True, port=5000)