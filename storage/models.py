from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class gradeReport(Base):
    __tablename__ = 'grade_report'
    id = mapped_column(Integer, primary_key=True)
    student_id = mapped_column(String(10), nullable=False)
    subject = mapped_column(String(50), nullable=False)
    grade = mapped_column(Integer, nullable=False)
    receive_time = mapped_column(DateTime, nullable=False)
    date_recorded = mapped_column(DateTime, nullable=False, default=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'subject': self.subject,
            'grade': self.grade,
            'receive_time': self.receive_time,
            'date_recorded': self.date_recorded
        }