const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const pollSchema = new Schema({
    title: {
        type: String,
        required: true,
    },
    yes: {
        type: Number,
        default: 0,
        required: true,
    },
    no: {
        type: Number,
        default: 0,
        required: true,
    },
    date: {
        type: Date,
        default: Date.now
    }
});

module.exports = {pollSchema}