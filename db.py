from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class ScrapedData(Base):
    __tablename__ = 'scraped_data'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    html = Column(Text)
    important_info = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    total_execution_time = Column(Integer)
    completed_processes = Column(Integer)
    tokens_used = Column(Integer)

    def __repr__(self):
        return f"<ScrapedData(url={self.url}, html={self.html}, important_info={self.important_info})>"

engine = create_engine('sqlite:///scraped_data.db')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)



