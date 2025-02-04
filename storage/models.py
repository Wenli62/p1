from sqlalchemy import Integer, Numeric, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, mapped_column
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass

class voteReport(Base):
    # SQLALchemy column definitions
    __tablename__ = 'vote_report'
    id = mapped_column(Integer, primary_key=True)
    user_input = mapped_column(String(10), nullable=False)
    vote_time = mapped_column(DateTime, nullable=False)
    date_created = mapped_column(DateTime, nullable=False, default=func.now())

    def to_dict(self):
        dict = {}
        dict['id'] = self.id
        dict['user_input'] = self.user_input
        dict['vote_time']= float(self.vote_time)
        dict['date_created']= self.date_created

        return dict