const express = require("express");
const app = express();
const db = require("./dbConnect");

app.get("/", (req, res) => {
  res.send("Analysis service running...");
});

const analyze = async () => {
  try {
    // get data
    const sql = "SELECT * FROM `grade_report`";
    const [rows] = await db.sqlConnection.execute(sql);

    let students = [];

    if (rows.length > 0) {
      // calculate stats
      // calculate average by student
      const student_grp = Object.groupBy(rows, ({ student_id }) => student_id);

      for (const [key, value] of Object.entries(student_grp)) {
        let all_averages = {
          mathematics: 0,
          physics: 0,
          chemistry: 0,
          biology: 0,
          history: 0,
          geography: 0,
          english: 0,
          "computer science": 0,
        };

        let subjects = Object.groupBy(value, ({ subject }) => subject);

        for (const array of Object.values(subjects)) {
          let sum = array.reduce((acc, item) => acc + item.grade, 0);
          let average = Math.round(sum / array.length);
          all_averages[`${array[0].subject.toLowerCase()}`] = average;
        }

        final_dict = {
          student_id: key,
          math_avg: all_averages["mathematics"],
          physics_avg: all_averages["physics"],
          chem_avg: all_averages["chemistry"],
          bio_avg: all_averages["biology"],
          his_avg: all_averages["history"],
          geo_avg: all_averages["geography"],
          eng_avg: all_averages["english"],
          cs_avg: all_averages["computer science"],
        };
        students.push(final_dict);
      }

      // calculate overall averages
      // group by subject, get the grades part, average
      const sub_grp = Object.groupBy(rows, ({ subject }) => subject);

      let sub_avg = {
        mathematics: 0,
        physics: 0,
        chemistry: 0,
        biology: 0,
        history: 0,
        geography: 0,
        english: 0,
        "computer science": 0,
      };

      for (const array of Object.values(sub_grp)) {
        let sum = array.reduce((acc, item) => acc + item.grade, 0);
        let average = Math.round(sum / array.length);
        sub_avg[`${array[0].subject.toLowerCase()}`] = average;
      }

      ov_stats = {
        id: 1,
        ov_math_avg: sub_avg["mathematics"],
        ov_physics_avg: sub_avg["physics"],
        ov_chem_avg: sub_avg["chemistry"],
        ov_bio_avg: sub_avg["biology"],
        ov_his_avg: sub_avg["history"],
        ov_geo_avg: sub_avg["geography"],
        ov_eng_avg: sub_avg["english"],
        ov_cs_avg: sub_avg["computer science"],
        total_grades: rows.length,
      };
    }

    async function run() {
      try {
        await db.client.connect();
        const database = db.client.db("db_stats");
        const stats = database.collection("stats");
        const studentsdb = database.collection("students");

        if (students.length > 0) {
          const deleteStudents = await studentsdb.deleteMany({});
          // console.log(deleteStudents.deletedCount);

          const insertStudents = await studentsdb.insertMany(students);
          // console.log(insertStudents.insertedCount);

          const saveOverall = await stats.findOneAndReplace(
            { id: 1 },
            ov_stats
          );
        }
      } finally {
        // Ensures that the client will close when you finish/error
        await db.client.close();
      }
    }
    run().catch(console.dir);
  } catch (err) {
    console.log(err);
  }
};  

const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
  // analyze();
  setInterval(analyze, 1000);
});
