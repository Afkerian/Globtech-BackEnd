const express = require('express');
const router = express.Router();


const usuario = require('../controllers/usuarios.controller');

router.get('/', usuario.getUsuarios );
//router.post('/', usuario.)

module.exports = router; 