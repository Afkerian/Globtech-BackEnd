from pymongo import MongoClient

def get_drones(db):
    
    drones = db.drones.find()

    resultado = []

    for drone in drones:
        resultado.append({
            'image': drone['image']
        })

    return {'drones': resultado}