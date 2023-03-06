const mongoose = require('mongoose');

const URI = 'mongodb+srv://Admin:Globtech@sciencecodes.kbi2kns.mongodb.net/Globtech';

mongoose.connect(URI)
    .then(db => console.log('DB is connect'))
    .catch(err => console.error(err)); //URI DE LA BASE DE DATOS

module.exports = mongoose;