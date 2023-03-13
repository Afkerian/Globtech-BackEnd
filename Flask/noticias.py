from pymongo import MongoClient
import datetime
import locale


def get_noticias(db):
    noticias = db.noticias.find()

    resultado = []

    # Iterar a través de las noticias y agregarlos a la lista de resultados
    for noticia in noticias:
        resultado.append({
            'id': noticia['_id'],
            'titulo': noticia['titulo'],
            'cuerpo': noticia['cuerpo'],
            'fecha': noticia['fecha'],
            'image': noticia['image']
        })

    # Devolver la lista de resultados como JSON
    return {'noticias': resultado}

def set_noticia(titulo, cuerpo, image, db):
    print('Agregando una noticia')
    
    noticias = db['noticias']
    
    # establecer el idioma local en español
    locale.setlocale(locale.LC_TIME, 'es_ES')

    # obtener la fecha actual
    fecha_actual = datetime.datetime.now()

    # formatear la fecha en el formato deseado
    fecha = fecha_actual.strftime('%d %B, %Y').upper()
    
    mydict = {'titulo': titulo, 'cuerpo': cuerpo, 'fecha': fecha, 'image': image}
    
    x = noticias.insert_one(mydict)
    
    if x is not None:
        return True
    else:
        return False

def eliminar_noticia(id, db):
    print('Eliminar Noticia')
    
    noticias = db['noticias']
    resultado = noticias.find_one({'id': id})
    
    if resultado is not None:
        # El usuario existe en la base de datos
        print('La noticia existe en la base de datos')
        noticias.delete_one({ 'id': id })
        return True
    else:
        return False
    
def get_noticia(id, db):
    noticias = db['noticias']
    resultado = noticias.find_one({'id': id})
    
    if resultado is not None:
        # El usuario existe en la base de datos
        print('La noticia existe en la base de datos')
        return resultado
    else:
        return False