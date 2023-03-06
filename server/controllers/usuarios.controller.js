const usuariosCtrl = {};

usuariosCtrl.getUsuarios = (req, res) => {
    res.json({
        status: 'Los adminitradores iran aqui'
    });
};

module.exports = usuariosCtrl;