
const express = require('express');
const mongoose = require('mongoose');
const bodyparser = require('body-parser');
const pollRoutes = require('./routes/pollRoutes')
    
const app = express();
const port = 3000;

// Connect to DB
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/ndioDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// bodyparser
app.use(bodyparser.urlencoded({extended: true}));
app.use(bodyparser.json());

// Link routes
pollRoutes.routes(app);

// Defaults
app.get('/', (req, res) => {
    res.send(`Ndio server listening on ${port}`)
});

app.listen(port, () => console.log(`Ndio server listening at http://localhost:${port}`))