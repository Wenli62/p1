print('Start #################################################################');

db.createCollection('stats');

var stats = db.getCollection("stats");

stats.insertOne(
    { id: 1, numCat: 0, numDog: 0, numVotes: 0 }
);

print('Complete ##############################################################');