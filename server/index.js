const express = require('express');
const morgan = require('morgan');
const app = express();
const {mongoose} = require('./database');

// Configuraciones
app.set('port', process.env.PORT || 3000);


//Middlewares
app.use(morgan('dev'));
app.use(express.json());


//Routes
app.use('/api/usuarios/',require('./routes/usuarios.routers'));
app.use('/api/noticias/', require('./routes/noticias.routers'));

//Iniciar servidor
app.listen(app.get('port'), () => {
    console.log('Server on port:', app.get('port'));

});