import os
from uuid import uuid4

def proces_image(file):
    print('Procesando Image')
    
    ext = os.path.splitext(file.filename)[1]  # obtiene la extensión del archivo
    
    filename = str(uuid4()) + ext  # genera un nombre aleatorio para el archivo
    filepath = os.path.join('../../uploads/', filename)  # especifica la ruta completa donde guardar el archivo
    file.save(filepath)  # guarda el archivo en la ruta especificada
    return filename