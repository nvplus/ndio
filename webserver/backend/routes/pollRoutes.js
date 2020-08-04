const pollController = require('../controllers/pollController');

const routes = (app) => {
    app.route('/polls')
        .post(pollController.addPoll);
}

module.exports = {routes}