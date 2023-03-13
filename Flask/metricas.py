

def actualizar_metricas(id, proyectos, clientes, km, socios, convenios, ventas, proformas ,db):
    print('Actualizando Metricas')
    
    metricas = db['usuarios']
    resultado = metricas.find_one({'id': id})

    if resultado is not None:
        # La metrica existe en la base de datos
        print('El usuario existe en la base de datos')
        
        myquery = { "id": id }
        newvalues = { "$set": { "proyectos": proyectos, "clientes": clientes, "km": km, "socios": socios, "convenios": convenios, "ventas": ventas, "proformas": proformas } }
        
        metricas.update_one(myquery, newvalues)
            
        return True
        
    else:
        return False

def obtener_metricas(id, db):
    print('Obteniendo Metricas')
    
    metricas = db['metricas']
    resultado = db.metricas.find_one({'id': id})
    
    if resultado is not None:
        # La metrica existe en la base de datos
        print('La metrica existe en la base de datos')
        return resultado
    else:
        return False