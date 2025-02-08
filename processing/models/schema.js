const mongoose = require('mongoose');

const statsSchema = new mongoose.Schema({
    id: Number,
    numDogs: Number,
    numCats: Number,
    numVotes: Number
});

const Stats = mongoose.model('Stats', statsSchema);

module.exports = Stats;