const mongoose = require('mongoose');
const { Schema } = mongoose;

const noticiasSchema = new Schema({
    title: {type: String, required: true},
    wallpapper: {type: Buffer, required: true},
    sampleImage: {type: Buffer, required: true},
    text: {type: String, required: true}
});

module.exports = mongoose.model('Noticias', noticiasSchema);
