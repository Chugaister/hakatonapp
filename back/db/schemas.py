from pydantic import BaseModel


class ResponseOK(BaseModel):
    ok: bool = True
    result: dict


class ResponseError(BaseModel):
    ok: bool = False
    error_code: int
    description: str


class Job(BaseModel):
    id: int
    title: str
    location: str
    coordinates: list | None
    description: str
    salary: str | None
    disable_category: str | None
    job_type: str
    source_url: str
