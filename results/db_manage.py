import sys
from pymongo import MongoClient


client = MongoClient("mongodb://root:zxcvbnm@localhost:27017/")
db = client["db_stats"]

def drop_collections():

    if "stats" in db.list_collection_names():
        db.drop_collection("stats")
    if "students" in db.list_collection_names():
        db.drop_collection("students")
    print("All collections dropped!")

def create_collections():

    stats = db["stats"]
    students = db["students"]
    
    students_data = [
        {"student_id": 1001, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1002, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1003, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1004, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1005, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1006, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1007, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1008, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1009, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
        {"student_id": 1010, "math_avg": 0, "physics_avg": 0, "chem_avg": 0, "bio_avg": 0, "his_avg": 0, "geo_avg": 0, "eng_avg": 0, "cs_avg": 0},
    ]
    
    stats_data = {
        "id": 1,
        "ov_math_avg": 0,
        "ov_physics_avg": 0,
        "ov_chem_avg": 0,
        "ov_bio_avg": 0,
        "ov_his_avg": 0,
        "ov_geo_avg": 0,
        "ov_eng_avg": 0,
        "ov_cs_avg": 0,
        "total_grades": 0
    }

    if db["students"].count_documents({}) == 0:
        students.insert_many(students_data)
        print("Inserted student data into the 'students' collection.")

    if db["stats"].count_documents({"id": 1}) == 0:
        stats.insert_one(stats_data)
        print("Inserted stats data into the 'stats' collection.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "drop":
        drop_collections()
    create_collections()
    print("Empty collections created!")
