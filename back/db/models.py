from re import sub, match
from sqlalchemy import Column, Integer, String
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_method

from . import schemas


Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128))
    location = Column(String(128))
    description = Column(String(1024))
    salary = Column(String(128))
    disability_category = Column(String(128))
    job_type = Column(String(128))
    source_url = Column(String(128))
    coordinates = Column(String(128))

    def salary_range(self):
        if not self.salary:
            return None
        cleaned_string = sub(r'\s|,', '', self.salary)
        sal_match = match(r'(\d+)(?:[\u202F\u2013\u2014-](\d+))?грн', cleaned_string)
        if match:
            return tuple(map(int, sal_match.groups())) if sal_match.group(2) else int(sal_match.group(1))
        else:
            return None

    def coordinates_list(self):
        if not self.coordinates:
            return None
        splited = self.coordinates.split(",")
        return [float(splited[0]), float(splited[1])]

    def to_schema(self) -> schemas.Job:
        return schemas.Job(
            id=self.id,
            title=self.title,
            location=self.location,
            coordinates=self.coordinates_list(),
            description=self.description,
            salary=self.salary,
            disable_category=self.disability_category,
            job_type=self.job_type,
            source_url=self.source_url
        )

    def __repr__(self) -> str:
        return f"<{self.id}, {self.title}, {self.salary}>"
