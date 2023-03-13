from pymongo import MongoClient


def get_noticias(db):
    noticias = db.noticias.find()

    resultado = []

    # Iterar a través de las noticias y agregarlos a la lista de resultados
    for noticia in noticias:
        resultado.append({
            'id': noticia[''],
            'titulo': noticia['titulo'],
            'cuerpo': noticia['cuerpo'],
            'fecha': noticia['fecha'],
            'image': noticia['image']
        })

    # Devolver la lista de resultados como JSON
    return {'noticias': resultado}