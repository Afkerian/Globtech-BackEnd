from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

def login(usuario, password, db):
    print('Ingresando Administrador')
    
    usuarios = db['usuarios']
    resultado = usuarios.find_one({'usuario': usuario})
    
    if resultado is not None:
        # El usuario existe en la base de datos
        print('El usuario existe en la base de datos')
        if check_password_hash(resultado['password'],password):
            return True
        else:
            return False
    else:
        print('El usuario no existe en la base de datos')
        return False

def registrar_usuario(usuario, password, rol, db):
    print('Registrando un Usuario')

    usuarios = db['usuarios']
    resultado = usuarios.find_one({'usuario': usuario})

    if resultado is not None:
        # El usuario existe en la base de datos
        return False
    else:
        print('El usuario no existe en la base de datos')
        password = generate_password_hash(password)
        
        mydict = {'usuario': usuario, 'password': password, 'rol': rol}
        x = usuarios.insert_one(mydict)

        return True

def eliminar_usuario(usuario, password, usuario_del, db):
    print('Eliminar Administrador')
    
    usuarios = db['usuarios']
    resultado = usuarios.find_one({'usuario': usuario})
    
    if resultado is not None:
        # El usuario existe en la base de datos
        print('El usuario existe en la base de datos')
        if check_password_hash(resultado['password'],password):
            if resultado['rol'] == 'root':
                usuarios.delete_one({ 'usuario': usuario_del })
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    

def editar_password(usuario, password, new_password, db):
    print('Cambiando Password')
    
    usuarios = db['usuarios']
    resultado = usuarios.find_one({'usuario': usuario})
    
    if resultado is not None:
        # El usuario existe en la base de datos
        print('El usuario existe en la base de datos')
        if check_password_hash(resultado['password'],password):
            myquery = { "usuario": usuario }
            newvalues = { "$set": { "password": new_password } }

            usuarios.update_one(myquery, newvalues)
            
            return True
        else:
            return False
    else:
        return False