const Noticias = require('../models/noticias');
const noticiasCtrl = {};

noticiasCtrl.getNoticias = async (req, res) => {
    const noticias = await Noticias.find();
    res.json(noticias);
};

noticiasCtrl.createNoticias = async (req, res) => {
    //console.log(req.body);
    const noticia =  new Noticias(req.body);
    //console.log(noticia);
    await noticia.save();
    res.json({
        'status':'Noticia Guardada'
    });
};

module.exports = noticiasCtrl;
