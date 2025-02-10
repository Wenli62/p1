print(
  "Start #################################################################"
);

db.createCollection("stats");
db.createCollection("students");

var stats = db.getCollection("stats");
var students = db.getCollection("students");

students.insertMany([
  {
    student_id: 1001,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1002,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1003,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1004,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1005,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1006,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1007,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1008,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1009,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
  {
    student_id: 1010,
    math_avg: 0,
    physics_avg: 0,
    chem_avg: 0,
    bio_avg: 0,
    his_avg: 0,
    geo_avg: 0,
    eng_avg: 0,
    cs_avg: 0,
  },
]);

stats.insertOne({
  id: 1,
  ov_math_avg: 0,
  ov_physics_avg: 0,
  ov_chem_avg: 0,
  ov_bio_avg: 0,
  ov_his_avg: 0,
  ov_geo_avg: 0,
  ov_eng_avg: 0,
  ov_cs_avg: 0,
  total_grades: 0
});


print(
  "Complete ##############################################################"
);
