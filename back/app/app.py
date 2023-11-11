from __future__ import annotations
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from db import Session, models, schemas
from sys import maxsize
from re import compile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Filter:

    def __init__(self, jobs: list[models.Job]):
        self.jobs = jobs

    def keyword(self, keyword: str) -> Filter:
        if not keyword:
            return self
        self.jobs = list(filter(lambda j: keyword in j.title or keyword in j.description, self.jobs))
        return self

    def location(self, location: str) -> Filter:
        if not location:
            return self
        self.jobs = list(filter(lambda j: location in j.location, self.jobs))
        return self

    def disability_category(self, category: str) -> Filter:
        if not category:
            return self
        self.jobs = list(filter(lambda j: category == j.disability_category, self.jobs))
        return self

    def job_type(self, type: str) -> Filter:
        if not type:
            return self
        self.jobs = list(filter(lambda j: type == j.job_type, self.jobs))
        return self

    def price_range(self, range: list[int, int]) -> Filter:
        if not range:
            return self
        filtered_jobs = []
        for job in self.jobs:
            job_salary_range = job.salary_range()
            if isinstance(job_salary_range, int):
                if range[0] <= job_salary_range <= range[1]:
                    filtered_jobs.append(job)
            elif isinstance(job_salary_range, list):
                if range[0] <= job_salary_range[0] and job_salary_range[1] <= range[1]:
                    filtered_jobs.append(job)
        self.jobs = filtered_jobs
        return self

    def page(self, page: int):
        page -= 1
        page_size = 8
        self.jobs = self.jobs[page*page_size: page*page_size+page_size]
        return self

    def get(self):
        return self.jobs

    def count(self):
        return len(self.jobs)


def parse_salary_range(range_str: str) -> list[int, int] | None:
    if not range_str:
        return None
    pattern1 = compile(r'(\d+)-(\d+)')
    pattern2 = compile(r'(\d+)-')
    pattern3 = compile(r'-(\d+)')
    match1 = pattern1.match(range_str)
    match2 = pattern2.match(range_str)
    match3 = pattern3.match(range_str)
    if match1:
        start, end = map(int, match1.groups())
    elif match2:
        start, end = int(match2.group(1)), maxsize
    elif match3:
        start, end = 0, int(match3.group(1))
    else:
        raise ValueError("Invalid input format")
    return [start, end]



@app.get("/status")
def get_status():
    return "OK"


@app.get("/jobs", response_model=schemas.ResponseOK | schemas.ResponseError)
def get_jobs(
    keyword: str = Query(None),
    location: str = Query(None),
    disability_category: str = Query(None),
    job_type: str = Query(None),
    salary_range: str = Query(None),
    page: int = Query(1)
):
    session = Session()
    filter_ = Filter(session.query(models.Job).all())
    filter_.keyword(keyword).location(location).disability_category(disability_category)
    filter_.price_range(parse_salary_range(salary_range)).job_type(job_type)
    total_count = filter_.count()
    jobs = filter_.page(page).get()
    jobs_list = [job.to_schema().model_dump() for job in jobs]
    return {"ok": True, "result": {"total_count": total_count, "jobs": jobs_list}}


@app.get("/job", response_model=schemas.ResponseOK | schemas.ResponseError)
def get_job_by_id(id: int):
    session = Session()
    job = session.query(models.Job).filter_by(id=id).first()
    if not job:
        return {"ok": False, "error_code": 404, "description": "Job not found"}
    return {"ok": True, "result": job.to_schema().model_dump()}

