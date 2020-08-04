const mongoose = require('mongoose');
const pollSchema = require('../models/pollModel');

const Poll = mongoose.model('Poll', pollSchema);

const addPoll = (req, res) => {
    let newPoll = new Poll(req.body);

    newPoll.save((err, Poll) => {
        if (err) {
            res.status(err);
        }

        res.json(Poll);
    });
}

module.exports = {addPoll}