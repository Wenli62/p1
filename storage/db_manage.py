import sys
from db import engine
from models import gradeReport

def create_tables():
    
    gradeReport.metadata.create_all(engine)

def drop_tables():
    
    gradeReport.metadata.drop_all(engine)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "drop":
        drop_tables()
        print("All tables droped!")
    create_tables()
    print("Empty tables created!")