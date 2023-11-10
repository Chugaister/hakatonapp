from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from . import schemas


Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128))
    location = Column(String(128))
    description = Column(String(1024))
    salary = Column(String(128))
    disable_category = Column(String(128))
    job_type = Column(String(128))
    source_url = Column(String(128))

    def to_schema(self) -> schemas.Job:
        return schemas.Job(
            id=self.id,
            title=self.title,
            location=self.location,
            description=self.description,
            salary=self.salary,
            disable_category=self.disable_category,
            job_type=self.job_type,
            source_url=self.source_url
        )

    def __repr__(self) -> str:
        return f"<{self.id}, {self.title}, {self.salary}>"
