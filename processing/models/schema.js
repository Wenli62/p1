const mongoose = require('mongoose');

const statsSchema = new mongoose.Schema({
    numDogs: Number,
    numCats: Number,
    numVotes: Number
});

const Stats = mongoose.model('Stats', statsSchema);

module.exports = Stats;