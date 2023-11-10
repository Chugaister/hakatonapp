from pydantic import BaseModel


class Job(BaseModel):
    id: int
    title: str
    location: str
    description: str
    salary: str | None
    disable_category: str | None
    job_type: str
    source_url: str
