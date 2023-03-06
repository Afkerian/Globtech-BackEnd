const express = require('express');
const router = express.Router();


const noticia = require('../controllers/noticias.controller');

router.get('/', noticia.getNoticias );
router.post('/', noticia.createNoticias );

module.exports = router; 