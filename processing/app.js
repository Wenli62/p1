const express = require('express');
const app = express();
const db = require("./dbConnect");
const Stats = require("./models/schema")

app.get('/', (req, res) => {
  res.send('Analysis service running...');
});

const analyze = async () => {
  try {

    // get data
    const sql = 'SELECT * FROM `vote_report`';
    const [ rows ] = await db.sqlConnection.execute(sql);

    // calculate stats
    const numDogs = rows.filter((entry) => entry.user_input === "Dogs").length;
    const numCats = rows.filter((entry) => entry.user_input === "Cats").length;
    const numRows = rows.length

    const stats = [ {"numDogs": numDogs, "numCats": numCats, "numVotes": numRows }]

    // output to mongodb
    Stats.overwrite(stats)
    await Stats.save();

    mongoose.connection.close()

  } catch (err){
    console.log(err);
  }
};


const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
  analyze();
});
