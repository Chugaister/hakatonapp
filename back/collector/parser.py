import requests
from lxml import html


from db import models, Session


def parse_job_page_workua(job_url) -> models.Job | None:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(job_url, headers=headers)
    if response.status_code == 404:
        return None
    tree = html.fromstring(response.text)
    title = tree.xpath('//h1[@id="h1-name"]/text()')[0].strip()
    salary_list = tree.xpath('//span[@title="Зарплата"]/following-sibling::b/text()')
    if salary_list:
        salary = salary_list[0].strip()
    else:
        salary = None
    description = tree.xpath('//div[@id="job-description"]')[0]
    description = html.tostring(description, encoding='unicode', method='html')# Find a child element
    job_type = tree.xpath('//span[@title="Умови й вимоги"]/following-sibling::text()')[0].strip()
    location = tree.xpath('//span[@title="Адреса роботи"]/following-sibling::text()')[0].strip()
    return models.Job(
        title=title,
        salary=salary,
        description=description,
        job_type=job_type,
        location=location,
        source_url=job_url
    )


def parse_page_workua(page_url: str) -> list[models.Job]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(page_url, headers=headers)
    tree = html.fromstring(response.text)
    urls = tree.xpath('//h2[@class=""]/a/@href')
    return [parse_job_page_workua("https://www.work.ua" + job_url) for job_url in urls]


def main():
    session = Session()
    jobs = []
    for page in range(1, 10):
        print("parsing page", page)
        jobs.extend(parse_page_workua(f"https://www.work.ua/jobs-lviv/?disability=1&page={page}"))
        session.add_all(jobs)
        session.commit()


def to_json():
    from json import dump
    session = Session()
    jobs = session.query(models.Job).all()[:10]
    dataset = [job.to_schema().model_dump() for job in jobs]
    with open("dataset.json", "w", encoding="utf-8") as file:
        dump(dataset, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    pass
